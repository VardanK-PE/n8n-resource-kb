---
n8n_id: "NnibaCNcbHCTnsqh"
name: "Hearth - onboarding alerts"
status: active
last_modified: 2025-07-03T18:02:56.761Z
tags: []
fingerprint: "3192da7504bc6acdd301eb7bc1009f9b355ee0a185a6ce1ab3defa32d1e07a70"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Hearth - onboarding alerts

## Summary

- **Status:** active
- **n8n ID:** `NnibaCNcbHCTnsqh`
- **Nodes:** 13
- **Last modified:** 2025-07-03T18:02:56.761Z

## Triggers

- **other** — node "Kafka Trigger" (id `7de73cab-5fe0-44f0-b0bb-f5aabdbc2f83`)
- **other** — node "Kafka Trigger1" (id `a36900c0-7540-4131-a1d4-ee8eedde1214`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `1397c13f-4b65-4b8d-8755-787cb3df9e21`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Slack" (id `30400f74-e468-46a8-83f6-99a83584a472`)
- [[../resources/credentials/67fejotk4a3tgz6y|Kafka account]] (`kafka`, id `67fEjoTk4A3tGZ6Y`) — node "Kafka Trigger" (id `7de73cab-5fe0-44f0-b0bb-f5aabdbc2f83`)
- [[../resources/credentials/67fejotk4a3tgz6y|Kafka account]] (`kafka`, id `67fEjoTk4A3tGZ6Y`) — node "Kafka Trigger1" (id `a36900c0-7540-4131-a1d4-ee8eedde1214`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `1397c13f-4b65-4b8d-8755-787cb3df9e21`)

### Slack channels

- [[../resources/slack-channels/c08th33rpng|hearth-onboarding-alerts]] (id `C08TH33RPNG`) — op `channel` — node "Slack" (id `30400f74-e468-46a8-83f6-99a83584a472`)

### Kafka topics

- [[../resources/kafka-topics/merchant-status-changed|merchant_status_changed]] (`consumer`) — node "Kafka Trigger" (id `7de73cab-5fe0-44f0-b0bb-f5aabdbc2f83`)
- [[../resources/kafka-topics/merchant-created|merchant_created]] (`consumer`) — node "Kafka Trigger1" (id `a36900c0-7540-4131-a1d4-ee8eedde1214`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
