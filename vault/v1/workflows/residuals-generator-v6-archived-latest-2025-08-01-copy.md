---
n8n_id: "lQXHjbNzIDRJ1Or1"
name: "Residuals Generator V6 (Archived) (latest 2025-08-01) copy"
status: inactive
last_modified: 2026-06-01T15:54:00.694Z
tags:
  - "Residuals"
fingerprint: "e6537bb3a37317166ca69a0e7c333b768ab71543d6899a38bd5b4097649365a0"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Residuals Generator V6 (Archived) (latest 2025-08-01) copy

## Summary

- **Status:** inactive
- **n8n ID:** `lQXHjbNzIDRJ1Or1`
- **Nodes:** 122
- **Last modified:** 2026-06-01T15:54:00.694Z

## Triggers

- **execute-workflow** — node "Execute Workflow Trigger" (id `ba0e72cf-1a6b-479a-8886-a8365a8dece7`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `0bf5fe98-7c7a-48b2-b258-e3407cf63ad5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get MASTER sheet" (id `1075bf97-6c36-48ff-95e8-efebb046e008`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v1" (id `11b9bd65-637c-4417-8950-d5b606090b9b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `17997a6a-689e-4b90-af53-bb977a82fe22`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `1ac87e90-5f4c-49c8-a76f-7c61bcdaf277`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Move file" (id `1bf0c18b-6167-4535-8784-ce0f0c65b8b0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AutoL2Merchants" (id `26dc3af9-2e6d-4cac-90d7-b97e06ec219a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsData" (id `2ab566e0-5c58-4b5e-98e6-33a063caf322`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request4" (id `2cdf8776-46b6-45a7-9400-16709115f94f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "SummarySheet" (id `352fafd8-d13d-44ef-a6eb-9396a2642c40`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request" (id `43ad9e0c-6de4-4cb8-9fb1-0b6e140fd48a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Folder ID" (id `4c645b6f-30d5-4878-a11c-534f5f74fdd3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "All ACH Transactions Report" (id `4ca5b36a-5744-427a-9e97-4b89ad6f91ce`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request1" (id `4d723836-4cc7-4b78-84c4-2c454ed9e41d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request5" (id `4ff88b49-8acf-4b35-a825-b49713d975aa`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request6" (id `50e3c6a1-6eda-4935-93ad-bcae9bfac625`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `52e03dcb-112c-4012-986d-cc858428ce3d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive" (id `57325408-a66c-4c2a-9566-136778a55e8b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `584db8a1-b6b2-4084-a95d-d396cc8e45e5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v2" (id `5ce809ce-b173-4574-ae4e-03999f2f48f6`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data" (id `617dcfdf-f8ad-4401-b751-9bcbf5c218d6`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get PE Account Details" (id `80e3adff-2528-4f84-ad13-26dd0e1dbeec`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "ICQualReport" (id `875ebedd-e0b2-45d3-987c-51200838b456`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Files List" (id `8969d47d-0c2c-4d7e-a8f7-5c6af71b2fbf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive5" (id `8ae184cf-8a10-4710-88c4-3e92e7cd3133`)
- [[../resources/credentials/wwm73d114letbuus|n8n-service-account Google Service Account account]] (`googleApi`, id `wwm73D114LETBUUS`) — node "Get row(s) in sheet1" (id `8e615b68-d2f4-4fa1-a900-3569be7d30f1`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data2" (id `9079cc8e-84e6-4afa-bfa5-ea231e10e62e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Search files and folders2" (id `98c7f6b9-c580-4c45-9008-70db4b0e71f9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create sheet" (id `99d9b30a-28ae-409b-9f2e-39cf76444bb1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive1" (id `aa4e3bc5-6508-4e2d-9a20-c2a935387c80`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "MiscExpensesData" (id `abc85afa-a2b9-46cf-bcfc-4a2722326a3e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Master Spreadsheet ID" (id `aef28497-ca75-48a2-b8f2-77cf86656ba0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive3" (id `af97a6e3-9cfe-45fa-89eb-afdf2ed397d5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet1" (id `afc896c6-d0c9-4764-9bf2-e71a3e36b47e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet2" (id `ba25b3e1-3450-4ef2-8667-8bac2b5dbb5d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AppendTotalsRow" (id `bf0df3f2-7947-4fd2-a22c-41e50b37f1c3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsTerms" (id `c424da37-6224-447b-8d79-85182ae05c82`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsTerms1" (id `c47d3dcc-9a49-40e1-baf5-d092af6907c2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get MerchantDetails Sheet Details" (id `c791b943-7586-4b90-8c0c-67cfb14dde55`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive2" (id `d15195c2-f3d9-4c3c-937a-a434fee2185a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request3" (id `dc6e845e-e1a9-40c6-9a81-a3342400efba`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v" (id `dd65d722-3489-4d99-bf1b-459570aa5425`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `e1b03fee-baa5-49e0-8378-bd41e11029b4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets8" (id `e326443c-8a2c-4068-8a91-e1dd54bf6ad6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive4" (id `e5bb52bd-fbb2-40c2-9a43-38b2a3b4b2c8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create spreadsheet" (id `ea29f321-1030-4e4b-a3b3-1e3739112649`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request2" (id `eb56f5c9-6202-4b59-8380-8ddd336c514b`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data1" (id `f1dd852c-391b-428e-9b5e-46e041a1fb14`)

### HTTP URLs

- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').all()[0].json.spreadsheetId }}:batchUpdate ` — node "HTTP Request4" (id `2cdf8776-46b6-45a7-9400-16709115f94f`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs:batchUpdate` — node "HTTP Request" (id `43ad9e0c-6de4-4cb8-9fb1-0b6e140fd48a`)
- [[../resources/http-urls/5bfe7780bed71843efae07da96917971-m-pipedream-net|5bfe7780bed71843efae07da96917971.m.pipedream.net]] — `POST https://5bfe7780bed71843efae07da96917971.m.pipedream.net` — node "HTTP Request1" (id `4d723836-4cc7-4b78-84c4-2c454ed9e41d`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1UNyfPl1I1IFSfVMVMSw5wEXMVqDxKj6CJzBZYlPVvAQ:batchUpdate` — node "HTTP Request5" (id `4ff88b49-8acf-4b35-a825-b49713d975aa`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').first().json.spreadsheetId }}:batchUpdate ` — node "HTTP Request6" (id `50e3c6a1-6eda-4935-93ad-bcae9bfac625`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get Master Spreadsheet ID').item.json.id }}?fields=sheets(properties(title,sheetId)) ` — node "Get MerchantDetails Sheet Details" (id `c791b943-7586-4b90-8c0c-67cfb14dde55`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get Master Spreadsheet ID').first().json.id }}?includeGridData=false ` — node "HTTP Request3" (id `dc6e845e-e1a9-40c6-9a81-a3342400efba`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs?includeGridData=false` — node "HTTP Request2" (id `eb56f5c9-6202-4b59-8380-8ddd336c514b`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data" (id `617dcfdf-f8ad-4401-b751-9bcbf5c218d6`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get PE Account Details" (id `80e3adff-2528-4f84-ad13-26dd0e1dbeec`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data2" (id `9079cc8e-84e6-4afa-bfa5-ea231e10e62e`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data1" (id `f1dd852c-391b-428e-9b5e-46e041a1fb14`)

### Google Sheets

- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets1').item.json.sheetId }}` — node "Append row in sheet" (id `0bf5fe98-7c7a-48b2-b258-e3407cf63ad5`)
- *(dynamic spreadsheet)* — op `?`, tab `MASTER` — node "Get MASTER sheet" (id `1075bf97-6c36-48ff-95e8-efebb046e008`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `auto_l2_mids` — node "AutoL2Merchants" (id `26dc3af9-2e6d-4cac-90d7-b97e06ec219a`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets5').item.json.sheets[0].properties.sheetId }}` — node "PartnerResidualsData" (id `2ab566e0-5c58-4b5e-98e6-33a063caf322`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "SummarySheet" (id `352fafd8-d13d-44ef-a6eb-9396a2642c40`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $('Get Master Spreadsheet ID').item.json.name.substring(0, 4) }}-{{ $('Get Master Spreadsheet ID').item.json.name.substring(4, 6) }}-ALL-AGGREGATE` — node "All ACH Transactions Report" (id `4ca5b36a-5744-427a-9e97-4b89ad6f91ce`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.properties.sheetId }}` — node "Get row(s) in sheet" (id `52e03dcb-112c-4012-986d-cc858428ce3d`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "Google Sheets1" (id `584db8a1-b6b2-4084-a95d-d396cc8e45e5`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.properties.sheetId }}` — node "ICQualReport" (id `875ebedd-e0b2-45d3-987c-51200838b456`)
- [[../resources/google-sheets/|]] (id ``) — op `?`, tab `` — node "Get row(s) in sheet1" (id `8e615b68-d2f4-4fa1-a900-3569be7d30f1`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "Create sheet" (id `99d9b30a-28ae-409b-9f2e-39cf76444bb1`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.sheetId }}` — node "MiscExpensesData" (id `abc85afa-a2b9-46cf-bcfc-4a2722326a3e`)
- *(dynamic spreadsheet)* — op `append`, tab `Summary` — node "Append row in sheet1" (id `afc896c6-d0c9-4764-9bf2-e71a3e36b47e`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $json.name.substring(0, 4) }}-{{ $json.name.substring(4, 6) }}-ALL-AGGREGATE` — node "Get row(s) in sheet2" (id `ba25b3e1-3450-4ef2-8667-8bac2b5dbb5d`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets5').first().json.sheets[0].properties.sheetId }}` — node "AppendTotalsRow" (id `bf0df3f2-7947-4fd2-a22c-41e50b37f1c3`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "PartnerResidualsTerms" (id `c424da37-6224-447b-8d79-85182ae05c82`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "PartnerResidualsTerms1" (id `c47d3dcc-9a49-40e1-baf5-d092af6907c2`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Create sheet').first().json.sheetId }}` — node "Google Sheets4" (id `e1b03fee-baa5-49e0-8378-bd41e11029b4`)
- *(dynamic spreadsheet)* — op `appendOrUpdate`, tab `={{ $('SummarySheet').item.json.sheetId }}` — node "Google Sheets8" (id `e326443c-8a2c-4068-8a91-e1dd54bf6ad6`)

### Google Drive

- *(dynamic)* — op `download` — node "Google Drive v1" (id `11b9bd65-637c-4417-8950-d5b606090b9b`)
- *(dynamic)* — op `move` — node "Move file" (id `1bf0c18b-6167-4535-8784-ce0f0c65b8b0`)
- *(dynamic)* — op `move` — node "Move file" (id `1bf0c18b-6167-4535-8784-ce0f0c65b8b0`)
- *(dynamic)* — op `download` — node "Google Drive v2" (id `5ce809ce-b173-4574-ae4e-03999f2f48f6`)
- *(dynamic)* — op `move` — node "Google Drive5" (id `8ae184cf-8a10-4710-88c4-3e92e7cd3133`)
- *(dynamic)* — op `move` — node "Google Drive5" (id `8ae184cf-8a10-4710-88c4-3e92e7cd3133`)
- *(dynamic)* — op `move` — node "Google Drive1" (id `aa4e3bc5-6508-4e2d-9a20-c2a935387c80`)
- *(dynamic)* — op `move` — node "Google Drive1" (id `aa4e3bc5-6508-4e2d-9a20-c2a935387c80`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
