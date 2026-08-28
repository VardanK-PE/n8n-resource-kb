---
n8n_id: "yrTbLLNUN76aNqmV"
name: "Check PCI/ACH Transaction Status"
status: inactive
last_modified: 2026-04-14T18:35:11.459Z
tags: []
fingerprint: "b631a009e6c3f7977916c50ab1670b3064305a972d5e93de46a8350529b74e4f"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Check PCI/ACH Transaction Status

## Summary

- **Status:** inactive
- **n8n ID:** `yrTbLLNUN76aNqmV`
- **Nodes:** 15
- **Last modified:** 2026-04-14T18:35:11.459Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `ff6f3447-0801-4c4f-abdd-aabe5b3635ef`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `109da278-109d-4ed1-9098-49f054d6b0a8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get PCI non-compliance charges" (id `6457de1f-a78c-4702-a42e-0010c0666349`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet1" (id `b377b72b-f614-4337-ac4d-950f6cc5b0ee`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get ACH Fees" (id `b400bd0a-797b-4977-8693-e6530bd8b29b`)

### Google Sheets

- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `update`, tab `={{ $('Spreadsheet Name').first().json.spreadsheet_name }}` — node "Update row in sheet" (id `109da278-109d-4ed1-9098-49f054d6b0a8`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `?`, tab `={{ $json.spreadsheet_name }}` — node "Get PCI non-compliance charges" (id `6457de1f-a78c-4702-a42e-0010c0666349`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `update`, tab `={{ $('Spreadsheet Name1').first().json.spreadsheet_name }}-ALL-AGGREGATE` — node "Update row in sheet1" (id `b377b72b-f614-4337-ac4d-950f6cc5b0ee`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $json.spreadsheet_name }}-ALL-AGGREGATE` — node "Get ACH Fees" (id `b400bd0a-797b-4977-8693-e6530bd8b29b`)

### Sub-workflows (Execute Workflow calls)

- [[billing-check-transaction-status|Billing - Check transaction status]] (n8n_id `0UmMSBevXhNQuBgD`) — node "Call 'Billing - Check transaction status'" (id `8a02cf38-7187-4ccd-92c1-4c4de91cdfb1`)
- [[billing-check-transaction-status|Billing - Check transaction status]] (n8n_id `0UmMSBevXhNQuBgD`) — node "Call 'Billing - Check transaction status'1" (id `c16621a6-e3e5-499f-9d48-be0d48f22805`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
