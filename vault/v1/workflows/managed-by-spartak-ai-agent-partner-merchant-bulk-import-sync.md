---
n8n_id: "7KYfIAaMHwIubEgZ"
instance: v1
name: "[Managed by Spartak AI Agent] Partner Merchant Bulk Import Sync"
status: inactive
last_modified: 2026-01-16T01:19:29.214Z
tags: []
fingerprint: "c8b8cb1dec061c7243604f7f8e7c9ad6444af1ff64afc8779cad58f0d0c7379c"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# [Managed by Spartak AI Agent] Partner Merchant Bulk Import Sync

## Summary

- **Status:** inactive
- **n8n ID:** `7KYfIAaMHwIubEgZ`
- **Nodes:** 11
- **Last modified:** 2026-01-16T01:19:29.214Z

## Triggers

- **manual** — node "Manual Trigger" (id `manual-trigger`)
- **schedule** — node "Schedule (5 min)" (id `schedule-trigger`) — `every 5 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Activate Merchant" (id `activate-merchant`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Create Gateway" (id `create-gateway`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Create Merchant" (id `create-merchant`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Read Merchants Sheet" (id `read-merchants`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Sheet: Success" (id `update-success`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $('Create Merchant').item.json.data?.id ?? $('Create Merchant').item.json.id }}/status` — node "Activate Merchant" (id `activate-merchant`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/merchant/{{ $json.data?.id ?? $json.id }}/gateways` — node "Create Gateway" (id `create-gateway`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/merchant` — node "Create Merchant" (id `create-merchant`)

### Google Sheets

- [[../resources/google-sheets/1fu4x5rdws9brjpdiv8h7ojdbq47l2u9bykeofmf-ke0|1Fu4x5Rdws9bRjpdiV8H7OjDbQ47L2u9BykEofMf_Ke0]] (id `1Fu4x5Rdws9bRjpdiV8H7OjDbQ47L2u9BykEofMf_Ke0`) — op `read`, tab `Merchants` — node "Read Merchants Sheet" (id `read-merchants`)
- [[../resources/google-sheets/1fu4x5rdws9brjpdiv8h7ojdbq47l2u9bykeofmf-ke0|1Fu4x5Rdws9bRjpdiV8H7OjDbQ47L2u9BykEofMf_Ke0]] (id `1Fu4x5Rdws9bRjpdiV8H7OjDbQ47L2u9BykEofMf_Ke0`) — op `update`, tab `Merchants` — node "Update Sheet: Success" (id `update-success`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
