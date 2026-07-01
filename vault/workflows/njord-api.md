---
n8n_id: "CLtY9Ihkm5vAGNVX"
name: "Njord API"
status: active
last_modified: 2026-03-24T19:56:39.382Z
tags: []
fingerprint: "6eab2892be78832e66c47e4d4786154eade399e10def5bad95964cb20587118d"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Njord API

## Summary

- **Status:** active
- **n8n ID:** `CLtY9Ihkm5vAGNVX`
- **Nodes:** 72
- **Last modified:** 2026-03-24T19:56:39.382Z

## Triggers

- **webhook** — node "Get Dashboard - PROD" (id `2ac3c30e-65c4-47c8-8de1-1731cea1be29`) — GET `njord/api/dashboard`
- **webhook** — node "Get Invoice Detail - PROD" (id `2dc15527-2de1-477a-9537-cd9c5852d146`) — GET `njord/api/invoice-detail`
- **webhook** — node "Get Invoice Detail - STAGE" (id `38f5207f-6140-4f3b-a353-08c5ef6ef9ed`) — GET `njord/stage/api/invoice-detail`
- **webhook** — node "Get Dashboard - STAGE" (id `3f8a83e4-e623-46a4-ad88-f05783020b24`) — GET `njord/stage/api/dashboard`
- **webhook** — node "Get Merchants - PROD" (id `46249afd-7718-45ef-a0f4-ee3b8d21d948`) — GET `njord/api/merchants`
- **webhook** — node "Get Merchants - STAGE" (id `509a792c-3043-41d9-9d21-13e67c323b6a`) — GET `njord/stage/api/merchants`
- **webhook** — node "Get Merchant Detail - STAGE" (id `8fb91b5c-3279-459e-a63e-31997bef3d7b`) — GET `njord/stage/api/merchant-detail`
- **webhook** — node "Get Invoices List - STAGE" (id `a8295b61-83c4-4eb2-a789-dc69c9ebc6b2`) — GET `njord/stage/api/invoices`
- **webhook** — node "Get Merchant Detail - PROD" (id `b5cf0e80-43b9-4819-9ffb-52681a6ae870`) — GET `njord/api/merchant-detail`
- **webhook** — node "Get Invoices List - PROD" (id `e0a6dd33-3259-4687-93c0-b12238132ba9`) — GET `njord/api/invoices`

## Depends on

### Credentials

- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "Execute Query STAGE" (id `0f927572-1892-4097-b4f4-c2939653f558`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Dashboard - PROD" (id `2ac3c30e-65c4-47c8-8de1-1731cea1be29`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Invoice Detail - PROD" (id `2dc15527-2de1-477a-9537-cd9c5852d146`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Invoice Detail - STAGE" (id `38f5207f-6140-4f3b-a353-08c5ef6ef9ed`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Dashboard - STAGE" (id `3f8a83e4-e623-46a4-ad88-f05783020b24`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Merchants - PROD" (id `46249afd-7718-45ef-a0f4-ee3b8d21d948`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Detail Query PROD" (id `46b3382f-083a-40e7-a8e3-75d871914cbf`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute Query PROD" (id `47970a12-31db-418a-9e4e-72361fd26975`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Merchants - STAGE" (id `509a792c-3043-41d9-9d21-13e67c323b6a`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "Inv List Merchants STAGE" (id `5d80640f-30e3-49fa-9c47-e9723fcf714d`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "Dashboard Merchants STAGE" (id `62ae59ab-18a8-4637-972d-ca1f165f15ff`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Dashboard Merchants PROD" (id `6acd0064-6a52-4a24-886f-cbd1a0c7a40b`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "Detail Query STAGE" (id `7681f8b7-f1ac-4cf7-881d-a13a3942a01f`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Merchant Detail - STAGE" (id `8fb91b5c-3279-459e-a63e-31997bef3d7b`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant Name PROD" (id `a3f5d972-b992-4e36-a197-6fe9641ae3df`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Invoices List - STAGE" (id `a8295b61-83c4-4eb2-a789-dc69c9ebc6b2`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Merchant Detail - PROD" (id `b5cf0e80-43b9-4819-9ffb-52681a6ae870`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Inv List Merchants PROD" (id `bd7ed277-975a-48f1-ba63-9a1de9298295`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "Merchant Name STAGE" (id `db457aad-9f9b-4b9d-b205-82617cc25838`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Invoices List - PROD" (id `e0a6dd33-3259-4687-93c0-b12238132ba9`)

### Databases

- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "Execute Query STAGE" (id `0f927572-1892-4097-b4f4-c2939653f558`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Detail Query PROD" (id `46b3382f-083a-40e7-a8e3-75d871914cbf`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute Query PROD" (id `47970a12-31db-418a-9e4e-72361fd26975`)
- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "Inv List Merchants STAGE" (id `5d80640f-30e3-49fa-9c47-e9723fcf714d`)
- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "Dashboard Merchants STAGE" (id `62ae59ab-18a8-4637-972d-ca1f165f15ff`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Dashboard Merchants PROD" (id `6acd0064-6a52-4a24-886f-cbd1a0c7a40b`)
- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "Detail Query STAGE" (id `7681f8b7-f1ac-4cf7-881d-a13a3942a01f`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant Name PROD" (id `a3f5d972-b992-4e36-a197-6fe9641ae3df`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Inv List Merchants PROD" (id `bd7ed277-975a-48f1-ba63-9a1de9298295`)
- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "Merchant Name STAGE" (id `db457aad-9f9b-4b9d-b205-82617cc25838`)

### Data tables (n8n)

- [[../resources/data-tables/eefxih6vfsgkmssi|EEFXIH6vFSgKmssi]] (id `EEFXIH6vFSgKmssi`) — op `get` — node "Fetch Dash PCI" (id `87bb287a-17ab-4b59-943d-fdec9bdbcf63`)
- [[../resources/data-tables/pz9zqssjshkjnyb9|pz9ZQssJShkJNYb9]] (id `pz9ZQssJShkJNYb9`) — op `get` — node "Fetch Dash Invoices" (id `9c3c2623-d9cb-436e-9b1a-3d432603ecd6`)
- [[../resources/data-tables/pz9zqssjshkjnyb9|pz9ZQssJShkJNYb9]] (id `pz9ZQssJShkJNYb9`) — op `get` — node "Lookup Invoice" (id `ac72634c-9366-4526-a930-39ac1224fbbe`)
- [[../resources/data-tables/pz9zqssjshkjnyb9|pz9ZQssJShkJNYb9]] (id `pz9ZQssJShkJNYb9`) — op `get` — node "Lookup Invoices" (id `b913ff62-29af-467a-a810-53a94039b494`)
- [[../resources/data-tables/eefxih6vfsgkmssi|EEFXIH6vFSgKmssi]] (id `EEFXIH6vFSgKmssi`) — op `get` — node "Lookup PCI" (id `db6f3467-0b5e-488d-b552-c43dda220fc2`)
- [[../resources/data-tables/pz9zqssjshkjnyb9|pz9ZQssJShkJNYb9]] (id `pz9ZQssJShkJNYb9`) — op `get` — node "Fetch All Invoices" (id `dbb4b277-38c3-4053-839e-b20308a57e19`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
