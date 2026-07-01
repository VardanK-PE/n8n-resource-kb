---
n8n_id: "c4k0seLSEFK7ZEO5"
name: "Dispute - Resolve Chargeback Transaction Info"
status: inactive
last_modified: 2026-01-16T15:53:26.234Z
tags: []
fingerprint: "6e38f579008608fe06142f27a4ecbe11ae919d2885e108d41665545f446da7f8"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Dispute - Resolve Chargeback Transaction Info

## Summary

- **Status:** inactive
- **n8n ID:** `c4k0seLSEFK7ZEO5`
- **Nodes:** 13
- **Last modified:** 2026-01-16T15:53:26.234Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `943fa230-4db4-49a2-8df8-483ce1bb45b6`)
- **manual** — node "When clicking ‘Execute workflow’" (id `db20441a-0047-4b58-93d6-26223b73272a`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks4" (id `4feace24-98e7-40bf-b821-8f58d73c1b1b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `9fc2feaf-85ef-4df0-ae51-9deb158f6adf`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks4" (id `4feace24-98e7-40bf-b821-8f58d73c1b1b`)

### Google Sheets

- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Get row(s) in sheet" (id `9fc2feaf-85ef-4df0-ae51-9deb158f6adf`)

## Used by (workflows)

- [[dispute-case-handler|Dispute - Case Handler]] — node "Resolve case transactions - elavon" (id `883137a4-fb26-4978-baa6-849c0506eb7e`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Resolve case transactions - merchant" (id `de78e652-5f2e-4b1b-b4e0-79302f369884`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
