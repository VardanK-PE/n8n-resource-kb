---
n8n_id: "VwGVEgcKjbaXKgU7"
name: "Hearth Merchant CC and ACH limits (Daily update)"
status: active
last_modified: 2025-10-31T19:33:21.898Z
tags: []
fingerprint: "c0a1511e08f4e8bd5abeeff1e9fe7165bccc6fc013574804e8bb26c76f654734"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Hearth Merchant CC and ACH limits (Daily update)

## Summary

- **Status:** active
- **n8n ID:** `VwGVEgcKjbaXKgU7`
- **Nodes:** 8
- **Last modified:** 2025-10-31T19:33:21.898Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `c7147d3d-091b-4b97-969d-0dd5fd364352`) — `daily at 6:00`
- **manual** — node "When clicking ‘Execute workflow’" (id `ed877285-a0af-42ca-bf18-d18d2803b580`)

## Depends on

### Credentials

- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Execute a SQL query" (id `6cfe49aa-1dde-434f-b1c9-ac6e767269b8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Clear sheet" (id `bbdd2746-f735-4d12-9ebd-d6152708204e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `f4d03788-0886-499d-8c89-d28ead84b20d`)

### Databases

- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Execute a SQL query" (id `6cfe49aa-1dde-434f-b1c9-ac6e767269b8`)

### Google Sheets

- [[../resources/google-sheets/12sbgqkcblsroqy3uksgjw1g-gj-8zswvsadajwgcwo|Hearth Merchants - CC and ACH limits]] (id `12sbGqKcBLSrOqy3ukSgjW1G-gJ-_8zswVsaDajwGCwo`) — op `clear`, tab `Hearth Merchants` — node "Clear sheet" (id `bbdd2746-f735-4d12-9ebd-d6152708204e`)
- [[../resources/google-sheets/12sbgqkcblsroqy3uksgjw1g-gj-8zswvsadajwgcwo|Hearth Merchants - CC and ACH limits]] (id `12sbGqKcBLSrOqy3ukSgjW1G-gJ-_8zswVsaDajwGCwo`) — op `appendOrUpdate`, tab `Hearth Merchants` — node "Append or update row in sheet" (id `f4d03788-0886-499d-8c89-d28ead84b20d`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
