---
n8n_id: "gJZszflg27CLAH0v"
instance: v1
name: "[Deprecated] Hearth - Transaction Alerts"
status: inactive
last_modified: 2025-11-21T15:55:05.285Z
tags: []
fingerprint: "d42da95df016bad0683da25a275f2441e77580ce5f2c9cf1f670bf6afeecfcde"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# [Deprecated] Hearth - Transaction Alerts

## Summary

- **Status:** inactive
- **n8n ID:** `gJZszflg27CLAH0v`
- **Nodes:** 10
- **Last modified:** 2025-11-21T15:55:05.285Z

## Triggers

- **error** — node "Error Trigger" (id `0e0416c3-03cd-4405-874e-18dea2f42363`)
- **schedule** — node "Schedule Trigger" (id `f6df0d59-4bee-4acd-b6a1-e9a5782d6402`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `100756ca-ec42-4c11-bdbf-32b305fdaaf3`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `98d31742-a7b9-4da7-9fab-9f2cf3107c1f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `b00afa1c-bd9a-42af-83cf-0dcf22fc8c04`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `e2db5cce-6d56-42aa-a96c-3c64a9751f07`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Slack1" (id `e50be185-4566-41c3-8b04-3719fde316cd`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `100756ca-ec42-4c11-bdbf-32b305fdaaf3`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `98d31742-a7b9-4da7-9fab-9f2cf3107c1f`)

### Slack channels

- [[../resources/slack-channels/c09jr6ph8tx|n8n-sandbox-of-doom]] (id `C09JR6PH8TX`) — op `channel` — node "Slack" (id `b00afa1c-bd9a-42af-83cf-0dcf22fc8c04`)
- [[../resources/slack-channels/c09pc6hkhpy|payengine-ai-alerts]] (id `C09PC6HKHPY`) — op `channel` — node "Send a message5" (id `e2db5cce-6d56-42aa-a96c-3c64a9751f07`)
- [[../resources/slack-channels/c08tfuk2ndq|hearth-transaction-alerts]] (id `C08TFUK2NDQ`) — op `channel` — node "Slack1" (id `e50be185-4566-41c3-8b04-3719fde316cd`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
