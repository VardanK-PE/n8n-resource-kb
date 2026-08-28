---
n8n_id: "MBqVe38zwY65TThs"
instance: v1
name: "Merchant Transactions Daily Summary"
status: active
last_modified: 2024-10-25T17:18:28.395Z
tags: []
fingerprint: "0edaba521dc9e02e40003b3f6fc82922101f0d492227770b0dc268a911268d6c"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Merchant Transactions Daily Summary

## Summary

- **Status:** active
- **n8n ID:** `MBqVe38zwY65TThs`
- **Nodes:** 9
- **Last modified:** 2024-10-25T17:18:28.395Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `e3c8a80d-59a2-4a64-95a4-6ee5cc6d4da6`) — `hourly at :05`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `3b62f7ae-52ac-4e6e-a360-bb588a78d64c`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres - w/ MTD and YTD, not formatted" (id `3c06c743-76b8-457c-84af-6b8d67616902`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `5c972407-03a5-4573-8add-e2dc3a0449fb`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `88c8a4e7-0b69-43fe-a15f-d349439e8956`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres- w/o MTD and YTD" (id `f3978116-f5a5-448f-8714-91bf32f15d8e`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `3b62f7ae-52ac-4e6e-a360-bb588a78d64c`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres - w/ MTD and YTD, not formatted" (id `3c06c743-76b8-457c-84af-6b8d67616902`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres- w/o MTD and YTD" (id `f3978116-f5a5-448f-8714-91bf32f15d8e`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
