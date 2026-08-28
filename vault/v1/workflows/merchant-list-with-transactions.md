---
n8n_id: "wWBXsjy2ArhEslNz"
name: "Merchant list with transactions"
status: inactive
last_modified: 2025-09-12T08:29:21.191Z
tags: []
fingerprint: "3167072c6d3ebf6c6332230e0566caa52aadd18f4c682bd8db9f05851968db67"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Merchant list with transactions

## Summary

- **Status:** inactive
- **n8n ID:** `wWBXsjy2ArhEslNz`
- **Nodes:** 9
- **Last modified:** 2025-09-12T08:29:21.191Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `8bc5d010-1605-4e59-9f90-3e3281f5c9ac`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `34969043-5e20-4a11-926e-cfa73c38580f`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query3" (id `6d911d9b-ee29-48d1-8dad-ddced521ee09`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet1" (id `81e84269-a213-40bb-97a8-f6d32edfba1a`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query1" (id `a1324424-0ceb-462a-b51c-b4a1b4cb39b0`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query2" (id `d713a3a7-7fe0-42aa-9309-bc6a6b0622f9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `e1d0d657-a2c3-404f-a086-e4cb69945335`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `34969043-5e20-4a11-926e-cfa73c38580f`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query3" (id `6d911d9b-ee29-48d1-8dad-ddced521ee09`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query1" (id `a1324424-0ceb-462a-b51c-b4a1b4cb39b0`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query2" (id `d713a3a7-7fe0-42aa-9309-bc6a6b0622f9`)

### Google Sheets

- [[../resources/google-sheets/1zo4x3refhbqzihipfi6go8uppikifjpns8boog1c-jk|Merchant Details]] (id `1zO4x3RefhbQZiHIPfI6GO8UPPiKIfjPnS8bOOG1c-jk`) — op `appendOrUpdate`, tab `Sheet1` — node "Append or update row in sheet1" (id `81e84269-a213-40bb-97a8-f6d32edfba1a`)
- [[../resources/google-sheets/1zo4x3refhbqzihipfi6go8uppikifjpns8boog1c-jk|Merchant Details]] (id `1zO4x3RefhbQZiHIPfI6GO8UPPiKIfjPnS8bOOG1c-jk`) — op `appendOrUpdate`, tab `Transactions >= 75` — node "Append or update row in sheet" (id `e1d0d657-a2c3-404f-a086-e4cb69945335`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
