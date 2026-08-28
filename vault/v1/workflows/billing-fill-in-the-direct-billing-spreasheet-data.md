---
n8n_id: "a3Y4lCqs1TkkFmSG"
instance: v1
name: "Billing - Fill in the Direct Billing Spreasheet data"
status: inactive
last_modified: 2026-07-15T18:26:08.830Z
tags: []
fingerprint: "ed86d2ee629d64280e35d2b84f268377aa7d0b728f2b5e28a5611eb3ec9989e6"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Billing - Fill in the Direct Billing Spreasheet data

## Summary

- **Status:** inactive
- **n8n ID:** `a3Y4lCqs1TkkFmSG`
- **Nodes:** 39
- **Last modified:** 2026-07-15T18:26:08.830Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `5b6f40da-2fdb-4795-8bb8-c945e3347b54`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `a1ba5684-b2a2-4ad6-8956-f2fb1b054900`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Write Auth Fees" (id `0142da2b-6ce8-455f-9ddf-02a71f7b4f5d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update FeeReport Rows" (id `0f1d16b4-2d9d-4dcd-ba35-39af6a779034`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Find Period Folder" (id `1385c650-b0b9-4d07-aadb-b70fc6deee8f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Write Tier + Rate" (id `2642cb52-f4bc-440c-928f-bc2cfcbfe053`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Find Copied Spreadsheet" (id `2821e3ef-970c-4f49-8073-cfdc670eaccc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Find Master Spreadsheet" (id `36085478-6a27-4538-91dd-763b834e3cc6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Find Copied Spreadsheet1" (id `47617faa-6123-499a-860d-9289a7becabf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Find Residuals Root Folder" (id `520abd56-820b-4c07-af57-17cd99b4fe7c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Add Auth Fee Headers" (id `582a7f4c-859f-485f-98d6-a28f99d91a44`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append FeeReport Rows" (id `5e3343bf-cb0f-4a0b-acf0-2815194b40c7`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Fetch Merchant + Fee Schedule" (id `647377ad-a9a4-497c-ad3f-08b66ecc0025`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get MerchantDetail Rows" (id `71a165c7-072b-4e75-8cc6-e4dbe53149b7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Add Tier+Rate Headers" (id `84b1348e-44b8-4fd1-9fc0-e0525a4ecf73`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get AuthDetail Rows" (id `8e9f1dd8-9e0e-4bfb-a021-d31f16c103ba`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Write MerchantDetail Fill" (id `92799649-0148-451d-8b75-24176927698c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Copy Spreadsheet" (id `c359f0ab-55d3-441e-b0c4-e741e6f488a7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get FeeReport Rows" (id `c4c159da-ea5b-4820-a002-b3a0809fb9cf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get ICQual Final" (id `dd1ed054-5abe-4cea-ab70-58fa415665c5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Find Period Folder1" (id `e6a5566b-3c68-4eba-9efa-99bd777775cb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Find Residuals Root Folder1" (id `eac700df-28f6-4d9d-8c32-d843c3ac532c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Intercharge Categories" (id `f925b780-448f-4b6f-8e85-e3a677af7e91`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `fd2a7f10-671f-4333-9395-80d79f069dee`)

### HTTP URLs

- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `PUT https://sheets.googleapis.com/v4/spreadsheets/{{ $('No Operation, do nothing').first().json.id }}/values/{{ encodeURIComponent("'" + $('Compute Target Period').first().json.authReportSheetName + "'!O1:P1") }}?valueInputOption=RAW` — node "Add Auth Fee Headers" (id `582a7f4c-859f-485f-98d6-a28f99d91a44`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `PUT https://sheets.googleapis.com/v4/spreadsheets/{{ $json.id }}/values/{{ encodeURIComponent("'" + $('Compute Target Period').first().json.qualReportSheetName + "'!T1:U1") }}?valueInputOption=RAW` — node "Add Tier+Rate Headers" (id `84b1348e-44b8-4fd1-9fc0-e0525a4ecf73`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Fetch Merchant + Fee Schedule" (id `647377ad-a9a4-497c-ad3f-08b66ecc0025`)

### Google Sheets

- *(dynamic spreadsheet)* — op `update`, tab `={{ $('Compute Target Period').first().json.authReportSheetName }}` — node "Write Auth Fees" (id `0142da2b-6ce8-455f-9ddf-02a71f7b4f5d`)
- *(dynamic spreadsheet)* — op `update`, tab `={{ $('Compute Target Period').first().json.feeReportSheetName }}` — node "Update FeeReport Rows" (id `0f1d16b4-2d9d-4dcd-ba35-39af6a779034`)
- *(dynamic spreadsheet)* — op `update`, tab `={{ $('Compute Target Period').first().json.qualReportSheetName }}` — node "Write Tier + Rate" (id `2642cb52-f4bc-440c-928f-bc2cfcbfe053`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Compute Target Period').first().json.feeReportSheetName }}` — node "Append FeeReport Rows" (id `5e3343bf-cb0f-4a0b-acf0-2815194b40c7`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $('Compute Target Period').first().json.merchantDetailSheetName }}` — node "Get MerchantDetail Rows" (id `71a165c7-072b-4e75-8cc6-e4dbe53149b7`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $('Compute Target Period').first().json.authReportSheetName }}` — node "Get AuthDetail Rows" (id `8e9f1dd8-9e0e-4bfb-a021-d31f16c103ba`)
- *(dynamic spreadsheet)* — op `update`, tab `={{ $('Compute Target Period').first().json.merchantDetailSheetName }}` — node "Write MerchantDetail Fill" (id `92799649-0148-451d-8b75-24176927698c`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $('Compute Target Period').first().json.feeReportSheetName }}` — node "Get FeeReport Rows" (id `c4c159da-ea5b-4820-a002-b3a0809fb9cf`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $('Compute Target Period').first().json.qualReportSheetName }}` — node "Get ICQual Final" (id `dd1ed054-5abe-4cea-ab70-58fa415665c5`)
- [[../resources/google-sheets/1nuktqz7lgvs5qtevsnvm-7kpi70id-txysjxdkginug|Interchange_Categories_US_Elavon_Partner_Merchants_April_2026]] (id `1NUktqZ7LgVs5qtevSnVm_7kpI70iD_TxysJxdKgiNUg`) — op `?`, tab `Interchange Categories` — node "Intercharge Categories" (id `f925b780-448f-4b6f-8e85-e3a677af7e91`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $('Compute Target Period').item.json.qualReportSheetName }}` — node "Get row(s) in sheet" (id `fd2a7f10-671f-4333-9395-80d79f069dee`)

### Google Drive

- *(dynamic)* — op `copy` — node "Copy Spreadsheet" (id `c359f0ab-55d3-441e-b0c4-e741e6f488a7`)

## Used by (workflows)

- [[residuals-generator-v6-active-latest-2026-06-01|Residuals Generator V7 (ACTIVE) (latest 2026-07-15)]] — node "Call 'Billing - Fill in the Direct Billing Spreasheet data'" (id `e2525f50-5e2b-41dc-861d-accdf7eb4ffe`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
