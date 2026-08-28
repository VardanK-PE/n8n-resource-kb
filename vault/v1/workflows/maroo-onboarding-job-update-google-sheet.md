---
n8n_id: "u1NfJVTQF5e9STXa"
name: "Maroo Onboarding Job - Update Google Sheet"
status: inactive
last_modified: 2025-02-21T18:44:25.627Z
tags: []
fingerprint: "58f7e6ab4a97dfabf8a961965b9a6c8a051f226cf7ca90369a72bc56e062e0e3"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Maroo Onboarding Job - Update Google Sheet

## Summary

- **Status:** inactive
- **n8n ID:** `u1NfJVTQF5e9STXa`
- **Nodes:** 5
- **Last modified:** 2025-02-21T18:44:25.627Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `bd35fd33-fc59-459f-939f-7d15823c5a77`) — `every 7 hour(s)`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `39cfa820-2488-4e0b-bf22-30d00e88f8cf`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `7029afb4-fc23-44f9-bd56-debadefc7b5b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `95b7b408-bb21-4500-bd7f-b424115ab335`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `select`, table `{"__rl":true,"value":"merchant_processor_detail","mode":"list","cachedResultName":"merchant_processor_detail"}` — node "Postgres1" (id `39cfa820-2488-4e0b-bf22-30d00e88f8cf`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `7029afb4-fc23-44f9-bd56-debadefc7b5b`)

### Google Sheets

- [[../resources/google-sheets/1kenlzlm4bnsd-8fx9fuhudpy1qujsmuyhpmkkh11k9a|Maroo Data 23-Jan-25]] (id `1keNlZLM4BNSd-8fx9fuhUDpy1quJsMuYHpMkkh11K9A`) — op `update`, tab `Output` — node "Google Sheets" (id `95b7b408-bb21-4500-bd7f-b424115ab335`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
