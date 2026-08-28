---
n8n_id: "EiRNXVDZkus6lf1J"
name: "Failed ACH notifications"
status: active
last_modified: 2026-05-29T19:55:14.355Z
tags: []
fingerprint: "4ed1611251b4d36b5d4a5e9ffa0db6d4951e26f1c1caa783085f4486065e7ad0"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Failed ACH notifications

## Summary

- **Status:** active
- **n8n ID:** `EiRNXVDZkus6lf1J`
- **Nodes:** 20
- **Last modified:** 2026-05-29T19:55:14.355Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `7357792e-0c98-4128-ac89-51b3e706de47`) — `every 4 hour(s)`
- **error** — node "Error Trigger" (id `75f36c76-2aa9-4b1f-86cb-dfe68c83dce6`)
- **manual** — node "When clicking ‘Execute workflow’" (id `f22b7642-73e6-459b-be40-ab0b4b8f8225`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `c855d4da-a27d-4dc3-8500-ddfcdc4f8b20`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `cc36e454-15f1-41db-b43a-e40bc9bc9929`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `c855d4da-a27d-4dc3-8500-ddfcdc4f8b20`)

### Data tables (n8n)

- [[../resources/data-tables/sngflppruyga2ymn|Failed ACH Transactions]] (id `sngFLPpruyGa2YMn`) — op `upsert` — node "Mark sent notifications" (id `83417030-1620-40fb-9669-7dc135b8f5a5`)
- [[../resources/data-tables/sngflppruyga2ymn|Failed ACH Transactions]] (id `sngFLPpruyGa2YMn`) — op `upsert` — node "Update failed transactions list" (id `92f8baf3-9451-477a-bd86-9ea2f9371a7a`)
- [[../resources/data-tables/sngflppruyga2ymn|Failed ACH Transactions]] (id `sngFLPpruyGa2YMn`) — op `get` — node "Get failed ACH transaction" (id `b55ab0ea-dbc3-43c8-b571-4d5e46b0421a`)

### Slack channels

- [[../resources/slack-channels/c09pc6hkhpy|payengine-ai-alerts]] (id `C09PC6HKHPY`) — op `channel` — node "Send a message5" (id `cc36e454-15f1-41db-b43a-e40bc9bc9929`)

### Sub-workflows (Execute Workflow calls)

- [[send-email-html|Send Email: HTML]] (n8n_id `H9qPciXCz00KxAyF`) — node "Call 'Send Email'" (id `193b21d1-a19e-4ba8-a07a-372287b8b351`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `70084f49-a6b7-4586-9546-869b91e731a1`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
