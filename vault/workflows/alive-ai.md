---
n8n_id: "YjWQewLm3lVchUAO"
name: "Alive AI"
status: inactive
last_modified: 2025-08-22T07:05:23.458Z
tags: []
fingerprint: "eb0cd26deef1736cf6d15a985ac3ec24d31956f0827f612a67a0258c07632f27"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Alive AI

## Summary

- **Status:** inactive
- **n8n ID:** `YjWQewLm3lVchUAO`
- **Nodes:** 9
- **Last modified:** 2025-08-22T07:05:23.458Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `76e35547-6032-40bf-8cd3-219e1e66151e`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message in Slack" (id `08d6a58b-f6f1-4571-bbf0-85064edc3042`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `5dc11573-4188-4586-93e3-f87de37f6a1e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `768c42c7-0c5c-4a9f-a118-a24835b1110d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Subprompt Updater1" (id `a525612f-eada-470d-b09b-24e727cd0fc9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `ac83ba31-4d17-4d79-9e1a-886f63aa9869`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `b3e0efc3-fee2-4402-8a19-e14a3906279d`)

### LLM models

- [[../resources/llm-models/anthropic-claude-opus-4-20250514|anthropic / claude-opus-4-20250514]] — node "Anthropic Chat Model" (id `5dc11573-4188-4586-93e3-f87de37f6a1e`)

### Google Sheets

- [[../resources/google-sheets/1vtitcoidswv1iowp7z-46tvurrempdwygo5uy1emkjy|Alive AI]] (id `1vtitcOiDsWv1IoWp7z-46tvurRemPdwYGO5Uy1EMKJY`) — op `append`, tab `SubPrompts` — node "Subprompt Updater1" (id `a525612f-eada-470d-b09b-24e727cd0fc9`)
- [[../resources/google-sheets/1vtitcoidswv1iowp7z-46tvurrempdwygo5uy1emkjy|Alive AI]] (id `1vtitcOiDsWv1IoWp7z-46tvurRemPdwYGO5Uy1EMKJY`) — op `?`, tab `Prompts` — node "Get row(s) in sheet" (id `ac83ba31-4d17-4d79-9e1a-886f63aa9869`)

### Slack channels

- [[../resources/slack-channels/c09bgkg55uj|alive-ai]] (id `C09BGKG55UJ`) — op `channel` — node "Send a message in Slack" (id `08d6a58b-f6f1-4571-bbf0-85064edc3042`)
- [[../resources/slack-channels/c09bgkg55uj|alive-ai]] (id `C09BGKG55UJ`) — op `channel` — node "Send a message" (id `768c42c7-0c5c-4a9f-a118-a24835b1110d`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
