---
n8n_id: "jXP8bYpE3EX9hm9L"
name: "Platform Fee monitoring"
status: inactive
last_modified: 2026-04-30T19:45:44.538Z
tags: []
fingerprint: "448ca0388203de02ac62264c310d57d6515f97204ab657712bc2109b04b0e0ca"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Platform Fee monitoring

## Summary

- **Status:** inactive
- **n8n ID:** `jXP8bYpE3EX9hm9L`
- **Nodes:** 30
- **Last modified:** 2026-04-30T19:45:44.538Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `92cede2d-6759-4abf-87d2-cdac39145c93`) — `every 1 hour(s)`
- **manual** — node "When clicking ‘Execute workflow’" (id `cb686405-038b-4820-a9f8-74ad19a134df`)

## Depends on

### Credentials

- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model3" (id `59ed7737-76c0-4849-9631-45fb52d2f655`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "DB Fee Schedules" (id `6401d833-4de9-4ca8-9a92-45d9f7ac2e81`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model2" (id `ed64741c-4041-415b-aa8d-782e8a437beb`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "DB Fee Schedules" (id `6401d833-4de9-4ca8-9a92-45d9f7ac2e81`)

### LLM models

- [[../resources/llm-models/anthropic-claude-opus-4-5-20251101|anthropic / claude-opus-4-5-20251101]] — node "Anthropic Chat Model3" (id `59ed7737-76c0-4849-9631-45fb52d2f655`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-6|anthropic / claude-sonnet-4-6]] — node "Anthropic Chat Model2" (id `ed64741c-4041-415b-aa8d-782e8a437beb`)

### Data tables (n8n)

- [[../resources/data-tables/xo77zzdfgtrmg1ur|Merchant Fee Schedules]] (id `Xo77ZZdFGtrmG1Ur`) — op `rowNotExists` — node "If row does not exist" (id `12a14532-5a56-456e-abc0-6cbfcbd50890`)
- [[../resources/data-tables/xo77zzdfgtrmg1ur|Merchant Fee Schedules]] (id `Xo77ZZdFGtrmG1Ur`) — op `upsert` — node "Upsert row(s)" (id `f6429c34-dab0-48f1-b898-d4c837e12e17`)

### Sub-workflows (Execute Workflow calls)

- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `1cd30bd0-dbf0-4986-8708-4fdefd87491d`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Send base message" (id `f892c871-5be7-4688-b416-581079bb9b40`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
