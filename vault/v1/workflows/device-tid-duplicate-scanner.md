---
n8n_id: "YlxMWB42htfwFgyC"
instance: v1
name: "Device TID duplicate scanner"
status: active
last_modified: 2024-10-26T18:51:55.661Z
tags: []
fingerprint: "770186bb406b2c80730a77b07b0f5c9a924ab69aa005ed8cc23a444766b039f4"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Device TID duplicate scanner

## Summary

- **Status:** active
- **n8n ID:** `YlxMWB42htfwFgyC`
- **Nodes:** 3
- **Last modified:** 2024-10-26T18:51:55.661Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `0dd5bc64-41ad-4ef9-a294-63951c2c9926`) — `every 15 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `2a303a08-fce3-4f97-9ef1-e5202a71d891`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `ae698340-f3df-4c23-8307-34c71ea9d8dc`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `ae698340-f3df-4c23-8307-34c71ea9d8dc`)

### Slack channels

- [[../resources/slack-channels/c06c06y8tdh|transaction-alerts]] (id `C06C06Y8TDH`) — op `channel` — node "Slack" (id `2a303a08-fce3-4f97-9ef1-e5202a71d891`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
