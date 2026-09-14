# Curbwaste MCC 4900 Visa Utility Program Notifier

## Context

Curbwaste merchants boarded on Elavon need to self-enrol with Visa for the Utilities Program
(MCC 4900) — Visa only accepts a direct merchant request, not an acquirer/partner submission.
Today nobody tells them. This builds the monitor that does: every 4 hours, find Curbwaste
merchants that have newly gone active with MCC 4900, email each one Visa's enrolment
instructions plus their Elavon MID, and record the notification so it happens exactly once.

Target is the existing but **empty** v1 workflow `ajjvV2MZyEtuMj49`
("Curbwaste Merchant MCC4900 Notification", 0 nodes, inactive).

**Hard constraint: zero emails may leave the system while we build and test.** Satisfied by
the `Send Email: Simple Text` sub-workflow's own contract, which fails safe (see below).

## Decisions taken

- Eligibility: Postgres `mcc_sic` normalizes to `4900` **and** merchant has a numeric Elavon MID.
- First run baselines the existing active set (no email); only new activations get notified.
- Sends from the PE Merchants inbox, no CC.
- Slack reporting to `n8n-sandbox-of-doom` during test, `ops-automation-alert` after.

## What already exists and gets reused

| Piece | Where |
|---|---|
| `Send Email: Simple Text` | v1 `Zr3vF0LVpsPrzHVY` |
| `Slack - Create a base message` | v1 `VQPaemuwy6FdMa9L` |
| `Slack - Send notification` | v1 `U3EyWwhZtcf2tMh5` |
| Closest reference implementation | v1 `kaos1lAi2PZ7wDAw` "Elavon CCO - Enrollment Monitor" — read its manual block in `vault/v1/workflows/elavon-cco-enrollment-monitor.md` before writing a node |
| Curbwaste account id | `3fc7c27f-c5a6-41db-84cb-f09c4b7164d7` |
| Postgres credential | Postgres Production `BDw1qoDl0V7mYwj6` |
| MCC / MID / `merchant_status` schema notes | `vault/v1/resources/databases/postgres-bdw1qodl0v7mywj6.md` |

### The three email-safety levers (verified in `Zr3vF0LVpsPrzHVY`)

`Set Email Parameters` does `create_draft == null ? true : create_draft` and
`skip_email == null ? true : skip_email` — **both default to true**, so a missing field
cannot cause a send. `create_draft: true` routes to Gmail nodes with `resource: draft`;
`skip_email: true` bypasses Gmail entirely. `partner` only distinguishes Hearth/Supermove —
anything else (`"Curbwaste"`) hits `is_pe_inbox` → `merchants@platformfactory.io`.

Test ladder: `skip_email: true` (dry run) → `skip_email: false, create_draft: true` (drafts) →
`create_draft: false` (live).

---

## Task 1: Save spec documentation

Create `agent-os/specs/2026-09-10-2239-curbwaste-mcc4900-notifier/` with `plan.md` (this file),
`shape.md` (scope + the decisions above), `standards.md` (the sync/notes standards that apply),
`references.md` (the reuse table above with why each matters). No visuals.

## Task 2: Create the tracking data table on v1

> **Must be done by hand in the n8n UI.** v1 (n8n 1.123.18) exposes **no** data-table endpoint
> on the public API — verified against the instance's own `/api/v1/openapi.yml`, which lists
> only audit/credentials/executions/tags/workflows/users/source-control/variables/projects.
> The internal `/rest/projects/{projectId}/data-tables` route exists (401, not 404) but needs a
> browser session cookie, not an API key.
>
> The four tracking nodes therefore ship with `dataTableId.value = "PLACEHOLDER_DATA_TABLE_ID"`.
> Once the table exists, run `set-table-id.sh <REAL_ID>` (scratchpad) — or re-run
> `build-workflow.py` with `TABLE_ID=<REAL_ID>` and PUT the result.

New n8n data table **`Curbwaste - MCC4900 Notifications`**, keyed on `merchant_id`:

`merchant_id`, `merchant_name`, `dba`, `business_email`, `mid`, `mcc`, `status`,
`first_seen_at`, `activated_at`, `notified_at`, `attempt_count` (number), `delivery_mode`,
`gmail_message_id`, `error_message`.

