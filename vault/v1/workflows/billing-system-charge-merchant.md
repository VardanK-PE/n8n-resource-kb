---
n8n_id: "acEoUXW1K4ilWWUV"
instance: v1
name: "Billing System - Charge Merchant"
status: inactive
last_modified: 2026-04-06T19:18:07.272Z
tags: []
fingerprint: "4c3e6d18aaa58b2c03fa0cd14f7256afb3d04bbb677021ecc8d96949c3a5b4fe"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Billing System - Charge Merchant

## Summary

- **Status:** inactive
- **n8n ID:** `acEoUXW1K4ilWWUV`
- **Nodes:** 32
- **Last modified:** 2026-04-06T19:18:07.272Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `af1fa625-27ba-40eb-b698-18625af3c66e`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `294c29c7-8ef3-486f-89e7-ad4d850c092f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Transaction Details3" (id `659780f4-5dc7-4e5a-8b5d-d37083a34bc5`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get Merchant Info" (id `6b55507c-eb4d-44d9-b759-d3b8a9c19c71`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Transaction Details1" (id `ad71d68f-dac3-4457-a424-6de2b693daf3`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/payment/ach` — node "Perform the Charge" (id `01e44b24-97f5-4c3b-b9ae-175ac56da26f`)
- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/bank-accounts` — node "Create Bank Account Token1" (id `d1bd3f7a-ac13-4e9d-85fa-e3911411cdb9`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get Merchant Info" (id `6b55507c-eb4d-44d9-b759-d3b8a9c19c71`)

### Google Sheets

- [[../resources/google-sheets/1wi-6uhhhtrnpk2c1wpfjwwgbvlmtp0tvswnlpy-poie|Combined ACH Transactions Data]] (id `1Wi_6UHhhtrnpk2c1WpfjwwGbvLmTp0TvSwnLPY_POIE`) — op `append`, tab `Transaction Log` — node "Append row in sheet" (id `294c29c7-8ef3-486f-89e7-ad4d850c092f`)
- [[../resources/google-sheets/1wi-6uhhhtrnpk2c1wpfjwwgbvlmtp0tvswnlpy-poie|Combined ACH Transactions Data]] (id `1Wi_6UHhhtrnpk2c1WpfjwwGbvLmTp0TvSwnLPY_POIE`) — op `append`, tab `Token Log` — node "Update Transaction Details3" (id `659780f4-5dc7-4e5a-8b5d-d37083a34bc5`)
- [[../resources/google-sheets/1wi-6uhhhtrnpk2c1wpfjwwgbvlmtp0tvswnlpy-poie|Combined ACH Transactions Data]] (id `1Wi_6UHhhtrnpk2c1WpfjwwGbvLmTp0TvSwnLPY_POIE`) — op `append`, tab `Error Log` — node "Update Transaction Details1" (id `ad71d68f-dac3-4457-a424-6de2b693daf3`)

### Data tables (n8n)

- [[../resources/data-tables/pz9zqssjshkjnyb9|Billing - Invoices]] (id `pz9ZQssJShkJNYb9`) — op `update` — node "Update row(s)1" (id `4e7782e7-eafe-4f84-a65f-4660ad68e208`)
- [[../resources/data-tables/pz9zqssjshkjnyb9|Billing - Invoices]] (id `pz9ZQssJShkJNYb9`) — op `get` — node "Get statement info" (id `5825a597-d5dc-4659-99fc-9db8114cab08`)
- [[../resources/data-tables/pz9zqssjshkjnyb9|Billing - Invoices]] (id `pz9ZQssJShkJNYb9`) — op `update` — node "Update row(s)" (id `fd3d3e23-0067-4d56-a36d-ee7232f59442`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
