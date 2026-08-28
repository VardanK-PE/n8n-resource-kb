---
n8n_id: "1GngUg26uDoLxlom"
name: "PCI generate invoices for already charged merchants"
status: inactive
last_modified: 2026-08-14T19:27:02.017Z
tags: []
fingerprint: "fdb40ea407fea1e65ac764820ba5d7f01df97d6103c38f9543dc823cd9b789c4"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PCI generate invoices for already charged merchants

## Summary

- **Status:** inactive
- **n8n ID:** `1GngUg26uDoLxlom`
- **Nodes:** 46
- **Last modified:** 2026-08-14T19:27:02.017Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `219650f6-f2da-4d49-acf6-0410e95a2410`)

## Depends on

### Credentials

- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Create Customer1" (id `0e2981b7-8dff-46da-8968-4eda0412f267`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get merchants for QB" (id `29613070-54eb-461e-a367-9f95da0c6ed4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Created Customer" (id `30685938-27c0-4771-a3c4-89bbee00ba4d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Search files and folders" (id `31f30578-92f1-4e30-8eea-765f24debff9`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Execute a SQL query" (id `3dcd6804-c687-46c7-8794-b7fcd31040ed`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Created Invoice" (id `404785b5-e227-4d12-84bf-ce5df2ca1caf`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant Details" (id `5d059abf-7049-46cb-9665-2013966d2605`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets10" (id `614e627a-00c7-479b-aa4f-4689af9e3ff7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get merchants for QB1" (id `6ce45f8e-3d61-437a-89e5-f6172f03380a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `7439bc3f-2ba6-4b4a-8e4d-ed3f204a0631`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `8be56f2f-f8d3-4442-8225-ca426b9686f0`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "FindCustomer" (id `986aabec-ccae-41d2-98db-eafe192e9818`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file" (id `9cc2839e-6c59-42a5-aab2-da80f41c942a`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Delete an invoice" (id `abd0ca83-fb34-403c-84ba-2255cdce8bfa`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Create QB Invoice1" (id `b5383c22-9c43-4c3c-ac65-ccf9fbadf806`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create folder" (id `b9834582-6900-4108-9614-ab0589bf0fea`)

### HTTP URLs

- [[../resources/http-urls/quickbooks-api-intuit-com|quickbooks.api.intuit.com]] — `POST https://quickbooks.api.intuit.com/v3/company/9341452828840730/customer?minorversion=75` — node "Create Customer1" (id `0e2981b7-8dff-46da-8968-4eda0412f267`)
- [[../resources/http-urls/pf-prod-ecs-task-container-gotenberg-3000|pf-prod-ecs-task-container-gotenberg:3000]] — `POST http://pf-prod-ecs-task-container-gotenberg:3000/forms/chromium/convert/html` — node "Convert To PDF [GOTENBERG]" (id `57197759-ceca-460b-b80f-e3cd3d324841`)
- [[../resources/http-urls/quickbooks-api-intuit-com|quickbooks.api.intuit.com]] — `POST https://quickbooks.api.intuit.com/v3/company/9341452828840730/invoice?minorversion=75` — node "Create QB Invoice1" (id `b5383c22-9c43-4c3c-ac65-ccf9fbadf806`)

### Databases

- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Execute a SQL query" (id `3dcd6804-c687-46c7-8794-b7fcd31040ed`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant Details" (id `5d059abf-7049-46cb-9665-2013966d2605`)

### Google Sheets

- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `?`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Get merchants for QB" (id `29613070-54eb-461e-a367-9f95da0c6ed4`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `append`, tab `QB LOGS - CUSTOMERS CREATED` — node "Log Created Customer" (id `30685938-27c0-4771-a3c4-89bbee00ba4d`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `append`, tab `QB LOGS - INVOICES` — node "Log Created Invoice" (id `404785b5-e227-4d12-84bf-ce5df2ca1caf`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Google Sheets10" (id `614e627a-00c7-479b-aa4f-4689af9e3ff7`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `?`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Get merchants for QB1" (id `6ce45f8e-3d61-437a-89e5-f6172f03380a`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `?`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Get row(s) in sheet" (id `7439bc3f-2ba6-4b4a-8e4d-ed3f204a0631`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `update`, tab `={{ $('Entry Point').first().json.spreadsheet_name }}` — node "Google Sheets4" (id `8be56f2f-f8d3-4442-8225-ca426b9686f0`)

### Google Drive

- *(dynamic)* — op `?` — node "Upload file" (id `9cc2839e-6c59-42a5-aab2-da80f41c942a`)
- [[../resources/google-drive/1cr3h8xm6e360wlswg4dxnfincmgmuhno|PCI Non Compliant Merchants Invoices]] (`folder`, id `1cr3h8XM6E360wlswg4DXNfINcMgMuHNo`) — op `?` — node "Create folder" (id `b9834582-6900-4108-9614-ab0589bf0fea`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
