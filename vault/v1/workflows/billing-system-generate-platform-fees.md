---
n8n_id: "EwkLygWj3EmYzk3t"
name: "Billing System - Generate Platform Fees"
status: inactive
last_modified: 2026-06-24T19:22:55.502Z
tags: []
fingerprint: "f19c935389e27c6d5b35b76cffeb05796f4bdffef3b9781158aa6fd9cb5b0658"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Billing System - Generate Platform Fees

## Summary

- **Status:** inactive
- **n8n ID:** `EwkLygWj3EmYzk3t`
- **Nodes:** 32
- **Last modified:** 2026-06-24T19:22:55.502Z

## Triggers

- **schedule** — node "ICQual Ingestion Schedule" (id `0ccf7907-6a87-4065-a1ed-bc70cbf6f77b`) — `daily at 8:00`
- **execute-workflow** — node "When Called by Orchestrator" (id `n-exectrigger`)
- **manual** — node "Manual Trigger" (id `n-manual`)
- **webhook** — node "Webhook" (id `n-webhook`) — POST `njord/api/merchant-direct-billing-statement`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Find Period Folder" (id `073b206a-3afc-484e-8fee-12c66a7cdf20`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Find Master Spreadsheet" (id `581d2859-815e-4a88-8782-7c5966342909`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Read ICQual Sheet" (id `9761e1a1-f079-4f2d-8f93-df4bfc440995`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Find Residuals Root Folder" (id `cf17158f-7232-4498-aee7-a816bc0c239a`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Fetch Merchant + Fee Schedule" (id `n-fetchmerch`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Webhook" (id `n-webhook`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Fetch Merchant + Fee Schedule" (id `n-fetchmerch`)

### Google Sheets

- *(dynamic spreadsheet)* — op `?`, tab `MS0PFORM ICQualReport tab` — node "Read ICQual Sheet" (id `9761e1a1-f079-4f2d-8f93-df4bfc440995`)

### Data tables (n8n)

- [[../resources/data-tables/pz9zqssjshkjnyb9|Billing - Invoices]] (id `pz9ZQssJShkJNYb9`) — op `?` — node "Write Statement Record" (id `007a6bcb-d68d-4beb-bf72-a003dd9ae32b`)
- [[../resources/data-tables/tozssnhfl1zrvv7r|Elavon - ICQual Fees]] (id `tOzssNhfl1ZRvV7R`) — op `get` — node "Check Existing Ingestion" (id `2968c8c7-07f2-4fb6-a03b-d7a5fed80da4`)
- [[../resources/data-tables/tozssnhfl1zrvv7r|Elavon - ICQual Fees]] (id `tOzssNhfl1ZRvV7R`) — op `get` — node "Fetch ICQual Rows" (id `bbadc15f-3b5e-4602-97f9-5733ca5dfe78`)
- [[../resources/data-tables/tozssnhfl1zrvv7r|Elavon - ICQual Fees]] (id `tOzssNhfl1ZRvV7R`) — op `?` — node "Write ICQual to Data Table" (id `dda77c99-154b-4021-ab16-c9b545858f34`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
