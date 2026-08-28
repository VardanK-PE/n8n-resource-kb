---
n8n_id: "pXpjChtEfW79WnTw"
name: "PE MCP Server - Backup 2026-01-06"
status: inactive
last_modified: 2026-01-06T20:43:27.926Z
tags: []
fingerprint: "2f89a7e136cc4bcab781b8c835b54e75ec245c1fde96c253dfeefe0bdbf1206c"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PE MCP Server - Backup 2026-01-06

## Summary

- **Status:** inactive
- **n8n ID:** `pXpjChtEfW79WnTw`
- **Nodes:** 6
- **Last modified:** 2026-01-06T20:43:27.926Z

## Triggers

- **other** — node "MCP Server Trigger" (id `b38b4be7-1a54-4b39-855f-70705c92b171`) — GET `05928f1e-c843-417a-bb4d-7a2e71392c5e`

## Depends on

### Credentials

- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "QBO API HTTP Request" (id `019cd99d-cd96-4629-98d8-340629b8adfe`)
- [[../resources/credentials/rlxlkmcb9jzcnyyk|Postgres ST production read replica]] (`postgres`, id `rlXLkMcb9jzcnYYK`) — node "ServiceTitan Account Postgress DB" (id `61b822e6-6e8d-4426-a2a6-a62c25732b9a`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Get many invoices in QuickBooks Online" (id `933fcd89-94e4-47c6-a96a-07bd78f0dc83`)
- [[../resources/credentials/giag80d8ix6fsdbg|N8N QB MCP Server Header Auth Token]] (`httpHeaderAuth`, id `GiaG80d8IX6fsDBG`) — node "MCP Server Trigger" (id `b38b4be7-1a54-4b39-855f-70705c92b171`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "HTTP Request" (id `ebbd9b38-69a7-4d66-930e-e62409dbcbdd`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "QBO API HTTP Request" (id `019cd99d-cd96-4629-98d8-340629b8adfe`)
- *(dynamic URL)* — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', `The base of the url needs to start with: https://quickbooks.api.intuit.com/v3/company/9341452828840730/{entity}`, 'string') }}` — node "HTTP Request" (id `ebbd9b38-69a7-4d66-930e-e62409dbcbdd`)

### Databases

- [[../resources/databases/postgres-rlxlkmcb9jzcnyyk|postgres (via Postgres ST production read replica)]] — op `executeQuery` — node "ServiceTitan Account Postgress DB" (id `61b822e6-6e8d-4426-a2a6-a62c25732b9a`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
