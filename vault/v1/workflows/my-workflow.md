---
n8n_id: "nRnqd6pG5n8065Ig"
instance: v1
name: "My workflow"
status: archived
last_modified: 2025-07-02T10:05:58.930Z
tags: []
fingerprint: "21b99277625f03455cb402de3082695873d24e1cfdfb271f00eb428c6b86f3b0"
auto_generated_at: 2026-08-28T21:59:10Z
---

<!-- auto:start -->

# My workflow

## Summary

- **Status:** archived
- **n8n ID:** `nRnqd6pG5n8065Ig`
- **Nodes:** 6
- **Last modified:** 2025-07-02T10:05:58.930Z

## Triggers

- **webhook** — node "Webhook" (id `8852fdac-d544-430c-8d00-490d0b8a1fee`) — POST `e98f95cd-a101-49d3-b01e-761487880b4f`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `542b4baf-5b51-4cfe-9e1d-2c7c429d9dd0`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model" (id `d3ea9606-48a5-4bd9-9e8d-11001dfea2f0`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `c64249b2-5d55-4ba3-92bd-b04b988d4d9f`)

### LLM models

- [[../resources/llm-models/openai-gpt-4-1-mini|openai / gpt-4.1-mini]] — node "OpenAI Chat Model" (id `d3ea9606-48a5-4bd9-9e8d-11001dfea2f0`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
