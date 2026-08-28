---
n8n_id: "yN8AkfJoZqN2ft9i"
instance: v1
name: "OpsInternalBot - Disputes"
status: archived
last_modified: 2026-04-20T16:32:27.878Z
tags: []
fingerprint: "84bc5abb9e7b52aff08d4eafaaf74bd68f8dd99a22d172fc50033cc9b46ebd19"
auto_generated_at: 2026-08-28T21:59:10Z
---

<!-- auto:start -->

# OpsInternalBot - Disputes

## Summary

- **Status:** archived
- **n8n ID:** `yN8AkfJoZqN2ft9i`
- **Nodes:** 51
- **Last modified:** 2026-04-20T16:32:27.878Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `8c975101-bb0b-476f-bf3e-1926c94c523d`)
- **schedule** — node "Schedule Trigger" (id `b27fe67f-5652-41ee-b85e-1d2d1b1593c5`) — `daily at 12:00`
- **execute-workflow** — node "When Executed by Another Workflow" (id `e38cdd49-e668-4ab3-bcae-0d2f5a51735d`)

## Depends on

### Credentials

- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message1" (id `20a707c1-e9d7-4dd1-9d87-98250857c1d5`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `5bb6f37d-c818-4d1e-b8d0-00637cc53140`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message2" (id `a8a827d2-9340-4fb4-a9f7-602d8d43c44a`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `b639b563-13d6-4237-ad05-40f5c9a8c228`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message" (id `e60090dc-dba6-49a7-b59a-2ab2cd6347a8`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `b639b563-13d6-4237-ad05-40f5c9a8c228`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-6|anthropic / claude-sonnet-4-6]] — node "Anthropic Chat Model" (id `5bb6f37d-c818-4d1e-b8d0-00637cc53140`)

### Data tables (n8n)

- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)2" (id `109c1903-42ac-4ca7-bac2-5f783e3850ba`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)5" (id `5cbbfac2-f660-4cbb-b568-1d2a6893b3a9`)
- [[../resources/data-tables/nkrufqkkpszwq07b|Dispute - Awaiting Processor Response]] (id `NkRUfQkkpsZWq07b`) — op `get` — node "Get row(s)3" (id `72c1e71c-2621-4ea0-9a4e-4da9fcb28815`)
- [[../resources/data-tables/da1d723wdyigobvw|Dispute - Merchant Responses]] (id `DA1d723WDyIGoBVW`) — op `get` — node "Get row(s)4" (id `774edbc0-53bc-421f-8ff6-9acd16514114`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)1" (id `776b9c15-76c1-4bec-b654-5a26adb0038b`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get row(s)" (id `ede24c4a-913c-4bc2-9af8-86d7a999e5ac`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Send a message1" (id `20a707c1-e9d7-4dd1-9d87-98250857c1d5`)
- *(dynamic channel)* — op `channel` — node "Send a message2" (id `a8a827d2-9340-4fb4-a9f7-602d8d43c44a`)
- [[../resources/slack-channels/c08r8h75n15|C08R8H75N15]] (id `C08R8H75N15`) — op `channel` — node "Send a message" (id `e60090dc-dba6-49a7-b59a-2ab2cd6347a8`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
