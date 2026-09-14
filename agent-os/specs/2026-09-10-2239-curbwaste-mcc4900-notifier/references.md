# References for Curbwaste MCC 4900 Notifier

## Similar implementations

### Elavon CCO - Enrollment Monitor — the template for this workflow

- **Location:** v1 `kaos1lAi2PZ7wDAw`; vault note
  `vault/v1/workflows/elavon-cco-enrollment-monitor.md`
- **Relevance:** Same shape end to end — scheduled monitor, Postgres eligibility query,
  data-table diff to decide what is "new", per-merchant action, outcome recorded, Slack
  threaded report, and a `run_mode`/`delivery_mode` pair that keeps it harmless until
  deliberately armed. **Read its manual block before writing a node**; it documents traps
  that were paid for once already.
- **Key patterns to borrow:**
  - `Collapse` before the eligibility query — the data-table read runs once per input item,
    so without folding to a single item first the query fires once per existing row. This is
    the trap that produced 44,944 rows (212×212) during the commodity-table load.
  - `alwaysOutputData: true` on the data-table `get` — the table is empty on the first run
    and without it nothing downstream executes at all.
  - Claim-then-act: write `processing` before the side effect, so a crash leaves a stuck row
    instead of a duplicate action.
  - Data-table write nodes declare **only the columns they write**. Declaring the full schema
    makes the n8n panel render every other column as an empty editable field — which reads as
    "these will be blanked". They are omitted at runtime, but it is one keystroke from wiping
    real data.
  - `mode: each` on sub-workflow calls, so one merchant's failure cannot take the batch down.
  - Slack kept off the main path; thread id stamped on by a Code node re-reading `$('Plan')`.
  - Retry policy split into retryable (`failed`) vs permanent (`skipped`), so a 4-hourly
    schedule does not re-attempt an impossible merchant six times a day.
  - A sub-workflow returns its **last** node's output. Appending a node to a child changes
    what the caller receives — this once made the CCO monitor record a row of nulls.

### Send Email: Simple Text — the email transport

- **Location:** v1 `Zr3vF0LVpsPrzHVY`; vault note `vault/v1/workflows/send-email-simple-text.md`
- **Relevance:** The mandated email sender, and the mechanism that guarantees no email
  escapes during testing.
- **Interface** (`executeWorkflowTrigger` inputs): `to`, `subject`, `message_body`, `cc`,
  `create_draft` (boolean), `partner`, `skip_email` (boolean), `slack_channel`,
  `slack_message_ts`, `debug_info`, `passthrough_item` (object).
- **Key patterns:**
  - `Set Email Parameters` normalizes with `create_draft == null ? true : create_draft` and
    `skip_email == null ? true : skip_email` — **both default to true**. Omitting a field
    cannot cause a send.
  - `is_pe_inbox` is `partner != 'Supermove' && partner != 'Hearth'`, so `"Curbwaste"` routes
    to PE Merchants Gmail (`OUcDLrjl56jcWUCa`, `merchants@platformfactory.io`).
  - `create_draft: true` selects the Gmail nodes with `resource: draft`; `create_draft: false`
    selects `resource: message` (`operation: send`). `skip_email: true` bypasses Gmail
    entirely via the switch's `Skip Email` output.
  - It posts its own Slack status into a thread when given `slack_channel` +
    `slack_message_ts`, so the caller gets per-email reporting for free.

### Slack - Create a base message / Slack - Send notification

- **Location:** v1 `VQPaemuwy6FdMa9L` and `U3EyWwhZtcf2tMh5`
- **Interface:** base message takes `partner_account`, `channel_name`, `base_message`,
  `passthrough_item`; notification takes `partner_account`, `channel_name`, `message_ts`,
  `message`, `passthrough_item`.
