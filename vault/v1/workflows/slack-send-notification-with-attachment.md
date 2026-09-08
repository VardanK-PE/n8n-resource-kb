---
n8n_id: "Ldmb0W2Y8CtaZtTM"
instance: v1
name: "Slack - Send notification with attachment"
status: inactive
last_modified: 2026-09-08T19:04:40.738Z
tags: []
fingerprint: "bf076acc05be5b0d9efe8866aa30a14c933d02fc024a078286564f4f586665eb"
auto_generated_at: 2026-09-08T19:06:15Z
---

<!-- auto:start -->

# Slack - Send notification with attachment

## Summary

- **Status:** inactive
- **n8n ID:** `Ldmb0W2Y8CtaZtTM`
- **Nodes:** 22
- **Last modified:** 2026-09-08T19:04:40.738Z

## Triggers

- **manual** — node "When clicking 'Execute workflow'" (id `4478e5e7-78f6-40f7-9d55-debf9b68d4ee`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `63024c68-6b90-4bfe-96de-c6a06dfb7714`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file" (id `07d40daa-5aaa-48cd-ada6-5986cda44572`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Supermove: Send a message" (id `0b5a0e43-de20-403b-af9b-32194b329be6`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "PE: Send a message" (id `5d341407-a34a-4be6-8cac-24de3f98965b`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Hearth: Send a message" (id `963213da-0ee5-40d5-8aa2-ae2f33a51766`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Supermove: Send a message" (id `0b5a0e43-de20-403b-af9b-32194b329be6`)
- *(dynamic channel)* — op `channel` — node "PE: Send a message" (id `5d341407-a34a-4be6-8cac-24de3f98965b`)
- *(dynamic channel)* — op `channel` — node "Hearth: Send a message" (id `963213da-0ee5-40d5-8aa2-ae2f33a51766`)

### Sub-workflows (Execute Workflow calls)

- [[slack-send-notification-with-attachment|Slack - Send notification with attachment]] (n8n_id `Ldmb0W2Y8CtaZtTM`) — node "A: upload + echo" (id `030397bb-3a28-4821-b9c6-805114b9657b`)
- [[slack-send-notification-with-attachment|Slack - Send notification with attachment]] (n8n_id `Ldmb0W2Y8CtaZtTM`) — node "D: bad binary field" (id `6c5440a5-7b2d-49ef-98bf-935764b96ea6`)
- [[slack-send-notification-with-attachment|Slack - Send notification with attachment]] (n8n_id `Ldmb0W2Y8CtaZtTM`) — node "B: baseline (today)" (id `8f14894c-a80e-4f91-aa89-39e8fa2e3944`)
- [[slack-send-notification-with-attachment|Slack - Send notification with attachment]] (n8n_id `Ldmb0W2Y8CtaZtTM`) — node "C: passthrough only" (id `d2c0aedb-cf00-4df1-bcb5-50e3ed1a572f`)

## Used by (workflows)

- [[elavon-cco-enrollment-monitor|Elavon CCO - Enrollment Monitor]] — node "Post evidence to Slack" (id `11110000-0000-4000-8000-000000000015`)
- [[slack-send-notification-with-attachment|Slack - Send notification with attachment]] — node "A: upload + echo" (id `030397bb-3a28-4821-b9c6-805114b9657b`)
- [[slack-send-notification-with-attachment|Slack - Send notification with attachment]] — node "B: baseline (today)" (id `8f14894c-a80e-4f91-aa89-39e8fa2e3944`)
- [[slack-send-notification-with-attachment|Slack - Send notification with attachment]] — node "C: passthrough only" (id `d2c0aedb-cf00-4df1-bcb5-50e3ed1a572f`)
- [[slack-send-notification-with-attachment|Slack - Send notification with attachment]] — node "D: bad binary field" (id `6c5440a5-7b2d-49ef-98bf-935764b96ea6`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
