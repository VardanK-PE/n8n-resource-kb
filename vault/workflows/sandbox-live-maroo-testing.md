---
n8n_id: "2aNE1cLr1DIf3MaB"
name: "Sandbox Live - Maroo Testing"
status: active
last_modified: 2025-03-04T02:09:30.137Z
tags: []
fingerprint: "c8bf8868979ceb2c3d33b49f85934def670d4e2dd36a78da93c11819b136779b"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Sandbox Live - Maroo Testing

## Summary

- **Status:** active
- **n8n ID:** `2aNE1cLr1DIf3MaB`
- **Nodes:** 20
- **Last modified:** 2025-03-04T02:09:30.137Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `4535e33f-243e-402e-bc90-8525456d9f9b`) — `every 30 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive" (id `11162bed-0fbd-4370-8523-6c9a657c82df`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Add Locks (All)" (id `19b13de5-89f8-4417-917b-b596336467cf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `4ba54f04-6c54-4b04-9f8c-49b9f3c589da`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Add Single Lock" (id `82ff354a-6fa1-43f4-b549-2cc9d4e9a43d`)
- [[../resources/credentials/6gbwfpl6n9qz81ho|Postgres Sandbox-Live]] (`postgres`, id `6GBwfPL6n9QZ81ho`) — node "Postgres" (id `856757db-c47e-44a9-adb5-81d6898e73bf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Remove Locks" (id `c51eb38a-6513-4e22-9fbb-6546eacb24f1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request2" (id `dea6e1b1-f4f8-4ec0-b924-be44b1929b6c`)
- [[../resources/credentials/6gbwfpl6n9qz81ho|Postgres Sandbox-Live]] (`postgres`, id `6GBwfPL6n9QZ81ho`) — node "Postgres1" (id `def2e646-c77e-4372-85cc-42c74537fe2b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `f55218e2-086a-49fc-9536-5ff23ee8f1de`)

### HTTP URLs

- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $json.spreadsheetID }}:batchUpdate` — node "Add Locks (All)" (id `19b13de5-89f8-4417-917b-b596336467cf`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $json.spreadsheetID }}:batchUpdate` — node "Add Single Lock" (id `82ff354a-6fa1-43f4-b549-2cc9d4e9a43d`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $json.spreadsheetID }}:batchUpdate` — node "Remove Locks" (id `c51eb38a-6513-4e22-9fbb-6546eacb24f1`)
- [[../resources/http-urls/sheets-googleapis-com|sheets.googleapis.com]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $json.id }}` — node "HTTP Request2" (id `dea6e1b1-f4f8-4ec0-b924-be44b1929b6c`)

### Databases

- [[../resources/databases/postgres-6gbwfpl6n9qz81ho|postgres (via Postgres Sandbox-Live)]] — op `executeQuery` — node "Postgres" (id `856757db-c47e-44a9-adb5-81d6898e73bf`)
- [[../resources/databases/postgres-6gbwfpl6n9qz81ho|postgres (via Postgres Sandbox-Live)]] — op `select`, table `{"__rl":true,"value":"account_groups","mode":"list","cachedResultName":"account_groups"}` — node "Postgres1" (id `def2e646-c77e-4372-85cc-42c74537fe2b`)

### Google Sheets

- [[../resources/google-sheets/1lhhokp7sfvamwkt5eo-1hdxesfhnb47-lmhhpidevqe|Maroo Testing 12 Feb 25]] (id `1LhHOkP7sFvAmwkt5EO_1HDXEsfHnB47_LmhhpIdEvQE`) — op `appendOrUpdate`, tab `Output` — node "Google Sheets" (id `4ba54f04-6c54-4b04-9f8c-49b9f3c589da`)
- [[../resources/google-sheets/148wedqfs59vghkv7da3wku61hmhsklekgycy2viegbm|Yumna Testing]] (id `148WEdqfS59VGHkv7da3wkU61HMHSKlEkgYCY2VIEgbM`) — op `?`, tab `Output` — node "Google Sheets1" (id `f55218e2-086a-49fc-9536-5ff23ee8f1de`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
