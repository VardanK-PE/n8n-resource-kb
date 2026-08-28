---
n8n_id: "CRVEpRZuvZVprFiL"
instance: v1
name: "MyKaarma Weekly Merchant Exports"
status: inactive
last_modified: 2025-12-12T18:39:01.276Z
tags: []
fingerprint: "c6234dc628915b66dccea817eab82f874a54ba9cc6b0f3e613ba4b90f0c931dd"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# MyKaarma Weekly Merchant Exports

## Summary

- **Status:** inactive
- **n8n ID:** `CRVEpRZuvZVprFiL`
- **Nodes:** 4
- **Last modified:** 2025-12-12T18:39:01.276Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `49736d94-f39b-466e-a32c-32c8eb05d190`) — `every 1 week(s)`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `8237846b-12bc-42e1-a6b3-d3dde6e77db4`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `8237846b-12bc-42e1-a6b3-d3dde6e77db4`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
