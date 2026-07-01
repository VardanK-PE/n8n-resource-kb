---
n8n_id: "wyv0NsWkA7UX7sUC"
name: "Converge MCP Server"
status: active
last_modified: 2025-11-06T14:16:49.313Z
tags: []
fingerprint: "1890a0221ee6b50035fd806ff68a4f865dd257923173ff010b30decba16d7b43"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Converge MCP Server

## Summary

- **Status:** active
- **n8n ID:** `wyv0NsWkA7UX7sUC`
- **Nodes:** 3
- **Last modified:** 2025-11-06T14:16:49.313Z

## Triggers

- **other** — node "MCP Server Trigger" (id `d40b2f22-53c1-477c-ab39-5a4a3d0e65a1`) — GET `21302e18-4f77-4674-a325-42e45b391284`

## Depends on

### Credentials

- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send a message in Gmail" (id `b0bdb48c-208e-4632-b5f3-ef7fc47a3685`)

### HTTP URLs

- [[../resources/http-urls/api-demo-convergepay-com|api.demo.convergepay.com]] — `POST https://api.demo.convergepay.com/VirtualMerchantDemo/processxml.do` — node "Elavon_Converge Transactions By Date Range" (id `36db7cdc-1d5e-423b-80fa-b0710c83313d`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
