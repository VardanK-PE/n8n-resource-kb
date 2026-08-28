---
n8n_id: "TPdOZheQOL2iuJ3H"
instance: v1
name: "Corksy Events Log Monitor"
status: active
last_modified: 2025-05-04T15:57:35.827Z
tags: []
fingerprint: "5e5545c7f379c95bdf47056ff185d397145c8172c53a09bfda9263cd6a840519"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Corksy Events Log Monitor

## Summary

- **Status:** active
- **n8n ID:** `TPdOZheQOL2iuJ3H`
- **Nodes:** 5
- **Last modified:** 2025-05-04T15:57:35.827Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `64e30118-801f-4281-a81f-69309be6a7ed`) — `every 1 hour(s)`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `2e1ecf8a-ad7d-46d2-9bf8-b018a71f2562`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `530e1ee1-b868-4f55-8ac8-9fba321b37f8`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `8d1b2569-c8b8-47e8-bfb1-f0fad71745ae`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `530e1ee1-b868-4f55-8ac8-9fba321b37f8`)

### Slack channels

- [[../resources/slack-channels/c08r5h3hp6v|corksy-event-logs]] (id `C08R5H3HP6V`) — op `channel` — node "Slack" (id `2e1ecf8a-ad7d-46d2-9bf8-b018a71f2562`)
- [[../resources/slack-channels/c08r5h3hp6v|corksy-event-logs]] (id `C08R5H3HP6V`) — op `channel` — node "Slack1" (id `8d1b2569-c8b8-47e8-bfb1-f0fad71745ae`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
