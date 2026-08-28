---
n8n_id: "YhBEB2syTygYFXO8"
instance: v1
name: "Calculate Chargeback Composite Key"
status: inactive
last_modified: 2025-11-25T19:31:33.989Z
tags: []
fingerprint: "f8749c414287e7d5002c399879d601e27c26ed49a61378b4ac16e77ed0d4d081"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Calculate Chargeback Composite Key

## Summary

- **Status:** inactive
- **n8n ID:** `YhBEB2syTygYFXO8`
- **Nodes:** 10
- **Last modified:** 2025-11-25T19:31:33.989Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `4378370f-c167-4b17-9b72-c182cec33f08`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `06c3589f-701a-473d-a225-b8c1bec5ccca`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `chargebacks` — node "Get row(s) in sheet" (id `06c3589f-701a-473d-a225-b8c1bec5ccca`)

## Used by (workflows)

- [[elavon-bi-automation-daily-monitor|Elavon BI Automation (Daily Monitor)]] — node "Execute Workflow1" (id `29e2fb4a-52f8-46c8-9df6-93e36bcfc1c9`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
