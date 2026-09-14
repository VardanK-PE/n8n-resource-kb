---
n8n_id: "ajjvV2MZyEtuMj49"
instance: v1
name: "Curbwaste Merchant MCC4900 Notification"
status: inactive
last_modified: 2026-09-14T19:00:38.575Z
tags: []
fingerprint: "989fef185aa879be09006f460fa7b6c80c6330b1b910063a8aff6761e89fadd0"
auto_generated_at: 2026-09-14T19:01:33Z
---

<!-- auto:start -->

# Curbwaste Merchant MCC4900 Notification

## Summary

- **Status:** inactive
- **n8n ID:** `ajjvV2MZyEtuMj49`
- **Nodes:** 22
- **Last modified:** 2026-09-14T19:00:38.575Z

## Triggers

- **schedule** — node "Every 4 hours" (id `22220000-0000-4000-8000-000000000001`) — `every 4 hour(s)`
- **manual** — node "When clicking ‘Execute workflow’" (id `22220000-0000-4000-8000-000000000002`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Find eligible" (id `22220000-0000-4000-8000-000000000006`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Find eligible" (id `22220000-0000-4000-8000-000000000006`)

### Data tables (n8n)

- [[../resources/data-tables/fehmmyxwrdom0xhx|Curbwaste - MCC4900 Notifications]] (id `FEHmmYXWRDom0XHX`) — op `get` — node "Get existing records" (id `22220000-0000-4000-8000-000000000004`)
- [[../resources/data-tables/fehmmyxwrdom0xhx|Curbwaste - MCC4900 Notifications]] (id `FEHmmYXWRDom0XHX`) — op `upsert` — node "Write baseline" (id `22220000-0000-4000-8000-00000000000c`)
- [[../resources/data-tables/fehmmyxwrdom0xhx|Curbwaste - MCC4900 Notifications]] (id `FEHmmYXWRDom0XHX`) — op `upsert` — node "Claim merchant" (id `22220000-0000-4000-8000-00000000000d`)
- [[../resources/data-tables/fehmmyxwrdom0xhx|Curbwaste - MCC4900 Notifications]] (id `FEHmmYXWRDom0XHX`) — op `update` — node "Record outcome" (id `22220000-0000-4000-8000-000000000011`)

### Sub-workflows (Execute Workflow calls)

- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Post Slack base message" (id `22220000-0000-4000-8000-000000000009`)
- [[send-email-html|Send Email: HTML]] (n8n_id `H9qPciXCz00KxAyF`) — node "Call 'Send Email: HTML'" (id `22220000-0000-4000-8000-00000000000f`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Post run tally" (id `22220000-0000-4000-8000-000000000013`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

## Purpose

Every 4 hours, finds Curbwaste merchants that have newly gone **active** with **MCC 4900**
and emails each one Visa's Utility Program enrolment instructions plus their Elavon MID, via
[[send-email-html]]. Records every notification in
[[../resources/data-tables/fehmmyxwrdom0xhx|Curbwaste - MCC4900 Notifications]] so it happens
exactly once, and reports each run into a Slack thread through
[[slack-create-a-base-message]] / [[slack-send-notification]].

Visa only accepts a **direct merchant request** for the Utilities Program — an acquirer or
partner cannot enrol them. So the deliverable is an email telling the merchant how to do it
themselves, with the one piece of data they cannot look up: the Elavon MID.

Built 2026-09-10/14. Spec: `agent-os/specs/2026-09-10-2239-curbwaste-mcc4900-notifier/`,
which also holds `build-workflow.py` — the generator this workflow's JSON was PUT from.

## Current state — production config, DEACTIVATED

`run_mode: notify`, `delivery_mode: send`, `slack_channel: ops-automation-alert`, and
`active: false` by deliberate choice (2026-09-14). Nothing runs until someone activates it.

All **103** tracked merchants sit at `baseline` and will **never** be emailed — that is what
the backfill was for. Notifying the existing book is a separate, deliberate act, not something
the schedule will drift into. The first live run therefore selects **nothing** until a
genuinely new merchant activates with MCC 4900.

ADM Rolloff LLC (`9c521b6f-9f4f-4db5-9931-ebcf0e4ff683`) was the draft-test subject and landed
at `simulated`, which counts as **unfinished** and would have been emailed on the next run. It
was hand-set to `baseline` on 2026-09-14 — the right call over `notified`, which would have
been a lie: it only ever received a draft. Both statuses are equally non-reprocessable in
`Plan`, so the effect is the same and the record stays honest.

## Why the HTML sender and not the simple-text one

Originally built on [[send-email-simple-text]] as specified. Switched to
[[send-email-html]] on 2026-09-14 because the enrolment URL would not render as a link.

In plain text there is no anchor markup, so clickability is entirely at the mercy of the
**receiving** client's autolinker. Writing the bare `VisaAccess.com` from the original copy
guaranteed failure (Gmail will not linkify a schemeless domain); adding
`https://www.visaaccess.com` should have worked on receipt, but **Gmail's plain-text composer
never linkifies anything**, so a draft could not be used to verify it — the `mailto:` address
in the same body was equally unlinked. Rather than ship 100+ merchant emails on "it probably
linkifies once delivered", the body became HTML with an explicit `<a href>`.

The swap was cheap because the two senders are **interface-identical**: same 11 inputs and
types, same returned status vocabulary (`notified` / `notification_failed` / `email_skipped` /
`email_not_provided`), same `is_pe_inbox` rule, and the same fail-safe
`x == null ? true : x` defaults on both `create_draft` and `skip_email`. Verified node-by-node
before switching. Reverting is a one-line change to the `workflowId`, plus restoring the
plain-text body block.

**Merchant names are HTML-escaped** in `Build email`. This is not theoretical — `S&P Dumpsters`
and `Superior Waste & Recycling` are both in the eligible set and would emit broken markup raw.

## The safety ladder

One config field, `delivery_mode`, drives both flags on the sub-workflow call:

| `delivery_mode` | `skip_email` | `create_draft` | Effect |
|---|---|---|---|
| `dry-run` | true | true | Gmail **never invoked**. Table + Slack only. |
| `draft` | false | true | Gmail `resource: draft` → draft in merchants@platformfactory.io. Nothing sent. |
| `send` | false | false | Live send. |

Safe by construction: `Set Email Parameters` inside [[send-email-html]] does
`skip_email == null ? true : skip_email` and the same for `create_draft`, so a **missing**
field cannot cause a send. The failure mode is a silent no-op, not a leak.

## Design decisions that are load-bearing

**"New" means "eligible and not in the tracking table"**, never an `activated_at` watermark.
Proven by the backfill: the 103 eligible merchants' activation dates span
**2022-02-19 → 2026-08-28**, so any timestamp cutoff would have missed nearly the whole book.
A merchant can also become eligible long after signup via an MCC edit or a reactivation.

**`Classify outcome` trusts OUR `delivery_mode`, not the child's status.** This fired for real
in the draft test: [[send-email-html]] returned `status: "notified"` with a
`message_id` for what was only a **draft** (`Edit Fields1` sets `notified` on the draft path
too). Believing it would have marked ADM Rolloff permanently done off an unsent draft. The
node overrides to `simulated` whenever `delivery_mode !== 'send'`.

**`Claim merchant` writes `processing` BEFORE the email.** Claim-then-act makes this
at-most-once: a crash leaves a visible stuck row rather than re-emailing on the next tick.
Duplicate merchant emails are the failure mode worth over-engineering against.

**`Collapse` stops an N×M fan-out.** The data-table read emits one item per existing row, so
without folding to a single item first the Postgres query would run once per tracked merchant.
Verified on the idempotency run: 103 rows in, 1 item out, 1 query.

**`alwaysOutputData` on `Get existing records`** — the table was empty on the first run and
without it nothing downstream executes at all.

**`Plan` always emits a `report` item as item 0**, so a quiet run still reaches Slack — that is
how you tell "nothing new" from "the monitor is dead". `Attach slack thread` filters it back
out. It rides along rather than going through workflow static data (which would persist
between runs) or being recomputed downstream (which would duplicate every gate and let the two
drift).

**A data-table write returns the WRITTEN ROW, not the item that went in.** `business_name` and
the Slack thread ts do not survive `Claim merchant`, which is why `Build email` re-attaches
them from `Attach slack thread` by `merchant_id`. Caught in review, before it shipped.

**Data-table write nodes declare only the columns they write.** Declaring the full schema
makes the n8n UI render every other column as an empty editable field — omitted at runtime,
but one keystroke from wiping real data.

**`activated_at` / `notified_at` write `null`, never `''`.** They are dateTime columns and an
empty string is not a valid value for one.

**Both Slack calls are best-effort** (`continueRegularOutput`). Losing the report is better
than losing the notification. `passthrough_item` is mandatory on both sub-workflows — they do
`jsonOutput = {{ trigger.passthrough_item }}` on the no-thread path and throw without it.

**`partner: "Curbwaste"` routes to the PE inbox.** [[send-email-html]]'s `is_pe_inbox`
rule is `partner != 'Supermove' && partner != 'Hearth'`, so any other value lands on
`merchants@platformfactory.io` — which matches the signature line.

## MCC: Postgres only, and why

The gate is `merchant.data->'business_type'->>'mcc_sic'` normalised (strip leading zeros;
reject non-numeric like `"5999J"`, never coerce). See
[[../resources/databases/postgres-bdw1qodl0v7mywj6]].

**Elavon's assigned MCC is deliberately NOT consulted.** An earlier build cross-checked
excluded merchants against [[../resources/data-tables/eefxih6vfsgkmssi|Elavon - MIDs]] and
found 8 of them boarded by Elavon as 4900. That branch was **removed** on instruction
(2026-09-14): `Elavon - MIDs` mirrors the Elavon BI spreadsheet via
[[elavon-mids-to-data-tables-sync]], which is **inactive** with no schedule trigger — rows
still read `Last_Sync 2025-11-15` — and the spreadsheet itself is suspected of sync problems.
Do not wire either source back into the eligibility decision.

Instead the Slack report **names** merchants excluded on MCC that are otherwise emailable, so
the merchant record gets fixed upstream in PayEngine. As of 2026-09-14 that list is 9:
Atlantic Trash and Transfer Scale (empty), Dump and Delivery (7394), Homestead Disposal
(7299), KC Dumpster (1799), Nu-Way Roll Off (4789), Nu-Way Bin Rentals (7299), S&P Dumpsters
(5039), Tristate Transfer (5039), Warren Disposal (7299).

## Gotchas for future edits

**A sub-workflow returns its LAST node's output.** If you append a node to
[[send-email-html]], check what this caller then receives — `Classify outcome` reads
`status`, `message_id` and the `passthrough_item` fields off it.

**[[send-email-html]] has a latent bug on its no-email path.** `Edit Fields` sets
`result=email_not_provided` but never `status`, so `Switch1`'s "Email not provided" output can
never match. This workflow does not rely on it — `Plan` gates empty emails itself with
`skipped/no_email`.

**n8n data tables have no public API.** The table had to be created by hand in the UI, and the
four node references carry its id literally. Verified against the instance's own
`/api/v1/openapi.yml`; `/rest/projects/{id}/data-tables` exists but needs a browser cookie.

**Rebuild via the generator, not the UI**, if you are making structural changes —
`agent-os/specs/2026-09-10-2239-curbwaste-mcc4900-notifier/build-workflow.py`, then PUT it.
Hand edits in the canvas and the generator will diverge.

## Verification performed (2026-09-10 → 14)

| Step | Execution | Result |
|---|---|---|
| Wiring via `scripts/jq/` | — | schedule 4h, 3 sub-workflows resolve, credential attached |
| `backfill` + `dry-run` | `19318328` | 113 active → 103 baselined, 0 Gmail calls |
| Idempotency re-run | `20073545` | 0 selected, 0 written, Slack still reported |
| `notify` + `draft` | `20076259` | 1 draft (ADM Rolloff LLC, MID 8046706399), row → `simulated` |
| Live send | — | **not yet performed** |

<!-- manual:end -->
