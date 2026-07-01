---
n8n_id: "Zbodr3mJ822pD7nB"
name: "Billing System - Get merchant ACH transactions"
status: inactive
last_modified: 2026-05-27T21:06:32.450Z
tags: []
fingerprint: "29a00a63fe2bd12cf3c5570a2993233f3f99ece1b0a986401840fae46b8083c6"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Billing System - Get merchant ACH transactions

## Summary

- **Status:** inactive
- **n8n ID:** `Zbodr3mJ822pD7nB`
- **Nodes:** 13
- **Last modified:** 2026-05-27T21:06:32.450Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `8c70af4d-d357-4c76-84c2-611839aae99a`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Merchant Aggregated Data" (id `17d0fefc-1b69-4ddd-984f-faa9073a911a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Merchant Transactions" (id `78fa450a-ff70-4df9-a0c8-754d30aec28e`)

### Google Sheets

- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $('Entry').item.json.period }}-ALL-AGGREGATE` — node "Get Merchant Aggregated Data" (id `17d0fefc-1b69-4ddd-984f-faa9073a911a`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $('Entry').first().json.period }}-ALL` — node "Get Merchant Transactions" (id `78fa450a-ff70-4df9-a0c8-754d30aec28e`)

## Used by (workflows)

- [[billing-system-generate-invoices-for-billing-period|Billing System - Generate Invoices for Billing Period]] — node "Call 'Billing System - Get merchant platform fees'1" (id `3615be83-de96-4c3e-94f8-aae565fafae4`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
