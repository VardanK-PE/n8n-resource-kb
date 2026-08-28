---
n8n_id: "NSSjohLXsIkmjKue"
name: "Residuals Generator V6 (Backup) (latest 2026-06-01)"
status: inactive
last_modified: 2026-07-15T18:32:44.241Z
tags:
  - "Residuals"
fingerprint: "d6c871e7faf8c595ae792926bff6c6745b0c683b7127c7d795fbf9987d318045"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Residuals Generator V6 (Backup) (latest 2026-06-01)

## Summary

- **Status:** inactive
- **n8n ID:** `NSSjohLXsIkmjKue`
- **Nodes:** 129
- **Last modified:** 2026-07-15T18:32:44.241Z

## Triggers

- **execute-workflow** — node "Execute Workflow Trigger" (id `3b01e45c-e1d4-4cab-9775-6c1063500ce8`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create sheet" (id `028c9261-4785-432d-bc4f-25145ab4d14e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "ICQualReport" (id `11266030-f2a1-4455-b8b4-14cde76c018a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Move file" (id `11f6d143-dbf6-4012-825c-4a1f6ea2d202`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get MerchantDetails Sheet Details" (id `1744ac65-303c-4b01-9f07-8bc5651243b0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request2" (id `18250842-cc21-4482-aaf6-6a8818277853`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsTerms1" (id `20f9379b-7d5b-4260-87a4-cd587c84115c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v" (id `229e8f8d-a7ff-4f3b-954f-423308cba1ba`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request5" (id `2b99bb50-b738-471d-8e0f-f8f40f51aad6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive2" (id `2f5f19af-f060-46c3-b6fa-cce8844cff91`)
- [[../resources/credentials/wwm73d114letbuus|n8n-service-account Google Service Account account]] (`googleApi`, id `wwm73D114LETBUUS`) — node "Get row(s) in sheet1" (id `44e5ade7-470d-4d39-8c3f-f2ebc3983892`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v1" (id `4720e739-eb2b-4bc4-8dee-b657fafa77d8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "All ACH Transactions Report" (id `47288eff-c1ac-4f52-9024-d84583d1fb1b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive5" (id `4928e9e7-2553-4307-a4d9-b45aff49dfc6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet1" (id `5bb3cd05-fafd-4f22-9c0e-f0eb8e2d9370`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets8" (id `62074dfc-a080-4dde-aaec-e8241fb75516`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive" (id `6236ff6b-75f5-4ba7-8619-945c78d1453d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `705a7965-b426-4c21-a891-c9a089ac3073`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data" (id `799adc8c-b656-4400-a231-517db55e42dd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "MiscExpensesData" (id `7ab098a9-2ec9-47bd-9017-a5629ea3c1ff`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsData" (id `86b92f04-0527-46c8-b3a5-009e38aafa82`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create spreadsheet" (id `8b6dd0c8-a7ca-471b-a810-5b7adaca1ce8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Files List" (id `8bbc7737-8984-46a5-b22d-d033978ffa05`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v2" (id `92c53b83-9aea-4a6c-927d-df833a197490`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get PE Account Details" (id `9b0432b0-8b31-4337-aa87-d356abd33247`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request1" (id `a98b598a-99b1-46c3-858c-18233ec1960d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `a9c8f5a5-c8a4-4b74-aac1-b303818314d7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request6" (id `ad7f525a-04d4-4b20-b6b3-b1c672214e33`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `b8197e3a-bd8f-420c-b987-b70724d653eb`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data2" (id `bd4345d4-7269-4668-8c3c-cab866ef1774`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AppendTotalsRow" (id `c71d3699-4fb8-425a-a30f-d51733035d5d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive1" (id `ca024349-01d1-4138-a75b-a8c21ba98df2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Master Spreadsheet ID" (id `d36e88d9-c198-4b08-bc09-9b1546b656a0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsTerms" (id `d5569c42-a906-4d13-b62f-266f4a0d2e0b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive4" (id `d9e6cf69-ee68-46e6-9d7c-9c7c97b75324`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data1" (id `dac88872-eab9-424e-82b4-f79ffee4dd27`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `e121a559-bbc8-4d86-989d-82da29ba2d8d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Search files and folders2" (id `e2603ac7-df1a-4655-844e-f4bd87a35ec9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get MASTER sheet" (id `e2eb154a-779d-4c54-9e2a-eb675a126e21`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "SummarySheet" (id `e2f3b959-3914-4695-a3d6-9129eed0cbbe`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request3" (id `e6344ce0-8f4f-4ad3-88a3-78a584089fb7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Folder ID" (id `ec7dc919-24a4-4b85-bbe0-979568a3ee0c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `ed84d48c-4848-4ae4-9b53-9ce2f10c18d0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request" (id `ef0f4211-4b2a-400f-be67-425808abc35b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `f2e620b2-f2af-45ee-9444-bc02e13b6921`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet2" (id `f9046026-e8a5-4b2a-bf60-82c0dd9f671a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AutoL2Merchants" (id `fa099990-5e4e-491a-9a96-d01839311c32`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request4" (id `fe6bde24-9fc9-4057-a8f0-29501066f32d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive3" (id `ff30c12a-c80e-47cf-a1c1-c54e48294005`)

### HTTP URLs

- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get Master Spreadsheet ID').item.json.id }}?fields=sheets(properties(title,sheetId)) ` — node "Get MerchantDetails Sheet Details" (id `1744ac65-303c-4b01-9f07-8bc5651243b0`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs?includeGridData=false` — node "HTTP Request2" (id `18250842-cc21-4482-aaf6-6a8818277853`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1UNyfPl1I1IFSfVMVMSw5wEXMVqDxKj6CJzBZYlPVvAQ:batchUpdate` — node "HTTP Request5" (id `2b99bb50-b738-471d-8e0f-f8f40f51aad6`)
- [[../resources/http-urls/5bfe7780bed71843efae07da96917971-m-pipedream-net|5bfe7780bed71843efae07da96917971.m.pipedream.net]] — `POST https://5bfe7780bed71843efae07da96917971.m.pipedream.net` — node "HTTP Request1" (id `a98b598a-99b1-46c3-858c-18233ec1960d`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').first().json.spreadsheetId }}:batchUpdate ` — node "HTTP Request6" (id `ad7f525a-04d4-4b20-b6b3-b1c672214e33`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get Master Spreadsheet ID').first().json.id }}?includeGridData=false ` — node "HTTP Request3" (id `e6344ce0-8f4f-4ad3-88a3-78a584089fb7`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs:batchUpdate` — node "HTTP Request" (id `ef0f4211-4b2a-400f-be67-425808abc35b`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').all()[0].json.spreadsheetId }}:batchUpdate ` — node "HTTP Request4" (id `fe6bde24-9fc9-4057-a8f0-29501066f32d`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data" (id `799adc8c-b656-4400-a231-517db55e42dd`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get PE Account Details" (id `9b0432b0-8b31-4337-aa87-d356abd33247`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data2" (id `bd4345d4-7269-4668-8c3c-cab866ef1774`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data1" (id `dac88872-eab9-424e-82b4-f79ffee4dd27`)

### Google Sheets

- *(dynamic spreadsheet)* — op `create`, tab `null` — node "Create sheet" (id `028c9261-4785-432d-bc4f-25145ab4d14e`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.properties.sheetId }}` — node "ICQualReport" (id `11266030-f2a1-4455-b8b4-14cde76c018a`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "PartnerResidualsTerms1" (id `20f9379b-7d5b-4260-87a4-cd587c84115c`)
- [[../resources/google-sheets/|]] (id ``) — op `?`, tab `` — node "Get row(s) in sheet1" (id `44e5ade7-470d-4d39-8c3f-f2ebc3983892`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $('Get Master Spreadsheet ID').item.json.name.substring(0, 4) }}-{{ $('Get Master Spreadsheet ID').item.json.name.substring(4, 6) }}-ALL-AGGREGATE` — node "All ACH Transactions Report" (id `47288eff-c1ac-4f52-9024-d84583d1fb1b`)
- *(dynamic spreadsheet)* — op `append`, tab `Summary` — node "Append row in sheet1" (id `5bb3cd05-fafd-4f22-9c0e-f0eb8e2d9370`)
- *(dynamic spreadsheet)* — op `appendOrUpdate`, tab `={{ $('SummarySheet').item.json.sheetId }}` — node "Google Sheets8" (id `62074dfc-a080-4dde-aaec-e8241fb75516`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.sheetId }}` — node "MiscExpensesData" (id `7ab098a9-2ec9-47bd-9017-a5629ea3c1ff`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets5').item.json.sheets[0].properties.sheetId }}` — node "PartnerResidualsData" (id `86b92f04-0527-46c8-b3a5-009e38aafa82`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Create sheet').first().json.sheetId }}` — node "Google Sheets4" (id `a9c8f5a5-c8a4-4b74-aac1-b303818314d7`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.properties.sheetId }}` — node "Get row(s) in sheet" (id `b8197e3a-bd8f-420c-b987-b70724d653eb`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets5').first().json.sheets[0].properties.sheetId }}` — node "AppendTotalsRow" (id `c71d3699-4fb8-425a-a30f-d51733035d5d`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "PartnerResidualsTerms" (id `d5569c42-a906-4d13-b62f-266f4a0d2e0b`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "Google Sheets1" (id `e121a559-bbc8-4d86-989d-82da29ba2d8d`)
- *(dynamic spreadsheet)* — op `?`, tab `MASTER` — node "Get MASTER sheet" (id `e2eb154a-779d-4c54-9e2a-eb675a126e21`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "SummarySheet" (id `e2f3b959-3914-4695-a3d6-9129eed0cbbe`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets1').item.json.sheetId }}` — node "Append row in sheet" (id `ed84d48c-4848-4ae4-9b53-9ce2f10c18d0`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $json.name.substring(0, 4) }}-{{ $json.name.substring(4, 6) }}-ALL-AGGREGATE` — node "Get row(s) in sheet2" (id `f9046026-e8a5-4b2a-bf60-82c0dd9f671a`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `auto_l2_mids` — node "AutoL2Merchants" (id `fa099990-5e4e-491a-9a96-d01839311c32`)

### Google Drive

- *(dynamic)* — op `move` — node "Move file" (id `11f6d143-dbf6-4012-825c-4a1f6ea2d202`)
- *(dynamic)* — op `move` — node "Move file" (id `11f6d143-dbf6-4012-825c-4a1f6ea2d202`)
- *(dynamic)* — op `download` — node "Google Drive v1" (id `4720e739-eb2b-4bc4-8dee-b657fafa77d8`)
- *(dynamic)* — op `move` — node "Google Drive5" (id `4928e9e7-2553-4307-a4d9-b45aff49dfc6`)
- *(dynamic)* — op `move` — node "Google Drive5" (id `4928e9e7-2553-4307-a4d9-b45aff49dfc6`)
- *(dynamic)* — op `download` — node "Google Drive v2" (id `92c53b83-9aea-4a6c-927d-df833a197490`)
- *(dynamic)* — op `move` — node "Google Drive1" (id `ca024349-01d1-4138-a75b-a8c21ba98df2`)
- *(dynamic)* — op `move` — node "Google Drive1" (id `ca024349-01d1-4138-a75b-a8c21ba98df2`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
