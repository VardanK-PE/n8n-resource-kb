---
n8n_id: "7Bxmbj0pKRQHzNC6"
name: "Dispute - Process Elavon attachments"
status: inactive
last_modified: 2026-06-26T17:15:20.165Z
tags: []
fingerprint: "860d80c44e1902e66918ff03f5ec24939fb3ddb40953902c305d5a57a4aa7444"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Dispute - Process Elavon attachments

## Summary

- **Status:** inactive
- **n8n ID:** `7Bxmbj0pKRQHzNC6`
- **Nodes:** 58
- **Last modified:** 2026-06-26T17:15:20.165Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `81720fbc-a6ff-49c4-a71b-506727a37817`)
- **manual** — node "When clicking ‘Execute workflow’" (id `fd16724f-5139-4629-b1d3-4b3cd16673a5`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks" (id `0ac31d66-f99d-4e5f-98c1-cc843bcba446`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request transaction data" (id `169cec85-0a1c-4df4-8044-813fb3cb0d2f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `279d870f-baad-45cc-97e9-23e604b46035`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Dispute Emails1" (id `675739f6-fdbd-457e-a0dd-ef880c109be6`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks10" (id `7679e790-bb6d-41f4-ab07-245ba693f9e2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download orphaned email file" (id `9758a5ca-b525-4e66-ab7e-acb0488ad336`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks" (id `0ac31d66-f99d-4e5f-98c1-cc843bcba446`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request transaction data" (id `169cec85-0a1c-4df4-8044-813fb3cb0d2f`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks10" (id `7679e790-bb6d-41f4-ab07-245ba693f9e2`)

### Google Sheets

- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `update`, tab `emails` — node "Update row in sheet" (id `279d870f-baad-45cc-97e9-23e604b46035`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Get Dispute Emails1" (id `675739f6-fdbd-457e-a0dd-ef880c109be6`)

### Google Drive

- *(dynamic)* — op `download` — node "Download orphaned email file" (id `9758a5ca-b525-4e66-ab7e-acb0488ad336`)

### Data tables (n8n)

- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Orphaned Email Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)4" (id `2573a89e-3481-442e-a04f-88ee91db91af`)
- [[../resources/data-tables/ge6lmhiugshxlwa3|Dispute - Shared Preferences]] (id `GE6LmHiUGSHxLWA3`) — op `get` — node "Get row(s)" (id `277ea805-5983-48ac-9a85-430b5457dae9`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Orphaned Email Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `rowNotExists` — node "If row does not exist" (id `40b474a3-0947-41e0-b82e-feeb6c234b6a`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Orphaned Email Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `upsert` — node "Upsert row(s)2" (id `466d503f-f3d7-49d5-ad20-8ecf9be01c14`)
- [[../resources/data-tables/ge6lmhiugshxlwa3|Dispute - Shared Preferences]] (id `GE6LmHiUGSHxLWA3`) — op `update` — node "Update row(s)" (id `5ffc9f13-24b4-4cf6-95fb-89e2f02007b6`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Orphaned Email Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)2" (id `8a3ae92f-cd6a-41eb-9aa6-73f028490621`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Orphaned Email Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `upsert` — node "Upsert row(s)" (id `9e5d5781-9e60-4b9e-8b0d-fe8e06b6aa20`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Orphaned Email Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `deleteRows` — node "Delete row(s)" (id `ace14950-946f-4a34-be5e-1b1bbc4be157`)
- [[../resources/data-tables/qz24nqzwcd4ofkjp|Disputes - MID overrides]] (id `QZ24NQZwcd4OFkjP`) — op `get` — node "Get row(s)5" (id `ae655553-1da2-47ea-9fa5-f0d61495cb82`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Orphaned Email Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)1" (id `b1111251-3562-4aa6-b45f-75778ebe8856`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Orphaned Email Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `upsert` — node "Upsert row(s)1" (id `bb0a1deb-8a7b-4e20-be00-73257961ef2c`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Orphaned Email Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `?` — node "Insert row" (id `c2834559-3a29-41d1-8dd8-db8f663097b8`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Orphaned Email Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)6" (id `deffa5a2-fb60-4719-a882-dd9dc9e9ac6e`)

### Sub-workflows (Execute Workflow calls)

- [[send-email-html|Send Email: HTML]] (n8n_id `H9qPciXCz00KxAyF`) — node "Call 'Send Email'" (id `246581ca-9fba-4f13-95ad-20bbba563757`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Create Base Message1" (id `82acd8fd-6cdc-4f19-a954-9acb35273502`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Email not sent notification" (id `8d78a625-b495-4603-a9cd-81690d9d02e9`)

## Used by (workflows)

- [[dispute-main-processor|Dispute - Main Processor]] — node "Call 'Dispute - Process orphaned email attachments'" (id `724f0d5d-cfd9-426d-a5bb-fa75b07c9a32`)
- [[dispute-main-processor|Dispute - Main Processor]] — node "Call 'Dispute - Process orphaned email attachments'1" (id `c2299fc3-3560-4a0f-9d3d-749a730ee9b0`)
- [[dispute-main-processor|Dispute - Main Processor]] — node "Call 'Dispute - Process orphaned email attachments'2" (id `8c6e967b-51ed-48ba-afd5-9a6975413ba7`)
- [[dispute-main-processor|Dispute - Main Processor]] — node "Call 'Dispute - Process orphaned email attachments'3" (id `b22bac98-fae0-491c-8e87-144885c5b83c`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
