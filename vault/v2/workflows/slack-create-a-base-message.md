---
n8n_id: "3u0JNKt3eNJrK4rq"
instance: v2
name: "Slack - Create a base message"
status: active
last_modified: 2026-08-31T18:27:46.583Z
tags: []
fingerprint: "fe172a7a5108a2dbe340aa31dd5574e5d04f548aa86a9931dbaecafcf2e8a30b"
auto_generated_at: 2026-09-08T19:19:58Z
---

<!-- auto:start -->

# Slack - Create a base message

## Summary

- **Status:** active
- **n8n ID:** `3u0JNKt3eNJrK4rq`
- **Nodes:** 17
- **Last modified:** 2026-08-31T18:27:46.583Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `9a25a55f-c748-4de1-83d6-4c6289efb60d`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `e87dfaf9-d3af-4453-b83b-297fb52fb3f9`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Create a base message2" (id `1f4ef060-7180-49c1-b941-b699a8e7ff6e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Create a base message" (id `e0e65431-e8ad-4a9a-b14a-3145b24bdc16`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Create a base message1" (id `ee39b47a-92d1-4ce5-9632-b078b89ae0a7`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Create a base message2" (id `1f4ef060-7180-49c1-b941-b699a8e7ff6e`)
- *(dynamic channel)* — op `channel` — node "Create a base message" (id `e0e65431-e8ad-4a9a-b14a-3145b24bdc16`)
- *(dynamic channel)* — op `channel` — node "Create a base message1" (id `ee39b47a-92d1-4ce5-9632-b078b89ae0a7`)

### Sub-workflows (Execute Workflow calls)

- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `3u0JNKt3eNJrK4rq`) — node "Call 'Slack - Create a base message'" (id `3db0bc08-39d7-40fb-8182-16a94770d5c0`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `fMgQKiyw6jrmjIWq`) — node "Call 'Slack - Send notification'" (id `9fc26989-0e06-4e0b-b053-123403509ece`)

## Used by (workflows)

- [[gmail-send-html-email|Gmail - Send HTML Email]] — node "Call 'Slack - Create a base message'" (id `1006d16e-dfdd-4a95-b4c2-0525bbdafa72`)
- [[gmail-send-simple-text-email|Gmail - Send Simple Text Email]] — node "Call 'Slack - Create a base message'" (id `2b3064ae-6edb-4b15-b42a-1a2a85b5b3dd`)
- [[slack-create-a-base-message|Slack - Create a base message]] — node "Call 'Slack - Create a base message'" (id `3db0bc08-39d7-40fb-8182-16a94770d5c0`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
