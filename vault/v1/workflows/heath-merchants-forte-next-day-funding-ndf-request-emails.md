---
n8n_id: "5S8DHEGcnRUFSOfM"
instance: v1
name: "Heath Merchants - Forte Next Day Funding (NDF) Request Emails"
status: inactive
last_modified: 2026-03-09T17:49:55.361Z
tags: []
fingerprint: "d55236e724031847165693cfdd92656089fd5f43ef32b91622b98ea03a1f8a98"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Heath Merchants - Forte Next Day Funding (NDF) Request Emails

## Summary

- **Status:** inactive
- **n8n ID:** `5S8DHEGcnRUFSOfM`
- **Nodes:** 30
- **Last modified:** 2026-03-09T17:49:55.361Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `dcf5e827-b9ae-400d-90e3-2933a448f579`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query1" (id `79a1a52d-326f-4609-86bb-cebb6240503e`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `95545e90-f9a2-47ac-8e80-3dd8674c8b73`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Delete partner sheets" (id `b8f1f15e-f6dd-47d2-acba-784c6ee232d3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Fill in the merchant info" (id `da62ced6-abf5-43cd-bc3a-9289681c6723`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create Partner spreadsheet" (id `e7bb7dd4-d914-4f2e-b26b-64a36351ba72`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query2" (id `f9c06f65-7a34-4830-8f62-a9f7780a0e2d`)

### HTTP URLs

- [[../resources/http-urls/pf-prod-ecs-task-container-gotenberg-3000|pf-prod-ecs-task-container-gotenberg:3000]] — `POST http://pf-prod-ecs-task-container-gotenberg:3000/forms/chromium/convert/html` — node "Convert To PDF [GOTENBERG]" (id `7e381729-caa0-459f-970e-cc4c3f0fedbe`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query1" (id `79a1a52d-326f-4609-86bb-cebb6240503e`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `95545e90-f9a2-47ac-8e80-3dd8674c8b73`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query2" (id `f9c06f65-7a34-4830-8f62-a9f7780a0e2d`)

### Google Sheets

- [[../resources/google-sheets/1i544spenddql307l3gkvlizkg5cum8o-1cn2qllontg|Forte NDF Enrollment Email Merchant List]] (id `1i544SPENDdql307l3gKvLizKG5CuM8o_1cn2QLlonTg`) — op `remove`, tab `={{ $json.partner }}` — node "Delete partner sheets" (id `b8f1f15e-f6dd-47d2-acba-784c6ee232d3`)
- [[../resources/google-sheets/1i544spenddql307l3gkvlizkg5cum8o-1cn2qllontg|Forte NDF Enrollment Email Merchant List]] (id `1i544SPENDdql307l3gKvLizKG5CuM8o_1cn2QLlonTg`) — op `appendOrUpdate`, tab `={{ $('Get Merchants for Report').item.json.partner }}` — node "Fill in the merchant info" (id `da62ced6-abf5-43cd-bc3a-9289681c6723`)
- [[../resources/google-sheets/1i544spenddql307l3gkvlizkg5cum8o-1cn2qllontg|Forte NDF Enrollment Email Merchant List]] (id `1i544SPENDdql307l3gKvLizKG5CuM8o_1cn2QLlonTg`) — op `create`, tab `null` — node "Create Partner spreadsheet" (id `e7bb7dd4-d914-4f2e-b26b-64a36351ba72`)

### Data tables (n8n)

- [[../resources/data-tables/l07eldv7wkow4jl0|Forte Next Day Funding Emails]] (id `L07eldV7wKow4jl0`) — op `get` — node "Get row(s)2" (id `182816bf-9f83-4dc5-bbb6-cec693067845`)
- [[../resources/data-tables/l07eldv7wkow4jl0|Forte Next Day Funding Emails]] (id `L07eldV7wKow4jl0`) — op `upsert` — node "Upsert row(s)" (id `219fb5c3-7d05-40a1-bb64-e51d5d6bbc4c`)
- [[../resources/data-tables/l07eldv7wkow4jl0|Forte Next Day Funding Emails]] (id `L07eldV7wKow4jl0`) — op `update` — node "Update row(s)1" (id `3515bd63-ced3-4af9-8fc5-5d8c893530cf`)
- [[../resources/data-tables/l07eldv7wkow4jl0|Forte Next Day Funding Emails]] (id `L07eldV7wKow4jl0`) — op `get` — node "Get Merchants for Report" (id `84c88eea-5dcf-4eed-a833-e80ee1c6e8ec`)
- [[../resources/data-tables/l07eldv7wkow4jl0|Forte Next Day Funding Emails]] (id `L07eldV7wKow4jl0`) — op `get` — node "Get row(s)" (id `b2141a09-86c7-4fee-8ba1-945fc17e94ad`)
- [[../resources/data-tables/l07eldv7wkow4jl0|Forte Next Day Funding Emails]] (id `L07eldV7wKow4jl0`) — op `get` — node "Get row(s)1" (id `bbd6a7c1-be02-4253-9cdc-059f634cfaff`)
- [[../resources/data-tables/l07eldv7wkow4jl0|Forte Next Day Funding Emails]] (id `L07eldV7wKow4jl0`) — op `update` — node "Update row(s)" (id `dcc4421b-4431-4bd7-9024-da972fcfba45`)

### Sub-workflows (Execute Workflow calls)

- [[send-email-html|Send Email: HTML]] (n8n_id `H9qPciXCz00KxAyF`) — node "Call 'Send Email: HTML'" (id `136b1c8b-a363-4778-bed3-77dd755dba3b`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `fd342657-cc4a-45b9-92b4-39fb77789479`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
