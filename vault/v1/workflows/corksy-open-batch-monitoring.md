---
n8n_id: "llmWN5owWFDM40az"
instance: v1
name: "Corksy open batch monitoring"
status: active
last_modified: 2026-07-13T18:51:44.329Z
tags: []
fingerprint: "8d01ed0362ea846055e6a55086ab4805ad667cb26a591620caab45bc9891f625"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Corksy open batch monitoring

## Summary

- **Status:** active
- **n8n ID:** `llmWN5owWFDM40az`
- **Nodes:** 13
- **Last modified:** 2026-07-13T18:51:44.329Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `94346505-267c-4883-8b15-3322e10288cf`) — `daily at 23:55`
- **manual** — node "When clicking ‘Execute workflow’" (id `d06cf550-2b1f-4371-9d1c-05d18bfb0825`)

## Depends on

### Credentials

- [[../resources/credentials/jc4f45um3ujq28gc|PF Prod Device Management Replica]] (`postgres`, id `JC4f45um3UjQ28Gc`) — node "Execute a SQL query" (id `3334eca0-4957-447a-be00-b3347d67d5cb`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Original - Query Open Batch transactions" (id `8334b83f-a5a3-49de-90c9-91c0177e123e`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Query Open Batch transactions" (id `d66b4d9a-099a-41c5-865b-c0e7214a7ea6`)

### Databases

- [[../resources/databases/postgres-jc4f45um3ujq28gc|postgres (via PF Prod Device Management Replica)]] — op `executeQuery` — node "Execute a SQL query" (id `3334eca0-4957-447a-be00-b3347d67d5cb`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Original - Query Open Batch transactions" (id `8334b83f-a5a3-49de-90c9-91c0177e123e`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Query Open Batch transactions" (id `d66b4d9a-099a-41c5-865b-c0e7214a7ea6`)

### Sub-workflows (Execute Workflow calls)

- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'1" (id `7a21fa32-7378-4419-980b-cd3513e1c39a`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'1" (id `bbcedc06-b775-4388-acdb-794fa94788e9`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
