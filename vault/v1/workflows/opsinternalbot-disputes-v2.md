---
n8n_id: "g7RlfTkDXNesywCu"
instance: v1
name: "OpsInternalBot - Disputes v2"
status: inactive
last_modified: 2026-05-08T16:33:39.482Z
tags: []
fingerprint: "00b55f1de5075137eba614cf1ddbf9cd3717eb6f0d296ccb21ae9756ff6660a7"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# OpsInternalBot - Disputes v2

## Summary

- **Status:** inactive
- **n8n ID:** `g7RlfTkDXNesywCu`
- **Nodes:** 32
- **Last modified:** 2026-05-08T16:33:39.482Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `b1f41b4c-c581-4456-bfe6-792a5456dfd4`) — `daily at 12:00`
- **execute-workflow** — node "When Executed by Another Workflow" (id `b252e378-bd57-43d3-a224-770af38d2bd4`)
- **manual** — node "When clicking ‘Execute workflow’" (id `f9d2efef-6b80-4edc-9e48-d82d7d7e012a`)

## Depends on

### Credentials

- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message3" (id `1fcda0b8-c69a-4ded-9efb-8460699f3bac`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message" (id `30334947-46bb-4365-affd-904e0d80f495`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `52ec5d27-9c8e-458e-86e0-82c30706a31c`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message2" (id `580344cc-7e1d-4d71-8aaa-89d3eaf9898a`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message1" (id `59c20ed3-4e34-43ac-8f5c-8e5126861d0f`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get transactions for period of time" (id `cc1c5960-cb06-4219-8913-f9a69d1f6e99`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get transactions for period of time" (id `cc1c5960-cb06-4219-8913-f9a69d1f6e99`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-6|anthropic / claude-sonnet-4-6]] — node "Anthropic Chat Model" (id `52ec5d27-9c8e-458e-86e0-82c30706a31c`)

### Data tables (n8n)

- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Find transaction attachments" (id `e9aa2313-3520-49f2-9f38-f3fd5b514db6`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Send a message3" (id `1fcda0b8-c69a-4ded-9efb-8460699f3bac`)
- [[../resources/slack-channels/c08r8h75n15|C08R8H75N15]] (id `C08R8H75N15`) — op `channel` — node "Send a message" (id `30334947-46bb-4365-affd-904e0d80f495`)
- *(dynamic channel)* — op `channel` — node "Send a message2" (id `580344cc-7e1d-4d71-8aaa-89d3eaf9898a`)
- *(dynamic channel)* — op `channel` — node "Send a message1" (id `59c20ed3-4e34-43ac-8f5c-8e5126861d0f`)

### Sub-workflows (Execute Workflow calls)

- [[dispute-compose-report|Dispute - Compose report]] (n8n_id `NWv022t59k7EtTFo`) — node "Call 'Dispute - Compose report'" (id `ba72beef-b168-49cd-a5d7-e94359de955d`)
- [[dispute-create-report|Dispute - Create Report]] (n8n_id `IM3wk08pLLTXawd2`) — node "Call 'Dispute - Create Report'" (id `efce57bd-1c6e-4b2c-9cf0-ad60d70532b1`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
