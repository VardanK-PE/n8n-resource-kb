---
n8n_id: "ru4K4o5884D9AiEj"
instance: v1
name: "Global open batch monitoring copy"
status: active
last_modified: 2026-08-12T15:41:21.876Z
tags: []
fingerprint: "5a847950730b94c1fc66a9fc42a00e67750db724d4faa2a9450d406a9390eaab"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Global open batch monitoring copy

## Summary

- **Status:** active
- **n8n ID:** `ru4K4o5884D9AiEj`
- **Nodes:** 23
- **Last modified:** 2026-08-12T15:41:21.876Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `65159094-f19a-4675-9c29-9a68f0a58c60`) — `daily at 23:55`
- **manual** — node "When clicking ‘Execute workflow’" (id `925e76a3-5ca0-4dc7-9449-fafcb352f630`)

## Depends on

### Credentials

- [[../resources/credentials/jc4f45um3ujq28gc|PF Prod Device Management Replica]] (`postgres`, id `JC4f45um3UjQ28Gc`) — node "Execute a SQL query" (id `1aa0020a-df5b-44a5-ad6b-da375b2eeeec`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Query Open Batch transactions" (id `59f40857-a20f-480e-bb1f-d6617a96a8c8`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Query Open Batch transactions2" (id `640f0661-b5b2-4bee-b2b8-93f6658acc44`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Query Open Batch transactions1" (id `c4bc3ad6-5cc4-4b32-89b1-afb76a26b1f3`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Original - Query Open Batch transactions" (id `ff777a6a-2dd1-4845-bf92-88e66fb60a17`)

### Databases

- [[../resources/databases/postgres-jc4f45um3ujq28gc|postgres (via PF Prod Device Management Replica)]] — op `executeQuery` — node "Execute a SQL query" (id `1aa0020a-df5b-44a5-ad6b-da375b2eeeec`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Query Open Batch transactions" (id `59f40857-a20f-480e-bb1f-d6617a96a8c8`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Query Open Batch transactions2" (id `640f0661-b5b2-4bee-b2b8-93f6658acc44`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Query Open Batch transactions1" (id `c4bc3ad6-5cc4-4b32-89b1-afb76a26b1f3`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Original - Query Open Batch transactions" (id `ff777a6a-2dd1-4845-bf92-88e66fb60a17`)

### Sub-workflows (Execute Workflow calls)

- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'1" (id `0ab773fc-a413-4db0-83d0-9f2b27e26567`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'1" (id `0f0ff571-2086-4e96-8e35-995e97e76c3f`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'2" (id `20716855-3e5d-490c-9d6a-1eb7bc6110b9`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'2" (id `44a06f23-2ad2-4a2d-b510-779fb3348378`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `cc14f6e1-3c48-423f-b335-898c5dcf3705`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `fb3a926c-ffbe-4c88-8828-d789deb4a066`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
