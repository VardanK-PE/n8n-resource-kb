---
n8n_id: "Q9j3wpVGvegSl4Sy"
name: "PAX Device Monitoring"
status: active
last_modified: 2026-07-10T13:45:14.136Z
tags: []
fingerprint: "f0a7e2f5ac8434180d8f248e45a0cd3dc3b323caae826a339a631d2f2ac5d04d"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PAX Device Monitoring

## Summary

- **Status:** active
- **n8n ID:** `Q9j3wpVGvegSl4Sy`
- **Nodes:** 59
- **Last modified:** 2026-07-10T13:45:14.136Z

## Triggers

- **error** — node "Error Trigger" (id `2f17adea-31a3-45fe-b4ea-0bbbcb624c1f`)
- **schedule** — node "Schedule Trigger" (id `5e5afcd0-577b-4863-9340-b13e214587ca`) — `every 1 hour(s) at :50`
- **manual** — node "When clicking ‘Execute workflow’" (id `b19dc6b0-0d64-4b84-81ce-f8a278397786`)
- **schedule** — node "Schedule Trigger1" (id `fe361edf-fc55-4a83-bd0a-b32ab534e37f`) — `daily at 4:50`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `34f4bd3c-8c6c-419f-ae45-67c58d75dea1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `6258568e-105a-4e0b-9cfc-6f063d9814a7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet1" (id `6eb5b564-fa26-4895-bd6c-624f349cde2c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Clear sheet" (id `715c54fe-4691-4096-9465-bf1d502db9aa`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "All Devices" (id `722da42f-4334-42b3-bbb6-50f69f27d999`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `782c1a2b-b9d8-4838-97a3-f693248d67e4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet2" (id `892e7e46-f354-4c1c-8aea-6b02730842e1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet3" (id `96e0bd48-85ea-43e7-bcc0-60710edefc0d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Clear sheet2" (id `a7e7401a-a301-41c3-8f85-db18a9e236a0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `b5ffa427-a75f-48f6-a338-5af47f163dd2`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `bc2e5bdc-b1b1-4317-a195-fd4fc86488dd`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "JWT" (id `d1100447-ec2b-4bbd-b0c3-1cc77d52d95f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet2" (id `d3ddf70e-4ada-4568-a36b-b7ab19807b12`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `d7a98db3-7942-4f5e-a6b7-f00fa0732845`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Clear sheet1" (id `e8f3bcb1-d113-4cfa-bdf5-4949944bab3c`)

### HTTP URLs

- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `POST https://auth.paxstore.us/passport/oauth/token` — node "POST /passport/oauth/token" (id `0b440d02-f1bb-495c-9617-d2ebd9dda9e7`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/oauth/authorize?response_type=code&client_id=portal&scope=openid&state=jJDkaSBeTzRk-ahPO83ehe6xMSLJNap~&locale=en&code_challenge=FMJ%252BonUbyajSGNA8PWdD7QCKIIB2wQzx2%252B8tYBSrPj8%253D&market=reseller` — node "GET /passport/oauth/authorize" (id `39782ca9-1aeb-4e04-acd2-5e928612e32b`)
- *(dynamic URL)* — `={{ $json.method }} {{ $json.url }}` — node "POST: /passport/loginService Request" (id `87662973-a5d0-4cc6-be74-5930eadf68b5`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/login?client_id=admin&market=reseller` — node "Get /login" (id `90702805-aecb-497f-bf52-88a7be920d76`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/check-acct?ln=spartak@platformfactory.io` — node "GET /check-acct" (id `d7376905-0f3e-466c-ba6b-7f28dfa7fd13`)

### Google Sheets

- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `?`, tab `Devices` — node "Get row(s) in sheet" (id `6258568e-105a-4e0b-9cfc-6f063d9814a7`)
- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `append`, tab `Misconfigured Sierra Devices` — node "Append row in sheet1" (id `6eb5b564-fa26-4895-bd6c-624f349cde2c`)
- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `clear`, tab `Misconfigured Viaconex Devices` — node "Clear sheet" (id `715c54fe-4691-4096-9465-bf1d502db9aa`)
- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `?`, tab `Devices` — node "All Devices" (id `722da42f-4334-42b3-bbb6-50f69f27d999`)
- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `?`, tab `Devices` — node "Get row(s) in sheet2" (id `892e7e46-f354-4c1c-8aea-6b02730842e1`)
- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `?`, tab `Devices` — node "Get row(s) in sheet3" (id `96e0bd48-85ea-43e7-bcc0-60710edefc0d`)
- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `clear`, tab `Wrong PEPay App Version` — node "Clear sheet2" (id `a7e7401a-a301-41c3-8f85-db18a9e236a0`)
- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `append`, tab `Misconfigured Viaconex Devices` — node "Append row in sheet" (id `b5ffa427-a75f-48f6-a338-5af47f163dd2`)
- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `append`, tab `Wrong PEPay App Version` — node "Append row in sheet2" (id `d3ddf70e-4ada-4568-a36b-b7ab19807b12`)
- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `clear`, tab `Misconfigured Sierra Devices` — node "Clear sheet1" (id `e8f3bcb1-d113-4cfa-bdf5-4949944bab3c`)

### Slack channels

- [[../resources/slack-channels/c09n4c30zpd|pax-device-monitoring]] (id `C09N4C30ZPD`) — op `channel` — node "Send a message6" (id `34f4bd3c-8c6c-419f-ae45-67c58d75dea1`)
- [[../resources/slack-channels/c09n4c30zpd|pax-device-monitoring]] (id `C09N4C30ZPD`) — op `channel` — node "Send a message" (id `782c1a2b-b9d8-4838-97a3-f693248d67e4`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `bc2e5bdc-b1b1-4317-a195-fd4fc86488dd`)
- [[../resources/slack-channels/c09n4c30zpd|pax-device-monitoring]] (id `C09N4C30ZPD`) — op `channel` — node "Send a message1" (id `d7a98db3-7942-4f5e-a6b7-f00fa0732845`)

### Sub-workflows (Execute Workflow calls)

- [[pax-portal-api-request|PAX Portal API Request]] (n8n_id `T0yGFQaEQnHpmPdt`) — node "GET /terminals/list Count" (id `0ef5e90b-3264-4991-a50d-2a3b42dde139`)
- [[pax-portal-api-request|PAX Portal API Request]] (n8n_id `T0yGFQaEQnHpmPdt`) — node "GET /resellers/tree" (id `36977806-6618-4345-beaa-99f8bd27ef94`)
- [[pax-portal-api-request|PAX Portal API Request]] (n8n_id `T0yGFQaEQnHpmPdt`) — node "GET /p-market-web/v1/common/system-config" (id `4105b336-3d81-43c1-b270-11750b6b3f6e`)
- [[pax-terminal-details-sync|PAX Terminal Details Sync]] (n8n_id `4ugBRdDoboJ4Uq3e`) — node "Call 'PAX Terminal Details Sync'" (id `6d00218a-9c16-4000-a105-c333f1564369`)
- [[pax-portal-access-token-manager|PAX Portal Access Token Manager]] (n8n_id `pY05hGyMJwslcwoH`) — node "Access Token" (id `7689206b-f7a6-4fca-80e8-496e440bb4df`)
- [[pax-portal-api-request|PAX Portal API Request]] (n8n_id `T0yGFQaEQnHpmPdt`) — node "GET /current-user" (id `a5209929-6698-42d7-b38d-6f8a5a29c1f7`)
- [[pax-portal-api-request|PAX Portal API Request]] (n8n_id `T0yGFQaEQnHpmPdt`) — node "GET /p-market-web/v1/common/system-config1" (id `ab28bd2b-f699-4456-aa07-213f3799864d`)
- [[pax-portal-api-request|PAX Portal API Request]] (n8n_id `T0yGFQaEQnHpmPdt`) — node "GET /terminals/list" (id `efbaf083-72c3-40ce-b996-572263c36ced`)

## Used by (workflows)

- [[pax-device-monitoring-backup-2025-10-25|PAX Device Monitoring backup 2025-10-25]] — node "GET /current-user" (id `85c0cd76-1372-4c3a-8dbf-2d30d736d279`)
- [[pax-device-monitoring-backup-2025-10-25|PAX Device Monitoring backup 2025-10-25]] — node "GET /installed-apks" (id `63ae018f-0a2b-4a3f-8b51-2a3e19fbe4e2`)
- [[pax-device-monitoring-backup-2025-10-25|PAX Device Monitoring backup 2025-10-25]] — node "GET /p-market-web/v1/common/system-config" (id `ff950144-3287-460b-aeb9-f041415319fb`)
- [[pax-device-monitoring-backup-2025-10-25|PAX Device Monitoring backup 2025-10-25]] — node "GET /p-market-web/v1/common/system-config1" (id `ca31a9e4-4da2-424c-93ff-b8574971fe70`)
- [[pax-device-monitoring-backup-2025-10-25|PAX Device Monitoring backup 2025-10-25]] — node "GET /param" (id `1657d637-a10f-4a1f-8ce7-c42f7919a609`)
- [[pax-device-monitoring-backup-2025-10-25|PAX Device Monitoring backup 2025-10-25]] — node "GET /resellers/tree" (id `e351caf3-86b6-4394-8d73-7f0d989fad8d`)
- [[pax-device-monitoring-backup-2025-10-25|PAX Device Monitoring backup 2025-10-25]] — node "GET /terminals/list Count" (id `b97a5263-2bae-4dfd-8aaa-1c21fbd26915`)
- [[pax-device-monitoring-backup-2025-10-25|PAX Device Monitoring backup 2025-10-25]] — node "GET /terminals/list1" (id `e8da3d52-611b-4553-abae-a730ebe5f5be`)
- [[pax-device-monitoring-bk-2025-10-23-|PAX Device Monitoring (BK-2025-10-23)]] — node "Call 'PAX Device Monitoring'" (id `d3350bd3-91db-4d46-9ddf-afbf946e1640`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
