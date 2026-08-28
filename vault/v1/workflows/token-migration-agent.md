---
n8n_id: "uMwamYPM4QPfs7SE"
name: "Token Migration Agent"
status: active
last_modified: 2026-04-27T14:52:24.874Z
tags: []
fingerprint: "ba29c7e127d9e676810cf62f880ccae967d984cd81d020e76044f82a9ed96fd1"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Token Migration Agent

## Summary

- **Status:** active
- **n8n ID:** `uMwamYPM4QPfs7SE`
- **Nodes:** 12
- **Last modified:** 2026-04-27T14:52:24.874Z

## Triggers

- **other** — node "Gmail Trigger" (id `269a21dd-99ae-4093-8e4c-608c48101154`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `00fd6d67-0bcd-411b-bcfe-762227e1b4e0`)
- [[../resources/credentials/q4evaiml6ruz4bst|migrations@payengine.co email]] (`gmailOAuth2`, id `q4eVAiML6rUZ4bSt`) — node "Gmail Trigger" (id `269a21dd-99ae-4093-8e4c-608c48101154`)
- [[../resources/credentials/q4evaiml6ruz4bst|migrations@payengine.co email]] (`gmailOAuth2`, id `q4eVAiML6rUZ4bSt`) — node "Get a message in Gmail" (id `90a3fed4-6576-4b49-b84f-c35c265b7114`)
- [[../resources/credentials/q4evaiml6ruz4bst|migrations@payengine.co email]] (`gmailOAuth2`, id `q4eVAiML6rUZ4bSt`) — node "Get a thread in Gmail" (id `a3d69abe-6231-4b89-8447-13f77274029a`)
- [[../resources/credentials/q4evaiml6ruz4bst|migrations@payengine.co email]] (`gmailOAuth2`, id `q4eVAiML6rUZ4bSt`) — node "Get many threads in Gmail" (id `c06c78f6-a5da-49cf-a89d-f1c5f4731dff`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Send a message in Gmail" (id `cdf6ddf5-a105-442e-bab3-f586a18a0b71`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `d210f076-4604-4362-b3f5-475991eae26d`)
- [[../resources/credentials/q4evaiml6ruz4bst|migrations@payengine.co email]] (`gmailOAuth2`, id `q4eVAiML6rUZ4bSt`) — node "Get many messages in Gmail" (id `e3854606-63f5-4716-b856-a38b2949be8c`)
- [[../resources/credentials/q4evaiml6ruz4bst|migrations@payengine.co email]] (`gmailOAuth2`, id `q4eVAiML6rUZ4bSt`) — node "Reply to a message in Gmail" (id `ff155ea8-a923-46e0-aabb-3890f19b623d`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `12285966-26a7-47f8-b285-f9731df616e1`)

### LLM models

- [[../resources/llm-models/anthropic-claude-opus-4-7|anthropic / claude-opus-4-7]] — node "Anthropic Chat Model" (id `d210f076-4604-4362-b3f5-475991eae26d`)

### Slack channels

- [[../resources/slack-channels/c0av2kqtqt1|migrations-ai]] (id `C0AV2KQTQT1`) — op `channel` — node "Send a message" (id `00fd6d67-0bcd-411b-bcfe-762227e1b4e0`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
