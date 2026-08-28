---
n8n_id: "KcGFKiEV1MczcbS8"
instance: v1
name: "Charge PCI non compliant merchants"
status: inactive
last_modified: 2026-08-14T19:33:34.539Z
tags: []
fingerprint: "ed9154f3f66387d15e0df49ec7395ad803096588e33960521b1b9ef48274990f"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Charge PCI non compliant merchants

## Summary

- **Status:** inactive
- **n8n ID:** `KcGFKiEV1MczcbS8`
- **Nodes:** 47
- **Last modified:** 2026-08-14T19:33:34.539Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `6c405b8f-a43b-40b1-9725-f9ad5e213417`) — `every 20 minute(s)`
- **manual** — node "When clicking ‘Execute workflow’" (id `9fedf117-16b4-4ed7-abfa-c1343a2ffed4`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `118230c5-1860-4532-916c-1073e650a1b4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet2" (id `11dd6537-9ff4-49c5-abd8-4ae7c6e3d007`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet2" (id `13c12d7f-ecc2-4c84-9ccb-bc89cf009094`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `230d82af-fbf5-4dc1-9bc7-b81f5dbb0b10`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Transaction Details1" (id `31d5d0a1-152a-4a03-8d72-7a09281bdb0d`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query1" (id `328ab454-b941-42e0-809c-3b3e8ebe78be`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `48097993-96de-4b74-95e7-8713a4f9ed5e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Bank Account Fields" (id `74ac1b30-29d2-412b-8305-3b194e9c4e2c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Transaction Details2" (id `85b5eeb7-717d-4ce0-bec3-120907e08d3a`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query2" (id `92e799c0-a041-492d-912f-04e44f3f41c8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet3" (id `a8f93c38-3c02-4191-b642-52a25c5957f6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `b430183a-e6e8-4950-a87c-0f2682818ca9`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres4" (id `bdb124ea-e29a-438b-a4a4-e8bfeedfd3ce`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query3" (id `c34bb1c2-ab2a-4711-9ffd-b518605af79b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `e195d898-4e35-49bf-880c-b60e45a6dd88`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Transaction Details" (id `e9eaf914-b1d6-4fab-b9b6-f49709d8ee0f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet1" (id `fb18da2f-6bc2-40e3-b5e2-df39df494e0b`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/payment/ach` — node "Perform the Charge" (id `4b2fe7c3-e7f5-40af-ac42-95705e10fa5c`)
- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/bank-accounts` — node "Create Bank Account Token US" (id `81ec8c22-fb33-4ef7-91ad-39f75f215530`)
- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/bank-accounts` — node "Create Bank Account Token - CA" (id `c908a3c6-5ffe-496f-9509-37cc0455736e`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `230d82af-fbf5-4dc1-9bc7-b81f5dbb0b10`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query1" (id `328ab454-b941-42e0-809c-3b3e8ebe78be`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query2" (id `92e799c0-a041-492d-912f-04e44f3f41c8`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres4" (id `bdb124ea-e29a-438b-a4a4-e8bfeedfd3ce`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query3" (id `c34bb1c2-ab2a-4711-9ffd-b518605af79b`)

### Google Sheets

- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `?`, tab `={{ $json.spreadsheet_name }}` — node "Get row(s) in sheet" (id `118230c5-1860-4532-916c-1073e650a1b4`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update row in sheet2" (id `11dd6537-9ff4-49c5-abd8-4ae7c6e3d007`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `?`, tab `={{ $json.spreadsheet_name }}` — node "Get row(s) in sheet2" (id `13c12d7f-ecc2-4c84-9ccb-bc89cf009094`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `append`, tab `Error Log` — node "Update Transaction Details1" (id `31d5d0a1-152a-4a03-8d72-7a09281bdb0d`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update row in sheet" (id `48097993-96de-4b74-95e7-8713a4f9ed5e`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update Bank Account Fields" (id `74ac1b30-29d2-412b-8305-3b194e9c4e2c`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `append`, tab `Token Logs` — node "Update Transaction Details2" (id `85b5eeb7-717d-4ce0-bec3-120907e08d3a`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get row(s) in sheet3" (id `a8f93c38-3c02-4191-b642-52a25c5957f6`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `append`, tab `Transaction Log` — node "Append row in sheet" (id `b430183a-e6e8-4950-a87c-0f2682818ca9`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `?`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Get row(s) in sheet1" (id `e195d898-4e35-49bf-880c-b60e45a6dd88`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update Transaction Details" (id `e9eaf914-b1d6-4fab-b9b6-f49709d8ee0f`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update row in sheet1" (id `fb18da2f-6bc2-40e3-b5e2-df39df494e0b`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
