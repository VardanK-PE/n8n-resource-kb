---
n8n_id: "aHkdQU78RVrDYoRI"
name: "ShiftAgent AI Related"
status: active
last_modified: 2026-04-02T22:35:39.627Z
tags: []
fingerprint: "ba09c29dedc7b922d738b316d104212dbe0514130feeea4ca52f5c7374c788b5"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# ShiftAgent AI Related

## Summary

- **Status:** active
- **n8n ID:** `aHkdQU78RVrDYoRI`
- **Nodes:** 39
- **Last modified:** 2026-04-02T22:35:39.627Z

## Triggers

- **webhook** — node "Webhook5" (id `0165fe4f-5703-4a46-a480-ccb374147a4d`) — POST `d0bc1a2c-8c7e-4d43-b808-993895a1724h`
- **schedule** — node "Schedule Trigger" (id `38b36bb6-aab4-48c1-9193-6bb14ec679c5`) — `every 1 week(s)`
- **other** — node "ShiftAgent MCP Server Trigger" (id `3a244cff-a0f0-4411-a526-92d35f7da0dd`) — GET `c37f105b-5b77-4fcf-ab7c-98fc032c19cc`
- **webhook** — node "Webhook3" (id `570bf72c-d72e-4b21-9781-e05cd5c156cf`) — POST `d0bc1a2c-8c7e-4d43-b808-993895a1724f`
- **webhook** — node "Webhook1" (id `63705945-8fe8-400f-9e4d-8876e211b29c`) — POST `d0bc1a2c-8c7e-4d43-b808-993895a1724d`
- **webhook** — node "Webhook2" (id `74605ea5-169f-48cf-a706-24528aedf7a2`) — POST `d0bc1a2c-8c7e-4d43-b808-993895a1724e`
- **webhook** — node "Webhook6" (id `888e9d33-158f-4f66-827d-fc78ab35ec2b`) — POST `d0bc1a2c-8c7e-4d43-b808-993895a1724k`
- **webhook** — node "Webhook4" (id `b60b8fdc-1cb9-4fe1-8d9c-967819e1cbee`) — POST `d0bc1a2c-8c7e-4d43-b808-993895a1724g`
- **webhook** — node "Webhook" (id `de1b0e21-2d2d-4ba0-8f31-0fd559f17a30`) — POST `d0bc1a2c-8c7e-4d43-b808-993895a1724c`

## Depends on

### Credentials