`status` domain: `baseline` | `processing` | `notified` | `simulated` | `failed` | `skipped`.

## Task 3: Build the workflow graph in `ajjvV2MZyEtuMj49`

Triggers: `Every 4 hours` (Schedule, 4-hour interval) + `When clicking 'Execute workflow'`.

1. **`Run mode`** (Set) — config in one place: `run_mode` (`backfill`|`notify`),
   `delivery_mode` (`dry-run`|`draft`|`send`), `slack_channel`, `curbwaste_account_id`,
   `max_attempts`.
2. **`Get existing records`** (Data Table `get`, no filter) — **`alwaysOutputData: true`**, or an
   empty table stops the whole run.
3. **`Collapse`** (Code, run-once-for-all-items) — fold all rows into one item
   (`{ existing: [...] }`). Without this the eligibility query runs once per existing row.
4. **`Find eligible`** (Postgres, `executeQuery`):

```sql
SELECT
  m.id                                                AS merchant_id,
  m.name                                              AS merchant_name,
  (m.data)::jsonb->'business_details'->>'email'       AS business_email,
  (m.data)::jsonb->'business_details'->'dba'->>'name' AS dba,
  (m.data)::jsonb->'business_type'->>'mcc_sic'        AS mcc_raw,
  m.status                                            AS merchant_status,
  (SELECT min(s.created_at) FROM merchant_status s
    WHERE s.merchant_id = m.id AND s.status = 'active') AS activated_at,
  (SELECT mpd.processor_merchant_id
     FROM merchant_processor_detail mpd
    WHERE mpd.merchant_id = m.id
      AND mpd.processor_id = 'elavon'
      AND mpd.processor_merchant_id ~ '^[0-9]+$'
    LIMIT 1)                                          AS mid
FROM merchant m
WHERE m.account_id = '3fc7c27f-c5a6-41db-84cb-f09c4b7164d7'
  AND m.status = 'active'
ORDER BY m.name;
```

5. **`Plan`** (Code) — normalize and classify; **do not filter in SQL**, so the Slack summary can
   report how many were excluded and why:
   - `mcc_raw` null → `mcc_missing`; fails `/^\d+$/` (e.g. `"5999J"`) → `mcc_non_numeric`,
     never coerced; strip leading zeros (`"0742"` → `742`) then compare to `4900`.
   - no `mid` → `skipped/no_elavon_mid`; no `business_email` → `skipped/no_email`.
   - `new` = passes every gate **and** `merchant_id` absent from `existing` (or present with a
     retryable `failed` and `attempt_count < max_attempts`). Never a `created_at`/`activated_at`
     watermark — the vault documents why that silently misses merchants.
   - `backfill` mode emits every active merchant as a `baseline` row and nothing else.
6. **`Post Slack base message`** (Execute Workflow `VQPaemuwy6FdMa9L`, mode `once`) —
   `partner_account: "PE"`, `channel_name` from `Run mode`, `passthrough_item: {{ $json }}`
   (mandatory — the sub-workflow throws on its no-thread path without it).
   `onError: continueRegularOutput`.
7. **`Attach slack thread`** (Code) — re-read `$('Plan').all()` and stamp `slack_channel` /
   `slack_message_ts` onto each merchant. Keeps Slack's item shape off the merchant path.
8. **`Route by mode`** (Switch) — `backfill` → step 9, `notify` → step 10.
9. **`Write baseline`** (Data Table `upsert`, key `merchant_id`) — status `baseline`.
10. **`Claim merchant`** (Data Table `upsert`) — write `processing` and bump `attempt_count`
    **before** the email. Claim-then-act makes this at-most-once; a crash leaves a visible
    stuck row rather than re-emailing.
11. **`Build email`** (Set) — `to`, `subject`, `message_body` per the template below.
12. **`Call 'Send Email: Simple Text'`** (Execute Workflow `Zr3vF0LVpsPrzHVY`, mode `each`) —
    `to`, `subject`, `message_body`, `partner: "Curbwaste"`,
    `create_draft: {{ delivery_mode !== 'send' }}`, `skip_email: {{ delivery_mode === 'dry-run' }}`,
    `slack_channel`, `slack_message_ts`, `passthrough_item`.
