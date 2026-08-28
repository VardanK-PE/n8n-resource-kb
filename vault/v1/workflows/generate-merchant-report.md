---
n8n_id: "9M8mejP6A4QaBqY5"
instance: v1
name: "Generate Merchant Report"
status: active
last_modified: 2026-06-12T20:34:35.371Z
tags: []
fingerprint: "7e57ae3080855e6f8b3a9b5e2c9d5e51421bdc2905a32e2a28426b22d18efcf8"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Generate Merchant Report

## Summary

- **Status:** active
- **n8n ID:** `9M8mejP6A4QaBqY5`
- **Nodes:** 30
- **Last modified:** 2026-06-12T20:34:35.371Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `133babac-d6d4-48a9-866f-f06b1f0096a3`)
- **manual** — node "When clicking ‘Execute workflow’" (id `394a11de-b79a-4e05-9c40-3f11d734830e`)
- **schedule** — node "Schedule Trigger" (id `54deff2e-a76f-4311-bd69-4728d4527514`) — `daily at 4:00`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet3" (id `17ddf778-8518-4008-9063-9c86bed21b0c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `2001e6ba-8413-4258-90dd-a5f3644a3c5c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `477294f3-f71c-49b3-aecd-494b61020feb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Copy template file" (id `4c664732-438d-4d3c-be6b-e2c35ed858af`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `5f544802-9d05-43c2-a2d3-3bda6a2a1c07`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `62b39a2d-9bdf-4d4b-9030-995555859ddc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet1" (id `755cfba6-a39d-4839-b42c-04b13789d59e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get merchants" (id `b7990f8f-4ea1-470e-9075-64499027a041`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Execute a SQL query1" (id `c8ff4e2a-40b8-4479-bc91-810a1644dfa7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Delete a file" (id `d16fdae5-3df4-4bee-9887-eaac0cc697a2`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `62b39a2d-9bdf-4d4b-9030-995555859ddc`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Execute a SQL query1" (id `c8ff4e2a-40b8-4479-bc91-810a1644dfa7`)

### Google Sheets

- [[../resources/google-sheets/1gvypzuxuyl-0jfej0jwk8tvkuzfgt4luo3kq7httffy|Daily Reports - Merchant Transactions]] (id `1GVyPZUXUYl-0jfeJ0JwK8TVKUzFgT4LUo3Kq7HttffY`) — op `update`, tab `Daily Schedule` — node "Update row in sheet3" (id `17ddf778-8518-4008-9063-9c86bed21b0c`)
- *(dynamic spreadsheet)* — op `append`, tab `Transaction Detail` — node "Append row in sheet" (id `2001e6ba-8413-4258-90dd-a5f3644a3c5c`)
- *(dynamic spreadsheet)* — op `update`, tab `Transaction Detail` — node "Update row in sheet" (id `477294f3-f71c-49b3-aecd-494b61020feb`)
- [[../resources/google-sheets/1gvypzuxuyl-0jfej0jwk8tvkuzfgt4luo3kq7httffy|Daily Reports - Merchant Transactions]] (id `1GVyPZUXUYl-0jfeJ0JwK8TVKUzFgT4LUo3Kq7HttffY`) — op `append`, tab `Log` — node "Append row in sheet1" (id `755cfba6-a39d-4839-b42c-04b13789d59e`)
- [[../resources/google-sheets/1gvypzuxuyl-0jfej0jwk8tvkuzfgt4luo3kq7httffy|Daily Reports - Merchant Transactions]] (id `1GVyPZUXUYl-0jfeJ0JwK8TVKUzFgT4LUo3Kq7HttffY`) — op `?`, tab `Daily Schedule` — node "Get merchants" (id `b7990f8f-4ea1-470e-9075-64499027a041`)

### Google Drive

- [[../resources/google-drive/1wkk6fxrsdnnvqibrufdnqiviqjexnbx7bl8tjq1bk8q|Merchant Transactions Report - Template]] (`file`, id `1wkK6FxRsDnnvqIBrufDNqiViQjexnbx7BL8TJq1bk8Q`) — op `copy` — node "Copy template file" (id `4c664732-438d-4d3c-be6b-e2c35ed858af`)
- [[../resources/google-drive/1p0wzyfjtzvl0gedpaltomijb6k8wbaxq|Generated Reports]] (`folder`, id `1p0WzyFJTzvL0gEdpAlToMIJb6k8wBAxQ`) — op `copy` — node "Copy template file" (id `4c664732-438d-4d3c-be6b-e2c35ed858af`)
- *(dynamic)* — op `download` — node "Download file" (id `5f544802-9d05-43c2-a2d3-3bda6a2a1c07`)
- *(dynamic)* — op `deleteFile` — node "Delete a file" (id `d16fdae5-3df4-4bee-9887-eaac0cc697a2`)

### Sub-workflows (Execute Workflow calls)

- [[generate-merchant-report|Generate Merchant Report]] (n8n_id `9M8mejP6A4QaBqY5`) — node "Call 'Generate Merchant Report'" (id `3e0486a7-618b-47fa-9e5f-4656ea033b5b`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `4b4e5e0f-646d-45cb-b54b-8e42bb4a6123`)
- [[send-email-simple-text|Send Email: Simple Text]] (n8n_id `Zr3vF0LVpsPrzHVY`) — node "Call 'Send Email: Simple Text'" (id `f3a60d2c-c452-4615-a273-7a138471c23d`)

## Used by (workflows)

- [[generate-merchant-report|Generate Merchant Report]] — node "Call 'Generate Merchant Report'" (id `3e0486a7-618b-47fa-9e5f-4656ea033b5b`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
