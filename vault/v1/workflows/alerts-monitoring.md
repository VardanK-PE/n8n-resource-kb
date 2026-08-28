---
n8n_id: "1n9bQ5pCEIL0oC2m"
instance: v1
name: "Alerts Monitoring"
status: inactive
last_modified: 2025-10-03T18:02:41.524Z
tags: []
fingerprint: "06147f1e9e99625513e366bea36c01e94ef2c00e8a1e2ee4fc7b02856111721d"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Alerts Monitoring

## Summary

- **Status:** inactive
- **n8n ID:** `1n9bQ5pCEIL0oC2m`
- **Nodes:** 6
- **Last modified:** 2025-10-03T18:02:41.524Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `39b260d2-9b61-4ba1-9d1e-4029be7d389f`)
- **schedule** — node "Schedule Trigger" (id `543abace-c5fa-456e-ab12-12119a3ffa1f`) — `daily at 9:00`

## Depends on

### Credentials

- [[../resources/credentials/tltmd1qdsyyj7k0p|PE Slack User Bot (Spartak)]] (`slackOAuth2Api`, id `TLtmD1QDsyYj7k0P`) — node "Send a message" (id `5d3a6450-58d9-42fd-8fc5-93ac6effe8e5`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `911b474c-1f82-4f5c-9d9f-301de08a07d9`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `911b474c-1f82-4f5c-9d9f-301de08a07d9`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
