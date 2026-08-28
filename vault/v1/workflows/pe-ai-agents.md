---
n8n_id: "8fQ3h68w8VAanRCJ"
instance: v1
name: "PE AI Agents"
status: active
last_modified: 2026-02-09T21:30:27.069Z
tags: []
fingerprint: "d5fb941e6994868b7c5fb29933d9c373509aa90921121b7e5c3abafee7d807a9"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PE AI Agents

## Summary

- **Status:** active
- **n8n ID:** `8fQ3h68w8VAanRCJ`
- **Nodes:** 31
- **Last modified:** 2026-02-09T21:30:27.069Z

## Triggers

- **other** — node "When chat message received" (id `28d56151-91e7-4de7-ad4f-ee86759e3ba1`)
- **webhook** — node "Webhook" (id `5761a2e1-0e8d-495c-8701-919bb213c40f`) — POST `17f34feb-8fd7-42fa-8d5a-66889e875186`
- **manual** — node "When clicking ‘Execute workflow’" (id `6d19c2c8-9295-428a-8292-f9272ea902d0`)

## Depends on

### Credentials

- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Email Drafts" (id `14e9bd85-18bd-4b24-949d-3dd0af153223`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `2cb420b3-4f67-47f1-8def-fadc303c1b77`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create a draft in Gmail" (id `323e41cf-5c37-45c2-a783-5237da4907ca`)
- [[../resources/credentials/godp5gdyjaspv2fj|Anthropic (spartak@platformfactory.io)]] (`anthropicApi`, id `Godp5GdYJAspV2fj`) — node "Anthropic Chat Model" (id `44cad096-a038-42a3-a6ea-7811cb5b523c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file1" (id `50e22646-6b94-4c79-862c-bdeb60597631`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create a document in Google Docs" (id `56ada100-1b89-43bc-9dab-93badb042ccc`)
- [[../resources/credentials/bcxreaoevqmwbtnu|PE Sandbox-Live (Overlay Access)]] (`postgres`, id `BCXReaoEvQMwbTNU`) — node "Agents Status Maintenance Tool" (id `63943f2f-32e7-4568-8058-29e9f3e56e03`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack11" (id `7d62fae7-af7f-4b34-affd-0f61fd6dd568`)
- [[../resources/credentials/gc45raivyrnqugiw|PE Automations Servie Account 2]] (`googleApi`, id `gc45RaIvyrNqUgiw`) — node "Create spreadsheet in Google Sheets" (id `a399b760-687c-4edf-a3a0-b31646c6f52f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Success Message2" (id `dd7a2b7e-9cba-46f3-ae18-7ad5a6254150`)
- [[../resources/credentials/bcxreaoevqmwbtnu|PE Sandbox-Live (Overlay Access)]] (`postgres`, id `BCXReaoEvQMwbTNU`) — node "AI Agent Events Tracker" (id `eedb989b-f850-4863-a91b-1a428b625873`)

### HTTP URLs

- [[../resources/http-urls/console-v2-payengine-dev|console-v2.payengine.dev]] — `POST https://console-v2.payengine.dev/overlay/api/ai-agents/{{ $('When chat message received').item.json.custom_metadata.agent_id }}/files` — node "HTTP Request2" (id `1981b776-272d-4a51-badb-67b4a73f99ba`)
- *(dynamic URL)* — `=GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `c10865b3-22bb-4e7a-b167-d407b4e2638f`)
- [[../resources/http-urls/api-ipify-org|api.ipify.org]] — `GET https://api.ipify.org?format=json` — node "HTTP Request1" (id `c22a46ef-5db4-4aa8-aeb8-b41535a7914f`)

### Databases

- [[../resources/databases/postgres-bcxreaoevqmwbtnu|postgres (via PE Sandbox-Live (Overlay Access))]] — op `update`, table `{"__rl":true,"value":"ai_agents","mode":"list","cachedResultName":"ai_agents"}` — node "Agents Status Maintenance Tool" (id `63943f2f-32e7-4568-8058-29e9f3e56e03`)
- [[../resources/databases/postgres-bcxreaoevqmwbtnu|postgres (via PE Sandbox-Live (Overlay Access))]] — op `?`, table `{"__rl":true,"value":"ai_agent_conversation_messages","mode":"list","cachedResultName":"ai_agent_conversation_messages"}` — node "AI Agent Events Tracker" (id `eedb989b-f850-4863-a91b-1a428b625873`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-5-20250929|anthropic / claude-sonnet-4-5-20250929]] — node "Anthropic Chat Model" (id `44cad096-a038-42a3-a6ea-7811cb5b523c`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Slack2" (id `2cb420b3-4f67-47f1-8def-fadc303c1b77`)
- *(dynamic channel)* — op `channel` — node "Slack11" (id `7d62fae7-af7f-4b34-affd-0f61fd6dd568`)
- *(dynamic channel)* — op `channel` — node "Success Message2" (id `dd7a2b7e-9cba-46f3-ae18-7ad5a6254150`)

### MCP servers (external)

- [[../resources/mcp-servers/https-3723f319a8c6-ngrok-app-mcp|3723f319a8c6.ngrok.app]] — `https://3723f319a8c6.ngrok.app/mcp` — node "PE Skills MCP" (id `28501c09-bcb0-4490-aee8-ab603e9f836f`)

### Sub-workflows (Execute Workflow calls)

- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Execute Workflow1" (id `0b08eb25-8c69-4c96-85ba-1237458d5915`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "PayEnginePE Bot" (id `30da42d3-ea10-4824-88fd-54906ccd4dee`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
