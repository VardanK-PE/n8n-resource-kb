---
n8n_id: "Mf9JkMvLriRuZw9D"
name: "[Managed by Spartak AI Agent] Partner Merchant Bulk Import Sync (SANDBOX)"
status: inactive
last_modified: 2026-05-11T04:26:42.418Z
tags: []
fingerprint: "ee4681fff12816fd312a68c34817286b902b70733dfaa6008c970ce4ff84c907"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# [Managed by Spartak AI Agent] Partner Merchant Bulk Import Sync (SANDBOX)

## Summary

- **Status:** inactive
- **n8n ID:** `Mf9JkMvLriRuZw9D`
- **Nodes:** 21
- **Last modified:** 2026-05-11T04:26:42.418Z

## Triggers

- **webhook** — node "Webhook Trigger" (id `df3996d4`) — POST `partner-merchant-sync-sandbox`
- **manual** — node "Manual Trigger" (id `manual-trigger`)
- **schedule** — node "Schedule (5 min)" (id `schedule-trigger`) — `every 5 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/24tzlx6tgpwvjaha|PE (SANDBOX) Master Bearer Token]] (`httpBearerAuth`, id `24TzLX6TGPWvJAha`) — node "Activate Merchant" (id `activate-merchant`)
- [[../resources/credentials/24tzlx6tgpwvjaha|PE (SANDBOX) Master Bearer Token]] (`httpBearerAuth`, id `24TzLX6TGPWvJAha`) — node "Create Gateway" (id `create-gateway`)
- [[../resources/credentials/24tzlx6tgpwvjaha|PE (SANDBOX) Master Bearer Token]] (`httpBearerAuth`, id `24TzLX6TGPWvJAha`) — node "Create Merchant" (id `create-merchant`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Debug: After Activate" (id `debug-after-activate`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Debug: After Create" (id `debug-after-create`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Debug: After Filter" (id `debug-after-filter`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Debug: After Gateway" (id `debug-after-gateway`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Debug: After Prepare" (id `debug-after-prepare`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Debug: After Switch" (id `debug-after-switch`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Debug: After Update" (id `debug-after-update`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Debug: Log After Read" (id `debug-log-after-read`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Read Merchants Sheet" (id `read-merchants`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Merchants Row" (id `update-merchants-row-v2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Success" (id `update-success`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-dev|console.payengine.dev]] — `PATCH https://console.payengine.dev/api/v2/merchant/{{ $('Create Merchant').item.json.data?.id ?? $('Create Merchant').item.json.id }}/status` — node "Activate Merchant" (id `activate-merchant`)
- [[../resources/http-urls/console-payengine-dev|console.payengine.dev]] — `POST https://console.payengine.dev/api/merchant/{{ $('Create Merchant').item.json.data?.id ?? $('Create Merchant').item.json.id }}/gateways` — node "Create Gateway" (id `create-gateway`)
- [[../resources/http-urls/console-payengine-dev|console.payengine.dev]] — `POST https://console.payengine.dev/api/merchant` — node "Create Merchant" (id `create-merchant`)

### Google Sheets

- [[../resources/google-sheets/1b3cirl5ddkepibchncs942kwm9zemun3okyja-rmur4|1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4]] (id `1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4`) — op `append`, tab `Sync Log` — node "Debug: After Activate" (id `debug-after-activate`)
- [[../resources/google-sheets/1b3cirl5ddkepibchncs942kwm9zemun3okyja-rmur4|1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4]] (id `1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4`) — op `append`, tab `Sync Log` — node "Debug: After Create" (id `debug-after-create`)
- [[../resources/google-sheets/1b3cirl5ddkepibchncs942kwm9zemun3okyja-rmur4|1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4]] (id `1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4`) — op `append`, tab `Sync Log` — node "Debug: After Filter" (id `debug-after-filter`)
- [[../resources/google-sheets/1b3cirl5ddkepibchncs942kwm9zemun3okyja-rmur4|1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4]] (id `1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4`) — op `append`, tab `Sync Log` — node "Debug: After Gateway" (id `debug-after-gateway`)
- [[../resources/google-sheets/1b3cirl5ddkepibchncs942kwm9zemun3okyja-rmur4|1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4]] (id `1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4`) — op `append`, tab `Sync Log` — node "Debug: After Prepare" (id `debug-after-prepare`)
- [[../resources/google-sheets/1b3cirl5ddkepibchncs942kwm9zemun3okyja-rmur4|1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4]] (id `1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4`) — op `append`, tab `Sync Log` — node "Debug: After Switch" (id `debug-after-switch`)
- [[../resources/google-sheets/1b3cirl5ddkepibchncs942kwm9zemun3okyja-rmur4|1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4]] (id `1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4`) — op `append`, tab `Sync Log` — node "Debug: After Update" (id `debug-after-update`)
- [[../resources/google-sheets/1b3cirl5ddkepibchncs942kwm9zemun3okyja-rmur4|1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4]] (id `1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4`) — op `append`, tab `Sync Log` — node "Debug: Log After Read" (id `debug-log-after-read`)
- [[../resources/google-sheets/1b3cirl5ddkepibchncs942kwm9zemun3okyja-rmur4|1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4]] (id `1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4`) — op `read`, tab `Merchants` — node "Read Merchants Sheet" (id `read-merchants`)
- [[../resources/google-sheets/1b3cirl5ddkepibchncs942kwm9zemun3okyja-rmur4|1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4]] (id `1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4`) — op `update`, tab `Merchants` — node "Update Merchants Row" (id `update-merchants-row-v2`)
- [[../resources/google-sheets/1b3cirl5ddkepibchncs942kwm9zemun3okyja-rmur4|1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4]] (id `1B3cIrL5ddKePiBCHNCs942KwM9zEmUn3okYja_rmUR4`) — op `append`, tab `Sync Log` — node "Log Success" (id `update-success`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
