---
n8n_id: "3DhTwA35k0XtBluu"
instance: v1
name: "PAX Device Monitoring backup 2025-10-25"
status: inactive
last_modified: 2025-10-25T21:32:44.104Z
tags:
  - "backups"
fingerprint: "073a47567156bc5be8a7e7b2863d6011617fee1ca332783995013bbd921bf5d2"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PAX Device Monitoring backup 2025-10-25

## Summary

- **Status:** inactive
- **n8n ID:** `3DhTwA35k0XtBluu`
- **Nodes:** 55
- **Last modified:** 2025-10-25T21:32:44.104Z

## Triggers

- **execute-workflow** — node "PAXStore API Request" (id `42733a83-3f3b-44da-8308-946aa63b63a4`)
- **manual** — node "When clicking ‘Execute workflow’" (id `94d4208a-9dfd-4fe0-a45a-a7b3511b6326`)
- **schedule** — node "Schedule Trigger" (id `a7bf80dc-119c-4098-91ec-abea770bef2e`) — `every 1 hour(s) at :17`
- **error** — node "Error Trigger" (id `d14ace8b-06ea-44d2-83ae-ab7ce1084ff3`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `5fd180f3-e98c-46db-ad9c-87aae86d6a35`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `68eec9bb-eb7f-482c-a441-50c391071ec7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `83f8ed8e-6391-4389-8acc-553c2c2eb945`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "JWT" (id `9d641b77-a66f-4221-8365-570d61d0d1ea`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `c1ebeb72-458c-451a-9cc8-d1b535553dfd`)

### HTTP URLs

- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `POST https://auth.paxstore.us/passport/oauth/token` — node "POST /passport/oauth/token" (id `5360c5bc-e8a7-42bf-8884-f2c19913356d`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/login?client_id=admin&market=reseller` — node "Get /login" (id `93361e1f-fe7f-4d16-8ec2-7543a4565613`)
- *(dynamic URL)* — `={{ $json.method }} {{ $json.url }}` — node "POST: /passport/loginService Request" (id `c5a5daec-2e35-4c1f-b6b5-a465e6d368fe`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/check-acct?ln=spartak@platformfactory.io` — node "GET /check-acct" (id `e6da3d78-3728-4b26-b4a5-d5aebeed8c10`)
- [[../resources/http-urls/auth-paxstore-us|auth.paxstore.us]] — `GET https://auth.paxstore.us/passport/oauth/authorize?response_type=code&client_id=portal&scope=openid&state=jJDkaSBeTzRk-ahPO83ehe6xMSLJNap~&locale=en&code_challenge=FMJ%252BonUbyajSGNA8PWdD7QCKIIB2wQzx2%252B8tYBSrPj8%253D&market=reseller` — node "GET /passport/oauth/authorize" (id `fe5467d8-fa93-4b71-ae01-7d02477b1663`)

### Google Sheets

- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `appendOrUpdate`, tab `Devices` — node "Append or update row in sheet" (id `83f8ed8e-6391-4389-8acc-553c2c2eb945`)

### Slack channels

- [[../resources/slack-channels/c09n4c30zpd|pax-device-monitoring]] (id `C09N4C30ZPD`) — op `channel` — node "Send a message6" (id `5fd180f3-e98c-46db-ad9c-87aae86d6a35`)
- [[../resources/slack-channels/c09n4c30zpd|pax-device-monitoring]] (id `C09N4C30ZPD`) — op `channel` — node "Send a message" (id `68eec9bb-eb7f-482c-a441-50c391071ec7`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `c1ebeb72-458c-451a-9cc8-d1b535553dfd`)

### Sub-workflows (Execute Workflow calls)

- [[pax-device-monitoring|PAX Device Monitoring]] (n8n_id `Q9j3wpVGvegSl4Sy`) — node "GET /param" (id `1657d637-a10f-4a1f-8ce7-c42f7919a609`)
- [[pax-device-monitoring|PAX Device Monitoring]] (n8n_id `Q9j3wpVGvegSl4Sy`) — node "GET /installed-apks" (id `63ae018f-0a2b-4a3f-8b51-2a3e19fbe4e2`)
- [[pax-device-monitoring|PAX Device Monitoring]] (n8n_id `Q9j3wpVGvegSl4Sy`) — node "GET /current-user" (id `85c0cd76-1372-4c3a-8dbf-2d30d736d279`)
- [[pax-portal-access-token-manager|PAX Portal Access Token Manager]] (n8n_id `pY05hGyMJwslcwoH`) — node "Access Token" (id `9a9ceab8-2d9d-428c-bb67-c4abf404c56d`)
- [[pax-device-monitoring|PAX Device Monitoring]] (n8n_id `Q9j3wpVGvegSl4Sy`) — node "GET /terminals/list Count" (id `b97a5263-2bae-4dfd-8aaa-1c21fbd26915`)
- [[pax-portal-access-token-manager|PAX Portal Access Token Manager]] (n8n_id `pY05hGyMJwslcwoH`) — node "Access Token1" (id `c54a71c2-aeeb-462c-b7ed-16f089288289`)
- [[pax-device-monitoring|PAX Device Monitoring]] (n8n_id `Q9j3wpVGvegSl4Sy`) — node "GET /p-market-web/v1/common/system-config1" (id `ca31a9e4-4da2-424c-93ff-b8574971fe70`)
- [[pax-device-monitoring|PAX Device Monitoring]] (n8n_id `Q9j3wpVGvegSl4Sy`) — node "GET /resellers/tree" (id `e351caf3-86b6-4394-8d73-7f0d989fad8d`)
- [[pax-device-monitoring|PAX Device Monitoring]] (n8n_id `Q9j3wpVGvegSl4Sy`) — node "GET /terminals/list1" (id `e8da3d52-611b-4553-abae-a730ebe5f5be`)
- [[pax-device-monitoring|PAX Device Monitoring]] (n8n_id `Q9j3wpVGvegSl4Sy`) — node "GET /p-market-web/v1/common/system-config" (id `ff950144-3287-460b-aeb9-f041415319fb`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
