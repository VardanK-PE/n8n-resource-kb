---
n8n_id: "IM3wk08pLLTXawd2"
name: "Dispute - Create Report"
status: inactive
last_modified: 2026-06-24T18:43:52.419Z
tags: []
fingerprint: "e93b0a95f3bfc163c25e912df1a3abea935a6fba45ad7c2b3794f0f3c1eaf22c"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Dispute - Create Report

## Summary

- **Status:** inactive
- **n8n ID:** `IM3wk08pLLTXawd2`
- **Nodes:** 74
- **Last modified:** 2026-06-24T18:43:52.419Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `1f5d00b9-3e73-4684-aaf1-391932a3b7ca`)
- **manual** — node "When clicking ‘Execute workflow’" (id `de66584d-2df9-439e-a48d-2653215f3b9e`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `0331474f-c193-4c7a-8aca-b8cd08b0e340`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query1" (id `813fa6ef-08d9-4b70-9665-4ec9bd206531`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get transactions for period of time1" (id `c9b5a143-c0ea-40e6-883a-1f0d33fbf477`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `0331474f-c193-4c7a-8aca-b8cd08b0e340`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query1" (id `813fa6ef-08d9-4b70-9665-4ec9bd206531`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get transactions for period of time1" (id `c9b5a143-c0ea-40e6-883a-1f0d33fbf477`)

### Data tables (n8n)

- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)2" (id `1cb5619c-924c-4294-8ccd-8a5a537a0e18`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)1" (id `280d83ee-2935-4682-ac72-e15e712e7642`)
- [[../resources/data-tables/da1d723wdyigobvw|Dispute - Merchant Responses]] (id `DA1d723WDyIGoBVW`) — op `get` — node "Get row(s)4" (id `5e01ce8d-2824-4afe-b353-cecf523c8742`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)5" (id `98d44034-82b6-46b4-8c9b-5a7fc53c9c87`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)" (id `a0006edd-caa6-4485-b56b-5c5d106d4c0e`)
- [[../resources/data-tables/nkrufqkkpszwq07b|Dispute - Awaiting Processor Response]] (id `NkRUfQkkpsZWq07b`) — op `get` — node "Get row(s)3" (id `b4ee4dea-9cf3-40dd-b3da-54ab07b8e619`)

## Used by (workflows)

- [[dispute-automatic-report-generation|Dispute - Automatic report generation]] — node "Call 'Dispute - Create Report'" (id `40fc8949-ca53-4ea8-a3f4-a91f7435b009`)
- [[opsinternalbot-disputes-NSkdXVo1|OpsInternalBot - Disputes]] — node "Call 'Dispute - Create Report'" (id `4c69f224-6237-4419-a136-f5ea6ef86371`)
- [[opsinternalbot-disputes-v2|OpsInternalBot - Disputes v2]] — node "Call 'Dispute - Create Report'" (id `efce57bd-1c6e-4b2c-9cf0-ad60d70532b1`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
