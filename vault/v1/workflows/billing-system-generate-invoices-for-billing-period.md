---
n8n_id: "esPJ6uwgFODvFnyt"
instance: v1
name: "Billing System - Generate Invoices for Billing Period"
status: inactive
last_modified: 2026-06-30T10:02:50.798Z
tags: []
fingerprint: "2fb06c8b0eedc404d7ef8e6570d78a3e220b588f0637c778630bb43d5f2e0626"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Billing System - Generate Invoices for Billing Period

## Summary

- **Status:** inactive
- **n8n ID:** `esPJ6uwgFODvFnyt`
- **Nodes:** 60
- **Last modified:** 2026-06-30T10:02:50.798Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `5cba2625-1335-4212-8679-eb5780affde9`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `08536798-f453-489e-95ab-b86e202ecc03`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Create QB Invoice" (id `307fc912-6b0c-442b-8666-a99b5a5077da`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `3917d6cb-eff3-4f7d-b2ae-428b987b20c6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Created Invoice" (id `43389d39-307e-4ce7-b508-9eeb759c642e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get ACH Transactions" (id `6ab626c7-4447-43a5-a821-a0ca83ff1238`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get PCI non compliant merchant details" (id `6cf6d027-82b4-4853-86fc-42536ce80390`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file" (id `7172f852-fbaf-4d5b-9771-75300fb7cc20`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Search files and folders" (id `c6d10005-c641-48bd-bbf8-5c0f8fb0045e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create sheet" (id `dd48b366-2e6d-4dde-8c9b-9c17fe2acb4c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `e5568aa0-0256-4692-86f5-02c30b963afd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get partner billing terms" (id `f0e6dbba-9dc4-4156-b32b-59061067b576`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `f2485891-d7ba-427f-9f1f-1e2bc4d76894`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create folder" (id `fe0a4643-64eb-4410-bd35-2cc4f121fa9e`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant Details" (id `fe3ce3eb-fce2-4a6d-98d8-9dbdf94b9d5c`)

### HTTP URLs

- [[../resources/http-urls/quickbooks-api-intuit-com|quickbooks.api.intuit.com]] — `POST https://quickbooks.api.intuit.com/v3/company/9341452828840730/invoice?minorversion=75` — node "Create QB Invoice" (id `307fc912-6b0c-442b-8666-a99b5a5077da`)
- [[../resources/http-urls/pf-prod-ecs-task-container-gotenberg-3000|pf-prod-ecs-task-container-gotenberg:3000]] — `POST http://pf-prod-ecs-task-container-gotenberg:3000/forms/chromium/convert/html` — node "Convert To PDF [GOTENBERG]" (id `4f0d787d-c9f8-4e5b-83fb-ed13b862c86b`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant Details" (id `fe3ce3eb-fce2-4a6d-98d8-9dbdf94b9d5c`)

### Google Sheets

- [[../resources/google-sheets/1wi-6uhhhtrnpk2c1wpfjwwgbvlmtp0tvswnlpy-poie|Combined ACH Transactions Data]] (id `1Wi_6UHhhtrnpk2c1WpfjwwGbvLmTp0TvSwnLPY_POIE`) — op `?`, tab `={{ $json.sheet_name }}` — node "Get row(s) in sheet" (id `08536798-f453-489e-95ab-b86e202ecc03`)
- [[../resources/google-sheets/1wi-6uhhhtrnpk2c1wpfjwwgbvlmtp0tvswnlpy-poie|Combined ACH Transactions Data]] (id `1Wi_6UHhhtrnpk2c1WpfjwwGbvLmTp0TvSwnLPY_POIE`) — op `append`, tab `={{ $('Set spreadsheet name').first().json.sheet_name }}` — node "Append row in sheet" (id `3917d6cb-eff3-4f7d-b2ae-428b987b20c6`)
- [[../resources/google-sheets/1hxh00hkhzskiwupgayf-bljqvrvjty0m88gx4h9zbri|N8N Quick Book Logs]] (id `1hXh00hKHzsKiwUPGAyf-BljqVRVJtY0m88gx4h9zbrI`) — op `append`, tab `Invoice Log` — node "Log Created Invoice" (id `43389d39-307e-4ce7-b508-9eeb759c642e`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $('Set spreadsheet name').first().json.snapshot_period }}-ALL-AGGREGATE` — node "Get ACH Transactions" (id `6ab626c7-4447-43a5-a821-a0ca83ff1238`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `?`, tab `={{ $('Set spreadsheet name').first().json.sheet_name }}` — node "Get PCI non compliant merchant details" (id `6cf6d027-82b4-4853-86fc-42536ce80390`)
- [[../resources/google-sheets/1wi-6uhhhtrnpk2c1wpfjwwgbvlmtp0tvswnlpy-poie|Combined ACH Transactions Data]] (id `1Wi_6UHhhtrnpk2c1WpfjwwGbvLmTp0TvSwnLPY_POIE`) — op `create`, tab `null` — node "Create sheet" (id `dd48b366-2e6d-4dde-8c9b-9c17fe2acb4c`)
- [[../resources/google-sheets/1wi-6uhhhtrnpk2c1wpfjwwgbvlmtp0tvswnlpy-poie|Combined ACH Transactions Data]] (id `1Wi_6UHhhtrnpk2c1WpfjwwGbvLmTp0TvSwnLPY_POIE`) — op `appendOrUpdate`, tab `={{ $('Set spreadsheet name').first().json.sheet_name }}` — node "Google Sheets" (id `e5568aa0-0256-4692-86f5-02c30b963afd`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "Get partner billing terms" (id `f0e6dbba-9dc4-4156-b32b-59061067b576`)
- [[../resources/google-sheets/1wi-6uhhhtrnpk2c1wpfjwwgbvlmtp0tvswnlpy-poie|Combined ACH Transactions Data]] (id `1Wi_6UHhhtrnpk2c1WpfjwwGbvLmTp0TvSwnLPY_POIE`) — op `appendOrUpdate`, tab `={{ $('Set spreadsheet name').first().json.sheet_name }}` — node "Google Sheets4" (id `f2485891-d7ba-427f-9f1f-1e2bc4d76894`)

### Google Drive

- *(dynamic)* — op `?` — node "Upload file" (id `7172f852-fbaf-4d5b-9771-75300fb7cc20`)
- [[../resources/google-drive/1du7zmdcqvq-gdn3dhrhnhr7umbbubst-|Combined ACH Transactions]] (`folder`, id `1Du7zmDCQvQ_GDN3dhrHnhr7uMbBuBSt-`) — op `?` — node "Create folder" (id `fe0a4643-64eb-4410-bd35-2cc4f121fa9e`)

### Data tables (n8n)

- [[../resources/data-tables/pz9zqssjshkjnyb9|Billing - Invoices]] (id `pz9ZQssJShkJNYb9`) — op `?` — node "Insert row" (id `1755592b-f0fe-43ab-b33f-5a2b018127ed`)

### Sub-workflows (Execute Workflow calls)

- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `2f225f5f-3611-4687-863b-52c69aa0a090`)
- [[billing-system-get-merchant-ach-transactions|Billing System - Get merchant ACH transactions]] (n8n_id `Zbodr3mJ822pD7nB`) — node "Call 'Billing System - Get merchant platform fees'1" (id `3615be83-de96-4c3e-94f8-aae565fafae4`)
- [[billing-system-get-merchant-platform-fees|Billing System - Get merchant platform fees]] (n8n_id `gJfB9BKQfkmsXvyt`) — node "Call 'Billing System - Get merchant platform fees'" (id `859b7296-ab39-428d-8dc2-21b1110b46f6`)
- [[billing-system-get-or-create-qb-merchant-info|Billing System - Get Or Create QB merchant info]] (n8n_id `jYTz952jPsD9jjWV`) — node "Get Or Create Merchant QB ID" (id `db4ade9d-7fe1-4121-aec0-348134259121`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
