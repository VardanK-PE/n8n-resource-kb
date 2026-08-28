---
n8n_id: "09FsMhwgZoSxA7m9"
name: "My workflow 5"
status: inactive
last_modified: 2026-01-15T17:37:30.972Z
tags: []
fingerprint: "7636f8cca46b1aa2d34ff792f923feef9693f0ae56c0e6fd7c48a9c80db21856"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# My workflow 5

## Summary

- **Status:** inactive
- **n8n ID:** `09FsMhwgZoSxA7m9`
- **Nodes:** 5
- **Last modified:** 2026-01-15T17:37:30.972Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `a45d1e71-3716-4806-8def-3e73a4772996`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `30feed05-8cd2-408b-8246-a4204f9c6ccb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `5f6ece75-e509-4c96-a54d-0bc38f9bdb87`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `e16fbe48-ac60-4b99-87f5-8f9184436889`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `e16fbe48-ac60-4b99-87f5-8f9184436889`)

### Google Sheets

- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `?`, tab `={{ $json.spreadsheet_name }}` — node "Get row(s) in sheet" (id `30feed05-8cd2-408b-8246-a4204f9c6ccb`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update row in sheet" (id `5f6ece75-e509-4c96-a54d-0bc38f9bdb87`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
