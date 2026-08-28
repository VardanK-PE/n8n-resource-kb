---
n8n_id: "fpxXdFGN6xhmWbJX"
instance: v1
name: "Local Line Merchant Exports"
status: inactive
last_modified: 2024-08-22T23:00:01.525Z
tags: []
fingerprint: "e364e6211fe12a4cf78edddd2519ead192049b50c68a6541373c3857bc80e63a"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Local Line Merchant Exports

## Summary

- **Status:** inactive
- **n8n ID:** `fpxXdFGN6xhmWbJX`
- **Nodes:** 7
- **Last modified:** 2024-08-22T23:00:01.525Z

## Triggers

- **manual** — node "When clicking "Test workflow"" (id `3df322d4-6f92-4b9c-9d59-d2914374ac02`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `6ef300d8-226f-4d36-b29f-85179060a0e1`)
- [[../resources/credentials/dejozqgfjq7qoncj|PGP key (jeffery@platformfactory.io)]] (`pgpKey`, id `DeJOzqGfjQ7QOncJ`) — node "PGP" (id `d7712cb8-a057-4fae-a924-38c10f2930f2`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `6ef300d8-226f-4d36-b29f-85179060a0e1`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-pgp|n8n-nodes-pgp]] — type `n8n-nodes-pgp.PGP` — node "PGP" (id `d7712cb8-a057-4fae-a924-38c10f2930f2`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
