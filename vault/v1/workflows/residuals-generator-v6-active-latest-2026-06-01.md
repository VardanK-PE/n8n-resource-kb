---
n8n_id: "zQrKaqapit7xko5v"
instance: v1
name: "Residuals Generator V7 (ACTIVE) (latest 2026-07-15)"
status: inactive
last_modified: 2026-07-15T18:35:53.816Z
tags:
  - "Residuals"
fingerprint: "ecd934d434dce7411b33e7f4ccacadc0a92ab188381b414c817cfea80360d936"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Residuals Generator V7 (ACTIVE) (latest 2026-07-15)

## Summary

- **Status:** inactive
- **n8n ID:** `zQrKaqapit7xko5v`
- **Nodes:** 132
- **Last modified:** 2026-07-15T18:35:53.816Z

## Triggers

- **execute-workflow** — node "Execute Workflow Trigger" (id `b68b88d4-31ae-420d-ab05-5bbfcc572768`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Move file" (id `0b2896f2-94a3-420f-8bb8-35f34b6122cd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create spreadsheet" (id `0f5c3109-a058-4ae5-a59a-fb6783f124b8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request5" (id `104c1ab3-e2cf-4ba6-a635-edea7b94e706`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsTerms" (id `10820390-8920-4d9e-a11c-5229190fc4e7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsData" (id `16080f33-c916-4530-b0e0-b94c9997fb15`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive2" (id `1c3d6725-0c33-4d32-a0bd-7c3ec3bba3e7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "MiscExpensesData" (id `1e052113-6d69-4596-afd2-e0e67e4bede9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive1" (id `1e7c32dc-3341-4236-b187-b2173177fa93`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data1" (id `2c78f685-7794-420c-a79c-3c89a7aa9e5f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive4" (id `2ea5b548-6557-4a2b-95cb-689d077e10f9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `31387a81-b97e-42b6-9415-d458f3cf42b8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AppendTotalsRow" (id `3185cbc2-8730-4b89-9c73-b7fe9e362073`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet1" (id `3333751e-b9ca-482e-9424-75bec94b7a86`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request1" (id `477f57ba-87ab-447a-b5b3-0b607baad05a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Folder ID" (id `50140207-6ea4-410b-815d-e38a007ea692`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive3" (id `5211afbe-34af-4f54-8cc3-9d0e9a293f6d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Master Spreadsheet ID" (id `55b8a283-15f3-498c-8519-4dec1a0cdac5`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get PE Account Details" (id `6362a9c5-5d99-4140-b2ce-211d1cd4d692`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `6d1afd3e-0934-4af1-9fbc-82d4678831d9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request4" (id `74953663-ee56-4ca1-b56f-491e6d4bb364`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive5" (id `75ecd26a-4d04-44cc-b086-7f4ac46e16ca`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Files List" (id `7b0a2edb-7de1-4d3e-8ca2-811c5f032089`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "SummarySheet" (id `8bfa817e-0c23-4ff5-a76d-31fed0ff55ee`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request3" (id `936f2bfa-1ae6-4c86-87f3-072ad508c173`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AutoL2Merchants" (id `a50459a7-1c8d-4781-aa3a-f675ee6f9af3`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data" (id `a5b5681e-9fa9-468a-aee3-2348abe337ae`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v1" (id `a914f52d-e2ae-447d-b29b-d74c24e283ff`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive" (id `ab500504-dc87-4eca-b669-f71873647315`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Search files and folders2" (id `b0e7b663-d181-4eb4-ab78-89da07a1a37d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request" (id `b12d2fc4-32ac-4f49-afe0-232448cd5897`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `b879269b-f44d-4de7-882a-f519021e2e2e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `bc84dd4a-d75f-4662-8720-24c3524bbc05`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request2" (id `c60128d9-d45e-4b25-b198-ad42164af506`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request6" (id `c89e8e3f-a7a7-4ee4-8013-f3d904ea9460`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data2" (id `c95fc720-4ff0-470c-b670-654a9f38488b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `cc89ee16-e213-47ac-bb75-869663b73197`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v" (id `d07d970b-cb0d-48d4-9457-8458f060c4bf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "ICQualReport" (id `db43a231-af8d-4550-ad96-3ed0b2e11f4e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get MerchantDetails Sheet Details" (id `e00b2888-4fb5-4a39-b412-f07c697ed289`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet2" (id `e2b447b9-8ace-4232-b0d5-f90172823bf2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get MASTER sheet" (id `e36a4f31-337d-43d2-bfd5-e86ecb3bdd9f`)
- [[../resources/credentials/wwm73d114letbuus|n8n-service-account Google Service Account account]] (`googleApi`, id `wwm73D114LETBUUS`) — node "Get row(s) in sheet1" (id `e3f61556-ee34-4cfb-933c-6e404d668f8d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v2" (id `e73d682e-1292-44b3-b800-73f24f90283a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create sheet" (id `ec98c094-1742-46f0-b677-c5b35d837bca`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "All ACH Transactions Report" (id `eed9c8da-3b50-4d06-a3ee-5e4b915eac3e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsTerms1" (id `fa396e7c-1fb8-4d3c-bd8e-d1f67c4e3dc9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets8" (id `fda1465f-78cd-4002-b9ee-793c05153469`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `ff973033-6813-4d3a-8d41-d505207c6e97`)

### HTTP URLs

- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1UNyfPl1I1IFSfVMVMSw5wEXMVqDxKj6CJzBZYlPVvAQ:batchUpdate` — node "HTTP Request5" (id `104c1ab3-e2cf-4ba6-a635-edea7b94e706`)
- [[../resources/http-urls/5bfe7780bed71843efae07da96917971-m-pipedream-net|5bfe7780bed71843efae07da96917971.m.pipedream.net]] — `POST https://5bfe7780bed71843efae07da96917971.m.pipedream.net` — node "HTTP Request1" (id `477f57ba-87ab-447a-b5b3-0b607baad05a`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').all()[0].json.spreadsheetId }}:batchUpdate ` — node "HTTP Request4" (id `74953663-ee56-4ca1-b56f-491e6d4bb364`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get Master Spreadsheet ID').first().json.id }}?includeGridData=false ` — node "HTTP Request3" (id `936f2bfa-1ae6-4c86-87f3-072ad508c173`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs:batchUpdate` — node "HTTP Request" (id `b12d2fc4-32ac-4f49-afe0-232448cd5897`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs?includeGridData=false` — node "HTTP Request2" (id `c60128d9-d45e-4b25-b198-ad42164af506`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').first().json.spreadsheetId }}:batchUpdate ` — node "HTTP Request6" (id `c89e8e3f-a7a7-4ee4-8013-f3d904ea9460`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get Master Spreadsheet ID').item.json.id }}?fields=sheets(properties(title,sheetId)) ` — node "Get MerchantDetails Sheet Details" (id `e00b2888-4fb5-4a39-b412-f07c697ed289`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data1" (id `2c78f685-7794-420c-a79c-3c89a7aa9e5f`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get PE Account Details" (id `6362a9c5-5d99-4140-b2ce-211d1cd4d692`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data" (id `a5b5681e-9fa9-468a-aee3-2348abe337ae`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data2" (id `c95fc720-4ff0-470c-b670-654a9f38488b`)

### Google Sheets

- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "PartnerResidualsTerms" (id `10820390-8920-4d9e-a11c-5229190fc4e7`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets5').item.json.sheets[0].properties.sheetId }}` — node "PartnerResidualsData" (id `16080f33-c916-4530-b0e0-b94c9997fb15`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.sheetId }}` — node "MiscExpensesData" (id `1e052113-6d69-4596-afd2-e0e67e4bede9`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Create sheet').first().json.sheetId }}` — node "Google Sheets4" (id `31387a81-b97e-42b6-9415-d458f3cf42b8`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets5').first().json.sheets[0].properties.sheetId }}` — node "AppendTotalsRow" (id `3185cbc2-8730-4b89-9c73-b7fe9e362073`)
- *(dynamic spreadsheet)* — op `append`, tab `Summary` — node "Append row in sheet1" (id `3333751e-b9ca-482e-9424-75bec94b7a86`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.properties.sheetId }}` — node "Get row(s) in sheet" (id `6d1afd3e-0934-4af1-9fbc-82d4678831d9`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "SummarySheet" (id `8bfa817e-0c23-4ff5-a76d-31fed0ff55ee`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `auto_l2_mids` — node "AutoL2Merchants" (id `a50459a7-1c8d-4781-aa3a-f675ee6f9af3`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "Google Sheets1" (id `cc89ee16-e213-47ac-bb75-869663b73197`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.properties.sheetId }}` — node "ICQualReport" (id `db43a231-af8d-4550-ad96-3ed0b2e11f4e`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $json.name.substring(0, 4) }}-{{ $json.name.substring(4, 6) }}-ALL-AGGREGATE` — node "Get row(s) in sheet2" (id `e2b447b9-8ace-4232-b0d5-f90172823bf2`)
- *(dynamic spreadsheet)* — op `?`, tab `MASTER` — node "Get MASTER sheet" (id `e36a4f31-337d-43d2-bfd5-e86ecb3bdd9f`)
- [[../resources/google-sheets/|]] (id ``) — op `?`, tab `` — node "Get row(s) in sheet1" (id `e3f61556-ee34-4cfb-933c-6e404d668f8d`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "Create sheet" (id `ec98c094-1742-46f0-b677-c5b35d837bca`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $('Get Master Spreadsheet ID').item.json.name.substring(0, 4) }}-{{ $('Get Master Spreadsheet ID').item.json.name.substring(4, 6) }}-ALL-AGGREGATE` — node "All ACH Transactions Report" (id `eed9c8da-3b50-4d06-a3ee-5e4b915eac3e`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "PartnerResidualsTerms1" (id `fa396e7c-1fb8-4d3c-bd8e-d1f67c4e3dc9`)
- *(dynamic spreadsheet)* — op `appendOrUpdate`, tab `={{ $('SummarySheet').item.json.sheetId }}` — node "Google Sheets8" (id `fda1465f-78cd-4002-b9ee-793c05153469`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets1').item.json.sheetId }}` — node "Append row in sheet" (id `ff973033-6813-4d3a-8d41-d505207c6e97`)

### Google Drive

- *(dynamic)* — op `move` — node "Move file" (id `0b2896f2-94a3-420f-8bb8-35f34b6122cd`)
- *(dynamic)* — op `move` — node "Move file" (id `0b2896f2-94a3-420f-8bb8-35f34b6122cd`)
- *(dynamic)* — op `move` — node "Google Drive1" (id `1e7c32dc-3341-4236-b187-b2173177fa93`)
- *(dynamic)* — op `move` — node "Google Drive1" (id `1e7c32dc-3341-4236-b187-b2173177fa93`)
- *(dynamic)* — op `move` — node "Google Drive5" (id `75ecd26a-4d04-44cc-b086-7f4ac46e16ca`)
- *(dynamic)* — op `move` — node "Google Drive5" (id `75ecd26a-4d04-44cc-b086-7f4ac46e16ca`)
- *(dynamic)* — op `download` — node "Google Drive v1" (id `a914f52d-e2ae-447d-b29b-d74c24e283ff`)
- *(dynamic)* — op `download` — node "Google Drive v2" (id `e73d682e-1292-44b3-b800-73f24f90283a`)

### Sub-workflows (Execute Workflow calls)

- [[billing-fill-in-the-direct-billing-spreasheet-data|Billing - Fill in the Direct Billing Spreasheet data]] (n8n_id `a3Y4lCqs1TkkFmSG`) — node "Call 'Billing - Fill in the Direct Billing Spreasheet data'" (id `e2525f50-5e2b-41dc-861d-accdf7eb4ffe`)

## Used by (workflows)

- [[residuals-generator-v6-webhook-wrapper|Residuals Generator V6 - Webhook Wrapper]] — node "Execute Residuals Generator" (id `execute-1`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
