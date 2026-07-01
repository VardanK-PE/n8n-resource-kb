---
n8n_id: "JowA2QmvBt4uIYrH"
name: "MyKaarma One-Off Merchant Exports"
status: inactive
last_modified: 2025-01-10T19:48:05.618Z
tags: []
fingerprint: "fad5e4389776fa9e1c51db725bbc3f1c5fe1b40f4806944449e4b1c9491d3991"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# MyKaarma One-Off Merchant Exports

## Summary

- **Status:** inactive
- **n8n ID:** `JowA2QmvBt4uIYrH`
- **Nodes:** 7
- **Last modified:** 2025-01-10T19:48:05.618Z

## Triggers

- **manual** — node "When clicking "Test workflow"" (id `e7099143-da1f-49b1-ba08-cba9dcccf58d`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `6d6889a4-a16a-4594-8446-6fcc82a1f3c6`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `6d6889a4-a16a-4594-8446-6fcc82a1f3c6`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-pgp|n8n-nodes-pgp]] — type `n8n-nodes-pgp.PGP` — node "PGP" (id `0a9e6a19-fc35-40ea-b68e-5fbd8143d019`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
