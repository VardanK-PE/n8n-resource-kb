---
n8n_id: "9OAYYzOeS4BoqQ5q"
instance: v1
name: "ST Prod Logs Monitor"
status: inactive
last_modified: 2025-09-25T14:38:22.074Z
tags: []
fingerprint: "9f382aa931dfe0f0a1b5d0ca3927f9ccddaaab5f6a4bfe166427185228ba0750"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# ST Prod Logs Monitor

## Summary

- **Status:** inactive
- **n8n ID:** `9OAYYzOeS4BoqQ5q`
- **Nodes:** 7
- **Last modified:** 2025-09-25T14:38:22.074Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `c7d9ece5-3a5b-4236-b39c-a63dba22a99b`) — `every 15 second(s)`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `1e8d18ac-d37e-476f-ad20-604a5915832b`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `9c1b6408-1690-422e-b945-67786b57958c`)
- [[../resources/credentials/rlxlkmcb9jzcnyyk|Postgres ST production read replica]] (`postgres`, id `rlXLkMcb9jzcnYYK`) — node "Postgres" (id `b8a0bd88-7b84-4f3b-a794-f83786bea116`)

### HTTP URLs

- [[../resources/http-urls/api-ipify-org|api.ipify.org]] — `GET https://api.ipify.org?format=json` — node "HTTP Request" (id `d8935fed-24ed-442f-8d96-a1f0032293f8`)

### Databases

- [[../resources/databases/postgres-rlxlkmcb9jzcnyyk|postgres (via Postgres ST production read replica)]] — op `executeQuery` — node "Postgres" (id `b8a0bd88-7b84-4f3b-a794-f83786bea116`)

### Slack channels

- [[../resources/slack-channels/c08r3tpsm33|st-prod-event-logs]] (id `C08R3TPSM33`) — op `channel` — node "Slack1" (id `1e8d18ac-d37e-476f-ad20-604a5915832b`)
- [[../resources/slack-channels/c08r3tpsm33|st-prod-event-logs]] (id `C08R3TPSM33`) — op `channel` — node "Slack" (id `9c1b6408-1690-422e-b945-67786b57958c`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
