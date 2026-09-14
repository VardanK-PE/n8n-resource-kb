---
type: data-table
instance: v1
resource_id: "FEHmmYXWRDom0XHX"
current_name: "Curbwaste - MCC4900 Notifications"
aliases: ["Curbwaste - MCC4900 Notifications"]
auto_generated_at: 2026-09-14T17:11:15Z
---

<!-- auto:start -->

# Curbwaste - MCC4900 Notifications

- **Resource id (canonical):** `FEHmmYXWRDom0XHX`
- **Current name:** Curbwaste - MCC4900 Notifications
- **Table ID:** `FEHmmYXWRDom0XHX`

## Used by

- [[../../workflows/curbwaste-merchant-mcc4900-notification|Curbwaste Merchant MCC4900 Notification]] — node "Claim merchant" (id `22220000-0000-4000-8000-00000000000d`)
- [[../../workflows/curbwaste-merchant-mcc4900-notification|Curbwaste Merchant MCC4900 Notification]] — node "Get existing records" (id `22220000-0000-4000-8000-000000000004`)
- [[../../workflows/curbwaste-merchant-mcc4900-notification|Curbwaste Merchant MCC4900 Notification]] — node "Record outcome" (id `22220000-0000-4000-8000-000000000011`)
- [[../../workflows/curbwaste-merchant-mcc4900-notification|Curbwaste Merchant MCC4900 Notification]] — node "Write baseline" (id `22220000-0000-4000-8000-00000000000c`)

<!-- auto:end -->

<!-- manual:start -->

## Role: the "who has been told" ledger for the Visa MCC 4900 notification

Sole consumer is [[../../workflows/curbwaste-merchant-mcc4900-notification]]. Keyed on
**`merchant_id`** (the PayEngine merchant UUID) — deliberately *not* on MID, because a MID is
not unique: `8046096999` maps to two different merchants. Created by hand in the n8n UI on
2026-09-14; n8n data tables have no public API on this instance.

This table **is** the workflow's definition of "already handled". A merchant absent from it is
new; a merchant present in it is left alone unless its status says otherwise. Editing rows
here therefore directly controls who gets emailed — treat it as operational state, not a log.

## Columns

| column | type | notes |
|---|---|---|
| `merchant_id` | String | PayEngine merchant UUID — the key |
| `merchant_name` | String | `merchant.name` |
| `dba` | String | `business_details.dba.name`; the email greets with this, falling back to `merchant_name` |
| `business_email` | String | `business_details.email` — the recipient |
| `mid` | String | Elavon MID from `merchant_processor_detail`, numeric-only |
| `mcc` | String | normalised Postgres `mcc_sic` (leading zeros stripped) |
| `status` | String | see below |
| `first_seen_at` | Datetime | when this workflow first saw the merchant |
| `activated_at` | Datetime | `min(merchant_status.created_at)` where status = `active` |
| `notified_at` | Datetime | set **only** on a real send; `null` otherwise |
| `attempt_count` | Number | drives the retry cap (`max_attempts`, default 3) |
| `delivery_mode` | String | which rung of the ladder produced the row |
| `gmail_message_id` | String | set **only** on a real send — a draft id is never recorded here |
| `error_message` | String | truncated to 500 chars |

## Status vocabulary — which values are reprocessable

| status | meaning | picked up again? |
|---|---|---|
| `baseline` | seeded by a `backfill` run; known, never to be emailed | **no** |
| `processing` | claimed, email in flight | **no** — a stuck row means a crash mid-send |
| `notified` | real email sent | **no** |
| `simulated` | dry-run or draft record — **unfinished work** | **yes** |
| `failed` | transient failure | **yes**, while `attempt_count < max_attempts` |
| `skipped` | permanent, needs a data fix | **no** |

`simulated` being reprocessable is the point: a draft is not a notification, so the merchant
stays in the queue for a later live run. To retire a draft-tested merchant without lying about
it, set `baseline` — not `notified`. That is what was done for ADM Rolloff LLC on 2026-09-14.

To deliberately re-notify someone: **delete their row**. A merchant absent from the table is
new by definition. Cleaner than editing fields, and it is how the draft test was staged.

## Current contents (2026-09-14)

**103 rows, all `baseline`** — the seeded Curbwaste book, activation dates spanning
2022-02-19 → 2026-08-28. None of them will ever be emailed by the schedule. Ten more active
Curbwaste merchants are **not** in this table at all because they failed the MCC 4900 gate;
they are reported by name in the Slack run report, not tracked here. Nothing is written for a
merchant that is not eligible — baselining a blocked merchant would permanently hide it, since
it would already be "known" if it later became eligible.

## Gotcha

The workflow's write nodes **declare only the columns they write**. With n8n's resource mapper
what the panel displays is not what gets written — declaring the full schema makes every other
column render as an empty editable field, which reads as "these will be blanked". They are
omitted at runtime, but it is one keystroke from wiping real data.

<!-- manual:end -->
