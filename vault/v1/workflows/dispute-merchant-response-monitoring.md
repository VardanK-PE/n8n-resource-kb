---
n8n_id: "NEbtl9SFLp7F1V5L"
instance: v1
name: "Dispute - Merchant Response Monitoring"
status: active
last_modified: 2026-08-27T18:43:01.123Z
tags: []
fingerprint: "ca4a3403bb01ec09f9fb43004de690bc99dfa693d3793e242c5a963d2bba9714"
auto_generated_at: 2026-08-28T21:13:05Z
---

<!-- auto:start -->

# Dispute - Merchant Response Monitoring

## Summary

- **Status:** active
- **n8n ID:** `NEbtl9SFLp7F1V5L`
- **Nodes:** 29
- **Last modified:** 2026-08-27T18:43:01.123Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `a379041d-fb18-4105-87db-9209faee971e`) — `every 15 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model" (id `0f4a3ff7-16b7-416b-a1f7-56eb46b8cd18`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `69d4a119-58ba-45a4-9f6d-9359dc3fe41e`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `a445276b-61bc-445a-94c7-44a39cb72b63`)

### LLM models

- [[../resources/llm-models/openai-gpt-5-mini|openai / gpt-5-mini]] — node "OpenAI Chat Model" (id `0f4a3ff7-16b7-416b-a1f7-56eb46b8cd18`)
- [[../resources/llm-models/anthropic-claude-sonnet-5|anthropic / claude-sonnet-5]] — node "Anthropic Chat Model1" (id `69d4a119-58ba-45a4-9f6d-9359dc3fe41e`)
- [[../resources/llm-models/anthropic-claude-haiku-4-5-20251001|anthropic / claude-haiku-4-5-20251001]] — node "Anthropic Chat Model" (id `a445276b-61bc-445a-94c7-44a39cb72b63`)

### Data tables (n8n)

- [[../resources/data-tables/da1d723wdyigobvw|Dispute - Merchant Responses]] (id `DA1d723WDyIGoBVW`) — op `?` — node "Insert row" (id `7a697e59-245d-495f-a8de-4c823a8a4652`)
- [[../resources/data-tables/da1d723wdyigobvw|Dispute - Merchant Responses]] (id `DA1d723WDyIGoBVW`) — op `rowNotExists` — node "If row does not exist" (id `87f25d56-06d4-433a-929a-492d087d552b`)

### Sub-workflows (Execute Workflow calls)

- [[email-get-emails-by-filter|Email - Get emails by filter]] (n8n_id `114H81oKKk4EXteM`) — node "Get PE Merchant Emails" (id `23a1c23b-880a-4084-a716-67a707edf321`)
- [[email-get-emails-by-filter|Email - Get emails by filter]] (n8n_id `114H81oKKk4EXteM`) — node "Get Hearth Merchant Emails" (id `41459dea-ce7b-42b6-b670-0ba8eef9e6ef`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `43dfbe48-cad6-4465-944c-8efd611e9007`)
- [[email-get-email-thread|Email - Get email thread]] (n8n_id `jJq7apxtmeis8y7Y`) — node "Call 'Email - Get email thread'" (id `49d2a468-938a-4837-9fe2-78a35cf41c05`)
- [[email-get-emails-by-filter|Email - Get emails by filter]] (n8n_id `114H81oKKk4EXteM`) — node "Get Supermove Merchant Emails" (id `56d5b54a-7ec6-44cc-b106-bc60d293286c`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `b86037ca-32f5-4340-8b88-b827a933e5b4`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
