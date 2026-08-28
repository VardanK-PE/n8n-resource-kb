---
n8n_id: "CLtY9Ihkm5vAGNVX"
instance: v1
name: "Njord API"
status: active
last_modified: 2026-08-17T18:27:39.615Z
tags: []
fingerprint: "f25dd8f08ab16a2900ac3e007c1ce5034aa5cb76659bd40aa9ac907ab4cb05a8"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Njord API

## Summary

- **Status:** active
- **n8n ID:** `CLtY9Ihkm5vAGNVX`
- **Nodes:** 138
- **Last modified:** 2026-08-17T18:27:39.615Z

## Triggers

- **webhook** — node "Get Disputes - STAGE" (id `0ec9fc94-1ca6-4200-8cde-5662b85b06de`) — GET `njord/stage/api/disputes`
- **webhook** — node "Get Dashboard - PROD" (id `2ac3c30e-65c4-47c8-8de1-1731cea1be29`) — GET `njord/api/dashboard`
- **webhook** — node "Post Dispute Action - STAGE" (id `2d17d310-4e50-4e21-9f39-c72aa21963bd`) — POST `njord/stage/api/dispute-action`
- **webhook** — node "Get Invoice Detail - PROD" (id `2dc15527-2de1-477a-9537-cd9c5852d146`) — GET `njord/api/invoice-detail`
- **webhook** — node "Get Merchant Disputes - PROD" (id `350b0dec-432c-4415-9fa4-557182222577`) — GET `njord/api/merchant-disputes`
- **webhook** — node "Get Invoice Detail - STAGE" (id `38f5207f-6140-4f3b-a353-08c5ef6ef9ed`) — GET `njord/stage/api/invoice-detail`
- **webhook** — node "Get Dashboard - STAGE" (id `3f8a83e4-e623-46a4-ad88-f05783020b24`) — GET `njord/stage/api/dashboard`
- **webhook** — node "Get Merchants - PROD" (id `46249afd-7718-45ef-a0f4-ee3b8d21d948`) — GET `njord/api/merchants`
- **webhook** — node "Get Dispute Detail - PROD" (id `48048d4e-6ed6-4c67-981e-d5a44fe3b64b`) — GET `njord/api/dispute-detail`
- **webhook** — node "Get Merchants - STAGE" (id `509a792c-3043-41d9-9d21-13e67c323b6a`) — GET `njord/stage/api/merchants`
- **webhook** — node "Get Dispute Document - PROD" (id `5813b3d3-75dc-4ea5-9d76-a81caf8b988f`) — GET `njord/api/dispute-document`
- **webhook** — node "Get Merchant Disputes - STAGE" (id `7ceabcf0-29b5-4b18-ac65-bd290f642a1e`) — GET `njord/stage/api/merchant-disputes`
- **webhook** — node "Get Merchant Detail - STAGE" (id `8fb91b5c-3279-459e-a63e-31997bef3d7b`) — GET `njord/stage/api/merchant-detail`
- **webhook** — node "Post Dispute Action - PROD" (id `95b21b95-37be-4059-9f05-d179840802db`) — POST `njord/api/dispute-action`
- **webhook** — node "Get Disputes - PROD" (id `9ba188c8-b9a6-461e-936e-c7f7304c3274`) — GET `njord/api/disputes`
- **webhook** — node "Get Invoices List - STAGE" (id `a8295b61-83c4-4eb2-a789-dc69c9ebc6b2`) — GET `njord/stage/api/invoices`
- **webhook** — node "Get Merchant Detail - PROD" (id `b5cf0e80-43b9-4819-9ffb-52681a6ae870`) — GET `njord/api/merchant-detail`
- **webhook** — node "Get Dispute Document - STAGE" (id `d6fd5423-748a-40d5-9173-c848e1fba969`) — GET `njord/stage/api/dispute-document`
- **webhook** — node "Get Invoices List - PROD" (id `e0a6dd33-3259-4687-93c0-b12238132ba9`) — GET `njord/api/invoices`
- **webhook** — node "Get Dispute Detail - STAGE" (id `ed138264-9087-4646-8743-411a3bee6e29`) — GET `njord/stage/api/dispute-detail`

## Depends on

### Credentials

