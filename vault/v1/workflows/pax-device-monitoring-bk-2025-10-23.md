---
n8n_id: "NVxfS5SmsjLAYKEx"
instance: v1
name: "PAX Device Monitoring (BK-2025-10-23)"
status: inactive
last_modified: 2025-10-23T19:24:10.576Z
tags:
  - "backups"
fingerprint: "ec5379ea9206ff3e71271c4e2a863e3d0b1fc501cdd07db1f47a89ffe356ad1c"
auto_generated_at: 2026-08-28T21:31:11Z
---

<!-- auto:start -->

# PAX Device Monitoring (BK-2025-10-23)

## Summary

- **Status:** inactive
- **n8n ID:** `NVxfS5SmsjLAYKEx`
- **Nodes:** 30
- **Last modified:** 2025-10-23T19:24:10.576Z

## Triggers

- **execute-workflow** — node "PAXStore API Request" (id `444c6ea8-33c1-4442-ad0c-c14f20a612ef`)
- **manual** — node "When clicking ‘Execute workflow’" (id `b79c25b6-c7d4-419b-8f28-cb0007964a2e`)

## Depends on

### Credentials

- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "JWT1" (id `8272fd8e-2c81-4513-bfb1-a2b8d2749520`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "JWT" (id `b31e1fce-e096-4286-be24-9cafb37beae1`)

### HTTP URLs

- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `POST https://auth.paxstore.us/passport/oauth/token` — node "POST /passport/oauth/token" (id `14dbb962-ad1a-4c36-be87-2db753aeda5d`)
- *(dynamic URL)* — `GET {{ $json.urlPath }}` — node "HTTP Request" (id `1af727ea-63ca-4ad4-9223-54d4a75adec6`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/login?client_id=admin&market=reseller` — node "Get /login1" (id `2e05f933-8fa0-43a9-aac6-5fdb2c3534d6`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/login?client_id=admin&market=reseller` — node "Get /login" (id `55afc2b8-911c-4160-93f8-f5f3f411a3d1`)
- [[../resources/http-urls/api-paxstore-us|api.paxstore.us]] — `GET https://api.paxstore.us/p-market-web/v1/admin/current-user` — node "HTTP Request2" (id `93d430ed-01ad-4250-858b-cb5b75d36ce6`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/check-acct?ln=spartak@platformfactory.io` — node "GET /check-acct" (id `9b3073dc-7386-4de5-8d65-baf28fa29657`)
- *(dynamic URL)* — `={{ $json.method }} {{ $json.url }}` — node "HTTP Request1" (id `b0742a80-27ec-4deb-b8bd-2b3764834b21`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/oauth/authorize?response_type=code&client_id=portal&scope=openid&state=jJDkaSBeTzRk-ahPO83ehe6xMSLJNap~&locale=en&code_challenge=FMJ%252BonUbyajSGNA8PWdD7QCKIIB2wQzx2%252B8tYBSrPj8%253D&market=reseller` — node "GET /passport/oauth/authorize" (id `c1e3c091-facd-40fe-b7d8-da7dc599217b`)
- *(dynamic URL)* — `GET {{ $json.urlPath }}` — node "HTTP Request3" (id `fc2c52ec-c9f0-4498-a150-264e0967901e`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `POST https://auth.paxstore.us/passport/loginService` — node "POST /passport/loginService" (id `fe5b8113-210d-4489-9060-46b3be734255`)

### Sub-workflows (Execute Workflow calls)

- [[pax-device-monitoring|PAX Device Monitoring]] (n8n_id `Q9j3wpVGvegSl4Sy`) — node "Call 'PAX Device Monitoring'" (id `d3350bd3-91db-4d46-9ddf-afbf946e1640`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
