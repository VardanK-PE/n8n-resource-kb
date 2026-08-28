---
n8n_id: "JVLCqZtCjjHDPThc"
name: "Opus - Transactions without batch"
status: inactive
last_modified: 2026-06-11T17:28:52.189Z
tags: []
fingerprint: "a0f72b189a06eb96778db7c3f9ad0fc1c8fae664ec57931ab8f0be27debf5c3c"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Opus - Transactions without batch

## Summary

- **Status:** inactive
- **n8n ID:** `JVLCqZtCjjHDPThc`
- **Nodes:** 13
- **Last modified:** 2026-06-11T17:28:52.189Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `ad614a0f-f4c7-4b51-80df-63f189ae7a5c`)

## Depends on

### Credentials

- [[../resources/credentials/jc4f45um3ujq28gc|PF Prod Device Management Replica]] (`postgres`, id `JC4f45um3UjQ28Gc`) — node "Execute a SQL query2" (id `0990678a-2246-4d1b-a426-ea617d4525ae`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Clear sheet" (id `7abdf3dc-36fa-46de-b4da-593f69ed4106`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `c9974f9d-ab8c-49fc-9e22-7d0aed4d7648`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query1" (id `f1a05545-0760-4fe9-9ebc-d42709eabeee`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `f3689a3a-2f4a-4428-b495-14244d4fccb3`)

### Databases

- [[../resources/databases/postgres-jc4f45um3ujq28gc|postgres (via PF Prod Device Management Replica)]] — op `executeQuery` — node "Execute a SQL query2" (id `0990678a-2246-4d1b-a426-ea617d4525ae`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `c9974f9d-ab8c-49fc-9e22-7d0aed4d7648`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query1" (id `f1a05545-0760-4fe9-9ebc-d42709eabeee`)

### Google Sheets

- [[../resources/google-sheets/1sur9udlwhhc7ijsqevdktysokp8sezlpz9tzv-e2nnu|Opus terminal data - Temporary]] (id `1Sur9UDLwhhc7ijSQevDKTYSOKp8SEzlpZ9Tzv-E2NnU`) — op `clear`, tab `Sheet1` — node "Clear sheet" (id `7abdf3dc-36fa-46de-b4da-593f69ed4106`)
- [[../resources/google-sheets/1sur9udlwhhc7ijsqevdktysokp8sezlpz9tzv-e2nnu|Opus terminal data - Temporary]] (id `1Sur9UDLwhhc7ijSQevDKTYSOKp8SEzlpZ9Tzv-E2NnU`) — op `append`, tab `Sheet1` — node "Append row in sheet" (id `f3689a3a-2f4a-4428-b495-14244d4fccb3`)

### Data tables (n8n)

- [[../resources/data-tables/exdhb72q9l5gfpis|PAX - Terminal Details]] (id `ExDhB72Q9l5GfPiS`) — op `get` — node "Get row(s)1" (id `177b800a-192c-4fd1-9170-927af6557cc7`)
- [[../resources/data-tables/exdhb72q9l5gfpis|PAX - Terminal Details]] (id `ExDhB72Q9l5GfPiS`) — op `get` — node "Get row(s)" (id `7306f6da-b764-4902-a69d-c6de58e68252`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
