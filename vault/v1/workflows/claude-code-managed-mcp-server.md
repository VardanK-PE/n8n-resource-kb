---
n8n_id: "ghGZcuWFADxqOWbl"
instance: v1
name: "Claude Code Managed MCP Server"
status: active
last_modified: 2026-08-27T18:42:15.136Z
tags:
  - "Spartak's Projects"
fingerprint: "0de868e7d10be58776a9e98aefca364e1d9c6fc9ee61364cdcb6812280c956be"
auto_generated_at: 2026-08-28T21:13:05Z
---

<!-- auto:start -->

# Claude Code Managed MCP Server

## Summary

- **Status:** active
- **n8n ID:** `ghGZcuWFADxqOWbl`
- **Nodes:** 13
- **Last modified:** 2026-08-27T18:42:15.136Z

## Triggers

- **webhook** — node "Webhook" (id `61428c7f-4955-4357-9454-50f2592995c1`) — POST `a6a41b09-4bce-48bd-b243-871cccae1bcb`
- **webhook** — node "LangChain Webhook" (id `6ef92460-16c7-4818-9873-2b298a938bd0`) — POST `25f6faa6-d594-4196-a5ef-a9276552ee1e`
- **other** — node "Chat Trigger" (id `chat-trigger-1`)

## Depends on

### Credentials

- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `4beafe8e-6150-4629-a145-f0c9a0305b1f`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Claude (Main)" (id `claude-main-1`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-5|anthropic / claude-sonnet-5]] — node "Anthropic Chat Model" (id `4beafe8e-6150-4629-a145-f0c9a0305b1f`)
- [[../resources/llm-models/anthropic-claude-sonnet-5|anthropic / claude-sonnet-5]] — node "Claude (Main)" (id `claude-main-1`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
