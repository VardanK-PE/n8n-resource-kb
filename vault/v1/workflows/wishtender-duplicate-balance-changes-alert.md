---
n8n_id: "AkPU4SjqKbuNu4Pb"
instance: v1
name: "Wishtender Duplicate Balance Changes Alert"
status: active
last_modified: 2024-10-25T17:19:56.527Z
tags: []
fingerprint: "7068dd7270e57477444cb73c5ababd5c527d13aa49c8fe50fafb055ebbea2f2e"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Wishtender Duplicate Balance Changes Alert

## Summary

- **Status:** active
- **n8n ID:** `AkPU4SjqKbuNu4Pb`
- **Nodes:** 5
- **Last modified:** 2024-10-25T17:19:56.527Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `4db937f1-9ca3-41a9-aae5-c37f5de0b137`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `4876919f-4bc6-4069-bd2b-fa8ae09d8a92`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres account]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `f526fb43-e864-43ee-a700-482b5d9e55f5`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres account)]] — op `executeQuery` — node "Postgres" (id `f526fb43-e864-43ee-a700-482b5d9e55f5`)

### Slack channels

- [[../resources/slack-channels/c06haphnnem|wishtender-internal]] (id `C06HAPHNNEM`) — op `channel` — node "Slack" (id `4876919f-4bc6-4069-bd2b-fa8ae09d8a92`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
