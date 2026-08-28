---
n8n_id: "QjGNbzyqbzyX52ia"
instance: v1
name: "Monthly Accounts Receivable Reports"
status: active
last_modified: 2025-07-10T14:55:39.940Z
tags: []
fingerprint: "ab188a1882d0392b64cc6a3037c1e346e45310cd32a50a423099e6fc3a4b4b75"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Monthly Accounts Receivable Reports

## Summary

- **Status:** active
- **n8n ID:** `QjGNbzyqbzyX52ia`
- **Nodes:** 11
- **Last modified:** 2025-07-10T14:55:39.940Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `09b27d46-56ee-4040-9ac9-eb0efcc450c0`)
- **schedule** — node "Schedule Trigger" (id `13c3261b-0f0f-40d7-9c6c-7a9728930380`) — `every 1 month(s)`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `247e9252-88f2-4735-9554-1555a0a50c0a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `51269420-ed6f-460a-a57b-f7aba9fb67b7`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `6e3e59ff-606e-4c86-85d8-34382ea709e4`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `c3a93832-1184-41f0-a5d6-d64e610d4ab5`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `6e3e59ff-606e-4c86-85d8-34382ea709e4`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `c3a93832-1184-41f0-a5d6-d64e610d4ab5`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
