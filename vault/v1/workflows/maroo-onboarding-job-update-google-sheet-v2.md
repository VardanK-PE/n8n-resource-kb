---
n8n_id: "q3KvU7OAnSev22Hh"
name: "Maroo Onboarding Job - Update Google Sheet v2"
status: active
last_modified: 2025-03-04T02:02:21.040Z
tags: []
fingerprint: "03a9e78d1a3a381985e7f552c14e6e589b8a4fcf72efe508f29477274d044b60"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Maroo Onboarding Job - Update Google Sheet v2

## Summary

- **Status:** active
- **n8n ID:** `q3KvU7OAnSev22Hh`
- **Nodes:** 19
- **Last modified:** 2025-03-04T02:02:21.040Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `be684d70-3355-40d3-a3e2-9b81f82fd67e`) — `every 1 hour(s)`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `13a19b58-fa38-40c1-8be5-54f583de6608`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `36507ea5-a5aa-41e7-b83e-299b49905ba0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Remove Locks" (id `617aa8ff-aeb1-4980-87f7-556010652414`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request2" (id `64daad7d-5805-4d2f-bfdb-9eb469e44fea`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive" (id `9e99772b-700f-4f84-b823-899241d2f23a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Add Locks (All)" (id `cc2474fe-f0c3-459a-b343-0458876ff135`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Add Single Lock" (id `f69c9b65-e368-47e1-8737-4399d346d9f2`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `ffbb033d-3fd1-4e72-b102-625a6a61fdb8`)

### HTTP URLs

- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $json.spreadsheetID }}:batchUpdate` — node "Remove Locks" (id `617aa8ff-aeb1-4980-87f7-556010652414`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $json.id }}` — node "HTTP Request2" (id `64daad7d-5805-4d2f-bfdb-9eb469e44fea`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $json.spreadsheetID }}:batchUpdate` — node "Add Locks (All)" (id `cc2474fe-f0c3-459a-b343-0458876ff135`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $json.spreadsheetID }}:batchUpdate` — node "Add Single Lock" (id `f69c9b65-e368-47e1-8737-4399d346d9f2`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `ffbb033d-3fd1-4e72-b102-625a6a61fdb8`)

### Google Sheets

- [[../resources/google-sheets/1kenlzlm4bnsd-8fx9fuhudpy1qujsmuyhpmkkh11k9a|Final Maroo Data]] (id `1keNlZLM4BNSd-8fx9fuhUDpy1quJsMuYHpMkkh11K9A`) — op `appendOrUpdate`, tab `Output` — node "Google Sheets" (id `13a19b58-fa38-40c1-8be5-54f583de6608`)
- [[../resources/google-sheets/148wedqfs59vghkv7da3wku61hmhsklekgycy2viegbm|Yumna Testing]] (id `148WEdqfS59VGHkv7da3wkU61HMHSKlEkgYCY2VIEgbM`) — op `?`, tab `Output` — node "Google Sheets1" (id `36507ea5-a5aa-41e7-b83e-299b49905ba0`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
