---
n8n_id: "CGjiDoLZSquAGct0"
instance: v1
name: "ECS Enrollment Response Processor"
status: active
last_modified: 2025-09-29T15:48:56.947Z
tags: []
fingerprint: "269b0adc13e5403daa8a742cd3f7394ece2d864719c83239d28cdb6ca8bd4ec4"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# ECS Enrollment Response Processor

## Summary

- **Status:** active
- **n8n ID:** `CGjiDoLZSquAGct0`
- **Nodes:** 18
- **Last modified:** 2025-09-29T15:48:56.947Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `1a118c62-6ea2-4c5d-9804-0db0f93d8183`) — `every 1 hour(s) at :49`
- **manual** — node "When clicking ‘Execute workflow’" (id `7be9c9fc-4f5b-4498-a3af-c9cd7e1bebc7`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Sent Docs1" (id `18473c2d-7e19-48be-a2b1-cdd2cb6cbdb9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Sent Docs" (id `a5ae38a0-5eeb-4cef-ae80-eb61f4512dea`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `becc271a-1fb0-46f1-8f1e-d82ab296e1ec`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages1" (id `cefa0b21-0870-4444-b181-0150700d4ef8`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Receipt Confirmation" (id `f3a17385-210c-4da3-b9f3-819c8c8cfbd6`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model" (id `becc271a-1fb0-46f1-8f1e-d82ab296e1ec`)

### Google Sheets

- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `appendOrUpdate`, tab `LatestEmailResponseStatuses` — node "Get Sent Docs1" (id `18473c2d-7e19-48be-a2b1-cdd2cb6cbdb9`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `?`, tab `Sheet1` — node "Get Sent Docs" (id `a5ae38a0-5eeb-4cef-ae80-eb61f4512dea`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
