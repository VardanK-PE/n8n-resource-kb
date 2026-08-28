---
n8n_id: "pY3AYD2FHkRWCY4w"
name: "Supermove Failed Refund Alerts"
status: inactive
last_modified: 2024-06-29T00:30:55.143Z
tags: []
fingerprint: "971218e8cf8e3dbb4033b9d5679451132ebc81e804955069753ace86bd319fb8"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Supermove Failed Refund Alerts

## Summary

- **Status:** inactive
- **n8n ID:** `pY3AYD2FHkRWCY4w`
- **Nodes:** 2
- **Last modified:** 2024-06-29T00:30:55.143Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `c5c37296-e88c-43af-8a06-4d67efc56062`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `e3a66a7c-237b-484c-9a53-3e91df4d7923`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `e3a66a7c-237b-484c-9a53-3e91df4d7923`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
