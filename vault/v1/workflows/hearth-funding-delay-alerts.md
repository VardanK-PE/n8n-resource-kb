---
n8n_id: "SKUc7koYq0qLDt2Y"
name: "Hearth - Funding Delay Alerts"
status: active
last_modified: 2025-11-21T16:32:32.521Z
tags: []
fingerprint: "80e828b61601f05bb90aee13393f104d63cd959ee96f2c53ac8f27b9c707f853"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Hearth - Funding Delay Alerts

## Summary

- **Status:** active
- **n8n ID:** `SKUc7koYq0qLDt2Y`
- **Nodes:** 40
- **Last modified:** 2025-11-21T16:32:32.521Z

## Triggers

- **schedule** — node "Schedule Trigger1" (id `48b03eb9-da85-432f-9142-f5287835c615`) — `every 1 hour(s)`
- **schedule** — node "Schedule Trigger" (id `4e2be0ed-ec5a-41f5-b483-5f5415b462b3`) — `daily at 13:00`
- **error** — node "Error Trigger" (id `c5d08110-6167-4c6d-ab37-9a78689d66fc`)
- **manual** — node "When clicking ‘Execute workflow’" (id `efb0aa5e-d59a-46eb-9bb0-e4014da3e425`)

## Depends on

### Credentials

- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages2" (id `017866c2-f4d3-47e1-b8d5-44aff287e503`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Slack" (id `08ab63b7-0a74-451d-9780-5a34fe068a75`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `09a0df60-9e8e-42d8-982c-09c9338bca82`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Slack1" (id `0f1c9a2c-cb15-46ee-836b-116164dfa89a`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages" (id `175538d4-23d9-4ef1-b9c4-c5acc649ea2f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `32bb6496-ea38-4be1-bed6-5afc82330f1d`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Slack2" (id `3866b373-9e08-4090-acf2-51c09c0377fd`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create a draft" (id `395da137-fe2b-4029-bd26-327f3368fd80`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `4b7ac2a8-d08c-4c6f-b6fa-f111105475fa`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `512699a6-9370-4796-b074-f61cff2ad9aa`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `5dee16a3-1b6a-46fa-8334-d6d87a8d139e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `8404a5d2-d8eb-479b-8938-e4ef5da51c66`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send a message in Slack" (id `95e86f55-ac6b-41d8-aa32-8ac57bc769ab`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `9935bf08-d707-4a4e-8d62-15ad4ec7d0e7`)
- [[../resources/credentials/godp5gdyjaspv2fj|Anthropic (spartak@platformfactory.io)]] (`anthropicApi`, id `Godp5GdYJAspV2fj`) — node "Anthropic Chat Model" (id `9b106ec3-d667-4fab-9e5e-6d645d5f4a31`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet in Google Sheets" (id `a1d9078f-146b-4143-86a0-29fa377979cb`)
- [[../resources/credentials/godp5gdyjaspv2fj|Anthropic (spartak@platformfactory.io)]] (`anthropicApi`, id `Godp5GdYJAspV2fj`) — node "Anthropic Chat Model1" (id `e38d296e-6761-4a95-a23d-604d4e87f9f9`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages1" (id `ff8df974-5a20-42dc-9d01-ad44ab79772c`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `5dee16a3-1b6a-46fa-8334-d6d87a8d139e`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-5-20250929|anthropic / claude-sonnet-4-5-20250929]] — node "Anthropic Chat Model" (id `9b106ec3-d667-4fab-9e5e-6d645d5f4a31`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-5-20250929|anthropic / claude-sonnet-4-5-20250929]] — node "Anthropic Chat Model1" (id `e38d296e-6761-4a95-a23d-604d4e87f9f9`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator" (id `3464ea05-d760-46c6-8bf3-51542e00bd8d`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `fundingDelays` — node "Append or update row in sheet" (id `32bb6496-ea38-4be1-bed6-5afc82330f1d`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `fundingDelays` — node "Get row(s) in sheet" (id `512699a6-9370-4796-b074-f61cff2ad9aa`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `fundingDelays` — node "Get row(s) in sheet1" (id `8404a5d2-d8eb-479b-8938-e4ef5da51c66`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `fundingDelays` — node "Update row in sheet" (id `9935bf08-d707-4a4e-8d62-15ad4ec7d0e7`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `fundingDelays` — node "Update row in sheet in Google Sheets" (id `a1d9078f-146b-4143-86a0-29fa377979cb`)

### Slack channels

- [[../resources/slack-channels/c08tfuf32e6|hearth-payout-delays]] (id `C08TFUF32E6`) — op `channel` — node "Slack" (id `08ab63b7-0a74-451d-9780-5a34fe068a75`)
- [[../resources/slack-channels/c09c901een4|hearth-alerts-internal]] (id `C09C901EEN4`) — op `channel` — node "Send a message" (id `09a0df60-9e8e-42d8-982c-09c9338bca82`)
- *(dynamic channel)* — op `channel` — node "Slack1" (id `0f1c9a2c-cb15-46ee-836b-116164dfa89a`)
- [[../resources/slack-channels/c08tfuf32e6|hearth-payout-delays]] (id `C08TFUF32E6`) — op `channel` — node "Slack2" (id `3866b373-9e08-4090-acf2-51c09c0377fd`)
- *(dynamic channel)* — op `channel` — node "Send a message1" (id `4b7ac2a8-d08c-4c6f-b6fa-f111105475fa`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
