---
n8n_id: "YCgzvAdfFwGvRidX"
name: "VAPI Server"
status: active
last_modified: 2025-08-28T21:16:40.876Z
tags: []
fingerprint: "c4c49357762f5215f0295283b501a8f222bdf4b761f2d58d181f462ba4d6a6b5"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# VAPI Server

## Summary

- **Status:** active
- **n8n ID:** `YCgzvAdfFwGvRidX`
- **Nodes:** 15
- **Last modified:** 2025-08-28T21:16:40.876Z

## Triggers

- **webhook** — node "Webhook" (id `02299495-f227-40d1-bc52-5fb372c9616a`) — POST `bb72c65b-b8df-4550-93de-59bf1ac89c34`
- **manual** — node "When clicking ‘Execute workflow’" (id `5768fcf4-c090-4421-a7ec-d2c7edcd41eb`)
- **error** — node "Error Trigger" (id `b39565ac-24b5-4c9d-b1d9-9cd0ac34df68`)

## Depends on

### Credentials

- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Get Call Details1" (id `19b766fd-f9db-49c1-a915-1f234ddeb212`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Update Call Name" (id `59975dfb-bf2e-444e-8f92-2ac2ce6c3848`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Get Calls" (id `6376b445-df93-4da8-857c-1a68010aa75c`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Get Call Details" (id `6bac8068-e856-496e-965a-5aa1c8ee4d7c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `6dea35e4-ed5b-4d0e-95ae-d5e2cf5386f5`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `7536001f-5e49-468b-89bd-76a61a69d0cb`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message3" (id `883e8270-c53a-4649-98e7-0a749afdcb44`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `a63e286e-d1ac-4550-a8e0-8cafefb945f9`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message2" (id `aa4fe544-6d2f-48fd-a982-18c8fb4ffee5`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `ec1feedb-1832-4cfc-bb1d-01e6f8926ec8`)

### HTTP URLs

- [[../resources/http-urls/api-vapi-ai|api.vapi.ai]] — `GET https://api.vapi.ai/call/{{ $('Switch').item.json.body.message.call.id }}` — node "Get Call Details1" (id `19b766fd-f9db-49c1-a915-1f234ddeb212`)
- [[../resources/http-urls/api-vapi-ai|api.vapi.ai]] — `PATCH https://api.vapi.ai/call/{{ $('Switch').item.json.body.message.call.id }}` — node "Update Call Name" (id `59975dfb-bf2e-444e-8f92-2ac2ce6c3848`)
- [[../resources/http-urls/api-vapi-ai|api.vapi.ai]] — `GET https://api.vapi.ai/call` — node "Get Calls" (id `6376b445-df93-4da8-857c-1a68010aa75c`)
- [[../resources/http-urls/api-vapi-ai|api.vapi.ai]] — `GET https://api.vapi.ai/call/{{ $('Switch').item.json.body.message.call.id }}` — node "Get Call Details" (id `6bac8068-e856-496e-965a-5aa1c8ee4d7c`)

### Slack channels

- [[../resources/slack-channels/c09c1grese7|inbound-calls]] (id `C09C1GRESE7`) — op `channel` — node "Send a message" (id `6dea35e4-ed5b-4d0e-95ae-d5e2cf5386f5`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `7536001f-5e49-468b-89bd-76a61a69d0cb`)
- [[../resources/slack-channels/c09c1grese7|inbound-calls]] (id `C09C1GRESE7`) — op `channel` — node "Send a message3" (id `883e8270-c53a-4649-98e7-0a749afdcb44`)
- *(dynamic channel)* — op `channel` — node "Send a message2" (id `aa4fe544-6d2f-48fd-a982-18c8fb4ffee5`)
- *(dynamic channel)* — op `channel` — node "Send a message1" (id `ec1feedb-1832-4cfc-bb1d-01e6f8926ec8`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
