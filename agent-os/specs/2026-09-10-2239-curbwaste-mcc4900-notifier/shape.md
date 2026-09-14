# Curbwaste MCC 4900 Visa Utility Program Notifier — Shaping Notes

## Scope

Build out the empty v1 workflow `ajjvV2MZyEtuMj49` ("Curbwaste Merchant MCC4900
Notification") into a 4-hourly monitor that:

1. Finds Curbwaste merchants that have newly gone **active** and carry MCC **4900**.
2. Emails each one Visa's Utility Program enrolment instructions plus their Elavon MID.
3. Records the notification in a persistent n8n data table so it happens **exactly once**.
4. Reports every run to Slack in a threaded message.

Out of scope: enrolling merchants with Visa on their behalf (Visa only accepts a direct
merchant request), and any change to the shared `Send Email` / `Slack` sub-workflows.

## Decisions

- **Instance is v1.** The workflow id the user gave resolves on v1 only; it 404s on v2. All
  three helper sub-workflows also live on v1 with v1-specific ids.

- **Eligibility = Postgres `mcc_sic` normalizes to `4900`, AND a numeric Elavon MID exists.**
  Chosen over "all active Curbwaste merchants" and over the Elavon-assigned MCC.
  *Accepted cost:* `mcc_sic` is the merchant's **applied** MCC and the vault measured it
  disagreeing with Elavon's **assigned** MCC for ~11% of merchants, so merchants Elavon
  actually boarded as 4900 but who applied as something else will be skipped. Mitigated (not
  fixed) by the cross-check reporting in Task 4 — it surfaces those misses in Slack without
  emailing them.
  MID is a hard requirement because the email body *is* the MID delivery mechanism.

- **First run baselines, it does not blast.** `run_mode: backfill` writes every currently
  active Curbwaste merchant into the tracking table as `baseline` and emails nobody. Only
  activations seen *after* that get notified. Rejected the "notify every not-yet-notified
  merchant" option because there is no undo on an email blast.

- **"New" means "eligible and not in the tracking table"** — never a `created_at` or
  `activated_at` watermark. A merchant can become eligible long after signup (MCC edit,
  reactivation), and a timestamp watermark silently misses those. Same reasoning as, and
  copied from, `Elavon CCO - Enrollment Monitor`. The full active set is diffed against the
  table every run; at Curbwaste's scale that is cheap.

- **Sends from the PE Merchants inbox (`merchants@platformfactory.io`), no CC.** Achieved by
  passing `partner: "Curbwaste"` — the sub-workflow's `is_pe_inbox` rule is
  `partner != 'Supermove' && partner != 'Hearth'`, so any other value routes to PE. Matches
  the signature line the user specified.

- **Zero emails escape during build/test**, enforced through a three-rung ladder rather than
  hand-editing nodes:

  | `delivery_mode` | `skip_email` | `create_draft` | Effect |
  |---|---|---|---|
  | `dry-run` | `true` | `true` | Gmail never invoked at all |
  | `draft` | `false` | `true` | Gmail `resource: draft` — draft in PE inbox, nothing sent |
  | `send` | `false` | `false` | Live send |

  This is safe by construction: `Set Email Parameters` in `Zr3vF0LVpsPrzHVY` does
  `create_draft == null ? true : create_draft` and `skip_email == null ? true : skip_email`,
  so a *missing* field cannot cause a send. The failure mode is a silent no-op, not a leak.

- **Claim-then-act.** `Claim merchant` writes `processing` to the data table **before** the
  email call. A crash therefore leaves a visible stuck row rather than re-emailing a merchant
  on the next 4-hourly tick. Duplicate merchant emails are the failure mode worth
  over-engineering against.

- **Slack stays off the merchant path.** `Slack - Create a base message` returns its own item
  shape, so its thread id is stamped onto merchants by a separate `Attach slack thread` Code
  node that re-reads `$('Plan').all()`. Both Slack calls are `onError:
  continueRegularOutput` — losing the report is better than losing the notification.

- **`passthrough_item` is mandatory** on both Slack sub-workflows; they do
  `jsonOutput = {{ trigger.passthrough_item }}` on the no-thread path and throw
  `Cannot convert undefined or null to object` when it is absent.

- **Business name = DBA, falling back to `merchant.name`.** DBA is what the merchant
  recognizes and what the Elavon-facing workflows already use.

- **Slack channel is config, not hardcoded.** `n8n-sandbox-of-doom` while testing,
  `ops-automation-alert` after — one field on the `Run mode` node.

- **MCC is classified, not filtered in SQL.** The eligibility query returns every active
  Curbwaste merchant and the `Plan` Code node applies the gates, so the Slack summary can
  report how many were excluded and why. Filtering in SQL would make a wrong gate invisible.

- **MCC normalization has three shapes** (measured and documented in the vault):
  `"4900"` usable as-is; `"0742"` zero-padded, strip leading zeros; `"5999J"` non-numeric,
  **reject, never coerce**.

## Context

- **Visuals:** None.
- **References:** See `references.md`. Primary is `Elavon CCO - Enrollment Monitor`
  (v1 `kaos1lAi2PZ7wDAw`) — near-identical shape, and its vault manual block is the source
  of most of the load-bearing decisions above.
- **Product alignment:** N/A — this is workflow authoring on the n8n instance, not a change
  to the vault-sync product described in `agent-os/product/`. The vault-facing obligation is
  the post-build refresh (Task 5).

## Standards Applied

- `sync/refresh-procedure` — the new workflow and new data table must reach the vault through
  a refresh, not a hand-written note.
- `notes/auto-manual-blocks` — the design rationale for this workflow goes in the manual
  block of its generated note; the auto block is refresh-owned.
- `sync/resource-taxonomy` — the new data table is a `data-tables` resource; no new taxonomy
  category is introduced, so no `taxonomy_gap` is expected.
- `sync/changelog-format` — the refresh that picks this up produces a changelog entry.
- `sync/large-workflow-handling` — read the workflow JSON through `scripts/jq/`, never into
  context raw.

## Open items carried into implementation

- Whether Curbwaste's active merchants actually have `business_details.email` populated is
  unverified — it can only be checked by running the eligibility query. If coverage is poor,
  `skipped/no_email` counts will show it in the first dry run.
- Whether any Curbwaste merchant has `mcc_sic = '4900'` at all is likewise unverified; a dry
  run returning zero eligible merchants is a signal to revisit the MCC source decision, not a
  bug.
