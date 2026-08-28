---
n8n_id: "kbTzKL7Gh8pcYRFO"
name: "Supermove onboarding alerts"
status: active
last_modified: 2024-11-27T21:48:34.400Z
tags: []
fingerprint: "0fcf32de8cc29d11121f64b2d246bd13e1c077dbbfac2e3ad965b82bf9a6f474"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Supermove onboarding alerts

## Summary

- **Status:** active
- **n8n ID:** `kbTzKL7Gh8pcYRFO`
- **Nodes:** 13
- **Last modified:** 2024-11-27T21:48:34.400Z

## Triggers

- **other** — node "Kafka Trigger" (id `5c611aee-a35e-4a94-addd-aab7de4d2ce2`)
- **other** — node "Kafka Trigger1" (id `b5553ed7-7e6b-46b6-8d01-ca247df28c3f`)

## Depends on

### Credentials

- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Slack" (id `45939b44-1645-46a1-a3dd-639caba04ea7`)
- [[../resources/credentials/67fejotk4a3tgz6y|Kafka account]] (`kafka`, id `67fEjoTk4A3tGZ6Y`) — node "Kafka Trigger" (id `5c611aee-a35e-4a94-addd-aab7de4d2ce2`)
- [[../resources/credentials/67fejotk4a3tgz6y|Kafka account]] (`kafka`, id `67fEjoTk4A3tGZ6Y`) — node "Kafka Trigger1" (id `b5553ed7-7e6b-46b6-8d01-ca247df28c3f`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `d787e80d-c097-4eef-8fd1-62eaf128bff2`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `d787e80d-c097-4eef-8fd1-62eaf128bff2`)

### Slack channels

- [[../resources/slack-channels/c07jkm5b4ax|supermove-onboarding-alerts]] (id `C07JKM5B4AX`) — op `channel` — node "Slack" (id `45939b44-1645-46a1-a3dd-639caba04ea7`)

### Kafka topics

- [[../resources/kafka-topics/merchant-status-changed|merchant_status_changed]] (`consumer`) — node "Kafka Trigger" (id `5c611aee-a35e-4a94-addd-aab7de4d2ce2`)
- [[../resources/kafka-topics/merchant-created|merchant_created]] (`consumer`) — node "Kafka Trigger1" (id `b5553ed7-7e6b-46b6-8d01-ca247df28c3f`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
