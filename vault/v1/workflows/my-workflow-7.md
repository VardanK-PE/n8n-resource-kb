---
n8n_id: "TaXStskv6zSvLi6V"
instance: v1
name: "My workflow 7"
status: archived
last_modified: 2026-06-18T15:50:40.034Z
tags: []
fingerprint: "a46990b87d3e5a412b5cb8240c791b08ccba3fb3e2fa2e2927b37a04a2171425"
auto_generated_at: 2026-08-28T21:59:10Z
---

<!-- auto:start -->

# My workflow 7

## Summary

- **Status:** archived
- **n8n ID:** `TaXStskv6zSvLi6V`
- **Nodes:** 4
- **Last modified:** 2026-06-18T15:50:40.034Z

## Triggers

- **webhook** — node "Webhook" (id `5f4e7bf2-923d-4998-831d-8007fd929365`) — GET `379194ab-2e30-440a-a7c8-a0a2fd371d3f`

## Depends on

### Credentials

- [[../resources/credentials/gc45raivyrnqugiw|PE Automations Servie Account 2]] (`googleApi`, id `gc45RaIvyrNqUgiw`) — node "Get row(s) in sheet in Google Sheets" (id `8c933488-dc6d-4c4f-848b-db04eb0d2932`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `a911da07-6cad-4e22-981a-4ee83296e9f4`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-5-20250929|anthropic / claude-sonnet-4-5-20250929]] — node "Anthropic Chat Model" (id `a911da07-6cad-4e22-981a-4ee83296e9f4`)

### Google Sheets

- [[../resources/google-sheets/|]] (id ``) — op `?`, tab `` — node "Get row(s) in sheet in Google Sheets" (id `8c933488-dc6d-4c4f-848b-db04eb0d2932`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
