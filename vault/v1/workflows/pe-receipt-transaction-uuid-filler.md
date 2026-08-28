---
n8n_id: "PvDSqgelSeNW6t3E"
instance: v1
name: "PE_Receipt_Transaction_UUID_Filler"
status: inactive
last_modified: 2025-12-17T19:19:27.580Z
tags: []
fingerprint: "f216129154843f0e27d349400fd805d5282857fd2ee9c6d1b991c87ebb297aa4"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PE_Receipt_Transaction_UUID_Filler

## Summary

- **Status:** inactive
- **n8n ID:** `PvDSqgelSeNW6t3E`
- **Nodes:** 4
- **Last modified:** 2025-12-17T19:19:27.580Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `f46c4038-7873-46d9-a7eb-0d087b3c9c77`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `38ca7009-f04a-4b80-af79-4bfbc9648367`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `cee48236-ddf0-4ba4-8a3c-4d892fbd0208`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `edb2f1f4-70e4-459f-a810-463eabaa76cc`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `edb2f1f4-70e4-459f-a810-463eabaa76cc`)

### Google Sheets

- [[../resources/google-sheets/1v4m2pbw-u-oqogetc-vxhnjhvlfy483q3rzijyeyjoe|pe_receipt]] (id `1v4m2pBw-U_oqogEtc-VXHNJhVlfY483Q3rZIJyEYJOE`) — op `?`, tab `Sheet1` — node "Get row(s) in sheet" (id `38ca7009-f04a-4b80-af79-4bfbc9648367`)
- [[../resources/google-sheets/1v4m2pbw-u-oqogetc-vxhnjhvlfy483q3rzijyeyjoe|pe_receipt]] (id `1v4m2pBw-U_oqogEtc-VXHNJhVlfY483Q3rZIJyEYJOE`) — op `update`, tab `Sheet1` — node "Update row in sheet" (id `cee48236-ddf0-4ba4-8a3c-4d892fbd0208`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
