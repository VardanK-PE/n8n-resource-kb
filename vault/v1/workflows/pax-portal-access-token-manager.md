---
n8n_id: "pY05hGyMJwslcwoH"
name: "PAX Portal Access Token Manager"
status: inactive
last_modified: 2026-07-10T10:18:19.914Z
tags: []
fingerprint: "40c21cbdb84c08b55cbe689f639a725fb38d727113e88f1f1cf7495b99dee8b9"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PAX Portal Access Token Manager

## Summary

- **Status:** inactive
- **n8n ID:** `pY05hGyMJwslcwoH`
- **Nodes:** 31
- **Last modified:** 2026-07-10T10:18:19.914Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `7e31f37e-5bfd-451f-8b42-959183b6781b`)
- **manual** — node "When clicking ‘Execute workflow’" (id `d44052d5-d2ac-4d36-9f48-7c4868cd1e4c`)
- **error** — node "Error Trigger" (id `fb01cf17-83ce-4e62-9c90-c8847020014a`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `058d628d-d6f9-4968-a96f-332bcd06d3d7`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `4f50cc7d-7f47-478e-b82f-b0bec9c3217c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `8287a574-b1de-41f5-b996-c02d6c93fb68`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `bbf3718f-73a7-4dc4-91b4-f5223c8e8639`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "JWT" (id `de53c702-3d56-4b94-9811-ade4de59a2fc`)

### HTTP URLs

- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/oauth/authorize?response_type=code&client_id=portal&scope=openid&state=jJDkaSBeTzRk-ahPO83ehe6xMSLJNap~&locale=en&code_challenge=FMJ%252BonUbyajSGNA8PWdD7QCKIIB2wQzx2%252B8tYBSrPj8%253D&market=reseller` — node "GET /passport/oauth/authorize" (id `0a55d638-a2bd-4f86-afc9-fb15f4947af0`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/check-acct?ln=vardan@platformfactory.io` — node "GET /check-acct" (id `0dd3f52d-e281-4caa-8f20-75438c0787ac`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `POST https://auth.paxstore.us/passport/oauth/token` — node "POST /passport/oauth/token" (id `5a8696df-f7af-4e62-93c9-aab73294c2c1`)
- *(dynamic URL)* — `={{ $json.method }} {{ $json.url }}` — node "POST: /passport/loginService Request" (id `8db8da26-64de-4491-a10d-dd2a01dc171c`)
- [[../resources/http-urls/api-paxstore-us|api.paxstore.us]] — `GET https://api.paxstore.us/p-market-web/v1/common/auth/ping` — node "Ping" (id `ad3890be-46b8-42db-9426-f0f580e1ac7f`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/login?client_id=admin&market=reseller` — node "Get /login" (id `cdc235ac-b77b-4ed5-b08e-94ce0a55f174`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/check-acct?ln=spartak@platformfactory.io` — node "GET /check-acct1" (id `e28cd076-0073-4675-88b7-a97f5cb10089`)

### Data tables (n8n)

- [[../resources/data-tables/wwsdy58edldxpmbg|PaxPortalBearerToken]] (id `WwsDy58edldXpmbg`) — op `get` — node "Get Current Access Token" (id `3bc5116d-af4e-4067-a26d-29e92d3ffeb2`)
- [[../resources/data-tables/wwsdy58edldxpmbg|PaxPortalAccessToken]] (id `WwsDy58edldXpmbg`) — op `upsert` — node "Upsert Access Token" (id `c872ab4d-7a7a-484e-a502-2de4e9a76742`)

### Slack channels

- [[../resources/slack-channels/c09n4c30zpd|pax-device-monitoring]] (id `C09N4C30ZPD`) — op `channel` — node "Send a message" (id `058d628d-d6f9-4968-a96f-332bcd06d3d7`)
- [[../resources/slack-channels/c09n4c30zpd|pax-device-monitoring]] (id `C09N4C30ZPD`) — op `channel` — node "Send a message6" (id `4f50cc7d-7f47-478e-b82f-b0bec9c3217c`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `8287a574-b1de-41f5-b996-c02d6c93fb68`)
- [[../resources/slack-channels/c09n4c30zpd|pax-device-monitoring]] (id `C09N4C30ZPD`) — op `channel` — node "Send a message1" (id `bbf3718f-73a7-4dc4-91b4-f5223c8e8639`)

## Used by (workflows)

- [[pax-device-monitoring|PAX Device Monitoring]] — node "Access Token" (id `7689206b-f7a6-4fca-80e8-496e440bb4df`)
- [[pax-device-monitoring-backup-2025-10-25|PAX Device Monitoring backup 2025-10-25]] — node "Access Token" (id `9a9ceab8-2d9d-428c-bb67-c4abf404c56d`)
- [[pax-device-monitoring-backup-2025-10-25|PAX Device Monitoring backup 2025-10-25]] — node "Access Token1" (id `c54a71c2-aeeb-462c-b7ed-16f089288289`)
- [[pax-portal-api-request|PAX Portal API Request]] — node "Access Token1" (id `7b7e813b-3212-4a6b-a8ba-38db77c4804d`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
