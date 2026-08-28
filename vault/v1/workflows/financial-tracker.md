---
n8n_id: "NySfya8Y5Fgrf5kj"
instance: v1
name: "Financial Tracker"
status: inactive
last_modified: 2025-09-16T14:38:39.836Z
tags: []
fingerprint: "8694ffafddc9e38d79b180928259df2a79f65897a20ffe9133c3f23337bea21b"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Financial Tracker

## Summary

- **Status:** inactive
- **n8n ID:** `NySfya8Y5Fgrf5kj`
- **Nodes:** 16
- **Last modified:** 2025-09-16T14:38:39.836Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `b7fcee6d-e4fd-473f-b000-9d95957810be`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `1b7d4a13-8b8f-43d9-bd92-31bfd1b181c2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Search files and folders1" (id `3791b75e-c543-4896-b761-5b53d2006d73`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `4fe37fe0-29e3-415d-b393-398a108e56fd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `54764ec8-6dcf-4ebb-941e-31f6f44cb4dd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Sheets" (id `686164f1-bf75-432e-b2b3-372cbd63a274`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `6eef02f5-bbd4-464e-92c2-53a648fbb4d1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Search files and folders" (id `f9d012dc-a9e1-4477-a695-a1882b1cb045`)

### HTTP URLs

- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $json.file_id }}?includeGridData=false ` — node "Get Sheets" (id `686164f1-bf75-432e-b2b3-372cbd63a274`)

### Google Sheets

- [[../resources/google-sheets/1aowq5ovlnv58g6umm3k8oly6na1emm5vmnsq-yi-v4|PE Residuals Financial Tracker]] (id `1aoWq5oVLnV58G6uMm3k8OlY6na1EMM5VmnSq__YI_v4`) — op `appendOrUpdate`, tab `General` — node "Append or update row in sheet" (id `1b7d4a13-8b8f-43d9-bd92-31bfd1b181c2`)
- [[../resources/google-sheets/1aowq5ovlnv58g6umm3k8oly6na1emm5vmnsq-yi-v4|PE Residuals Financial Tracker]] (id `1aoWq5oVLnV58G6uMm3k8OlY6na1EMM5VmnSq__YI_v4`) — op `update`, tab `General` — node "Update row in sheet" (id `4fe37fe0-29e3-415d-b393-398a108e56fd`)
- [[../resources/google-sheets/1aowq5ovlnv58g6umm3k8oly6na1emm5vmnsq-yi-v4|PE Residuals Financial Tracker]] (id `1aoWq5oVLnV58G6uMm3k8OlY6na1EMM5VmnSq__YI_v4`) — op `?`, tab `General` — node "Get row(s) in sheet1" (id `54764ec8-6dcf-4ebb-941e-31f6f44cb4dd`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.sheets[0].properties.sheetId }}` — node "Get row(s) in sheet" (id `6eef02f5-bbd4-464e-92c2-53a648fbb4d1`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
