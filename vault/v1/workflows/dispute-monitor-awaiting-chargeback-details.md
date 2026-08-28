---
n8n_id: "CTTTMXZgE1E1owyB"
instance: v1
name: "Dispute - Monitor awaiting chargeback details"
status: active
last_modified: 2026-01-09T17:28:18.918Z
tags: []
fingerprint: "8ccaf4e17ab42fe5895aa1820171893a06e9d29271f0bd92ab023548320bfcaf"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Dispute - Monitor awaiting chargeback details

## Summary

- **Status:** active
- **n8n ID:** `CTTTMXZgE1E1owyB`
- **Nodes:** 15
- **Last modified:** 2026-01-09T17:28:18.918Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `1556ed12-79d1-446c-9684-cf51069ab0b5`)
- **schedule** — node "Schedule Trigger" (id `a6598599-72a1-4ccc-b4f6-831b94985519`) — `every 12 hour(s)`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `3b52870b-9def-4e5f-9629-267b942f22d6`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `42c8c140-5e7a-41a5-8b2f-ebc96b01ff42`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Clear sheet" (id `76ffa21f-d0e7-4670-b432-88059f3289a7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `7c3e5ccd-f990-437c-bdec-24daa1c6ae63`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `d3e65b3f-68a6-41c4-844d-41ad4f8ac9d6`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `42c8c140-5e7a-41a5-8b2f-ebc96b01ff42`)

### Google Sheets

- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Get row(s) in sheet" (id `3b52870b-9def-4e5f-9629-267b942f22d6`)
- [[../resources/google-sheets/1wmpz3rfpxz7mconomolfgiquisbmq6-yhy6nokjlfmc|Daily Report - Awaiting Chargeback Transactions]] (id `1wmPZ3RFPxZ7mcONOmOLFGIQUISBmq6-YhY6Nokjlfmc`) — op `clear`, tab `Transactions` — node "Clear sheet" (id `76ffa21f-d0e7-4670-b432-88059f3289a7`)
- [[../resources/google-sheets/1wmpz3rfpxz7mconomolfgiquisbmq6-yhy6nokjlfmc|Daily Report - Awaiting Chargeback Transactions]] (id `1wmPZ3RFPxZ7mcONOmOLFGIQUISBmq6-YhY6Nokjlfmc`) — op `append`, tab `Transactions` — node "Append row in sheet" (id `7c3e5ccd-f990-437c-bdec-24daa1c6ae63`)
- [[../resources/google-sheets/1wmpz3rfpxz7mconomolfgiquisbmq6-yhy6nokjlfmc|Daily Report - Awaiting Chargeback Transactions]] (id `1wmPZ3RFPxZ7mcONOmOLFGIQUISBmq6-YhY6Nokjlfmc`) — op `update`, tab `Transactions` — node "Update row in sheet" (id `d3e65b3f-68a6-41c4-844d-41ad4f8ac9d6`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
