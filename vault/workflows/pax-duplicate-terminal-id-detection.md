---
n8n_id: "iIwj8usNfzTMAWlc"
name: "PAX: Duplicate Terminal ID detection"
status: inactive
last_modified: 2026-05-29T16:59:00.912Z
tags: []
fingerprint: "5f691e78c193ef37922f436ae7df1efaffa560edf4237e4ba85f8b1acc14a5b9"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PAX: Duplicate Terminal ID detection

## Summary

- **Status:** inactive
- **n8n ID:** `iIwj8usNfzTMAWlc`
- **Nodes:** 31
- **Last modified:** 2026-05-29T16:59:00.912Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `036266dc-5376-4ced-a44c-cff068bdfb45`) — `daily at 12:00`
- **manual** — node "When clicking ‘Execute workflow’" (id `32d953dc-6fb8-4a93-a40d-33c724058b85`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `22d3f7cc-f7ff-4e51-ae4c-4ef3d82501bf`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query3" (id `358923f0-5e6c-4bf1-bdb2-3779d178746e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `7f5b6877-9821-4e23-833e-5dcb670ca707`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `ae7fe56b-81b3-4474-b82a-aed38cb7305c`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `c9e2c3ca-ac96-469b-a3fb-473c480bdf5e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `cdb6b591-1e96-4dac-8d58-41eb8529ba8e`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query1" (id `f4d3bd2c-26c7-436a-82a2-33e4a2e47864`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query3" (id `358923f0-5e6c-4bf1-bdb2-3779d178746e`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `c9e2c3ca-ac96-469b-a3fb-473c480bdf5e`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query1" (id `f4d3bd2c-26c7-436a-82a2-33e4a2e47864`)

### Google Sheets

- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `?`, tab `Devices` — node "Get row(s) in sheet1" (id `22d3f7cc-f7ff-4e51-ae4c-4ef3d82501bf`)
- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `?`, tab `Devices` — node "Get row(s) in sheet" (id `7f5b6877-9821-4e23-833e-5dcb670ca707`)

### Slack channels

- [[../resources/slack-channels/c09jr6ph8tx|n8n-sandbox-of-doom]] (id `C09JR6PH8TX`) — op `channel` — node "Send a message1" (id `ae7fe56b-81b3-4474-b82a-aed38cb7305c`)
- [[../resources/slack-channels/c09swt8k6qm|corksy-payengine-alerts]] (id `C09SWT8K6QM`) — op `channel` — node "Send a message" (id `cdb6b591-1e96-4dac-8d58-41eb8529ba8e`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
