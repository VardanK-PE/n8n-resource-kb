---
n8n_id: "Nb9lIuQUHYbBrDdo"
instance: v1
name: "Statement Analyzer"
status: active
last_modified: 2026-03-16T15:28:26.843Z
tags: []
fingerprint: "3502f250c997ece085b968d8d09e6128e2a0749393e6b65922c63010209c135c"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Statement Analyzer

## Summary

- **Status:** active
- **n8n ID:** `Nb9lIuQUHYbBrDdo`
- **Nodes:** 34
- **Last modified:** 2026-03-16T15:28:26.843Z

## Triggers

- **webhook** — node "Webhook1" (id `14a4abb6-930c-4827-804d-a202e02136cb`) — GET `9bede04c-43b3-43df-b7c5-7f67c3f2052f-status-check`
- **webhook** — node "Webhook" (id `1df514ed-d5dd-4ddb-82fd-3813eef796df`) — POST `9bede04c-43b3-43df-b7c5-7f67c3f2052f`
- **manual** — node "When clicking ‘Execute workflow’" (id `38adff1f-602a-4fef-a0f2-a63709393147`)
- **webhook** — node "Webhook2" (id `7ff6e42f-b3d9-407a-bffb-110114918359`) — GET `8d369728-01cc-4e41-982e-d4f842b48788`
- **other** — node "When chat message received" (id `e0a3b933-8b21-47b3-9a72-705851cbafbd`)

## Depends on

### Credentials

- [[../resources/credentials/vjyobgaeh30bqna6|n8nio-pg]] (`n8nApi`, id `vJyOBgaEh30bQnA6`) — node "Delete an execution" (id `2d7fe8cf-168f-4696-ae7e-63d6b7275308`)
- [[../resources/credentials/gc45raivyrnqugiw|PE Automations Servie Account 2]] (`googleApi`, id `gc45RaIvyrNqUgiw`) — node "Get many messages" (id `416f5157-874a-4970-a896-82c7ef0f3a70`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get System Prompt" (id `659c9d42-43c2-42eb-976d-fcd97c0411a2`)
- [[../resources/credentials/wwm73d114letbuus|n8n-service-account Google Service Account account]] (`googleApi`, id `wwm73D114LETBUUS`) — node "Google Vision1" (id `6663a90c-2074-4105-bf06-d0fa7158f9c5`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `b4127bf4-6bb9-49dd-933c-d02782687254`)
- [[../resources/credentials/6wtnt8qzxtulvy6q|SerpAPI account]] (`serpApi`, id `6WTnT8qZXtulvY6q`) — node "SerpAPI" (id `c2814ba8-7d5a-4265-b192-b615986265ab`)
- [[../resources/credentials/wwm73d114letbuus|n8n-service-account Google Service Account account]] (`googleApi`, id `wwm73D114LETBUUS`) — node "Google Vision" (id `c3dc98cd-0f11-4596-82b8-a5f0cf3fd41d`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `c559dfa9-994b-459f-89ba-633fe57613a2`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model" (id `d24c3171-55be-40e0-95ec-8be924637e88`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `ed12480f-0e30-43ed-8d95-d3774c9ce1ca`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `533cf046-7d2f-425a-9d29-3ca2c66cc8fd`)
- [[../resources/http-urls/vision-googleapis-com|vision.googleapis.com]] — `POST https://vision.googleapis.com/v1/files:annotate` — node "Google Vision1" (id `6663a90c-2074-4105-bf06-d0fa7158f9c5`)
- [[../resources/http-urls/vision-googleapis-com|vision.googleapis.com]] — `POST https://vision.googleapis.com/v1/files:annotate` — node "Google Vision" (id `c3dc98cd-0f11-4596-82b8-a5f0cf3fd41d`)

### LLM models

- [[../resources/llm-models/anthropic-claude-opus-4-6|anthropic / claude-opus-4-6]] — node "Anthropic Chat Model" (id `c559dfa9-994b-459f-89ba-633fe57613a2`)
- [[../resources/llm-models/openai-gpt-5|openai / gpt-5]] — node "OpenAI Chat Model" (id `d24c3171-55be-40e0-95ec-8be924637e88`)

### Google Drive

- [[../resources/google-drive/1hrjablm2o7kxlaagt-jz0fm5ee-dspi74qbh5ke8xmg|PE Statement Analyzer Prompt]] (`file`, id `1hrjAblm2O7kxLAAgT-JZ0fm5EE-DsPI74Qbh5Ke8Xmg`) — op `download` — node "Get System Prompt" (id `659c9d42-43c2-42eb-976d-fcd97c0411a2`)

### Data tables (n8n)

- [[../resources/data-tables/wd21lrwtpmzlsu2h|StatementAnalysis]] (id `wd21lrwTpmzLSU2h`) — op `update` — node "Update row(s)" (id `64c9c2ca-a280-4c30-8e93-704fcd4fbd16`)
- [[../resources/data-tables/wd21lrwtpmzlsu2h|StatementAnalysis]] (id `wd21lrwTpmzLSU2h`) — op `?` — node "Insert row" (id `ca56787f-aaae-4a4f-8bba-8b0b54800259`)
- [[../resources/data-tables/wd21lrwtpmzlsu2h|StatementAnalysis]] (id `wd21lrwTpmzLSU2h`) — op `get` — node "Get row(s)" (id `e15c5ba1-8d4f-4463-8f7d-8742831a3777`)

### Slack channels

- [[../resources/slack-channels/c09swm8cm6h|pe-statement-analyzer-alerts]] (id `C09SWM8CM6H`) — op `channel` — node "Send a message1" (id `b4127bf4-6bb9-49dd-933c-d02782687254`)
- [[../resources/slack-channels/c09swm8cm6h|pe-statement-analyzer-alerts]] (id `C09SWM8CM6H`) — op `channel` — node "Send a message" (id `ed12480f-0e30-43ed-8d95-d3774c9ce1ca`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
