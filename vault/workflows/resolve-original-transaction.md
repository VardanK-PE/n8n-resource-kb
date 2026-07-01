---
n8n_id: "VEpBuJNtK176eCyn"
name: "Resolve Original Transaction"
status: inactive
last_modified: 2025-11-05T13:58:38.914Z
tags: []
fingerprint: "b3efaa56b01baa8e044c61abd91d156732b42bf8c0eeba2b980053a261fa5219"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Resolve Original Transaction

## Summary

- **Status:** inactive
- **n8n ID:** `VEpBuJNtK176eCyn`
- **Nodes:** 19
- **Last modified:** 2025-11-05T13:58:38.914Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `44b1f558-4d49-472b-8723-e4be1ffb8739`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request transaction details" (id `56a272c5-02a2-4a07-91f3-798fe6f0d219`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request transaction details3" (id `60200f23-23b8-4d48-8e20-9cc84e636983`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request transaction details2" (id `b141837e-e0cc-4534-a44a-4cc17d182b7b`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request transaction details1" (id `dece334b-61c8-4172-9bf7-5146f949619f`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request transaction details" (id `56a272c5-02a2-4a07-91f3-798fe6f0d219`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request transaction details3" (id `60200f23-23b8-4d48-8e20-9cc84e636983`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request transaction details2" (id `b141837e-e0cc-4534-a44a-4cc17d182b7b`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request transaction details1" (id `dece334b-61c8-4172-9bf7-5146f949619f`)

## Used by (workflows)

- [[elavon-disputes-reporting|Elavon Disputes Reporting]] — node "Call 'Resolve Original Transaction'" (id `4153bd49-05fc-476e-8f01-22176b267e96`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
