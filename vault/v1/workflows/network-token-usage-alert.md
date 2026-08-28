---
n8n_id: "EKauDa1N1I7F1HXo"
instance: v1
name: "Network Token Usage Alert"
status: active
last_modified: 2024-10-25T17:18:22.744Z
tags: []
fingerprint: "82a1daa27919a377241c0c8b214fa99829875b73fc5d6a448fe2457c4c75fddc"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Network Token Usage Alert

## Summary

- **Status:** active
- **n8n ID:** `EKauDa1N1I7F1HXo`
- **Nodes:** 9
- **Last modified:** 2024-10-25T17:18:22.744Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `8f7023c1-526b-44b0-ab88-250f0fbbb793`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `212455f7-6b82-4e4a-989f-cd28325ea2b3`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `8afe116c-556b-43c5-9762-5d42a34c2c83`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `8efdbe7a-d0de-46b9-b940-9c45bd22d4ab`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `d9f87cdf-83e0-4f58-8a9c-5a0a2488da50`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `212455f7-6b82-4e4a-989f-cd28325ea2b3`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `8afe116c-556b-43c5-9762-5d42a34c2c83`)

### Slack channels

- [[../resources/slack-channels/transaction-anomalies|transaction-anomalies]] (id `transaction-anomalies`) — op `channel` — node "Slack" (id `8efdbe7a-d0de-46b9-b940-9c45bd22d4ab`)
- [[../resources/slack-channels/transaction-anomalies|transaction-anomalies]] (id `transaction-anomalies`) — op `channel` — node "Slack1" (id `d9f87cdf-83e0-4f58-8a9c-5a0a2488da50`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
