---
n8n_id: "OaSrs8Ux3bG8PdKj"
instance: v1
name: "OpsInternalBot - Disputes [Backup original]"
status: inactive
last_modified: 2026-05-08T16:13:50.160Z
tags: []
fingerprint: "a2ab62f84b6428040a70a4795b8f40a63ab6945ae53380de4d57f0e386942d13"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# OpsInternalBot - Disputes [Backup original]

## Summary

- **Status:** inactive
- **n8n ID:** `OaSrs8Ux3bG8PdKj`
- **Nodes:** 115
- **Last modified:** 2026-05-08T16:13:50.160Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `6b0fb7ac-e552-4253-9b14-c34d91113a84`)
- **schedule** — node "Schedule Trigger" (id `78f04c04-2abc-4c98-a47c-ce28a715305c`) — `daily at 12:00`
- **execute-workflow** — node "When Executed by Another Workflow" (id `81b0c8ed-3659-4c43-b91b-3fa348eb8856`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get transactions for period of time" (id `03383050-1f67-4bc2-9ce8-0a51cc95523c`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message" (id `29509fec-0c7e-42c7-abe5-33d599b9243a`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message1" (id `82a54df6-842a-4c9f-9ef5-2185cef5b667`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message3" (id `a227f6fd-053b-42aa-bf0c-2d1b32c1f8a4`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message2" (id `a511b8c4-5422-4aab-b5dd-dabaa3ec3804`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `b1612ee6-17cd-48e3-94a8-b0d1fc4dce56`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query1" (id `b47d8026-46eb-41c5-a398-482dfa8d6c5e`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `de72c71c-29c4-4135-b432-662d3272a4a7`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get transactions for period of time1" (id `dec5636c-acaf-44f6-a39d-0f2ae469d632`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get transactions for period of time" (id `03383050-1f67-4bc2-9ce8-0a51cc95523c`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `b1612ee6-17cd-48e3-94a8-b0d1fc4dce56`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query1" (id `b47d8026-46eb-41c5-a398-482dfa8d6c5e`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get transactions for period of time1" (id `dec5636c-acaf-44f6-a39d-0f2ae469d632`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-6|anthropic / claude-sonnet-4-6]] — node "Anthropic Chat Model" (id `de72c71c-29c4-4135-b432-662d3272a4a7`)

### Data tables (n8n)

- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)5" (id `0d7443a5-cdc8-4673-b77e-dc326fb7617d`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)1" (id `1830a491-988a-4ee4-b509-8c24a83eaaa4`)
- [[../resources/data-tables/nkrufqkkpszwq07b|Dispute - Awaiting Processor Response]] (id `NkRUfQkkpsZWq07b`) — op `get` — node "Get row(s)3" (id `375f2cfb-9188-4cd0-9d77-e4d8920a741c`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)" (id `3b2f6b6f-262d-4829-bbb5-89559ef96c74`)
- [[../resources/data-tables/da1d723wdyigobvw|Dispute - Merchant Responses]] (id `DA1d723WDyIGoBVW`) — op `get` — node "Get row(s)4" (id `a1d668f4-6dbd-4763-b6fc-33bf29dd827e`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Find transaction attachments" (id `cc107062-df82-4dfa-966b-89f8e4a4a5e7`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `update` — node "Update row(s)" (id `dd6bc462-1aee-4877-964c-eb95eb333371`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)2" (id `e517b182-086c-435a-bf6b-fe483537b321`)

### Slack channels

- [[../resources/slack-channels/c08r8h75n15|C08R8H75N15]] (id `C08R8H75N15`) — op `channel` — node "Send a message" (id `29509fec-0c7e-42c7-abe5-33d599b9243a`)
- *(dynamic channel)* — op `channel` — node "Send a message1" (id `82a54df6-842a-4c9f-9ef5-2185cef5b667`)
- *(dynamic channel)* — op `channel` — node "Send a message3" (id `a227f6fd-053b-42aa-bf0c-2d1b32c1f8a4`)
- *(dynamic channel)* — op `channel` — node "Send a message2" (id `a511b8c4-5422-4aab-b5dd-dabaa3ec3804`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
