---
n8n_id: "kaos1lAi2PZ7wDAw"
instance: v1
name: "Elavon CCO - Enrollment Monitor"
status: inactive
last_modified: 2026-09-08T18:51:02.484Z
tags: []
fingerprint: "001581ba40ac5f4aed9992d089c766470ac0718fd2fc07f501efd2e5f933c546"
auto_generated_at: 2026-09-08T19:06:15Z
---

<!-- auto:start -->

# Elavon CCO - Enrollment Monitor

## Summary

- **Status:** inactive
- **n8n ID:** `kaos1lAi2PZ7wDAw`
- **Nodes:** 21
- **Last modified:** 2026-09-08T18:51:02.484Z

## Triggers

- **schedule** — node "Every hour" (id `11110000-0000-4000-8000-000000000001`) — `every 1 hour(s)`
- **manual** — node "When clicking ‘Execute workflow’" (id `11110000-0000-4000-8000-000000000002`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Find eligible" (id `11110000-0000-4000-8000-000000000006`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Post screenshot to Slack" (id `11110000-0000-4000-8000-000000000015`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Resolve Slack channel" (id `11110000-0000-4000-8000-000000000016`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Find eligible" (id `11110000-0000-4000-8000-000000000006`)

### Data tables (n8n)

- [[../resources/data-tables/7gmbnwaqh8zntima|Elavon - CCO Enrollments]] (id `7GMBNwAQh8ZNTiMA`) — op `get` — node "Get existing records" (id `11110000-0000-4000-8000-000000000004`)
- [[../resources/data-tables/7gmbnwaqh8zntima|Elavon - CCO Enrollments]] (id `7GMBNwAQh8ZNTiMA`) — op `upsert` — node "Write baseline" (id `11110000-0000-4000-8000-000000000009`)
- [[../resources/data-tables/7gmbnwaqh8zntima|Elavon - CCO Enrollments]] (id `7GMBNwAQh8ZNTiMA`) — op `upsert` — node "Claim merchant" (id `11110000-0000-4000-8000-00000000000a`)
- [[../resources/data-tables/7gmbnwaqh8zntima|Elavon - CCO Enrollments]] (id `7GMBNwAQh8ZNTiMA`) — op `update` — node "Mark failed" (id `11110000-0000-4000-8000-00000000000f`)
- [[../resources/data-tables/7gmbnwaqh8zntima|Elavon - CCO Enrollments]] (id `7GMBNwAQh8ZNTiMA`) — op `update` — node "Record outcome" (id `11110000-0000-4000-8000-000000000012`)

### Sub-workflows (Execute Workflow calls)

- [[elavon-cco-edit-merchant-application-cco-enrollment|Elavon CCO - Edit merchant application (CCO Enrollment)]] (n8n_id `Q16AhMTvfmtLzuI6`) — node "Build CCO PDF" (id `11110000-0000-4000-8000-00000000000b`)
- [[elavon-cco-submit-qualtrics-form|Elavon CCO - Submit Qualtrics form]] (n8n_id `1u22D61vqFen7q0m`) — node "Submit CCO form" (id `11110000-0000-4000-8000-00000000000c`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Post Slack base message" (id `11110000-0000-4000-8000-000000000013`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

## Purpose

Hourly monitor that finds merchants newly eligible for Elavon Commercial Card Optimization,
builds their enrollment PDF via
[[elavon-cco-edit-merchant-application-cco-enrollment]], submits it to Elavon's **Qualtrics
form** via [[elavon-cco-submit-qualtrics-form]], posts the resulting screenshot to Slack
through [[slack-send-notification-with-attachment]], and records the outcome in
[[../resources/data-tables/7gmbnwaqh8zntima|Elavon - CCO Enrollments]].

**Built 2026-09-07, switched from email to the Qualtrics form 2026-09-08. Currently INACTIVE
and in `fill` mode** — it fills the form and stops without submitting. See the "Flow
execution control" sticky note on the canvas.

## Why a form and not email

Elavon refused email intake for CCO enrollment and has no plans to add it. The only channel
is `https://usbank.az1.qualtrics.com/jfe/form/SV_9SvtaSacONfKrpI`
("Payment Optimization CCO Request Form"). The earlier email implementation via
[[send-email-html]] was removed entirely — do not reintroduce it.

## Before enabling

1. Review the latest screenshot in the Slack channel and confirm the filled form is correct.
2. Point `slack_channel` off `n8n-sandbox-of-doom` at a real channel.
3. Only then set `delivery_mode` to `submit`.

`Platform Factory Inc. - 8040466289` sits in the ready set. Since Platform Factory Inc *is*
the partner in Elavon's context, that is likely PayEngine's own account rather than a
merchant to enrol. It is `baseline` so it will never be submitted, but consider excluding it.

`MS0PFORM` (the Partner Short Name on the form) is **US-only** by Ops' note. Every eligible
merchant is US today and nothing enforces it — worth a guard if the eligible set widens.

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

**`Claim merchant` writes `processing` *before* the form is opened.** Claim-then-act makes
this at-most-once: a crash leaves a visible stuck `processing` row, whereas act-then-record
would re-submit on the next run. Duplicate submissions to a processor are the failure mode
worth over-engineering against.

**`mode: each` on the sub-workflow calls**, so one merchant's failure cannot take the batch
down and each PDF binary stays paired to its own item.

**Slack is deliberately off the PDF path.** `Slack - Create a base message` returns its own
item shape and drops binary — which is why `Elavon ACH Enrollment Project` has to merge it
back by MID. Instead `Attach slack thread` re-reads `$('Plan').all()` and stamps the thread
onto each merchant, leaving `Claim → Build CCO PDF → Submit CCO form` untouched. Verified the
156 kB PDF survives to the submitter.

**Both Slack calls are best-effort** (`onError: continueRegularOutput`). If Slack is down you
lose the evidence trail but the enrollment still proceeds and is still recorded; the reverse
would be worse.

## Slack: use the sub-workflows, not the node

[[slack-send-notification-with-attachment]] posts by **channel name** and then reuses the
channel id from its own message response for the file upload. That matters because Slack's
file upload rejects a channel *name* (`invalid_arguments`) with or without a leading `#` —
it needs an id. An earlier version of this workflow used the Slack node directly and had to
resolve the id itself; that node and its lookup were removed on 2026-09-08.

Worse, an **empty** channel id makes the upload *succeed* while storing the file where
nobody can see it — a silent loss of the evidence trail. Prefer the sub-workflow, which
never exposes that failure mode.

`passthrough_item` is mandatory on both Slack sub-workflows: each does
`jsonOutput = {{ trigger.passthrough_item }}` on its no-thread path and throws
`Cannot convert undefined or null to object` when absent.

## Retry policy

`Classify failure` splits failures into retryable and hopeless, so the hourly schedule does
not re-attempt an impossible merchant 24 times a day:

- `failed` — transient (download 500, timeout, browser hiccup). Retried while
  `attempt_count < max_attempts`.
- `skipped` — permanent; needs a data fix (MCC absent from Elavon's guide, non-numeric
  `mcc_sic`, no Elavon MID, a missing submitter config value, a dropdown option that is not
  on the form). Never retried.

`simulated` rows — a completed `fill` run — are treated as unfinished, so the merchant is
picked up again by a later `submit` run.

## Gotchas for future edits

**A stuck `mode: backfill` fails silently.** It does not error; it just writes baseline rows
and submits nothing. Check `Run mode` first if a run looks suspiciously quiet.

**The data-table write nodes declare only the columns they write.** Declaring the full
18-column table schema made the n8n UI render every other column as an empty editable field,
which reads as "these will be blanked" — they were omitted at runtime, but it is one
keystroke away from wiping real data. With n8n's resource mapper, *what the panel displays
is not what gets written*: the panel reflects the declared schema, and only entries with
values are sent. Same family of trap as an unset boolean rendering as ON.

**A sub-workflow returns its LAST node's output.** Ending the submitter on its Slack upload
once made this workflow record a row of nulls, because it received Slack's file object
instead of the fill result. If you append a node to a sub-workflow, check what the caller
now receives.

<!-- manual:end -->