- **Key patterns:**
  - `partner_account` switches only on `Hearth` / `Supermove`; pass `"PE"` to hit the
    fallback (PEBot), as the CCO monitor does.
  - Posts by **channel name**, and reuses the channel id from its own message response for
    any file upload — Slack's file upload rejects a channel *name*, and an *empty* channel id
    makes the upload succeed while storing the file where nobody can see it. Prefer the
    sub-workflow over the Slack node, which exposes that failure mode.
  - `passthrough_item` is mandatory on both.

### Edit Curbwaste statements — the Curbwaste query shape

- **Location:** v1 `HSEk0Ep12O8S2waU`
- **Relevance:** Only existing workflow that queries Curbwaste merchants directly. Source of
  the account id `3fc7c27f-c5a6-41db-84cb-f09c4b7164d7` and of the `merchant_status` history
  join that yields a real activation timestamp:

```sql
INNER JOIN LATERAL (
    SELECT s.status, s.created_at
    FROM merchant_status s
    WHERE s.merchant_id = m.id
    ORDER BY s.created_at DESC
    LIMIT 1
) ms ON true
```

  This workflow takes the **latest** status row. For activation time we want the **earliest**
  `status = 'active'` row instead (`min(s.created_at)`), so a suspend/reactivate cycle does
  not reset it.

## Schema knowledge (read, don't re-derive)

### `vault/v1/resources/databases/postgres-bdw1qodl0v7mywj6.md`

The authoritative note on the PayEngine production Postgres. Relevant sections:

- **MID resolution** — `merchant_processor_detail.processor_merchant_id` is the *only*
  reliable bridge from a PayEngine merchant UUID to an Elavon MID. `merchant.processor_merchant_id`
  is **null** for the merchants that matter. Both filters are required:
  `processor_id = 'elavon'` (merchants board on several processors) and
  `processor_merchant_id ~ '^[0-9]+$'` (excludes gateway ids like `org_440947`).
  MID is **not** unique — one MID maps to two merchants — which is why tracking tables are
  keyed on `merchant_id`.
- **MCC lives in `merchant.data -> 'business_type' ->> 'mcc_sic'`.** There is no `mcc` column
  anywhere on `merchant` or `merchant_processor_detail`. Populated for 10,218 of 22,163
  merchants. Three value shapes: `"4900"` fine; `"0742"` zero-padded; `"5999J"` non-numeric,
  must be rejected and never coerced. Length distribution: 4 chars ×10186, 3 ×3, 5 ×29.
- **It disagrees with Elavon for ~11% of merchants** (measured 2026-09-07, 3,063 numeric MIDs
  joined against `Elavon - MIDs`): agree 2046, disagree-by-staleness 142, genuine disagreement
  271. Differences run systematically generic → specific, i.e. Postgres holds what the
  merchant *applied* with and Elavon holds what underwriting *assigned*.
- **`account_settings` / `merchant_setting`** flag-resolution convention (merchant overrides
  partner) — not used by this workflow, but the pattern to follow if a Curbwaste-level
  opt-out flag is ever added.

### `vault/v1/resources/data-tables/eefxih6vfsgkmssi.md` — `Elavon - MIDs`

Keyed on `MID` (Elavon's 10-digit id, stored as **number**). 2,537 rows, every one populated
for both `MCC` and `DBA`, across 94 distinct MCCs. Carries **no PayEngine UUID**. `Last_Sync`
was 2025-11-11 .. 2026-03-14 as of 2026-09-07, i.e. ~6 months stale. This is the source for
the Task 4 cross-check and the reason it is reporting-only.

### `vault/v1/resources/data-tables/kepdpgqsjwflp5lz.md` — `Elavon - MCC Commodity Codes`

MCC → Elavon commodity code, for CCO enrollment forms. **Not relevant to this workflow** —
noted so nobody wires it in by MCC-keyword association.

## Extraction tooling

`scripts/jq/nodes-summary.jq`, `extract-subworkflows.jq`, `extract-data-tables.jq`,
`extract-triggers.jq`, `extract-credentials.jq` — use these to inspect the built workflow.
Never `Read` or `cat` anything under `vault/v1/_cache/workflows/`.