- [[../resources/credentials/w4wa61x6umwxzrlf|Elavon Disputes API (Sandbox)]] (`httpBasicAuth`, id `w4wa61x6UmWXzrlF`) — node "Elavon Token (D Detail)" (id `09a07a65-68db-4b96-a7f5-617196eef422`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Disputes - STAGE" (id `0ec9fc94-1ca6-4200-8cde-5662b85b06de`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "Execute Query STAGE" (id `0f927572-1892-4097-b4f4-c2939653f558`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "D Doc Merchant PROD" (id `1131ab17-7f21-4659-991b-7e5b107ec626`)
- [[../resources/credentials/w4wa61x6umwxzrlf|Elavon Disputes API (Sandbox)]] (`httpBasicAuth`, id `w4wa61x6UmWXzrlF`) — node "Elavon Token (M Disputes)" (id `1223b4cc-253c-4e06-bcb6-2b1bdf3c4651`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "M Disputes Merchant STAGE" (id `15cf3066-3b75-41eb-80ad-9ae5c6edc472`)
- [[../resources/credentials/w4wa61x6umwxzrlf|Elavon Disputes API (Sandbox)]] (`httpBasicAuth`, id `w4wa61x6UmWXzrlF`) — node "Elavon Token (Disputes)" (id `18f4cedc-4060-438b-84cd-56e0737d88f1`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "D Detail Merchant STAGE" (id `1f0363e3-05f8-440f-857e-8d887749ea20`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Dashboard - PROD" (id `2ac3c30e-65c4-47c8-8de1-1731cea1be29`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Post Dispute Action - STAGE" (id `2d17d310-4e50-4e21-9f39-c72aa21963bd`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Invoice Detail - PROD" (id `2dc15527-2de1-477a-9537-cd9c5852d146`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Merchant Disputes - PROD" (id `350b0dec-432c-4415-9fa4-557182222577`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Invoice Detail - STAGE" (id `38f5207f-6140-4f3b-a353-08c5ef6ef9ed`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Disputes Merchants PROD" (id `39c47f0d-1743-4a1a-890f-2230188e1463`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Dashboard - STAGE" (id `3f8a83e4-e623-46a4-ad88-f05783020b24`)
- [[../resources/credentials/w4wa61x6umwxzrlf|Elavon Disputes API (Sandbox)]] (`httpBasicAuth`, id `w4wa61x6UmWXzrlF`) — node "Elavon Token (D Action)" (id `42348ef5-3a1c-4bd2-b2a6-1f9291c79f41`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Merchants - PROD" (id `46249afd-7718-45ef-a0f4-ee3b8d21d948`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Detail Query PROD" (id `46b3382f-083a-40e7-a8e3-75d871914cbf`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute Query PROD" (id `47970a12-31db-418a-9e4e-72361fd26975`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Dispute Detail - PROD" (id `48048d4e-6ed6-4c67-981e-d5a44fe3b64b`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Merchants - STAGE" (id `509a792c-3043-41d9-9d21-13e67c323b6a`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Dispute Document - PROD" (id `5813b3d3-75dc-4ea5-9d76-a81caf8b988f`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "Inv List Merchants STAGE" (id `5d80640f-30e3-49fa-9c47-e9723fcf714d`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "Dashboard Merchants STAGE" (id `62ae59ab-18a8-4637-972d-ca1f165f15ff`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Dashboard Merchants PROD" (id `6acd0064-6a52-4a24-886f-cbd1a0c7a40b`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "M Disputes Merchant PROD" (id `74202ffb-a795-43c1-add2-c72d2e7b3c0f`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "Detail Query STAGE" (id `7681f8b7-f1ac-4cf7-881d-a13a3942a01f`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Merchant Disputes - STAGE" (id `7ceabcf0-29b5-4b18-ac65-bd290f642a1e`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Merchant Detail - STAGE" (id `8fb91b5c-3279-459e-a63e-31997bef3d7b`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Post Dispute Action - PROD" (id `95b21b95-37be-4059-9f05-d179840802db`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Disputes - PROD" (id `9ba188c8-b9a6-461e-936e-c7f7304c3274`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant Name PROD" (id `a3f5d972-b992-4e36-a197-6fe9641ae3df`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "D Detail Merchant PROD" (id `a7b20e4c-e025-4210-9bbf-bb912ea32eff`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Invoices List - STAGE" (id `a8295b61-83c4-4eb2-a789-dc69c9ebc6b2`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Merchant Detail - PROD" (id `b5cf0e80-43b9-4819-9ffb-52681a6ae870`)
- [[../resources/credentials/w4wa61x6umwxzrlf|Elavon Disputes API (Sandbox)]] (`httpBasicAuth`, id `w4wa61x6UmWXzrlF`) — node "Elavon Token (D Doc)" (id `bc3c9fa0-79a9-4fa9-874c-c8a73eb0d37a`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Inv List Merchants PROD" (id `bd7ed277-975a-48f1-ba63-9a1de9298295`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "D Action Merchant STAGE" (id `bfa6b0b9-eb49-43dd-89fc-2421e4177f50`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "D Doc Merchant STAGE" (id `c06327ab-0720-4459-abc6-191d07117042`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "Disputes Merchants STAGE" (id `d0b01e86-2eab-43e1-983e-87b92e2032b8`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Dispute Document - STAGE" (id `d6fd5423-748a-40d5-9173-c848e1fba969`)
- [[../resources/credentials/7298gzdhlw0ssdfs|Postgres Staging Sandbox]] (`postgres`, id `7298gzDHlw0sSdFs`) — node "Merchant Name STAGE" (id `db457aad-9f9b-4b9d-b205-82617cc25838`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Get Invoices List - PROD" (id `e0a6dd33-3259-4687-93c0-b12238132ba9`)
- [[../resources/credentials/azztrn2qdajzlrfm|PE Staging Master JWT Auth account]] (`jwtAuth`, id `AzztRn2QdajzLrFm`) — node "Get Dispute Detail - STAGE" (id `ed138264-9087-4646-8743-411a3bee6e29`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "D Action Merchant PROD" (id `ff9ed832-6b4e-4cb7-9a49-9da4b8972832`)

### HTTP URLs

- *(dynamic URL)* — `POST {{ $json.elavonHost }}/oauth2/client-credentials/v2/token` — node "Elavon Token (D Detail)" (id `09a07a65-68db-4b96-a7f5-617196eef422`)
- *(dynamic URL)* — `POST {{ $json.elavonHost }}/oauth2/client-credentials/v2/token` — node "Elavon Token (M Disputes)" (id `1223b4cc-253c-4e06-bcb6-2b1bdf3c4651`)
- *(dynamic URL)* — `POST {{ $json.elavonHost }}/oauth2/client-credentials/v2/token` — node "Elavon Token (Disputes)" (id `18f4cedc-4060-438b-84cd-56e0737d88f1`)
- *(dynamic URL)* — `POST {{ $json.elavonHost }}/oauth2/client-credentials/v2/token` — node "Elavon Token (D Action)" (id `42348ef5-3a1c-4bd2-b2a6-1f9291c79f41`)
- *(dynamic URL)* — `POST {{ $json.elavonHost }}/oauth2/client-credentials/v2/token` — node "Elavon Token (D Doc)" (id `bc3c9fa0-79a9-4fa9-874c-c8a73eb0d37a`)

### Databases

- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "Execute Query STAGE" (id `0f927572-1892-4097-b4f4-c2939653f558`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "D Doc Merchant PROD" (id `1131ab17-7f21-4659-991b-7e5b107ec626`)
- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "M Disputes Merchant STAGE" (id `15cf3066-3b75-41eb-80ad-9ae5c6edc472`)
- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "D Detail Merchant STAGE" (id `1f0363e3-05f8-440f-857e-8d887749ea20`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Disputes Merchants PROD" (id `39c47f0d-1743-4a1a-890f-2230188e1463`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Detail Query PROD" (id `46b3382f-083a-40e7-a8e3-75d871914cbf`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute Query PROD" (id `47970a12-31db-418a-9e4e-72361fd26975`)
- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "Inv List Merchants STAGE" (id `5d80640f-30e3-49fa-9c47-e9723fcf714d`)
- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "Dashboard Merchants STAGE" (id `62ae59ab-18a8-4637-972d-ca1f165f15ff`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Dashboard Merchants PROD" (id `6acd0064-6a52-4a24-886f-cbd1a0c7a40b`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "M Disputes Merchant PROD" (id `74202ffb-a795-43c1-add2-c72d2e7b3c0f`)
- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "Detail Query STAGE" (id `7681f8b7-f1ac-4cf7-881d-a13a3942a01f`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant Name PROD" (id `a3f5d972-b992-4e36-a197-6fe9641ae3df`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "D Detail Merchant PROD" (id `a7b20e4c-e025-4210-9bbf-bb912ea32eff`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Inv List Merchants PROD" (id `bd7ed277-975a-48f1-ba63-9a1de9298295`)
- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "D Action Merchant STAGE" (id `bfa6b0b9-eb49-43dd-89fc-2421e4177f50`)
- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "D Doc Merchant STAGE" (id `c06327ab-0720-4459-abc6-191d07117042`)
- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "Disputes Merchants STAGE" (id `d0b01e86-2eab-43e1-983e-87b92e2032b8`)
- [[../resources/databases/postgres-7298gzdhlw0ssdfs|postgres (via Postgres Staging Sandbox)]] — op `executeQuery` — node "Merchant Name STAGE" (id `db457aad-9f9b-4b9d-b205-82617cc25838`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "D Action Merchant PROD" (id `ff9ed832-6b4e-4cb7-9a49-9da4b8972832`)

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
