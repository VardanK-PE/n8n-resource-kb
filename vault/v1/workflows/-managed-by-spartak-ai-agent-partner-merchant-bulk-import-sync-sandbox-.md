---
n8n_id: "QbFajy9S4G2FxoCb"
instance: v1
name: "[Managed by Spartak AI Agent] Partner Merchant Bulk Import Sync (SANDBOX)"
status: inactive
last_modified: 2026-01-16T01:52:20.595Z
tags: []
fingerprint: "fdba6fb86f8db9863cff4dfeae6c63d81f4cc95fecb04738abe962371a7443f7"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# [Managed by Spartak AI Agent] Partner Merchant Bulk Import Sync (SANDBOX)

## Summary

- **Status:** inactive
- **n8n ID:** `QbFajy9S4G2FxoCb`
- **Nodes:** 12
- **Last modified:** 2026-01-16T01:52:20.595Z

## Triggers

- **manual** — node "Manual Trigger" (id `manual-trigger`)
- **schedule** — node "Schedule (5 min)" (id `schedule-trigger`) — `every 5 minute(s)`
- **webhook** — node "Webhook Trigger" (id `webhook-trigger`) — POST `partner-merchant-sandbox-test`

## Depends on

### Credentials

- [[../resources/credentials/24tzlx6tgpwvjaha|PE (SANDBOX) Master Bearer Token]] (`httpBearerAuth`, id `24TzLX6TGPWvJAha`) — node "Activate Merchant" (id `activate-merchant`)
- [[../resources/credentials/24tzlx6tgpwvjaha|PE (SANDBOX) Master Bearer Token]] (`httpBearerAuth`, id `24TzLX6TGPWvJAha`) — node "Create Gateway" (id `create-gateway`)
- [[../resources/credentials/24tzlx6tgpwvjaha|PE (SANDBOX) Master Bearer Token]] (`httpBearerAuth`, id `24TzLX6TGPWvJAha`) — node "Create Merchant" (id `create-merchant`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Read Merchants Sheet" (id `read-merchants`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Sheet: Success" (id `update-success`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-dev|console.payengine.dev]] — `PATCH https://console.payengine.dev/api/v2/merchant/{{ $('Create Merchant').item.json.data?.id ?? $('Create Merchant').item.json.id }}/status` — node "Activate Merchant" (id `activate-merchant`)
- [[../resources/http-urls/console-payengine-dev|console.payengine.dev]] — `POST https://console.payengine.dev/api/merchant/{{ $json.data?.id ?? $json.id }}/gateways` — node "Create Gateway" (id `create-gateway`)
- [[../resources/http-urls/console-payengine-dev|console.payengine.dev]] — `POST https://console.payengine.dev/api/merchant` — node "Create Merchant" (id `create-merchant`)

### Google Sheets

- [[../resources/google-sheets/1b3cirl5ddkepibchncs942kwm9zemun3okyja-rmur4|1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4]] (id `1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4`) — op `read`, tab `Merchants` — node "Read Merchants Sheet" (id `read-merchants`)
- [[../resources/google-sheets/1b3cirl5ddkepibchncs942kwm9zemun3okyja-rmur4|1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4]] (id `1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4`) — op `update`, tab `Merchants` — node "Update Sheet: Success" (id `update-success`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
