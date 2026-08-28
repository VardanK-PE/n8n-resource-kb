---
n8n_id: "4vhauPylbvMDJF06"
instance: v1
name: "PPD: Transaction Alerts"
status: active
last_modified: 2026-01-13T20:20:56.649Z
tags: []
fingerprint: "a272eb53077b76a3e30bdfdb016df907f267e676a3659ad685bb6dd5a1a7a04e"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PPD: Transaction Alerts

## Summary

- **Status:** active
- **n8n ID:** `4vhauPylbvMDJF06`
- **Nodes:** 10
- **Last modified:** 2026-01-13T20:20:56.649Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `1f2930dd-9d04-4295-a111-17481a34884d`) — `every 1 minute(s)`
- **error** — node "Error Trigger" (id `6771b604-459f-46ec-adcd-0d6da1ead2b3`)
- **manual** — node "When clicking ‘Execute workflow’" (id `cde07aa2-3276-4979-9e9b-e33a4e37d267`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `51ea5c04-f96e-4e16-85ae-f51946c27721`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `c3d01256-854c-44df-8fcd-6f66ebf69db3`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `fc55cd21-7042-4ac0-8be4-9486797d0445`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `fc55cd21-7042-4ac0-8be4-9486797d0445`)

### Slack channels

- [[../resources/slack-channels/c0a8n5un6fk|ppd-transaction-alert]] (id `C0A8N5UN6FK`) — op `channel` — node "Slack1" (id `51ea5c04-f96e-4e16-85ae-f51946c27721`)
- [[../resources/slack-channels/c09pc6hkhpy|payengine-ai-alerts]] (id `C09PC6HKHPY`) — op `channel` — node "Send a message5" (id `c3d01256-854c-44df-8fcd-6f66ebf69db3`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
