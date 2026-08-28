---
n8n_id: "GkK1uh8fpTkIK2MW"
name: "ST Prod Batch Settlements Monitor"
status: active
last_modified: 2025-06-26T13:03:48.850Z
tags: []
fingerprint: "14850102ff493cdb33d7a90404f9b4182467e089bf187473fc448d694168175b"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# ST Prod Batch Settlements Monitor

## Summary

- **Status:** active
- **n8n ID:** `GkK1uh8fpTkIK2MW`
- **Nodes:** 4
- **Last modified:** 2025-06-26T13:03:48.850Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `936a5831-20b8-4c95-8591-373c41c23920`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `44d7dbaa-f816-42a4-82d4-bc62b4908199`)
- [[../resources/credentials/2ororcdmsnjxthsy|Postgres ST Prod Sierra DB Replica]] (`postgres`, id `2orOrcdMsnJXThSY`) — node "Postgres" (id `73be8892-fd41-47fb-b6da-d53932b6764e`)

### Databases

- [[../resources/databases/postgres-2ororcdmsnjxthsy|postgres (via Postgres ST Prod Sierra DB Replica)]] — op `executeQuery` — node "Postgres" (id `73be8892-fd41-47fb-b6da-d53932b6764e`)

### Slack channels

- [[../resources/slack-channels/c08nyf47mup|st-payment-failures-prod]] (id `C08NYF47MUP`) — op `channel` — node "Slack" (id `44d7dbaa-f816-42a4-82d4-bc62b4908199`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
