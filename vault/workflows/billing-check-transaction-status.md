---
n8n_id: "0UmMSBevXhNQuBgD"
name: "Billing - Check transaction status"
status: inactive
last_modified: 2026-04-13T18:58:30.507Z
tags: []
fingerprint: "6b236ec167a72344d3db843721ea15a61bb381939815dec01a38abbdde2232a2"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Billing - Check transaction status

## Summary

- **Status:** inactive
- **n8n ID:** `0UmMSBevXhNQuBgD`
- **Nodes:** 6
- **Last modified:** 2026-04-13T18:58:30.507Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `0abd3aba-dea3-41df-b397-21a0192120c7`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `ecf2ef39-9a59-4d42-8b23-70170ce24755`)

## Depends on

### Credentials

- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Execute a SQL query" (id `a6bd0681-5f9a-4f66-a26a-dbcd5eb8d31c`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "HTTP Request" (id `f9cfd66c-8e6a-43d3-a58e-00f381c4346f`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/merchant/b860f8af-11e9-4146-99b8-a9d75624c0fd/transaction/{{ $json.payment_id }}` — node "HTTP Request" (id `f9cfd66c-8e6a-43d3-a58e-00f381c4346f`)

### Databases

- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Execute a SQL query" (id `a6bd0681-5f9a-4f66-a26a-dbcd5eb8d31c`)

## Used by (workflows)

- [[check-pci-ach-transaction-status|Check PCI/ACH Transaction Status]] — node "Call 'Billing - Check transaction status'" (id `8a02cf38-7187-4ccd-92c1-4c4de91cdfb1`)
- [[check-pci-ach-transaction-status|Check PCI/ACH Transaction Status]] — node "Call 'Billing - Check transaction status'1" (id `c16621a6-e3e5-499f-9d48-be0d48f22805`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
