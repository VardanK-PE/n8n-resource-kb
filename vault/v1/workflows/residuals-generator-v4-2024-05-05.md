---
n8n_id: "WPHQG7lFBozRrk9C"
instance: v1
name: "Residuals Generator V4 (2024-05-05)"
status: inactive
last_modified: 2024-10-17T18:13:59.744Z
tags:
  - "Residuals"
fingerprint: "ec92ccb313e6c0352c5490d1af3a6febc203bd99db1bd86a317db06ec0493aca"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Residuals Generator V4 (2024-05-05)

## Summary

- **Status:** inactive
- **n8n ID:** `WPHQG7lFBozRrk9C`
- **Nodes:** 70
- **Last modified:** 2024-10-17T18:13:59.744Z

## Triggers

- **execute-workflow** — node "Execute Workflow Trigger" (id `4355b98f-a151-4656-83f8-6ed6f95c36e6`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `0396b7a4-0dc6-475f-97cb-7e2006d08dc7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "MiscExpensesData" (id `16aaccd9-7e3c-43a1-87ba-8f17eb498ff1`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `1a27e783-9adc-4380-a350-1d796c495c5b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `28663fab-ec24-4db8-a222-638755303085`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsTerms" (id `296b677c-9980-40b8-a6a3-68e554745af9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request2" (id `2bb47846-d83d-4d28-8baf-62f255c04874`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive2" (id `2e184b94-ae97-48e2-aa29-8cf57284a4e3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v2" (id `38d09755-acfd-4881-b8c3-b6e109c33035`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request1" (id `3befcd04-b646-4474-9723-399e85841049`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive3" (id `3d4cae4f-f272-46f0-9656-e8a3d3566f4e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `3f851e16-4fa0-4ae7-9123-58951484d1ec`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request5" (id `4070c02f-760c-449c-9d2f-1b03f571924c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AppendTotalsRow" (id `50a582f6-42f1-4ca7-ac1b-775ad6c0c427`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `5dc958ec-1005-4ad5-b714-be59d1f40531`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request3" (id `6a227ebe-e416-4b33-8e06-3d21dae1bfe6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive" (id `6f1a598d-6cd1-441c-a06e-e295f9ac3995`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsData" (id `82aae0c7-1909-47b5-b137-4aaedb196282`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `888a3c42-0ff2-4dcd-93e8-65df99a7a2e6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `8a268791-1d7c-4e07-b3cb-bea6483d9e2d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request6" (id `8b72ebba-959a-4c1a-91a0-e6a8e73b5136`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request" (id `8da39847-be96-4e85-b8af-6d944a98cebb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request4" (id `90326b4a-1459-4d0f-bda1-9cfd215a5431`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v" (id `a8e53269-a568-4410-87f8-4975c9002a56`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive1" (id `acb3d96e-29c2-4900-ac3b-1b434788f014`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v1" (id `ceef6ba7-cc99-4041-99ce-7aa29dd1727f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "ICQualReport" (id `dcd71c39-6f0d-4ce5-89dc-24f8f3178773`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets7" (id `e5fcadeb-ddc8-4c58-89ac-cdd33b6e7d2e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive5" (id `ee4185a5-1096-49c1-a904-ee34fee3c1d3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive4" (id `f87edd66-3511-4496-8671-83a38c5bb0d6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Files List" (id `fbcb4e38-53cf-4de7-af69-e3966967de1c`)

### HTTP URLs

- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs?includeGridData=false` — node "HTTP Request2" (id `2bb47846-d83d-4d28-8baf-62f255c04874`)
- [[../resources/http-urls/5bfe7780bed71843efae07da96917971-m-pipedream-net|5bfe7780bed71843efae07da96917971.m.pipedream.net]] — `POST https://5bfe7780bed71843efae07da96917971.m.pipedream.net` — node "HTTP Request1" (id `3befcd04-b646-4474-9723-399e85841049`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1UNyfPl1I1IFSfVMVMSw5wEXMVqDxKj6CJzBZYlPVvAQ:batchUpdate` — node "HTTP Request5" (id `4070c02f-760c-449c-9d2f-1b03f571924c`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get MerchantDetailReport.dat').all()[0].json.spreadsheetId }}?includeGridData=false ` — node "HTTP Request3" (id `6a227ebe-e416-4b33-8e06-3d21dae1bfe6`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').first().json.spreadsheetId }}:batchUpdate ` — node "HTTP Request6" (id `8b72ebba-959a-4c1a-91a0-e6a8e73b5136`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs:batchUpdate` — node "HTTP Request" (id `8da39847-be96-4e85-b8af-6d944a98cebb`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').all()[0].json.spreadsheetId }}:batchUpdate ` — node "HTTP Request4" (id `90326b4a-1459-4d0f-bda1-9cfd215a5431`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `1a27e783-9adc-4380-a350-1d796c495c5b`)

### Google Sheets

- *(dynamic spreadsheet)* — op `create`, tab `null` — node "Google Sheets3" (id `0396b7a4-0dc6-475f-97cb-7e2006d08dc7`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.sheetId }}` — node "MiscExpensesData" (id `16aaccd9-7e3c-43a1-87ba-8f17eb498ff1`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "PartnerResidualsTerms" (id `296b677c-9980-40b8-a6a3-68e554745af9`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "Google Sheets1" (id `3f851e16-4fa0-4ae7-9123-58951484d1ec`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets5').first().json.sheets[0].properties.sheetId }}` — node "AppendTotalsRow" (id `50a582f6-42f1-4ca7-ac1b-775ad6c0c427`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets1').item.json.sheetId }}` — node "Google Sheets2" (id `5dc958ec-1005-4ad5-b714-be59d1f40531`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets5').item.json.sheets[0].properties.sheetId }}` — node "PartnerResidualsData" (id `82aae0c7-1909-47b5-b137-4aaedb196282`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets3').first().json.sheetId }}` — node "Google Sheets4" (id `8a268791-1d7c-4e07-b3cb-bea6483d9e2d`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.sheetId }}` — node "ICQualReport" (id `dcd71c39-6f0d-4ce5-89dc-24f8f3178773`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.sheetId }}` — node "Google Sheets7" (id `e5fcadeb-ddc8-4c58-89ac-cdd33b6e7d2e`)

### Google Drive

- *(dynamic)* — op `download` — node "Google Drive v2" (id `38d09755-acfd-4881-b8c3-b6e109c33035`)
- *(dynamic)* — op `move` — node "Google Drive1" (id `acb3d96e-29c2-4900-ac3b-1b434788f014`)
- *(dynamic)* — op `move` — node "Google Drive1" (id `acb3d96e-29c2-4900-ac3b-1b434788f014`)
- *(dynamic)* — op `download` — node "Google Drive v1" (id `ceef6ba7-cc99-4041-99ce-7aa29dd1727f`)
- *(dynamic)* — op `move` — node "Google Drive5" (id `ee4185a5-1096-49c1-a904-ee34fee3c1d3`)
- *(dynamic)* — op `move` — node "Google Drive5" (id `ee4185a5-1096-49c1-a904-ee34fee3c1d3`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
