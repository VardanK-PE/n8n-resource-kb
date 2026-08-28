---
n8n_id: "rFnI8ZlZh8Bj0qo7"
instance: v1
name: "Elavon_SFTP_Alerts"
status: inactive
last_modified: 2024-10-25T17:13:47.307Z
tags: []
fingerprint: "2d646981e5f8127fefa7ee0715fd328bcf67b632eeccccd91b17ea54b1fc1e11"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Elavon_SFTP_Alerts

## Summary

- **Status:** inactive
- **n8n ID:** `rFnI8ZlZh8Bj0qo7`
- **Nodes:** 7
- **Last modified:** 2024-10-25T17:13:47.307Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `c7acd17d-2820-430d-b144-919b27485dbb`) — `every 1 hour(s)`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "ElavonFiles" (id `421cba54-07f0-4984-8a58-0da5330dac13`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "ElavonBatchData" (id `86b229cd-e4ff-4556-adf8-d6122490123c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `b3fbefd4-9c9e-4d30-907c-1839ab2a8bed`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `ce93c5ec-55f8-46c2-8301-20064f4cebdf`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "ElavonFiles" (id `421cba54-07f0-4984-8a58-0da5330dac13`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "ElavonBatchData" (id `86b229cd-e4ff-4556-adf8-d6122490123c`)

### Slack channels

- [[../resources/slack-channels/c077w62bd7w|ops_alerts]] (id `C077W62BD7W`) — op `channel` — node "Slack1" (id `b3fbefd4-9c9e-4d30-907c-1839ab2a8bed`)
- [[../resources/slack-channels/c077w62bd7w|ops_alerts]] (id `C077W62BD7W`) — op `channel` — node "Slack" (id `ce93c5ec-55f8-46c2-8301-20064f4cebdf`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
