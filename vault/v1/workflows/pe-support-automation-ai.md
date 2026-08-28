---
n8n_id: "3iWyLrdJlm1RBMsx"
instance: v1
name: "PE Support Automation AI"
status: inactive
last_modified: 2025-09-07T21:13:17.776Z
tags: []
fingerprint: "678859bb07bd38823f48b23c9f428cc19a737000dd28f062e2d328d09cbb7ddf"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PE Support Automation AI

## Summary

- **Status:** inactive
- **n8n ID:** `3iWyLrdJlm1RBMsx`
- **Nodes:** 22
- **Last modified:** 2025-09-07T21:13:17.776Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `65b39b8a-e2ac-4b4f-a76c-ab5cd0a1d37d`)

## Depends on

### Credentials

- [[../resources/credentials/tltmd1qdsyyj7k0p|PE Slack User Bot]] (`slackOAuth2Api`, id `TLtmD1QDsyYj7k0P`) — node "Get many channels" (id `0277d862-e286-4bda-a3c7-0de790db19c6`)
- [[../resources/credentials/tltmd1qdsyyj7k0p|PE Slack User Bot]] (`slackOAuth2Api`, id `TLtmD1QDsyYj7k0P`) — node "Search for messages1" (id `2ae8fcb2-aa9f-4620-8334-7f1f8730db64`)
- [[../resources/credentials/tltmd1qdsyyj7k0p|PE Slack User Bot]] (`slackOAuth2Api`, id `TLtmD1QDsyYj7k0P`) — node "Get a thread of messages posted to a channel" (id `3c9dfba5-e6c9-416c-8d49-b83db0d1f2e0`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "HTTP Request1" (id `420d77d2-647c-4618-895b-395dc9c20640`)
- [[../resources/credentials/tltmd1qdsyyj7k0p|PE Slack User Bot]] (`slackOAuth2Api`, id `TLtmD1QDsyYj7k0P`) — node "HTTP Request1" (id `420d77d2-647c-4618-895b-395dc9c20640`)
- [[../resources/credentials/tltmd1qdsyyj7k0p|PE Slack User Bot]] (`slackOAuth2Api`, id `TLtmD1QDsyYj7k0P`) — node "Get information about a user" (id `53d2c122-8b93-4132-8abb-50c924f76f0e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "HTTP Request" (id `e1049995-68d2-41a8-88cf-649f1a04e0ff`)
- [[../resources/credentials/tltmd1qdsyyj7k0p|PE Slack User Bot]] (`slackOAuth2Api`, id `TLtmD1QDsyYj7k0P`) — node "HTTP Request" (id `e1049995-68d2-41a8-88cf-649f1a04e0ff`)
- [[../resources/credentials/tltmd1qdsyyj7k0p|PE Slack User Bot]] (`slackOAuth2Api`, id `TLtmD1QDsyYj7k0P`) — node "Get the history of a channel1" (id `e1937bb3-fd07-4603-8f3b-4ecdb051d9d5`)
- [[../resources/credentials/tltmd1qdsyyj7k0p|PE Slack User Bot]] (`slackOAuth2Api`, id `TLtmD1QDsyYj7k0P`) — node "Search for messages" (id `f067a0e5-7a0e-4739-8103-5708b0ff84fd`)
- [[../resources/credentials/tltmd1qdsyyj7k0p|PE Slack User Bot]] (`slackOAuth2Api`, id `TLtmD1QDsyYj7k0P`) — node "Get the history of a channel" (id `f925cb0e-575c-4836-a718-d7fe5f6a4bb7`)
- [[../resources/credentials/tltmd1qdsyyj7k0p|PE Slack User Bot]] (`slackOAuth2Api`, id `TLtmD1QDsyYj7k0P`) — node "Get many users" (id `ff839c6f-bb67-46e3-b81e-43be11b35068`)

### HTTP URLs

- [[../resources/http-urls/slack-com|slack.com]] — `POST https://slack.com/api/assistant.search.context` — node "HTTP Request1" (id `420d77d2-647c-4618-895b-395dc9c20640`)
- [[../resources/http-urls/slack-com|slack.com]] — `GET https://slack.com/api/search.messages` — node "HTTP Request" (id `e1049995-68d2-41a8-88cf-649f1a04e0ff`)

### Slack channels

- *(dynamic channel)* — op `replies` — node "Get a thread of messages posted to a channel" (id `3c9dfba5-e6c9-416c-8d49-b83db0d1f2e0`)
- *(dynamic channel)* — op `history` — node "Get the history of a channel1" (id `e1937bb3-fd07-4603-8f3b-4ecdb051d9d5`)
- *(dynamic channel)* — op `history` — node "Get the history of a channel" (id `f925cb0e-575c-4836-a718-d7fe5f6a4bb7`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
