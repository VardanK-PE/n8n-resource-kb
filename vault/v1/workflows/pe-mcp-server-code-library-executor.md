---
n8n_id: "0vil2rHs6k3EOv6J"
name: "PE MCP Server: Code Library Executor"
status: inactive
last_modified: 2025-12-21T16:08:05.565Z
tags: []
fingerprint: "d6f1a576283d2124b367c2b37fb3b97f85c7ecc5fd119f115439f2847120239d"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PE MCP Server: Code Library Executor

## Summary

- **Status:** inactive
- **n8n ID:** `0vil2rHs6k3EOv6J`
- **Nodes:** 4
- **Last modified:** 2025-12-21T16:08:05.565Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `ab6356e1-67a9-4a83-8d23-a6a866fa84ff`)

## Depends on

### Credentials

- [[../resources/credentials/rlxlkmcb9jzcnyyk|Postgres ST production read replica]] (`postgres`, id `rlXLkMcb9jzcnYYK`) — node "Execute a SQL query" (id `3112c9dc-2c49-4a67-abe3-c28a79047b2f`)

### Databases

- [[../resources/databases/postgres-rlxlkmcb9jzcnyyk|postgres (via Postgres ST production read replica)]] — op `executeQuery` — node "Execute a SQL query" (id `3112c9dc-2c49-4a67-abe3-c28a79047b2f`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
