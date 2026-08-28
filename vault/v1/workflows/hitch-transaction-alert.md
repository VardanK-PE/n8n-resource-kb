---
n8n_id: "XnkG5r6iy9Vrkie8"
instance: v1
name: "Hitch: Transaction Alert"
status: active
last_modified: 2026-01-29T15:38:21.733Z
tags: []
fingerprint: "5f65f7920b4cdbc1c9155aef8e86d236d032812e381844684adad0cade06ca14"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Hitch: Transaction Alert

## Summary

- **Status:** active
- **n8n ID:** `XnkG5r6iy9Vrkie8`
- **Nodes:** 8
- **Last modified:** 2026-01-29T15:38:21.733Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `a9a05d44-f758-4b34-be78-245bb30a5bef`) — `every 15 minute(s)`
- **manual** — node "When clicking ‘Execute workflow’" (id `ed019b76-fb02-41fb-90ca-15fed505264c`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `1ec8cfe4-e019-49b9-9f96-36e9ac7420d6`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `3628a5a9-66fa-463a-9ca1-2a862f9ee370`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `3628a5a9-66fa-463a-9ca1-2a862f9ee370`)

### Data tables (n8n)

- [[../resources/data-tables/ndquxgiwyxyofskq|Transaction Alerts - Hitch]] (id `ndqUxgIWYXYoFSkq`) — op `?` — node "Insert row" (id `ad14ede1-4462-4d78-804b-d14a4f43af21`)
- [[../resources/data-tables/ndquxgiwyxyofskq|Transaction Alerts - Hitch]] (id `ndqUxgIWYXYoFSkq`) — op `rowNotExists` — node "If row does not exist" (id `ebb55a43-a2c5-4894-be4e-4e42176026fb`)

### Slack channels

- [[../resources/slack-channels/c0a8sgx5p5f|hitch-alerts]] (id `C0A8SGX5P5F`) — op `channel` — node "Slack1" (id `1ec8cfe4-e019-49b9-9f96-36e9ac7420d6`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
