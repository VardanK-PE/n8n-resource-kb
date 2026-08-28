---
n8n_id: "ODD88GwGlwvoAm4B"
instance: v1
name: "Supermove Late Payout Alerts"
status: active
last_modified: 2025-11-20T18:38:53.302Z
tags: []
fingerprint: "f6bf20d69a9b8a3359d3ab22ea4b1873d418d646ff6baea5c08b18df46a9714c"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Supermove Late Payout Alerts

## Summary

- **Status:** active
- **n8n ID:** `ODD88GwGlwvoAm4B`
- **Nodes:** 5
- **Last modified:** 2025-11-20T18:38:53.302Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `52975cc1-df34-4187-9840-eeb61b7f2f39`) — `0 13 * * *`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `389ad05b-9e92-4123-845b-cfab2bbcc002`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Slack" (id `5f93c5fe-c066-42c4-abbd-347bb302839e`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `389ad05b-9e92-4123-845b-cfab2bbcc002`)

### Slack channels

- [[../resources/slack-channels/c072d0nfhd5|supermove-transaction-alerts]] (id `C072D0NFHD5`) — op `channel` — node "Slack" (id `5f93c5fe-c066-42c4-abbd-347bb302839e`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
