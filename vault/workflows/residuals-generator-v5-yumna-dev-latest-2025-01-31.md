---
n8n_id: "vwmig5DqkHOd5Y0g"
name: "Residuals Generator V5 (Yumna Dev) (latest 2025-01-31)"
status: inactive
last_modified: 2025-02-26T15:41:52.239Z
tags:
  - "Residuals"
  - "latest"
fingerprint: "4959c7baeeaba7bd6ecd2cdf19caa773753a326f2f44a11723d98e96ee314ad0"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Residuals Generator V5 (Yumna Dev) (latest 2025-01-31)

## Summary

- **Status:** inactive
- **n8n ID:** `vwmig5DqkHOd5Y0g`
- **Nodes:** 87
- **Last modified:** 2025-02-26T15:41:52.239Z

## Triggers

- **execute-workflow** — node "Execute Workflow Trigger" (id `7cfcf2cd-4815-428d-af7d-4f88faf45f62`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive" (id `0ac1693e-f48f-48ed-97a6-4c4e2cac79c0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive3" (id `0cc7459e-3863-45fa-8392-f1ad37356da8`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `10b2eac8-2c15-4186-afe9-834125fd9866`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request5" (id `12311d3b-3349-49d9-b869-d9196ca544fc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive4" (id `13b5bd0d-8ed6-4d59-aa1d-6e379297efd9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request" (id `28983bbf-4358-43b2-8735-4c987209cb25`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Read Final Sheet" (id `37ed582b-4b7c-478c-b53e-6bd97347b8ae`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v1" (id `3ab8b74c-37a7-4371-b9fe-666fb329db9f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AppendTotalsRow" (id `3d0d09f5-9835-483f-804e-b99b9b60f218`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `43f2540b-9122-41c4-9d20-be10166d94fd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request2" (id `476702a7-0004-409d-9eec-c1eda03638fa`)
- [[../resources/credentials/67fejotk4a3tgz6y|Kafka account]] (`kafka`, id `67fEjoTk4A3tGZ6Y`) — node "Kafka" (id `480fab5a-0049-4495-9a8d-247c9704cbac`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v2" (id `4921f83c-2f25-4694-8566-0026bc7980fc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "ICQualReport" (id `631570c4-c152-4a19-b27e-3a748fe9a063`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data1" (id `657551a2-2a7b-4e63-b33d-896c6c228783`)
- [[../resources/credentials/mla6ntr86w0mqqdf|PE AWS Account (Prod)]] (`aws`, id `mLa6NtR86w0mqQDF`) — node "AWS S3" (id `6d68d83a-01cd-4ea2-a988-1f549c6b7a6b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Files List" (id `72c46412-e0e0-4f45-b3e7-368fce3d90c6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "MiscExpensesData" (id `7af29142-dffe-4c71-9b0b-618bdae762a4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive1" (id `7f38ad72-3c8c-4f0e-ae75-bee0ceefe597`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive2" (id `8561ca9e-800d-4e30-8ecc-fdea3aa960a1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request6" (id `88716889-5fc8-47e0-986c-f5a28133ca25`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `8ac7ff52-90ed-4e62-86fc-35e7ac2207a5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive5" (id `8c2e98ef-3b25-44f7-9709-1d67d5aecec1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request3" (id `941c3230-7d7c-425a-b243-4df827fb672b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `a0169226-4721-439d-ae9b-f4164e6357c2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "SummarySheet" (id `a0d47181-bc4e-46e6-b222-bff264a1319f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsData" (id `a34845d3-0139-43c1-bc77-a95ccb34e8c1`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data2" (id `a39e54de-4a55-4a70-8539-0b251f01041e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `a94ca435-7e13-4a66-a9d7-094f20f937d4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets8" (id `be72c2bd-b885-43f5-8d90-87961a1bf83d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AutoL2Merchants" (id `bf9e2033-6679-46da-9814-bd3deb642722`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive v" (id `d27d40bd-e4db-48a8-a2d0-2b316af5e81e`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AutoL2Data" (id `d2a43fbe-2acc-492e-839b-387847fe78ae`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request1" (id `df94a984-e2c5-492c-8fd1-47a9f989827d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PartnerResidualsTerms" (id `e045f67a-36aa-4a13-8e31-d54f70e84c1b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets7" (id `e2614d4d-fbb5-436a-8131-3d708f08a3c8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `e296e46a-bf4a-48d2-bbb5-1c7199f2b713`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request4" (id `ef94b997-a6cb-451a-81c1-883a8d2c453d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `f7439600-0b3e-4385-91ed-7290b7400526`)

### HTTP URLs

- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1UNyfPl1I1IFSfVMVMSw5wEXMVqDxKj6CJzBZYlPVvAQ:batchUpdate` — node "HTTP Request5" (id `12311d3b-3349-49d9-b869-d9196ca544fc`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs:batchUpdate` — node "HTTP Request" (id `28983bbf-4358-43b2-8735-4c987209cb25`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs?includeGridData=false` — node "HTTP Request2" (id `476702a7-0004-409d-9eec-c1eda03638fa`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').first().json.spreadsheetId }}:batchUpdate ` — node "HTTP Request6" (id `88716889-5fc8-47e0-986c-f5a28133ca25`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get MerchantDetailReport.dat').all()[0].json.spreadsheetId }}?includeGridData=false ` — node "HTTP Request3" (id `941c3230-7d7c-425a-b243-4df827fb672b`)
- [[../resources/http-urls/5bfe7780bed71843efae07da96917971-m-pipedream-net|5bfe7780bed71843efae07da96917971.m.pipedream.net]] — `POST https://5bfe7780bed71843efae07da96917971.m.pipedream.net` — node "HTTP Request1" (id `df94a984-e2c5-492c-8fd1-47a9f989827d`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').all()[0].json.spreadsheetId }}:batchUpdate ` — node "HTTP Request4" (id `ef94b997-a6cb-451a-81c1-883a8d2c453d`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `10b2eac8-2c15-4186-afe9-834125fd9866`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data1" (id `657551a2-2a7b-4e63-b33d-896c6c228783`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data2" (id `a39e54de-4a55-4a70-8539-0b251f01041e`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AutoL2Data" (id `d2a43fbe-2acc-492e-839b-387847fe78ae`)

### Google Sheets

- *(dynamic spreadsheet)* — op `?`, tab `={{ $('Google Sheets5').first().json.sheets[0].properties.sheetId }}` — node "Read Final Sheet" (id `37ed582b-4b7c-478c-b53e-6bd97347b8ae`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets5').first().json.sheets[0].properties.sheetId }}` — node "AppendTotalsRow" (id `3d0d09f5-9835-483f-804e-b99b9b60f218`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.sheetId }}` — node "ICQualReport" (id `631570c4-c152-4a19-b27e-3a748fe9a063`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.sheetId }}` — node "MiscExpensesData" (id `7af29142-dffe-4c71-9b0b-618bdae762a4`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "Google Sheets1" (id `8ac7ff52-90ed-4e62-86fc-35e7ac2207a5`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets3').first().json.sheetId }}` — node "Google Sheets4" (id `a0169226-4721-439d-ae9b-f4164e6357c2`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "SummarySheet" (id `a0d47181-bc4e-46e6-b222-bff264a1319f`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets5').item.json.sheets[0].properties.sheetId }}` — node "PartnerResidualsData" (id `a34845d3-0139-43c1-bc77-a95ccb34e8c1`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets1').item.json.sheetId }}` — node "Google Sheets2" (id `a94ca435-7e13-4a66-a9d7-094f20f937d4`)
- *(dynamic spreadsheet)* — op `appendOrUpdate`, tab `={{ $('SummarySheet').item.json.sheetId }}` — node "Google Sheets8" (id `be72c2bd-b885-43f5-8d90-87961a1bf83d`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `auto_l2_mids` — node "AutoL2Merchants" (id `bf9e2033-6679-46da-9814-bd3deb642722`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "PartnerResidualsTerms" (id `e045f67a-36aa-4a13-8e31-d54f70e84c1b`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.sheetId }}` — node "Google Sheets7" (id `e2614d4d-fbb5-436a-8131-3d708f08a3c8`)
- *(dynamic spreadsheet)* — op `create`, tab `null` — node "Google Sheets3" (id `e296e46a-bf4a-48d2-bbb5-1c7199f2b713`)

### Google Drive

- *(dynamic)* — op `download` — node "Google Drive v1" (id `3ab8b74c-37a7-4371-b9fe-666fb329db9f`)
- *(dynamic)* — op `download` — node "Google Drive v2" (id `4921f83c-2f25-4694-8566-0026bc7980fc`)
- *(dynamic)* — op `move` — node "Google Drive1" (id `7f38ad72-3c8c-4f0e-ae75-bee0ceefe597`)
- *(dynamic)* — op `move` — node "Google Drive1" (id `7f38ad72-3c8c-4f0e-ae75-bee0ceefe597`)
- *(dynamic)* — op `move` — node "Google Drive5" (id `8c2e98ef-3b25-44f7-9709-1d67d5aecec1`)
- *(dynamic)* — op `move` — node "Google Drive5" (id `8c2e98ef-3b25-44f7-9709-1d67d5aecec1`)

### AWS S3 buckets

- [[../resources/s3-buckets/partner-residuals-prod|partner-residuals-prod]] — op `upload` — node "AWS S3" (id `6d68d83a-01cd-4ea2-a988-1f549c6b7a6b`)

### Kafka topics

- [[../resources/kafka-topics/partner-residuals|partner-residuals]] (`producer`) — node "Kafka" (id `480fab5a-0049-4495-9a8d-247c9704cbac`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
