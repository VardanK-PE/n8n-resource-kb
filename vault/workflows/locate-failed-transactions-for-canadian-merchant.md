---
n8n_id: "2ROy2xewAu0IgoBw"
name: "Locate failed transactions for Canadian merchant"
status: inactive
last_modified: 2026-04-14T18:37:17.591Z
tags: []
fingerprint: "9b2c588de961dcb8de0dfb83c2c79347c2d9d0337dad65a27bfc3b0cddfa4610"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Locate failed transactions for Canadian merchant

## Summary

- **Status:** inactive
- **n8n ID:** `2ROy2xewAu0IgoBw`
- **Nodes:** 25
- **Last modified:** 2026-04-14T18:37:17.591Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `fe25e08b-0789-43ef-a091-9a63e911996f`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet3" (id `5f23c6e6-940f-4bbe-b348-ea3e26b1c735`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `676b557e-1194-451f-a6f3-eee8940e693d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `d9c7cf2e-a419-4252-94d9-604a49bd605b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet1" (id `dfbf6799-7e63-4403-af54-36395c7476af`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `eaedc36e-46a3-406c-9464-a5447a57acae`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet2" (id `fa104d18-ab47-47b2-a7f3-4798f0fadab1`)

### Google Sheets

- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.month }}` — node "Get row(s) in sheet3" (id `5f23c6e6-940f-4bbe-b348-ea3e26b1c735`)
- [[../resources/google-sheets/17bpppbtv5qgjkqgcddyctudpn5h4xoiwzrgyuagusw0|PCI non compliant merchants]] (id `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`) — op `?`, tab `Error Log` — node "Get row(s) in sheet" (id `676b557e-1194-451f-a6f3-eee8940e693d`)
- *(dynamic spreadsheet)* — op `?`, tab `={{ $json.month }}` — node "Get row(s) in sheet1" (id `d9c7cf2e-a419-4252-94d9-604a49bd605b`)
- [[../resources/google-sheets/1ipuxx2l-6equ2ksh3ggv17upwrfsgetzc3kucurmyz4|Canadian Merchants - failed transactions]] (id `1iPUxX2L-6equ2ksh3GGv17upwrfSGEtzC3kucUrmyZ4`) — op `append`, tab `Combined spreadsheet` — node "Append row in sheet1" (id `dfbf6799-7e63-4403-af54-36395c7476af`)
- [[../resources/google-sheets/1ipuxx2l-6equ2ksh3ggv17upwrfsgetzc3kucurmyz4|Canadian Merchants - failed transactions]] (id `1iPUxX2L-6equ2ksh3GGv17upwrfSGEtzC3kucUrmyZ4`) — op `append`, tab `Combined spreadsheet` — node "Append row in sheet" (id `eaedc36e-46a3-406c-9464-a5447a57acae`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $json.month }}-ALL-AGGREGATE` — node "Get row(s) in sheet2" (id `fa104d18-ab47-47b2-a7f3-4798f0fadab1`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
