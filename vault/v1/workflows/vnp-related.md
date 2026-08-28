---
n8n_id: "D2Ja6zhlMvvETntC"
instance: v1
name: "VNP Related"
status: active
last_modified: 2025-10-30T21:22:43.062Z
tags: []
fingerprint: "0399eaee018ccb4eb5874742412da10f10c351ee04ce8383399959b07cd08770"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# VNP Related

## Summary

- **Status:** active
- **n8n ID:** `D2Ja6zhlMvvETntC`
- **Nodes:** 20
- **Last modified:** 2025-10-30T21:22:43.062Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `69d3e37c-dc5a-4a6e-872a-3400cf745fa2`)
- **schedule** — node "Schedule Trigger" (id `f6ed427a-5cdc-40b9-8ef7-b6a5f427a5f2`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Activate Submerchants" (id `09c02269-f82d-4cd7-897b-e6d46128f6dc`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `21f43b25-4692-48fb-aa75-0b25c0c32fc6`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Activate Submerchants3" (id `2864d847-da41-467e-b4e2-b990586ec819`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Activate Submerchants3" (id `2864d847-da41-467e-b4e2-b990586ec819`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Update Descriptor1" (id `33cd12dc-60a9-4dda-aa4f-eb340cad4624`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Update Descriptor1" (id `33cd12dc-60a9-4dda-aa4f-eb340cad4624`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Submerchants" (id `4a54713e-b406-483e-844a-ef344b13e6c3`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Get Submerchants1" (id `4a9ca114-9522-41cb-969e-75c674d2432d`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Update Descriptor" (id `b332d4be-a50f-470e-8a77-4c23b6816155`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Update Descriptor" (id `b332d4be-a50f-470e-8a77-4c23b6816155`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Set to editing" (id `ba871b45-848e-4971-9fcd-f995197b4f48`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Set to editing" (id `ba871b45-848e-4971-9fcd-f995197b4f48`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Submerchants2" (id `c7de144b-ff54-452e-b88a-806794d8f2df`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Submerchant Sheet" (id `cc3a6fb4-af24-4e5b-9443-d34f1a263278`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Create Submerchants" (id `cd966d4a-fd6a-447e-a53f-719b9a69839a`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Activate Submerchants4" (id `fcf1d2ca-908e-48b0-b768-5f5ae21bb83f`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.id ?? $json.data.id}}/status` — node "Activate Submerchants" (id `09c02269-f82d-4cd7-897b-e6d46128f6dc`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $('Get Submerchants2').item.json.pe_mid }}/status` — node "Activate Submerchants3" (id `2864d847-da41-467e-b4e2-b990586ec819`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.data.id }}` — node "Update Descriptor1" (id `33cd12dc-60a9-4dda-aa4f-eb340cad4624`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/merchant` — node "Get Submerchants1" (id `4a9ca114-9522-41cb-969e-75c674d2432d`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $('Get Submerchants2').item.json.pe_mid }}` — node "Update Descriptor" (id `b332d4be-a50f-470e-8a77-4c23b6816155`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_mid }}/status` — node "Set to editing" (id `ba871b45-848e-4971-9fcd-f995197b4f48`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/merchant` — node "Create Submerchants" (id `cd966d4a-fd6a-447e-a53f-719b9a69839a`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_mid }}/status` — node "Activate Submerchants4" (id `fcf1d2ca-908e-48b0-b768-5f5ae21bb83f`)

### Google Sheets

- [[../resources/google-sheets/1ewr7qr1xxpb3sazqnzfalick1m1zxrtxt-yupzbpjwe|VNP ISV Datastore]] (id `1ewr7qr1xxpb3SAzQnZfAlICk1m1Zxrtxt_yupzBPjwE`) — op `?`, tab `Virtaul MIDS` — node "Get Submerchants" (id `4a54713e-b406-483e-844a-ef344b13e6c3`)
- [[../resources/google-sheets/1ewr7qr1xxpb3sazqnzfalick1m1zxrtxt-yupzbpjwe|VNP ISV Datastore]] (id `1ewr7qr1xxpb3SAzQnZfAlICk1m1Zxrtxt_yupzBPjwE`) — op `?`, tab `Virtaul MIDS` — node "Get Submerchants2" (id `c7de144b-ff54-452e-b88a-806794d8f2df`)
- [[../resources/google-sheets/1ewr7qr1xxpb3sazqnzfalick1m1zxrtxt-yupzbpjwe|VNP ISV Datastore]] (id `1ewr7qr1xxpb3SAzQnZfAlICk1m1Zxrtxt_yupzBPjwE`) — op `update`, tab `Virtaul MIDS` — node "Update Submerchant Sheet" (id `cc3a6fb4-af24-4e5b-9443-d34f1a263278`)

### Slack channels

- [[../resources/slack-channels/c09p9rk9nh1|vnp-merchant-alerts]] (id `C09P9RK9NH1`) — op `channel` — node "Send a message" (id `21f43b25-4692-48fb-aa75-0b25c0c32fc6`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