13. **`Classify outcome`** (Code) — `notified` / `simulated` (dry-run or draft) / `failed`
    (retryable) / `skipped` (permanent). `simulated` counts as unfinished so a later live run
    picks the merchant up.
14. **`Record outcome`** / **`Mark failed`** (Data Table `update`) — declare **only the columns
    being written**; declaring the full schema makes the n8n panel render every other column as
    blank-and-editable, one keystroke from wiping real data.
15. **`Run summary`** (Code) + **`Post run summary`** (Execute Workflow `U3EyWwhZtcf2tMh5`, in
    thread, `onError: continueRegularOutput`) — counts per status and the exclusion breakdown.
16. Sticky notes: flow-control config, the email-safety ladder, and the go-live checklist.

### Email template

Subject:
`Notification to register with Visa for Utilities Program (MCC 4900) for Curbwaste Merchant Account {{ business_name }} {{ mid }}`

Body — plain text, verbatim wording, the four steps rendered as a numbered list:

```
Hi {{ business_name }},

To enrol for Visa Utility Program (MCC 4900), you will have to submit direct request to Visa. Here is the enrolment process to be followed

1. Visit VisaAccess.com and select "Enroll".
2. Complete the Contact Information and Physical Location sections.
3. Click "Confirm and Proceed".
4. After reaching the confirmation screen, a member of Visa's support team will complete the enrollment process and contact you within 2-3 business days.

For any questions regarding the enrollment process, merchants can contact Visa at VisaUtilitySolutions@visa.com

Here is the Payment Processor's (Elavon's) Merchant ID required for Visa Enrollment Process: {{ mid }}

Regards,
PayEngine Merchant Services (on behalf of Curbwaste Payments Team)
```

`business_name` = `dba` falling back to `merchant_name` — DBA is what the merchant recognizes,
and it is what the Elavon-facing workflows already use. Flag if you want legal name instead.

## Task 4 (optional — say the word to drop it): Elavon MCC cross-check

For merchants **excluded** by the `mcc_sic != 4900` gate, look their MID up in the
`Elavon - MIDs` data table (`EEFXIH6vFSgKmssi`) and report any whose Elavon-assigned MCC *is*
4900. Data Table `get` filtered on `MID`, mode each, `onError: continueRegularOutput`, results
only in the Slack summary — never gating an email. This exists because the vault measured the
two MCC sources disagreeing for ~11% of merchants (271 genuine + 142 staleness of 3,063), so
the chosen filter will miss merchants Elavon actually boarded as 4900.

## Task 5: Refresh the vault

Run `agent-os/standards/sync/refresh-procedure.md` for `v1`, then write the manual blocks on the
new workflow note and the new data-table note: purpose, the go-live ladder, why "new" is a
table diff and not a timestamp, the claim-then-act ordering, and the MCC-source caveat.

---

## Verification

1. `scripts/n8n-api.sh v1 /api/v1/workflows/ajjvV2MZyEtuMj49` piped through
   `scripts/jq/nodes-summary.jq` + `extract-subworkflows.jq` + `extract-data-tables.jq` —
   confirm wiring, that all three sub-workflow ids resolve, and the schedule is 4 hours.
2. **Dry run.** `run_mode: backfill`, `delivery_mode: dry-run`. Manual execute. Assert: every
   Gmail node in the child execution is unreached, the table holds one `baseline` row per active
   Curbwaste merchant, and the Slack thread in `n8n-sandbox-of-doom` shows the exclusion
   breakdown. Cross-check the row count against the SQL run standalone.
3. **Draft run.** Hand-flip one baseline row to `failed`/`attempt_count: 0` to make it eligible,
   set `run_mode: notify`, `delivery_mode: draft`. Assert exactly one draft appears in
   `merchants@platformfactory.io`, **nothing in Sent**, subject/body render with real DBA and
   MID, and the row lands `simulated`.
4. **Idempotency.** Re-run step 3 unchanged. Assert zero new drafts and zero table writes.
5. **Go live.** Point `slack_channel` at `ops-automation-alert`, set `delivery_mode: send`,
   activate. Watch the first scheduled run end-to-end, then confirm `notified_at` and
   `gmail_message_id` are populated.
