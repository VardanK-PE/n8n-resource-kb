---
n8n_id: "kaos1lAi2PZ7wDAw"
instance: v1
name: "Elavon BI - CCO Enrollment Monitor"
status: inactive
last_modified: 2026-09-07T19:00:08.791Z
tags: []
fingerprint: "1f46a2896cb664fa2368889b815d4f65573e7faf87fa48f4e99fba4ee5a27876"
auto_generated_at: 2026-09-07T19:04:01Z
---

<!-- auto:start -->

# Elavon BI - CCO Enrollment Monitor

## Summary

- **Status:** inactive
- **n8n ID:** `kaos1lAi2PZ7wDAw`
- **Nodes:** 19
- **Last modified:** 2026-09-07T19:00:08.791Z

## Triggers

- **schedule** — node "Every hour" (id `11110000-0000-4000-8000-000000000001`) — `every 1 hour(s)`
- **manual** — node "When clicking ‘Execute workflow’" (id `11110000-0000-4000-8000-000000000002`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Find eligible" (id `11110000-0000-4000-8000-000000000006`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Find eligible" (id `11110000-0000-4000-8000-000000000006`)

### Data tables (n8n)

- [[../resources/data-tables/7gmbnwaqh8zntima|Elavon - CCO Enrollments]] (id `7GMBNwAQh8ZNTiMA`) — op `get` — node "Get existing records" (id `11110000-0000-4000-8000-000000000004`)
- [[../resources/data-tables/7gmbnwaqh8zntima|Elavon - CCO Enrollments]] (id `7GMBNwAQh8ZNTiMA`) — op `upsert` — node "Write baseline" (id `11110000-0000-4000-8000-000000000009`)
- [[../resources/data-tables/7gmbnwaqh8zntima|Elavon - CCO Enrollments]] (id `7GMBNwAQh8ZNTiMA`) — op `upsert` — node "Claim merchant" (id `11110000-0000-4000-8000-00000000000a`)
- [[../resources/data-tables/7gmbnwaqh8zntima|Elavon - CCO Enrollments]] (id `7GMBNwAQh8ZNTiMA`) — op `update` — node "Mark failed" (id `11110000-0000-4000-8000-00000000000f`)
- [[../resources/data-tables/7gmbnwaqh8zntima|Elavon - CCO Enrollments]] (id `7GMBNwAQh8ZNTiMA`) — op `update` — node "Record outcome" (id `11110000-0000-4000-8000-000000000012`)

### Sub-workflows (Execute Workflow calls)

- [[elavon-bi-edit-merchant-application-and-send-cco-enrollment|Elavon BI - Edit merchant application and send (CCO Enrollment)]] (n8n_id `Q16AhMTvfmtLzuI6`) — node "Build CCO PDF" (id `11110000-0000-4000-8000-00000000000b`)
- [[send-email-html|Send Email: HTML]] (n8n_id `H9qPciXCz00KxAyF`) — node "Send CCO email" (id `11110000-0000-4000-8000-00000000000c`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Post Slack base message" (id `11110000-0000-4000-8000-000000000013`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

## Purpose

Hourly monitor that finds merchants newly eligible for Elavon Commercial Card Optimization,
builds their enrollment PDF via
[[elavon-bi-edit-merchant-application-and-send-cco-enrollment]], emails it through
[[send-email-html]], and records the outcome in
[[../resources/data-tables/7gmbnwaqh8zntima|Elavon - CCO Enrollments]].

**Built 2026-09-07. Currently INACTIVE and in `draft` email mode** — it creates a Gmail
draft for review rather than emailing Elavon. See the "Flow execution control" sticky note
on the canvas for the full option matrix.

## Before enabling

1. Set `cco_recipient` on **Run mode** — it is deliberately a `.invalid` placeholder, which
   is undeliverable by RFC 2606, so a premature switch to `send` fails safe.
   For reference, the ACH equivalent uses `AddEquipmentService@elavon.com`; the CCO address
   is likely different — confirm with Ops.
2. Replace the placeholder email wording (the body is marked `[PLACEHOLDER]`).
3. Point `slack_channel` off `n8n-sandbox-of-doom` at a real channel.
4. Only then set `email_mode` to `send`.

`Platform Factory Inc. - 8040466289` sits in the ready set and looks like an internal test
merchant. It is `baseline` so it will never be sent, but consider excluding it explicitly.

## Design decisions that are load-bearing

**"New" means "ready and not in the tracking table", never "created recently".** A merchant
becomes eligible when its partner flag or fee schedule changes, which can be years after
signup, so a `createdAt` watermark would silently miss merchants. `Plan` diffs the full
eligible set (91 rows) against the table every run — cheap at this size.

**`Collapse` exists to stop an N×M fan-out.** The data-table read runs once per input item,
so without collapsing to a single item first the eligibility query would execute once per
existing row. This is the same trap that produced 44,944 rows (212×212) during the
commodity-table load.

**`alwaysOutputData` on `Get existing records`** — the table was empty on the first run and
without it nothing downstream executes at all.

**`Claim merchant` writes `processing` *before* the email is created.** Claim-then-act makes
this at-most-once: a crash leaves a visible stuck `processing` row, whereas act-then-record
would re-send on the next run. Duplicate submissions to a processor are the failure mode
worth over-engineering against.

**`mode: each` on both `executeWorkflow` calls**, so one merchant's failure cannot take the
batch down and each PDF binary stays paired to its own item.

**Slack is deliberately off the PDF path.** `Slack - Create a base message` returns its own
item shape and drops binary — which is why `Elavon ACH Enrollment Project` has to merge it
back by MID. Instead `Attach slack thread` re-reads `$('Plan').all()` and stamps the thread
onto each merchant, leaving `Claim → Build CCO PDF → Send CCO email` untouched. Verified the
156 kB PDF survives to the send node.

**`Post Slack base message` is best-effort** (`onError: continueRegularOutput`). If Slack is
down you lose notifications but the enrollment emails still go out; the reverse would be
worse.

## Two non-obvious requirements of `Send Email: HTML`

Both cost a debugging cycle and are easy to reintroduce:

1. **`passthrough_item` is mandatory.** Its `Edit Fields3` node does
   `jsonOutput = {{ trigger.passthrough_item }}` on the no-Slack-thread path and throws
   `Cannot convert undefined or null to object` when absent. It is also how `merchant_id`
   is echoed back to us, which is what the update nodes key on.
   [[slack-create-a-base-message]] has the identical requirement.
2. **`skip_email` and `create_draft` both default to `true` when null**
   (`$json.skip_email == null ? true : ...`). Omitting `skip_email` silently skips every
   email. Both are passed explicitly, and `convertFieldsToString` is **off** — as a string,
   `"false"` is truthy and would invert both.

`partner: "PE"` selects the PayEngine sending inbox (`Hearth` / `Supermove` are the others);
confirmed the draft comes from `"PayEngine Merchants" <merchants@payengine.co>`.

## Retry policy

`Classify failure` splits failures into retryable and hopeless, so the hourly schedule does
not re-attempt an impossible merchant 24 times a day:

- `failed` — transient (download 500, timeout). Retried while `attempt_count < max_attempts`.
- `skipped` — permanent; needs a data fix (MCC absent from Elavon's guide, non-numeric
  `mcc_sic`, no Elavon MID). Never retried.

## Gotcha for future edits

The data-table write nodes declare **only the columns they write**. Declaring the full
18-column table schema made the n8n UI render every other column as an empty editable field,
which reads as "these will be blanked" — they were omitted at runtime, but it is one
keystroke away from wiping real data. With n8n's resource mapper, *what the panel displays
is not what gets written*: the panel reflects the declared schema, and only entries with
values are sent. Same family of trap as an unset boolean rendering as ON.

<!-- manual:end -->
