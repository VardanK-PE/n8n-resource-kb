---
n8n_id: "mKFnZtwtcehhGGBx"
instance: v1
name: "Hearth - Merchants with rejected Elavon ACH but enabled Gateway"
status: inactive
last_modified: 2026-07-24T19:13:33.496Z
tags: []
fingerprint: "94afd653acb9b71ce48c75888d464c891cd504fc681d9ee19ce2268fad46d6bc"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Hearth - Merchants with rejected Elavon ACH but enabled Gateway

## Summary

- **Status:** inactive
- **n8n ID:** `mKFnZtwtcehhGGBx`
- **Nodes:** 15
- **Last modified:** 2026-07-24T19:13:33.496Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `78d92f65-f9c8-4803-ae46-d2fb2ec2c680`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `90815f51-d14e-4237-85ab-88f4e822d4ee`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Execute a SQL query" (id `e7fdb0ae-d9b5-4397-a00f-59209260ec47`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Clear sheet" (id `ea0aca98-f2eb-4690-9321-21a6795331c2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `f9079c2f-0ad6-42a5-8afd-3c94424c2a3a`)

### Databases

- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Execute a SQL query" (id `e7fdb0ae-d9b5-4397-a00f-59209260ec47`)

### Google Sheets

- [[../resources/google-sheets/14uef1aeuttfl-q1zqnwq-2-xggufbren-riren0b1dw|Hearth - Merchants marked for ACH rejection with active ACH on gateway]] (id `14UEF1AEUTtfl-q1ZqNWQ-2-XGgUFbREN-rIren0B1dw`) — op `append`, tab `Sheet1` — node "Append row in sheet" (id `90815f51-d14e-4237-85ab-88f4e822d4ee`)
- [[../resources/google-sheets/14uef1aeuttfl-q1zqnwq-2-xggufbren-riren0b1dw|Hearth - Merchants marked for ACH rejection with active ACH on gateway]] (id `14UEF1AEUTtfl-q1ZqNWQ-2-XGgUFbREN-rIren0B1dw`) — op `clear`, tab `Sheet1` — node "Clear sheet" (id `ea0aca98-f2eb-4690-9321-21a6795331c2`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `ElavonDeclinedACH` — node "Get row(s) in sheet1" (id `f9079c2f-0ad6-42a5-8afd-3c94424c2a3a`)

### Data tables (n8n)

- [[../resources/data-tables/s79t8iehgnurdtue|Elavon - Disable ACH Gateway Queue]] (id `s79T8iEHGNuRDtuE`) — op `get` — node "Get row(s)" (id `f073df9f-b479-4d5b-866a-6fb6d5989f15`)

### Sub-workflows (Execute Workflow calls)

- [[check-elavon-ach-gateway-status|Check Elavon ACH gateway status]] (n8n_id `MgUymrWWSzLhoUxF`) — node "Call 'Check Elavon ACH gateway status'1" (id `be1ead95-8974-46ad-a10c-641915277950`)
- [[check-elavon-ach-gateway-status|Check Elavon ACH gateway status]] (n8n_id `MgUymrWWSzLhoUxF`) — node "Call 'Check Elavon ACH gateway status'" (id `ff1667f4-f3ef-44d4-a962-73eb9209c453`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
