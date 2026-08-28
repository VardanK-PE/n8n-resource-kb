---
n8n_id: "sDWG4fBwq4dVRAq7"
instance: v1
name: "Tsys_SFTP_Alerts"
status: active
last_modified: 2024-10-25T17:19:08.074Z
tags: []
fingerprint: "cf32806d15c27574c00e5c606dbcc730bc7a19d0fde5f3d6390841b4ea5ff32e"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Tsys_SFTP_Alerts

## Summary

- **Status:** active
- **n8n ID:** `sDWG4fBwq4dVRAq7`
- **Nodes:** 7
- **Last modified:** 2024-10-25T17:19:08.074Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `38d9f9c1-4d6f-4cf1-a46f-5e7a0d640bb4`) — `every 1 hour(s)`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "TsysFiles" (id `11d4ae42-984b-4239-b32b-1f7366a17f28`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `7b7c33f9-194e-4e71-b1c2-da8b62559ea4`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `9599595d-8743-41c5-8f87-b211c92bcd3f`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "TsysBatchData" (id `ae04371c-1053-4ef0-9978-d456b5607b76`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "TsysFiles" (id `11d4ae42-984b-4239-b32b-1f7366a17f28`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "TsysBatchData" (id `ae04371c-1053-4ef0-9978-d456b5607b76`)

### Slack channels

- [[../resources/slack-channels/c077w62bd7w|ops_alerts]] (id `C077W62BD7W`) — op `channel` — node "Slack" (id `7b7c33f9-194e-4e71-b1c2-da8b62559ea4`)
- [[../resources/slack-channels/c077w62bd7w|ops_alerts]] (id `C077W62BD7W`) — op `channel` — node "Slack1" (id `9599595d-8743-41c5-8f87-b211c92bcd3f`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
