---
n8n_id: "xXRFRVgdiTc06Rvm"
name: "My workflow 3"
status: inactive
last_modified: 2025-08-30T14:08:16.314Z
tags: []
fingerprint: "b44c9caad2c448b17336b1d6c71d3aec98eeb300a144626c7f3b27ed4d5b22b5"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# My workflow 3

## Summary

- **Status:** inactive
- **n8n ID:** `xXRFRVgdiTc06Rvm`
- **Nodes:** 8
- **Last modified:** 2025-08-30T14:08:16.314Z

## Triggers

- **webhook** — node "Webhook" (id `779a3a80-1a0e-4b97-9fbe-97528cfbd817`) — POST `fda5b141-2447-498c-ac23-17f0b32a59f9`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `68adfa84-b97d-4473-988c-e94b37717272`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `7e998a8b-d87c-438d-9765-658937a292a3`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `a6a9e066-f088-4475-9ece-56bd71745e26`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `f54801bd-a6bd-46bb-a581-d481e363c33d`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model" (id `7e998a8b-d87c-438d-9765-658937a292a3`)

### Google Sheets

- [[../resources/google-sheets/1ccd2nb32miyleeld3vxsjp71pvoklbltaznimj9ki6c|Test AI Sheet]] (id `1cCD2Nb32MiYLeEld3VxSjP71pVOklBLtAZNimj9KI6c`) — op `append`, tab `Sheet1` — node "Append row in sheet" (id `68adfa84-b97d-4473-988c-e94b37717272`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
