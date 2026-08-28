---
n8n_id: "sKQuQS8JhtyGGc4b"
name: "SGv1 TTP"
status: active
last_modified: 2024-12-14T22:09:21.443Z
tags:
  - "daily reports"
fingerprint: "b7909e3fe9f4b49c84cd99fa376e299573a18e9eaf678d5d7e44efde7e72f1ac"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# SGv1 TTP

## Summary

- **Status:** active
- **n8n ID:** `sKQuQS8JhtyGGc4b`
- **Nodes:** 4
- **Last modified:** 2024-12-14T22:09:21.443Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `cc876e99-1a74-43cc-8029-da61eced84ed`) — `every 24 hour(s)`

## Depends on

### Credentials

- [[../resources/credentials/ofbbh6yyak1p8fhf|ShaTestn8n]] (`slackOAuth2Api`, id `ofBbh6yYak1p8FHf`) — node "Slack" (id `90cda2ee-6448-4f11-9cb6-eb4d965a92cf`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `ee8a7b10-a22e-457f-937c-9ab4c3448068`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `ee8a7b10-a22e-457f-937c-9ab4c3448068`)

### Slack channels

- [[../resources/slack-channels/c0845g6bml7|ttp]] (id `C0845G6BML7`) — op `channel` — node "Slack" (id `90cda2ee-6448-4f11-9cb6-eb4d965a92cf`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
