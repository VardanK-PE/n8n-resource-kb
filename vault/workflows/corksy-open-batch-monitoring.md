---
n8n_id: "llmWN5owWFDM40az"
name: "Corksy open batch monitoring"
status: inactive
last_modified: 2026-05-05T19:25:42.417Z
tags: []
fingerprint: "f570d1bf0a56e14a5f3fd13a8cc9152817bee91f76327f3503dadf7dd05510e9"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Corksy open batch monitoring

## Summary

- **Status:** inactive
- **n8n ID:** `llmWN5owWFDM40az`
- **Nodes:** 13
- **Last modified:** 2026-05-05T19:25:42.417Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `d06cf550-2b1f-4371-9d1c-05d18bfb0825`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `5f7419ec-a277-4ad2-bc6a-8ab1657c6ce9`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `5f7419ec-a277-4ad2-bc6a-8ab1657c6ce9`)

### Data tables (n8n)

- [[../resources/data-tables/eyflj97t1yo74igu|Corksy - Open Batch transactions]] (id `EyFLJ97T1YO74iGu`) — op `?` — node "Insert row" (id `5f2caff2-3833-4a39-b2b9-338d03735a3f`)
- [[../resources/data-tables/eyflj97t1yo74igu|Corksy - Open Batch transactions]] (id `EyFLJ97T1YO74iGu`) — op `update` — node "Update row(s)" (id `774f4e44-1b31-4bec-91fc-ba9c5a37b0fe`)
- [[../resources/data-tables/eyflj97t1yo74igu|Corksy - Open Batch transactions]] (id `EyFLJ97T1YO74iGu`) — op `get` — node "Get row(s)" (id `7a8e2d56-367d-4d40-aa23-bf981683f2ad`)
- [[../resources/data-tables/eyflj97t1yo74igu|Corksy - Open Batch transactions]] (id `EyFLJ97T1YO74iGu`) — op `rowNotExists` — node "If row does not exist" (id `c3a1757e-7462-45ac-a317-39e8fe1537af`)

### Sub-workflows (Execute Workflow calls)

- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `56c7f65b-79f2-4b97-8c67-e24640789d55`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `78cf89d0-bf1b-455f-b0cb-e2ba9caeda39`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
