---
type: data-table
instance: v1
resource_id: "7GMBNwAQh8ZNTiMA"
current_name: "Elavon - CCO Enrollments"
aliases: ["Elavon - CCO Enrollments"]
auto_generated_at: 2026-09-07T19:04:01Z
---

<!-- auto:start -->

# Elavon - CCO Enrollments

- **Resource id (canonical):** `7GMBNwAQh8ZNTiMA`
- **Current name:** Elavon - CCO Enrollments
- **Table ID:** `7GMBNwAQh8ZNTiMA`

## Used by

- [[../../workflows/elavon-cco-enrollment-monitor|Elavon CCO - Enrollment Monitor]] — node "Claim merchant" (id `11110000-0000-4000-8000-00000000000a`)
- [[../../workflows/elavon-cco-enrollment-monitor|Elavon CCO - Enrollment Monitor]] — node "Get existing records" (id `11110000-0000-4000-8000-000000000004`)
- [[../../workflows/elavon-cco-enrollment-monitor|Elavon CCO - Enrollment Monitor]] — node "Mark failed" (id `11110000-0000-4000-8000-00000000000f`)
- [[../../workflows/elavon-cco-enrollment-monitor|Elavon CCO - Enrollment Monitor]] — node "Record outcome" (id `11110000-0000-4000-8000-000000000012`)
- [[../../workflows/elavon-cco-enrollment-monitor|Elavon CCO - Enrollment Monitor]] — node "Write baseline" (id `11110000-0000-4000-8000-000000000009`)

<!-- auto:end -->

<!-- manual:start -->

## Role: the "have we sent this merchant's CCO form" ledger

Created 2026-09-07 for [[../../workflows/elavon-cco-enrollment-monitor]]. **This table is
the idempotency guarantee** — it is the only thing preventing a merchant's enrollment form
from being submitted to Elavon twice.

Rows are created by exactly two nodes: `Write baseline` (backfill mode) and `Claim merchant`
(process mode). `Record outcome` and `Mark failed` only ever update existing rows.

## Why keyed on `merchant_id`, not MID

The alternative considered was adding `CCO_*` columns to
[[eefxih6vfsgkmssi|Elavon - MIDs]], which already carries workflow state for other processes
(`Email_Change_Requested`, `PCI_SAQ_Web_Portal_Sign_State`, …), so there was real precedent.
Rejected on three counts:

1. **MID is not unique** — `8046096999` maps to two different merchants, so marking one sent
   could mark the wrong one.
2. **That table has no PayEngine UUID**, while the workflow is driven by `merchant_id`, so
   every read/write would need a UUID→MID hop — and only 16 of the 91 eligible merchants
   even have an Elavon MID, so the rest could not be represented at all.
3. **It is upserted from Google Sheets** by `Elavon MIDs to Data Tables sync`. A bulk reload
   there would wipe our sent-state and cause duplicate submissions to Elavon.

A Postgres table would arguably be the better long-term home — "new and not yet sent"
collapses into one `LEFT JOIN … IS NULL` — but needs a schema change and Ops sign-off.

## Status vocabulary

| status | meaning | re-processed? |
|---|---|---|
| `baseline` | Seeded by the one-time backfill; nothing was sent | no |
| `processing` | Claimed, in flight. A stuck row means a crash mid-run | no |
| `simulated` | `delivery_mode: fill` — the form was filled but never submitted | **yes** |
| `sent` | Submitted to Elavon and a confirmation page was seen | no |
| `failed` | Transient; retried while `attempt_count < max_attempts` | **yes** |
| `skipped` | Permanent; needs a data fix first | no |

`status` deliberately **does not name the delivery mechanism** — that lives in
`delivery_mode` (`fill` | `submit` | `submit-failed`). Enrollment moved from email to
Elavon's Qualtrics form on 2026-09-08 and this vocabulary did not have to change, which was
the point of separating the two.

`sent` is trustworthy here in a way it was not under the email design: the submitter clicks
Submit, then requires a confirmation page before returning `submitted: true`. If the form is
still displayed, or no confirmation text is found, it throws and the row is recorded
`failed` — never `sent`. The evidence is the full-page screenshot posted to Slack.

What we still cannot see is Elavon's side. Qualtrics returns nothing machine-readable to us
beyond the confirmation page, so `sent` means "submitted and acknowledged by the form", not
"accepted by Elavon".

## Snapshot columns are intentional

`mcc`, `item_commodity_code`, `item_description`, `dba` and `ship_from_zip_code` record what
was actually printed on the form we submitted, not what the merchant looks like today. This
matters because PayEngine's `mcc_sic` and Elavon's MCC already disagree for ~11% of
merchants — without the snapshot there would be no way to prove what a signed form said.

`mid` is stored as **string**, not number. `Elavon - MIDs` stores it as a number; number is
exactly what would reintroduce the leading-zero problem.

`status` and `delivery_mode` are strings rather than booleans partly because more than two
states are needed, and partly because an unset boolean is the field type that renders as ON
in the n8n UI while the runtime sees `null`.

## Backfill note

The one-time backfill seeded only the **15 ready** merchants, not all 91 eligible. Seeding
the blocked ones would permanently hide them: they are blocked today only for missing an
Elavon MID or MCC, and once that data lands they would already be "known" and never picked
up. Blocked merchants are logged each run with a reason instead.

<!-- manual:end -->
