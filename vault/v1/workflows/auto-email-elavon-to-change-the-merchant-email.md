---
n8n_id: "1DtbETjoUehasEAG"
instance: v1
name: "Auto-email Elavon to change the merchant email"
status: active
last_modified: 2025-11-19T16:21:17.764Z
tags: []
fingerprint: "13a59c39a67271af3d8c5e4e15bd9af29e93e6f210fd3af66f620460d5fe3151"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Auto-email Elavon to change the merchant email

## Summary

- **Status:** active
- **n8n ID:** `1DtbETjoUehasEAG`
- **Nodes:** 18
- **Last modified:** 2025-11-19T16:21:17.764Z

## Triggers

- **error** — node "Error Trigger" (id `ba291bb6-74c5-4267-a9d5-3c7a0c4e78a1`)
- **manual** — node "When clicking ‘Execute workflow’" (id `caac44cc-fbcb-49c1-887e-0900f6cb1f4b`)
- **schedule** — node "Schedule Trigger" (id `dfd2576c-4f11-4314-83fa-5e7d1d313b5d`) — `daily at 10:00`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `532fdef8-aae3-4522-885d-6e3bde297971`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `7e29ac99-bd27-4a85-a088-12d4ae9997eb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `9f13de98-5e6e-4543-b057-f0016d49f49c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get the list of MIDs" (id `d18b8447-3be7-419c-b631-1aadd7417fa1`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `532fdef8-aae3-4522-885d-6e3bde297971`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update row in sheet" (id `9f13de98-5e6e-4543-b057-f0016d49f49c`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get the list of MIDs" (id `d18b8447-3be7-419c-b631-1aadd7417fa1`)

### Slack channels

- [[../resources/slack-channels/c09pc6hkhpy|payengine-ai-alerts]] (id `C09PC6HKHPY`) — op `channel` — node "Send a message5" (id `7e29ac99-bd27-4a85-a088-12d4ae9997eb`)

### Sub-workflows (Execute Workflow calls)

- [[send-email-html|Send Email: HTML]] (n8n_id `H9qPciXCz00KxAyF`) — node "Call 'Send Email'" (id `c9cd9161-98f4-4473-ad5f-a044f5e93bcd`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
