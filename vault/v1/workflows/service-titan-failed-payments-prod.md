---
n8n_id: "VlzWblqsB2b9Vfm0"
instance: v1
name: "Service-Titan Failed Payments (prod)"
status: active
last_modified: 2025-04-23T22:30:22.180Z
tags: []
fingerprint: "90a31d69dec2cc783fa1e4cc299f7686629546785065ac26f274121bfb075063"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Service-Titan Failed Payments (prod)

## Summary

- **Status:** active
- **n8n ID:** `VlzWblqsB2b9Vfm0`
- **Nodes:** 4
- **Last modified:** 2025-04-23T22:30:22.180Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `e622f342-ee5c-4f1d-8c12-fb6753ca8a29`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `0aa8259c-c5af-4289-8e99-a4e0a37b9e11`)
- [[../resources/credentials/rlxlkmcb9jzcnyyk|Postgres ST production read replica]] (`postgres`, id `rlXLkMcb9jzcnYYK`) — node "Postgres" (id `7631373d-1d00-4cd6-9b6d-81a316e9cd36`)

### Databases

- [[../resources/databases/postgres-rlxlkmcb9jzcnyyk|postgres (via Postgres ST production read replica)]] — op `executeQuery` — node "Postgres" (id `7631373d-1d00-4cd6-9b6d-81a316e9cd36`)

### Slack channels

- [[../resources/slack-channels/c08nyf47mup|st-payment-failures-prod]] (id `C08NYF47MUP`) — op `channel` — node "Slack" (id `0aa8259c-c5af-4289-8e99-a4e0a37b9e11`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
