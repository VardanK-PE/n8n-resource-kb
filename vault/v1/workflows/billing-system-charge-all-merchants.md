---
n8n_id: "Qo3jFiVJhnmFeBMU"
name: "Billing System - Charge All Merchants"
status: inactive
last_modified: 2026-03-18T19:54:59.581Z
tags: []
fingerprint: "2ebb3aecd0e20a31387142e72e7c70addc8460eda55b35b76934610f6072d942"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Billing System - Charge All Merchants

## Summary

- **Status:** inactive
- **n8n ID:** `Qo3jFiVJhnmFeBMU`
- **Nodes:** 28
- **Last modified:** 2026-03-18T19:54:59.581Z

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `00819d56-0ca8-4377-8646-b60d147d1f14`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres4" (id `0b3f83a5-cca8-4180-9cd2-6583aaa12cd3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `1f31e478-d506-4155-abc6-246e74523818`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Transaction Details1" (id `2daf3189-781e-45f9-b547-882baf60c98e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Transaction Details2" (id `735307cf-f2eb-418a-9d26-1398804209bc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `91f48b32-3af6-476f-b707-23b534ed78d6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `9a63ba87-dd6a-4899-a517-2845a22ee2f3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Bank Account Fields" (id `cb8aeb79-805f-41b5-a45f-a9dd5892d464`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Transaction Details" (id `d1265286-ae69-40f3-8442-e74a0928f39c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `d2aeada4-d050-40a9-a576-04b6f849179a`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/payment/ach` — node "Perform the Charge" (id `62753ebd-0ba5-47eb-8bf6-7d209db7a828`)
- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/bank-accounts` — node "Create Bank Account Token" (id `db287a2d-4621-44b0-8278-17db22170c42`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `00819d56-0ca8-4377-8646-b60d147d1f14`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres4" (id `0b3f83a5-cca8-4180-9cd2-6583aaa12cd3`)

### Google Sheets

- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `append`, tab `Transaction Log` — node "Append row in sheet" (id `1f31e478-d506-4155-abc6-246e74523818`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `append`, tab `Error Log` — node "Update Transaction Details1" (id `2daf3189-781e-45f9-b547-882baf60c98e`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `append`, tab `Token Logs` — node "Update Transaction Details2" (id `735307cf-f2eb-418a-9d26-1398804209bc`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update row in sheet" (id `91f48b32-3af6-476f-b707-23b534ed78d6`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `?`, tab `={{ $json.spreadsheet_name }}` — node "Get row(s) in sheet" (id `9a63ba87-dd6a-4899-a517-2845a22ee2f3`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update Bank Account Fields" (id `cb8aeb79-805f-41b5-a45f-a9dd5892d464`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update Transaction Details" (id `d1265286-ae69-40f3-8442-e74a0928f39c`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `?`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Get row(s) in sheet1" (id `d2aeada4-d050-40a9-a576-04b6f849179a`)

### Data tables (n8n)

- [[../resources/data-tables/|]] (id ``) — op `get` — node "Get row(s)" (id `851eb97a-f27d-4832-9806-c8f23c1ea497`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
