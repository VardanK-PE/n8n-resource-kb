---
n8n_id: "2CFKEpFtHI2Xuvx5"
instance: v1
name: "Savings Analysis"
status: inactive
last_modified: 2025-11-19T03:34:47.694Z
tags: []
fingerprint: "9fbef11d41079461f8e9aca50d51b296b81c6be6e121a13be1b8878b527c1698"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Savings Analysis

## Summary

- **Status:** inactive
- **n8n ID:** `2CFKEpFtHI2Xuvx5`
- **Nodes:** 6
- **Last modified:** 2025-11-19T03:34:47.694Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `f168c349-2d90-428d-ba52-e353ff4aaad9`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `4047de90-e2a0-4e58-a668-b971fc50597c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `a79af010-1799-45b3-a5fa-ae7e2ac43878`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `f4554a9f-3cb2-494e-b2c1-ef81f460fd23`)

### Google Sheets

- [[../resources/google-sheets/10lvzmbb3fqsqvpn50cfjjfec6bpwedlkra7j2xdywea|ST Statements Analysis 2024-08-15]] (id `10LvzmBB3FqSQVPN50cfJjFEC6BPwEDlkRA7j2xDYWeA`) — op `?`, tab `batch_1` — node "Get row(s) in sheet1" (id `4047de90-e2a0-4e58-a668-b971fc50597c`)
- [[../resources/google-sheets/1gy5ppl-xnwdkkecl4pbvu1esr5wejrlqfnwfta5fe5q|ST Payments Review 2025]] (id `1GY5PpL_XnwDkkECl4PBVU1EsR5wEjrLQfNwfTa5Fe5Q`) — op `?`, tab `TLReport_MerchantInterchangeDetail_MID2` — node "Get row(s) in sheet" (id `a79af010-1799-45b3-a5fa-ae7e2ac43878`)
- [[../resources/google-sheets/1gy5ppl-xnwdkkecl4pbvu1esr5wejrlqfnwfta5fe5q|ST Payments Review 2025]] (id `1GY5PpL_XnwDkkECl4PBVU1EsR5wEjrLQfNwfTa5Fe5Q`) — op `update`, tab `TLReport_MerchantInterchangeDetail_MID2` — node "Update row in sheet" (id `f4554a9f-3cb2-494e-b2c1-ef81f460fd23`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
