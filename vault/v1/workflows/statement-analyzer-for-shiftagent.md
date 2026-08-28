---
n8n_id: "j6YUK5QH6hEcT00a"
instance: v1
name: "Statement Analyzer (for ShiftAgent)"
status: inactive
last_modified: 2026-03-16T15:28:52.150Z
tags: []
fingerprint: "3eebc1206e016a7e73db20e130c8fdfcf01e3d1d02f632e99e9ddb088a6fdf10"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Statement Analyzer (for ShiftAgent)

## Summary

- **Status:** inactive
- **n8n ID:** `j6YUK5QH6hEcT00a`
- **Nodes:** 34
- **Last modified:** 2026-03-16T15:28:52.150Z

## Triggers

- **webhook** — node "Webhook1" (id `45cec40a-66cd-4459-b6dc-f11d5be600ba`) — GET `5e936f9d-9a7f-40aa-ae1d-c6cc06daead9`
- **webhook** — node "Webhook" (id `7c2687ce-e2cf-4232-bb20-b953e6b0004d`) — POST `110400f9-ddb6-4224-92ea-f43be90f9bb7`
- **webhook** — node "Webhook2" (id `8a4b2c3d-62aa-4712-9f6d-3a2ff058b72b`) — GET `8dc692e9-e1b3-42ba-9e9a-2b914fea90c8`
- **other** — node "When chat message received" (id `a819f932-7856-42c4-b839-7886aad91b94`) — GET `ed459d0e-b55a-43ab-afeb-5ef5f6e7ce64`
- **manual** — node "When clicking ‘Execute workflow’" (id `c9f6431d-aa9f-43db-a8d5-ce0436795a7b`)

## Depends on

### Credentials

- [[../resources/credentials/vjyobgaeh30bqna6|n8nio-pg]] (`n8nApi`, id `vJyOBgaEh30bQnA6`) — node "Delete an execution" (id `164befe1-24a2-4317-bc94-1a69c264ac17`)
- [[../resources/credentials/6wtnt8qzxtulvy6q|SerpAPI account]] (`serpApi`, id `6WTnT8qZXtulvY6q`) — node "SerpAPI" (id `5567884d-3e12-422a-abdb-9898aa75003f`)
- [[../resources/credentials/wwm73d114letbuus|n8n-service-account Google Service Account account]] (`googleApi`, id `wwm73D114LETBUUS`) — node "Google Vision1" (id `6e59601e-23d8-4004-a4c7-16a9ce0c8e55`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `6fa64dc7-725a-4ac9-84bf-4c69fbeb3bf2`)
- [[../resources/credentials/gc45raivyrnqugiw|PE Automations Servie Account 2]] (`googleApi`, id `gc45RaIvyrNqUgiw`) — node "Get many messages" (id `7307c467-2d6e-4cd7-a2f8-4e46e7126eea`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `b40334c4-8ac3-47d9-a68c-f5b60ffa2e36`)
- [[../resources/credentials/wwm73d114letbuus|n8n-service-account Google Service Account account]] (`googleApi`, id `wwm73D114LETBUUS`) — node "Google Vision" (id `b549082a-d175-478e-bbc0-eca3720f7e2d`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model" (id `c680fc5c-239e-4489-97c7-64cf4054c0ea`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `db9956fc-1d1b-4e96-9c70-7ce261d27fe0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get System Prompt" (id `f69274f7-45a0-4f66-a246-92c35f226874`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `502a9f39-6089-485d-8f5d-ec471bdccf49`)
- [[../resources/http-urls/vision-googleapis-com|vision.googleapis.com]] — `POST https://vision.googleapis.com/v1/files:annotate` — node "Google Vision1" (id `6e59601e-23d8-4004-a4c7-16a9ce0c8e55`)
- [[../resources/http-urls/vision-googleapis-com|vision.googleapis.com]] — `POST https://vision.googleapis.com/v1/files:annotate` — node "Google Vision" (id `b549082a-d175-478e-bbc0-eca3720f7e2d`)

### LLM models

- [[../resources/llm-models/openai-gpt-5|openai / gpt-5]] — node "OpenAI Chat Model" (id `c680fc5c-239e-4489-97c7-64cf4054c0ea`)
- [[../resources/llm-models/anthropic-claude-opus-4-6|anthropic / claude-opus-4-6]] — node "Anthropic Chat Model" (id `db9956fc-1d1b-4e96-9c70-7ce261d27fe0`)

### Google Drive

- [[../resources/google-drive/1hrjablm2o7kxlaagt-jz0fm5ee-dspi74qbh5ke8xmg|PE Statement Analyzer Prompt]] (`file`, id `1hrjAblm2O7kxLAAgT-JZ0fm5EE-DsPI74Qbh5Ke8Xmg`) — op `download` — node "Get System Prompt" (id `f69274f7-45a0-4f66-a246-92c35f226874`)

### Data tables (n8n)

- [[../resources/data-tables/wd21lrwtpmzlsu2h|StatementAnalysis]] (id `wd21lrwTpmzLSU2h`) — op `get` — node "Get row(s)" (id `8ef754eb-e4e1-4c74-81af-84dbe9ab63eb`)
- [[../resources/data-tables/wd21lrwtpmzlsu2h|StatementAnalysis]] (id `wd21lrwTpmzLSU2h`) — op `update` — node "Update row(s)" (id `984eccde-92b1-4d93-9686-762600e15bf4`)
- [[../resources/data-tables/wd21lrwtpmzlsu2h|StatementAnalysis]] (id `wd21lrwTpmzLSU2h`) — op `?` — node "Insert row" (id `bc340826-7730-4745-ad47-adf08fa0b421`)

### Slack channels

- [[../resources/slack-channels/c09swm8cm6h|pe-statement-analyzer-alerts]] (id `C09SWM8CM6H`) — op `channel` — node "Send a message" (id `6fa64dc7-725a-4ac9-84bf-4c69fbeb3bf2`)
- [[../resources/slack-channels/c09swm8cm6h|pe-statement-analyzer-alerts]] (id `C09SWM8CM6H`) — op `channel` — node "Send a message1" (id `b40334c4-8ac3-47d9-a68c-f5b60ffa2e36`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
