---
n8n_id: "NSkdXVo1cjKZO7SG"
instance: v1
name: "OpsInternalBot - Disputes"
status: inactive
last_modified: 2026-05-08T18:06:49.753Z
tags: []
fingerprint: "076e107e6df807b2ac41fcb53f59fa17e1ec728705bda6836d1e788895305b0f"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# OpsInternalBot - Disputes

## Summary

- **Status:** inactive
- **n8n ID:** `NSkdXVo1cjKZO7SG`
- **Nodes:** 20
- **Last modified:** 2026-05-08T18:06:49.753Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `2f30b34e-0415-479f-93b5-9d2385f09d71`)
- **manual** — node "When clicking ‘Execute workflow’" (id `8dbe670c-570d-426e-a3d2-516a2b4b4eea`)
- **schedule** — node "Schedule Trigger" (id `c8d1d048-ebaa-438f-97a4-5f1ede578ee9`) — `daily at 12:00`

## Depends on

### Credentials

- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message2" (id `08ed9bfc-995e-4aa2-bb95-5d16701ef861`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message3" (id `8cbccd31-3e4e-48ed-87d1-9f61d49e9d03`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message1" (id `d1c321b2-1cef-418b-bc62-ca08f15b6c94`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `f22da969-46b3-45c8-b13b-57aebd02d933`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message" (id `f36e0159-0c25-4c1c-bc1c-4daa204e3767`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-6|anthropic / claude-sonnet-4-6]] — node "Anthropic Chat Model" (id `f22da969-46b3-45c8-b13b-57aebd02d933`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Send a message2" (id `08ed9bfc-995e-4aa2-bb95-5d16701ef861`)
- *(dynamic channel)* — op `channel` — node "Send a message3" (id `8cbccd31-3e4e-48ed-87d1-9f61d49e9d03`)
- *(dynamic channel)* — op `channel` — node "Send a message1" (id `d1c321b2-1cef-418b-bc62-ca08f15b6c94`)
- [[../resources/slack-channels/c08r8h75n15|C08R8H75N15]] (id `C08R8H75N15`) — op `channel` — node "Send a message" (id `f36e0159-0c25-4c1c-bc1c-4daa204e3767`)

### Sub-workflows (Execute Workflow calls)

- [[dispute-create-report|Dispute - Create Report]] (n8n_id `IM3wk08pLLTXawd2`) — node "Call 'Dispute - Create Report'" (id `4c69f224-6237-4419-a136-f5ea6ef86371`)
- [[dispute-compose-report|Dispute - Compose report]] (n8n_id `NWv022t59k7EtTFo`) — node "Call 'Dispute - Compose report'" (id `dd282231-5d51-40f3-9efd-2f68f407f9df`)

## Used by (workflows)

- [[opsinternalbot-main|OpsInternalBot - Main]] — node "Call 'OpsInternalBot - Token Inport Job'1" (id `7a0b812c-df11-4c55-878d-f1d38e9ee578`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
