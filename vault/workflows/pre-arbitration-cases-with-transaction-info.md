---
n8n_id: "UHVH2fElpy3vcD4t"
name: "Pre-Arbitration cases with transaction info"
status: inactive
last_modified: 2026-01-15T18:33:10.259Z
tags: []
fingerprint: "df64f4cf738da61980f9f35b0a03dea159ad572d83c14b58aa1b99236633ec56"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Pre-Arbitration cases with transaction info

## Summary

- **Status:** inactive
- **n8n ID:** `UHVH2fElpy3vcD4t`
- **Nodes:** 8
- **Last modified:** 2026-01-15T18:33:10.259Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `da98cdfd-f811-454b-907b-98cc8132b99b`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Clear sheet" (id `09c9e5fd-6df3-46f4-886d-cbe7658b2c14`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `1089b758-4e3d-4621-8b19-f723daa05943`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `b710bcd2-9bb8-482f-a6b1-79f8ebe6c520`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `d3849363-525e-4f0d-916d-69a0d2aff1bf`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `1089b758-4e3d-4621-8b19-f723daa05943`)

### Google Sheets

- [[../resources/google-sheets/1jrwnojq-y2vwyjzn8-btqtmjdm8ntlzekdvlfkikstm|Pre-Arbitration Cases]] (id `1jRWnOJq_y2vWyJzn8_btqTmjDm8ntLZEKDvlFkIkStM`) — op `clear`, tab `Sheet1` — node "Clear sheet" (id `09c9e5fd-6df3-46f4-886d-cbe7658b2c14`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Get row(s) in sheet" (id `b710bcd2-9bb8-482f-a6b1-79f8ebe6c520`)
- [[../resources/google-sheets/1jrwnojq-y2vwyjzn8-btqtmjdm8ntlzekdvlfkikstm|Pre-Arbitration Cases]] (id `1jRWnOJq_y2vWyJzn8_btqTmjDm8ntLZEKDvlFkIkStM`) — op `appendOrUpdate`, tab `Sheet1` — node "Append or update row in sheet" (id `d3849363-525e-4f0d-916d-69a0d2aff1bf`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
