---
n8n_id: "JkeR16lXouUHHtZn"
name: "PE MCP Server"
status: active
last_modified: 2026-02-02T16:59:28.228Z
tags: []
fingerprint: "a9ad65b7f11cf3e2d144f254768ecb502834a9f1478d03a84a085727461f0bae"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PE MCP Server

## Summary

- **Status:** active
- **n8n ID:** `JkeR16lXouUHHtZn`
- **Nodes:** 13
- **Last modified:** 2026-02-02T16:59:28.228Z

## Triggers

- **other** — node "MCP Server Trigger" (id `b38b4be7-1a54-4b39-855f-70705c92b171`) — GET `05928f1e-c843-417a-bb4d-7a2e71392c5e`

## Depends on

### Credentials

- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "QBO API HTTP Request" (id `019cd99d-cd96-4629-98d8-340629b8adfe`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "PE Prod Postgress DB" (id `379fc435-6786-4ca9-84e2-97a306cbf111`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove Gmail - List Drafts" (id `522bb9a6-030c-42e1-b3f0-da9d10530956`)
- [[../resources/credentials/rlxlkmcb9jzcnyyk|Postgres ST production read replica]] (`postgres`, id `rlXLkMcb9jzcnYYK`) — node "ServiceTitan Account Postgress DB" (id `61b822e6-6e8d-4426-a2a6-a62c25732b9a`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove Gmail - Search Messages" (id `84d818aa-f0af-4054-b40d-71864199f16b`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Get many invoices in QuickBooks Online" (id `933fcd89-94e4-47c6-a96a-07bd78f0dc83`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove Gmail - Get Draft" (id `a40a2e95-7c90-4dd9-8fa7-3b05dc8e3ba8`)
- [[../resources/credentials/giag80d8ix6fsdbg|N8N QB MCP Server Header Auth Token]] (`httpHeaderAuth`, id `GiaG80d8IX6fsDBG`) — node "MCP Server Trigger" (id `b38b4be7-1a54-4b39-855f-70705c92b171`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "HTTP Request" (id `ebbd9b38-69a7-4d66-930e-e62409dbcbdd`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove Gmail - Get Message" (id `f6c5c125-9992-4d2a-a61c-f5adfe697671`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "QBO API HTTP Request" (id `019cd99d-cd96-4629-98d8-340629b8adfe`)
- *(dynamic URL)* — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', `The base of the url needs to start with: https://quickbooks.api.intuit.com/v3/company/9341452828840730/{entity}`, 'string') }}` — node "HTTP Request" (id `ebbd9b38-69a7-4d66-930e-e62409dbcbdd`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "PE Prod Postgress DB" (id `379fc435-6786-4ca9-84e2-97a306cbf111`)
- [[../resources/databases/postgres-rlxlkmcb9jzcnyyk|postgres (via Postgres ST production read replica)]] — op `executeQuery` — node "ServiceTitan Account Postgress DB" (id `61b822e6-6e8d-4426-a2a6-a62c25732b9a`)

### MCP servers (external)

- [[../resources/mcp-servers/https-c67b7799ff2a-ngrok-app-mcp|c67b7799ff2a.ngrok.app]] — `https://c67b7799ff2a.ngrok.app/mcp` — node "Skills MCP" (id `5bea090f-b58b-4dfb-bb56-404aeb8b1737`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
