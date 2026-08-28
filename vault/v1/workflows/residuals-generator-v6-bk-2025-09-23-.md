---
n8n_id: "d7Squ8HrMcIQ0ueg"
name: "Residuals Generator V6 (bk 2025-09-23)"
status: inactive
last_modified: 2025-09-23T23:01:59.935Z
tags:
  - "backups"
fingerprint: "29cde332e9bb7286d3079047c18006b73c681a5663ea3c321b5ab22ff7e360ff"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Residuals Generator V6 (bk 2025-09-23)

## Summary

- **Status:** inactive
- **n8n ID:** `d7Squ8HrMcIQ0ueg`
- **Nodes:** 112
- **Last modified:** 2025-09-23T23:01:59.935Z

## Triggers

- **execute-workflow** — node "Execute Workflow Trigger" (id `66dac158-1413-4e9e-9d7c-c0ebe248a393`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Files List" (id `0fcaeef4-5e5c-472a-b243-48d7680d85ec`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create spreadsheet" (id `22b21d89-5538-4fd2-96e2-4c48048d91a2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create sheet" (id `2503d323-f2cd-43fc-9e95-c4af5b752df9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Search files and folders2" (id `33dea836-011e-488c-ad56-28d3c942c302`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request" (id `3740c39b-df82-4837-bf97-d1e39fe82c96`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Master Spreadsheet ID" (id `405412e7-9ee8-4c4c-9c89-6fb84784bd85`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "SummarySheet" (id `4181e657-a4ac-4de5-a648-1b5ba36ba3bf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `463802d3-c67c-4d18-98e9-879d0ff537b4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive4" (id `4663c85c-4945-4584-8461-58f9dd3756b2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AppendTotalsRow" (id `4817d151-0b1f-406a-8fd0-4b9ab4d4ff08`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `4de86632-5d55-48a3-a44e-fd76327abd43`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get MerchantDetails Sheet Details" (id `540cc098-21fc-4412-a6e1-8c06f8c08fbc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `5a7eb24b-379f-4a23-9a76-3af89e71c0fd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive" (id `5d919a81-ba58-4282-a653-5d60c2246eb3`)
- [[../resources/credentials/wwm73d114letbuus|n8n-service-account Google Service Account account]] (`googleApi`, id `wwm73D114LETBUUS`) — node "Get row(s) in sheet1" (id `5f367584-62e4-4649-8199-7c65f933116c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request2" (id `68d0905e-0325-4056-9a30-5974c8c40d10`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v2" (id `6a8f7b0a-0131-4fe8-bd5c-fccc423bb82e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive1" (id `6e8996f7-62b5-4fca-8f3b-da28df21f1e2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsTerms" (id `6ea0dd09-4052-43d5-ac54-973640f9c510`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request1" (id `70bcdb7e-d5e5-4026-9316-edae22d5a2d6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get MASTER sheet" (id `73f3a15b-d976-4b4d-9575-f4dfa867d01b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "All ACH Transactions Report" (id `7e832088-8741-4a44-b8ec-282b6ab366ac`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet1" (id `83554e4e-9547-4dc4-af93-8076f929190f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request4" (id `86b03020-3f81-45d3-b760-07463f94c229`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data2" (id `891c803d-5236-4fac-a5d4-e9a25cb22575`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Folder ID" (id `8bd45eb8-569c-4ae3-b278-1017cf5fcc40`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsTerms1" (id `8d558e74-bc6a-4f43-b3f7-d2bb95d678db`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Move file" (id `93b81c9a-3a87-4857-a483-3aba32bc64d9`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data" (id `acd43692-3062-45cc-8b64-f94bd6e81006`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data1" (id `b4fc275c-edcd-46ec-9704-85222fbb00b9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `b565bf60-8740-46df-8a11-9ee2c5b9836a`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get PE Account Details" (id `bc5be881-171c-4667-8b1a-d8bd33796cee`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive5" (id `be87b780-8079-497f-85e7-90b17f829b80`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsData" (id `c51601d5-3052-40ff-9040-35867671a11f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets8" (id `c79b8a58-91e0-4988-a57b-d57938f22a2b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive3" (id `ccf8bd92-0153-4506-9fea-ae7326ff883c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive2" (id `cece2ebe-d732-4f40-a847-0b3c2de5ec4d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AutoL2Merchants" (id `cfc38fc2-cf47-4ae0-8faf-0f708eef4594`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request6" (id `d0ca792c-fab9-49c6-97fd-865cf68caf3b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "ICQualReport" (id `d6eb9aa0-acae-4455-924f-54e64008b63a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `d97267b4-a42a-422b-a5fe-61ff2e7022e2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request3" (id `e4f36208-549f-44af-a223-4d8bc95772db`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v1" (id `e7f5318c-2b9b-456a-a45a-53731af8868d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet2" (id `ec6c77ff-8e64-4e66-9103-ff6058872b41`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request5" (id `ece3214f-b553-433f-8e64-51fae91427b1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "MiscExpensesData" (id `eeb87cc2-5280-44da-9d31-c1e9184a73a2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `f75ddf27-6ddd-4d6c-b343-73089a207a15`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v" (id `fff2c26a-5897-439e-9097-d4f752a67cc4`)

### HTTP URLs

- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs:batchUpdate` — node "HTTP Request" (id `3740c39b-df82-4837-bf97-d1e39fe82c96`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get Master Spreadsheet ID').item.json.id }}?fields=sheets(properties(title,sheetId)) ` — node "Get MerchantDetails Sheet Details" (id `540cc098-21fc-4412-a6e1-8c06f8c08fbc`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs?includeGridData=false` — node "HTTP Request2" (id `68d0905e-0325-4056-9a30-5974c8c40d10`)
- [[../resources/http-urls/5bfe7780bed71843efae07da96917971-m-pipedream-net|5bfe7780bed71843efae07da96917971.m.pipedream.net]] — `POST https://5bfe7780bed71843efae07da96917971.m.pipedream.net` — node "HTTP Request1" (id `70bcdb7e-d5e5-4026-9316-edae22d5a2d6`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').all()[0].json.spreadsheetId }}:batchUpdate ` — node "HTTP Request4" (id `86b03020-3f81-45d3-b760-07463f94c229`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').first().json.spreadsheetId }}:batchUpdate ` — node "HTTP Request6" (id `d0ca792c-fab9-49c6-97fd-865cf68caf3b`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get Master Spreadsheet ID').first().json.id }}?includeGridData=false ` — node "HTTP Request3" (id `e4f36208-549f-44af-a223-4d8bc95772db`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1UNyfPl1I1IFSfVMVMSw5wEXMVqDxKj6CJzBZYlPVvAQ:batchUpdate` — node "HTTP Request5" (id `ece3214f-b553-433f-8e64-51fae91427b1`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data2" (id `891c803d-5236-4fac-a5d4-e9a25cb22575`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data" (id `acd43692-3062-45cc-8b64-f94bd6e81006`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data1" (id `b4fc275c-edcd-46ec-9704-85222fbb00b9`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get PE Account Details" (id `bc5be881-171c-4667-8b1a-d8bd33796cee`)

### Google Sheets

- *(dynamic spreadsheet)* — op `create`, tab `null` — node "Create sheet" (id `2503d323-f2cd-43fc-9e95-c4af5b752df9`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "SummarySheet" (id `4181e657-a4ac-4de5-a648-1b5ba36ba3bf`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets1').item.json.sheetId }}` — node "Append row in sheet" (id `463802d3-c67c-4d18-98e9-879d0ff537b4`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets5').first().json.sheets[0].properties.sheetId }}` — node "AppendTotalsRow" (id `4817d151-0b1f-406a-8fd0-4b9ab4d4ff08`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.properties.sheetId }}` — node "Get row(s) in sheet" (id `4de86632-5d55-48a3-a44e-fd76327abd43`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "Google Sheets1" (id `5a7eb24b-379f-4a23-9a76-3af89e71c0fd`)
- [[../resources/google-sheets/|]] (id ``) — op `?`, tab `` — node "Get row(s) in sheet1" (id `5f367584-62e4-4649-8199-7c65f933116c`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "PartnerResidualsTerms" (id `6ea0dd09-4052-43d5-ac54-973640f9c510`)
- *(dynamic spreadsheet)* — op `?`, tab `MASTER` — node "Get MASTER sheet" (id `73f3a15b-d976-4b4d-9575-f4dfa867d01b`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $('Get Master Spreadsheet ID').item.json.name.substring(0, 4) }}-{{ $('Get Master Spreadsheet ID').item.json.name.substring(4, 6) }}-ALL-AGGREGATE` — node "All ACH Transactions Report" (id `7e832088-8741-4a44-b8ec-282b6ab366ac`)
- *(dynamic spreadsheet)* — op `append`, tab `Summary` — node "Append row in sheet1" (id `83554e4e-9547-4dc4-af93-8076f929190f`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "PartnerResidualsTerms1" (id `8d558e74-bc6a-4f43-b3f7-d2bb95d678db`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets5').item.json.sheets[0].properties.sheetId }}` — node "PartnerResidualsData" (id `c51601d5-3052-40ff-9040-35867671a11f`)
- *(dynamic spreadsheet)* — op `appendOrUpdate`, tab `={{ $('SummarySheet').item.json.sheetId }}` — node "Google Sheets8" (id `c79b8a58-91e0-4988-a57b-d57938f22a2b`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `auto_l2_mids` — node "AutoL2Merchants" (id `cfc38fc2-cf47-4ae0-8faf-0f708eef4594`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.properties.sheetId }}` — node "ICQualReport" (id `d6eb9aa0-acae-4455-924f-54e64008b63a`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Create sheet').first().json.sheetId }}` — node "Google Sheets4" (id `d97267b4-a42a-422b-a5fe-61ff2e7022e2`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $json.name.substring(0, 4) }}-{{ $json.name.substring(4, 6) }}-ALL-AGGREGATE` — node "Get row(s) in sheet2" (id `ec6c77ff-8e64-4e66-9103-ff6058872b41`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.sheetId }}` — node "MiscExpensesData" (id `eeb87cc2-5280-44da-9d31-c1e9184a73a2`)

### Google Drive

- *(dynamic)* — op `download` — node "Google Drive v2" (id `6a8f7b0a-0131-4fe8-bd5c-fccc423bb82e`)
- *(dynamic)* — op `move` — node "Google Drive1" (id `6e8996f7-62b5-4fca-8f3b-da28df21f1e2`)
- *(dynamic)* — op `move` — node "Google Drive1" (id `6e8996f7-62b5-4fca-8f3b-da28df21f1e2`)
- *(dynamic)* — op `move` — node "Move file" (id `93b81c9a-3a87-4857-a483-3aba32bc64d9`)
- *(dynamic)* — op `move` — node "Move file" (id `93b81c9a-3a87-4857-a483-3aba32bc64d9`)
- *(dynamic)* — op `move` — node "Google Drive5" (id `be87b780-8079-497f-85e7-90b17f829b80`)
- *(dynamic)* — op `move` — node "Google Drive5" (id `be87b780-8079-497f-85e7-90b17f829b80`)
- *(dynamic)* — op `download` — node "Google Drive v1" (id `e7f5318c-2b9b-456a-a45a-53731af8868d`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
