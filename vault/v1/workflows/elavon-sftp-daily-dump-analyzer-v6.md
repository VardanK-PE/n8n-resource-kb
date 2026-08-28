---
n8n_id: "e93RsgQXI8GlYNLa"
name: "Elavon SFTP Daily Dump/Analyzer V6"
status: active
last_modified: 2024-10-25T17:18:00.369Z
tags:
  - "daily reports"
fingerprint: "c8776a0df2d665d72f6c2d8704fb8b1003e9ace0f9bbbc050f14398e138757a9"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Elavon SFTP Daily Dump/Analyzer V6

## Summary

- **Status:** active
- **n8n ID:** `e93RsgQXI8GlYNLa`
- **Nodes:** 42
- **Last modified:** 2024-10-25T17:18:00.369Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `80a6b12a-8995-4b64-94d4-d4bbe42a5feb`) — `every 6 hour(s)`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres2" (id `091b5bc2-d832-46d0-b5b3-af50c5cbc4b5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `14065604-8ba3-4a0a-a8b3-1b52f42e222f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `32eceb8a-009e-400f-841d-f98ede7a0cfa`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `3dbb3b84-753c-468d-9ad1-e148f6d671c2`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres5" (id `406f67b0-ee5b-4999-97ea-550ae41c8218`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack5" (id `583187ef-0a6f-43d9-8e6a-d11e017add5b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `5beb5bf8-c80f-460c-8f3d-6000a14db8e3`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres3" (id `5d2903fb-c67c-4e63-a088-d854de28285e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `64ca0b76-ecae-42b6-ae3e-e423b2f70128`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `68b0dab7-b075-4ae2-8de7-a6f45bd01a71`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `8d82d727-5e10-4777-952e-c5dc81548394`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `97cd81ac-a694-40fa-a3f4-04c7a42f7d11`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack4" (id `b6799591-8945-4f3d-81d4-b814935d3493`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `bd3258f8-221b-4824-b305-09ea6c68e53f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `d3761b51-948e-48c9-a311-f393c483bb4e`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres6" (id `dac66a28-f2ce-4a11-9853-d3ec68af433f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack3" (id `e3f2e171-d41f-42c9-9ddb-f52a58ee9a6e`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres4" (id `e4935f09-4016-4c14-84c1-beabbb03cbe5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets7" (id `f5cfcb38-fb76-4076-b6c6-07da8934f516`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack6" (id `fe9ee333-dc6b-462e-9d27-a018bce8e89e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `ff873c11-3346-43b7-9431-0873c6c14e7b`)

### HTTP URLs

- [[../resources/http-urls/pf-prod-ecs-task-container-gotenberg-3000|pf-prod-ecs-task-container-gotenberg:3000]] — `POST http://pf-prod-ecs-task-container-gotenberg:3000/forms/chromium/convert/html` — node "Convert To PDF [GOTENBERG]" (id `98391800-ff80-438b-912b-1b3c379e2061`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres2" (id `091b5bc2-d832-46d0-b5b3-af50c5cbc4b5`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres5" (id `406f67b0-ee5b-4999-97ea-550ae41c8218`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres3" (id `5d2903fb-c67c-4e63-a088-d854de28285e`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `68b0dab7-b075-4ae2-8de7-a6f45bd01a71`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `97cd81ac-a694-40fa-a3f4-04c7a42f7d11`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres6" (id `dac66a28-f2ce-4a11-9853-d3ec68af433f`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres4" (id `e4935f09-4016-4c14-84c1-beabbb03cbe5`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "JSON To MD Table" (id `cbd6d76b-0cd5-49b5-a0c1-20ac16b11eaa`)

### Google Sheets

- [[../resources/google-sheets/1ig4gdkebzb3i-9uwyrqzy9sthjqlta2p7z6dpi2wpt4|ElavonSettlementFileAnalyzer]] (id `1IG4gDKEbZb3I-9uWYrqZY9SthJqlTA2p7z6dPi2WPt4`) — op `append`, tab `SFTP` — node "Google Sheets2" (id `14065604-8ba3-4a0a-a8b3-1b52f42e222f`)
- [[../resources/google-sheets/1njjo3rraqm3un75k-sqow2tulzzpito6foj7nur48xu|ElavonDailyL2MissesAnalyzer]] (id `1nJJO3rRaQM3un75k_sqOW2TULzzPitO6FOj7nUR48XU`) — op `append`, tab `DailyL2Misses` — node "Google Sheets5" (id `32eceb8a-009e-400f-841d-f98ede7a0cfa`)
- *(dynamic spreadsheet)* — op `append`, tab `={{ $('Google Sheets').item.json.sheetId }}` — node "Google Sheets1" (id `5beb5bf8-c80f-460c-8f3d-6000a14db8e3`)
- [[../resources/google-sheets/1ig4gdkebzb3i-9uwyrqzy9sthjqlta2p7z6dpi2wpt4|ElavonSettlementFileAnalyzer]] (id `1IG4gDKEbZb3I-9uWYrqZY9SthJqlTA2p7z6dPi2WPt4`) — op `create`, tab `null` — node "Google Sheets" (id `8d82d727-5e10-4777-952e-c5dc81548394`)
- [[../resources/google-sheets/1q6uhbw-yzimqo0umlx8xf3ofdo8qlvy0nvciywnvgwe|INVOICES / DEVICES / RESERVE FUNDING]] (id `1Q6uHbW_YZImQO0uMLx8xF3OFdo8qlvY0nVciyWNVGwE`) — op `append`, tab `Reserve Funding MID Alerts` — node "Google Sheets4" (id `bd3258f8-221b-4824-b305-09ea6c68e53f`)
- [[../resources/google-sheets/1q6uhbw-yzimqo0umlx8xf3ofdo8qlvy0nvciywnvgwe|INVOICES / DEVICES / RESERVE FUNDING]] (id `1Q6uHbW_YZImQO0uMLx8xF3OFdo8qlvY0nVciyWNVGwE`) — op `?`, tab `Reserve Funding` — node "Google Sheets3" (id `d3761b51-948e-48c9-a311-f393c483bb4e`)
- [[../resources/google-sheets/15sof5rlrq-cx6rm6io-kib6-jpnfolq9jsuvjilwru|N8N_ElavonCardType]] (id `15sOF5RlRQ_CX6RM6iO_-kib6_JpNfOlq9JSUvjILwrU`) — op `?`, tab `ElavonCardTypes` — node "Google Sheets7" (id `f5cfcb38-fb76-4076-b6c6-07da8934f516`)

### Slack channels

- [[../resources/slack-channels/c06c06y8tdh|transaction-alerts]] (id `C06C06Y8TDH`) — op `channel` — node "Slack1" (id `3dbb3b84-753c-468d-9ad1-e148f6d671c2`)
- [[../resources/slack-channels/c06c06y8tdh|transaction-alerts]] (id `C06C06Y8TDH`) — op `channel` — node "Slack3" (id `e3f2e171-d41f-42c9-9ddb-f52a58ee9a6e`)
- [[../resources/slack-channels/c06c06y8tdh|transaction-alerts]] (id `C06C06Y8TDH`) — op `channel` — node "Slack" (id `ff873c11-3346-43b7-9431-0873c6c14e7b`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