- [[../resources/credentials/csjokkl6yo9scgcu|ShiftAget PG Access API Key]] (`httpHeaderAuth`, id `CSjokKL6yO9ScGCu`) — node "Webhook5" (id `0165fe4f-5703-4a46-a480-ccb374147a4d`)
- [[../resources/credentials/6iq3hrw7e8hxpeoa|PE Support Gmail Account (support@payengine.co)]] (`gmailOAuth2`, id `6Iq3hRW7e8hxpEOa`) — node "Send a message in Gmail" (id `01a343cc-bb19-4fcd-a30a-fb24673a7e8b`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `04f843b5-ac85-48b2-bed2-30d19934d27c`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send a message" (id `0f0ae416-1316-408d-a353-867d76876a70`)
- [[../resources/credentials/csjokkl6yo9scgcu|ShiftAget PG Access API Key]] (`httpHeaderAuth`, id `CSjokKL6yO9ScGCu`) — node "ShiftAgent MCP Server Trigger" (id `3a244cff-a0f0-4411-a526-92d35f7da0dd`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `4958ab1c-0b30-49ae-8c54-e5f79d761741`)
- [[../resources/credentials/csjokkl6yo9scgcu|ShiftAget PG Access API Key]] (`httpHeaderAuth`, id `CSjokKL6yO9ScGCu`) — node "Webhook3" (id `570bf72c-d72e-4b21-9781-e05cd5c156cf`)
- [[../resources/credentials/csjokkl6yo9scgcu|ShiftAget PG Access API Key]] (`httpHeaderAuth`, id `CSjokKL6yO9ScGCu`) — node "Webhook1" (id `63705945-8fe8-400f-9e4d-8876e211b29c`)
- [[../resources/credentials/6iq3hrw7e8hxpeoa|PE Support Gmail Account (support@payengine.co)]] (`gmailOAuth2`, id `6Iq3hRW7e8hxpEOa`) — node "Send Email Through support@payengine.co" (id `702f53d5-4e82-4b0b-990e-7021ef60561f`)
- [[../resources/credentials/csjokkl6yo9scgcu|ShiftAget PG Access API Key]] (`httpHeaderAuth`, id `CSjokKL6yO9ScGCu`) — node "Webhook2" (id `74605ea5-169f-48cf-a706-24528aedf7a2`)
- [[../resources/credentials/csjokkl6yo9scgcu|ShiftAget PG Access API Key]] (`httpHeaderAuth`, id `CSjokKL6yO9ScGCu`) — node "Webhook6" (id `888e9d33-158f-4f66-827d-fc78ab35ec2b`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `9ce64ca1-6e52-443d-b53f-8f305b6f500c`)
- [[../resources/credentials/rlxlkmcb9jzcnyyk|Postgres ST production read replica]] (`postgres`, id `rlXLkMcb9jzcnYYK`) — node "Execute a SQL query1" (id `b4f2424a-ba46-450a-a56a-873884eb17b0`)
- [[../resources/credentials/csjokkl6yo9scgcu|ShiftAget PG Access API Key]] (`httpHeaderAuth`, id `CSjokKL6yO9ScGCu`) — node "Webhook4" (id `b60b8fdc-1cb9-4fe1-8d9c-967819e1cbee`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "PE Database Inspector" (id `cbec1cea-ac5c-4890-9e07-ae5be369354e`)
- [[../resources/credentials/csjokkl6yo9scgcu|ShiftAget PG Access API Key]] (`httpHeaderAuth`, id `CSjokKL6yO9ScGCu`) — node "Webhook" (id `de1b0e21-2d2d-4ba0-8f31-0fd559f17a30`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query2" (id `e00b88a5-76ae-4fd6-bc9f-c0b2e9703f96`)

### HTTP URLs

- [[../resources/http-urls/pf-prod-ecs-task-container-gotenberg-3000|pf-prod-ecs-task-container-gotenberg:3000]] — `POST http://pf-prod-ecs-task-container-gotenberg:3000/forms/chromium/convert/html` — node "Convert To PDF [GOTENBERG]" (id `60c386da-5ea4-4086-ac60-e477b9a8ac46`)
- [[../resources/http-urls/pf-prod-ecs-task-container-gotenberg-3000|pf-prod-ecs-task-container-gotenberg:3000]] — `POST http://pf-prod-ecs-task-container-gotenberg:3000/forms/chromium/convert/html` — node "Convert To PDF [GOTENBERG]1" (id `697eb367-b507-41f4-ab5e-fc74398f731a`)
- [[../resources/http-urls/pf-prod-ecs-task-container-gotenberg-3000|pf-prod-ecs-task-container-gotenberg:3000]] — `POST http://pf-prod-ecs-task-container-gotenberg:3000/forms/chromium/convert/html` — node "Gotenberg Server" (id `8940ac2e-2fef-4d05-86a7-59370bb7b2e8`)
- [[../resources/http-urls/pf-prod-ecs-task-container-gotenberg-3000|pf-prod-ecs-task-container-gotenberg:3000]] — `POST http://pf-prod-ecs-task-container-gotenberg:3000/forms/chromium/convert/html` — node "Gotenberg Server1" (id `c5e8214a-1654-471f-9b4b-440514ea2fe5`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `4958ab1c-0b30-49ae-8c54-e5f79d761741`)
- [[../resources/databases/postgres-rlxlkmcb9jzcnyyk|postgres (via Postgres ST production read replica)]] — op `executeQuery` — node "Execute a SQL query1" (id `b4f2424a-ba46-450a-a56a-873884eb17b0`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "PE Database Inspector" (id `cbec1cea-ac5c-4890-9e07-ae5be369354e`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query2" (id `e00b88a5-76ae-4fd6-bc9f-c0b2e9703f96`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-5-20250929|anthropic / claude-sonnet-4-5-20250929]] — node "Anthropic Chat Model" (id `04f843b5-ac85-48b2-bed2-30d19934d27c`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-6|anthropic / claude-sonnet-4-6]] — node "Anthropic Chat Model1" (id `9ce64ca1-6e52-443d-b53f-8f305b6f500c`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
