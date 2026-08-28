---
n8n_id: "TvvOeCowTLGapuKT"
instance: v1
name: "VNP Bulk Transactions Processor: Perform Sale with Tokenization"
status: inactive
last_modified: 2025-12-12T21:20:44.958Z
tags: []
fingerprint: "9d6e1d5138177a807f7fb9775b33811429d7ac55542c26783f887e524714cbf7"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# VNP Bulk Transactions Processor: Perform Sale with Tokenization

## Summary

- **Status:** inactive
- **n8n ID:** `TvvOeCowTLGapuKT`
- **Nodes:** 24
- **Last modified:** 2025-12-12T21:20:44.958Z

## Triggers

- **execute-workflow** — node "Start" (id `a4d537cb-c3d1-45bd-94a1-bd699633dbe9`)

## Depends on

### Credentials

- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Prod Transaction" (id `87ec4c01-b17d-4b67-9f65-fbcb98923d78`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `8db3b70b-41b1-41fd-bb9d-b6e06ce016ad`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Prod Transaction1" (id `b3bd326a-c50a-4d49-9528-b05defb7bfcd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `e2fba6f8-51ad-4904-af33-c76e96324409`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Create Token" (id `f6e812e3-e9e4-42df-828c-fbd955fadb31`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/payment/sale` — node "Prod Transaction" (id `87ec4c01-b17d-4b67-9f65-fbcb98923d78`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/payment/sale` — node "Prod Transaction1" (id `b3bd326a-c50a-4d49-9528-b05defb7bfcd`)
- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/cards` — node "Create Token" (id `f6e812e3-e9e4-42df-828c-fbd955fadb31`)

### Google Sheets

- [[../resources/google-sheets/1ewr7qr1xxpb3sazqnzfalick1m1zxrtxt-yupzbpjwe|VNP ISV Datastore]] (id `1ewr7qr1xxpb3SAzQnZfAlICk1m1Zxrtxt_yupzBPjwE`) — op `update`, tab `Gateways` — node "Update row in sheet" (id `8db3b70b-41b1-41fd-bb9d-b6e06ce016ad`)
- [[../resources/google-sheets/1ewr7qr1xxpb3sazqnzfalick1m1zxrtxt-yupzbpjwe|VNP ISV Datastore]] (id `1ewr7qr1xxpb3SAzQnZfAlICk1m1Zxrtxt_yupzBPjwE`) — op `?`, tab `Gateways` — node "Get row(s) in sheet" (id `e2fba6f8-51ad-4904-af33-c76e96324409`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
