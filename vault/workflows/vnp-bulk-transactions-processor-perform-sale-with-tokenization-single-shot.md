---
n8n_id: "cdfm7KHD1A2WeYfb"
name: "VNP Bulk Transactions Processor: Perform Sale with Tokenization (Single Shot)"
status: inactive
last_modified: 2026-01-12T21:02:26.915Z
tags: []
fingerprint: "b028e5285f40b3285715f43a312c5a15b8457398a419fcfffb2288c201c2895d"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# VNP Bulk Transactions Processor: Perform Sale with Tokenization (Single Shot)

## Summary

- **Status:** inactive
- **n8n ID:** `cdfm7KHD1A2WeYfb`
- **Nodes:** 18
- **Last modified:** 2026-01-12T21:02:26.915Z

## Triggers

- **execute-workflow** — node "Start" (id `ed8c8596-cf42-48a1-9ef1-5b65e9277fda`)

## Depends on

### Credentials

- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Create Token" (id `24ff44c5-a2b3-4142-9d72-69e17ae6a3ab`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `3c7f6fe1-bed1-40c3-b3ab-e8441cbce9f1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `62cacb11-ad36-4a72-aa1d-2b62f268b13d`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Prod Transaction" (id `d4f73964-d3bf-4381-8ef7-fc334223811f`)

### HTTP URLs

- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/cards` — node "Create Token" (id `24ff44c5-a2b3-4142-9d72-69e17ae6a3ab`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/payment/sale` — node "Prod Transaction" (id `d4f73964-d3bf-4381-8ef7-fc334223811f`)

### Google Sheets

- [[../resources/google-sheets/1ewr7qr1xxpb3sazqnzfalick1m1zxrtxt-yupzbpjwe|VNP ISV Datastore]] (id `1ewr7qr1xxpb3SAzQnZfAlICk1m1Zxrtxt_yupzBPjwE`) — op `?`, tab `Gateways` — node "Get row(s) in sheet" (id `3c7f6fe1-bed1-40c3-b3ab-e8441cbce9f1`)
- [[../resources/google-sheets/1ewr7qr1xxpb3sazqnzfalick1m1zxrtxt-yupzbpjwe|VNP ISV Datastore]] (id `1ewr7qr1xxpb3SAzQnZfAlICk1m1Zxrtxt_yupzBPjwE`) — op `update`, tab `Gateways` — node "Update row in sheet" (id `62cacb11-ad36-4a72-aa1d-2b62f268b13d`)

## Used by (workflows)

- [[vnp-bulk-transactions-processor|VNP Bulk Transactions Processor]] — node "Call VNP Bulk Transaction Perform Sale with Tokenization" (id `2acfb8f0-30e3-4fe9-b74d-cc62403323e7`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
