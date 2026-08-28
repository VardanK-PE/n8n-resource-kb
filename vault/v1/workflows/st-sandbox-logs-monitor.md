---
n8n_id: "lCngyFjfXKtEtC2I"
instance: v1
name: "ST Sandbox Logs Monitor"
status: inactive
last_modified: 2025-09-25T01:44:10.018Z
tags: []
fingerprint: "26a06b3b94c529d7dcf72681b6380bab5d7040fc075a0b59ab81ff02ed1de125"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# ST Sandbox Logs Monitor

## Summary

- **Status:** inactive
- **n8n ID:** `lCngyFjfXKtEtC2I`
- **Nodes:** 12
- **Last modified:** 2025-09-25T01:44:10.018Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `13817bea-0b7d-461a-9203-3f0f0e4f85a4`) — `every 15 second(s)`
- **manual** — node "When clicking ‘Test workflow’" (id `e76bda1d-711f-480c-82ac-d459be53b4bc`)

## Depends on

### Credentials

- [[../resources/credentials/6gbwfpl6n9qz81ho|Postgres Sandbox-Live]] (`postgres`, id `6GBwfPL6n9QZ81ho`) — node "Postgres" (id `6fe3fea5-2332-498d-96b5-e2e5cb95354a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `7114a05e-10f1-44aa-9127-fc42e087dd74`)
- [[../resources/credentials/6gbwfpl6n9qz81ho|Postgres Sandbox-Live]] (`postgres`, id `6GBwfPL6n9QZ81ho`) — node "Postgres2" (id `b31fcb5f-d6d4-4b3b-9301-8678f8173837`)
- [[../resources/credentials/6gbwfpl6n9qz81ho|Postgres Sandbox-Live]] (`postgres`, id `6GBwfPL6n9QZ81ho`) — node "Postgres1" (id `e3025fe2-e7e1-45f1-963e-954d230bc101`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `f2e8b147-ac16-4502-918d-04e296154417`)

### Databases

- [[../resources/databases/postgres-6gbwfpl6n9qz81ho|postgres (via Postgres Sandbox-Live)]] — op `executeQuery` — node "Postgres" (id `6fe3fea5-2332-498d-96b5-e2e5cb95354a`)
- [[../resources/databases/postgres-6gbwfpl6n9qz81ho|postgres (via Postgres Sandbox-Live)]] — op `executeQuery` — node "Postgres2" (id `b31fcb5f-d6d4-4b3b-9301-8678f8173837`)
- [[../resources/databases/postgres-6gbwfpl6n9qz81ho|postgres (via Postgres Sandbox-Live)]] — op `executeQuery` — node "Postgres1" (id `e3025fe2-e7e1-45f1-963e-954d230bc101`)

### Slack channels

- [[../resources/slack-channels/c08qjldrl1l|st-sandbox-event-logs]] (id `C08QJLDRL1L`) — op `channel` — node "Slack1" (id `7114a05e-10f1-44aa-9127-fc42e087dd74`)
- [[../resources/slack-channels/c08qjldrl1l|st-sandbox-event-logs]] (id `C08QJLDRL1L`) — op `channel` — node "Slack" (id `f2e8b147-ac16-4502-918d-04e296154417`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
