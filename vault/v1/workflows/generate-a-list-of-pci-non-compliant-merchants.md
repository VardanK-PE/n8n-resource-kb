---
n8n_id: "62BRoOJ3o0VRHCnh"
instance: v1
name: "Generate a list of PCI non compliant merchants"
status: active
last_modified: 2026-06-30T13:04:27.366Z
tags: []
fingerprint: "c255a10ad6cdad1dba7a647fe37379185cec1bccd73d59f0d3f60b5d0ca229c4"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Generate a list of PCI non compliant merchants

## Summary

- **Status:** active
- **n8n ID:** `62BRoOJ3o0VRHCnh`
- **Nodes:** 28
- **Last modified:** 2026-06-30T13:04:27.366Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `0c91eff3-ad4e-4a88-926f-1d26365ffe32`) — `every 1 month(s)`
- **manual** — node "When clicking ‘Execute workflow’" (id `adaf4bda-bffa-460f-86dc-97452fe2873a`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `2084221f-fedc-4367-b63b-cd8fe30d3f2d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `419cc89a-0e80-4530-b0e5-c3b6d196166c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Delete sheet" (id `52575859-0fc4-49d7-889f-2e8e43323559`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create sheet1" (id `5351a342-128c-4065-a285-f942941e39f7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet1" (id `5f149088-6210-4386-a462-6fda858c574b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `68d01ded-337f-4ce0-be3f-e2a41917654a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create sheet" (id `77e0731b-66c5-4b24-9d17-2fe9acfd1aaf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `aca5e4e6-be0c-4bf8-9e84-69999b6ea026`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Request non compliant active merchants" (id `d484c7d6-68d3-467f-9625-b885ba7daf12`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Delete sheet1" (id `e54bea50-65e1-41c4-85e3-8f04775feaf1`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `f4e6fdd1-a1a2-481f-affa-bf6748754874`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `f4e6fdd1-a1a2-481f-affa-bf6748754874`)

### Google Sheets

- [[../resources/google-sheets/1kxkjxqxq8xyymtb1mabdezphkruxamiklwleqpfwrwm|Elavon BI (mids) snapshots]] (id `1kXKJXQxQ8xYYmtb1mAbdeZPHKrUXamIklwLeqpfwRwM`) — op `append`, tab `={{ $('Entry Point').first().json.sheet_name }}` — node "Append row in sheet" (id `2084221f-fedc-4367-b63b-cd8fe30d3f2d`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get row(s) in sheet" (id `419cc89a-0e80-4530-b0e5-c3b6d196166c`)
- [[../resources/google-sheets/1kxkjxqxq8xyymtb1mabdezphkruxamiklwleqpfwrwm|Elavon BI (mids) snapshots]] (id `1kXKJXQxQ8xYYmtb1mAbdeZPHKrUXamIklwLeqpfwRwM`) — op `remove`, tab `={{ $('Entry Point').first().json.sheet_name }}` — node "Delete sheet" (id `52575859-0fc4-49d7-889f-2e8e43323559`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `create`, tab `null` — node "Create sheet1" (id `5351a342-128c-4065-a285-f942941e39f7`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `append`, tab `={{ $('Entry Point').first().json.sheet_name }}` — node "Append row in sheet1" (id `5f149088-6210-4386-a462-6fda858c574b`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `update`, tab `={{ $('Entry Point').first().json.sheet_name }}` — node "Update row in sheet" (id `68d01ded-337f-4ce0-be3f-e2a41917654a`)
- [[../resources/google-sheets/1kxkjxqxq8xyymtb1mabdezphkruxamiklwleqpfwrwm|Elavon BI (mids) snapshots]] (id `1kXKJXQxQ8xYYmtb1mAbdeZPHKrUXamIklwLeqpfwRwM`) — op `create`, tab `null` — node "Create sheet" (id `77e0731b-66c5-4b24-9d17-2fe9acfd1aaf`)
- [[../resources/google-sheets/1yso2a6ltbrwik4vlhzg1thkokth-7vxc0eimuj2t-iq|Copy of Elavon BI Automation - May 1, 12:16 AM]] (id `1YSO2A6lTBRwiK4VlhZG1ThkOktH-7vXC0EimuJ2t-iQ`) — op `?`, tab `mid` — node "Get row(s) in sheet1" (id `aca5e4e6-be0c-4bf8-9e84-69999b6ea026`)
- [[../resources/google-sheets/1kxkjxqxq8xyymtb1mabdezphkruxamiklwleqpfwrwm|Elavon BI (mids) snapshots]] (id `1kXKJXQxQ8xYYmtb1mAbdeZPHKrUXamIklwLeqpfwRwM`) — op `?`, tab `={{ $('Entry Point').first().json.sheet_name }}` — node "Request non compliant active merchants" (id `d484c7d6-68d3-467f-9625-b885ba7daf12`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `remove`, tab `={{ $('Entry Point').first().json.sheet_name }}` — node "Delete sheet1" (id `e54bea50-65e1-41c4-85e3-8f04775feaf1`)

### Sub-workflows (Execute Workflow calls)

- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `2082fe1b-446e-4188-b402-b1c44602d96c`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
