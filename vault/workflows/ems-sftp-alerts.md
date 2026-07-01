---
n8n_id: "iHredV3ioIIhaVfv"
name: "EMS_SFTP_Alerts"
status: active
last_modified: 2024-10-25T17:18:07.028Z
tags: []
fingerprint: "bd6110e89bb9af945d9b4a82df5f5cb7d8e5b627a45c46e5421a686234168eef"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# EMS_SFTP_Alerts

## Summary

- **Status:** active
- **n8n ID:** `iHredV3ioIIhaVfv`
- **Nodes:** 10
- **Last modified:** 2024-10-25T17:18:07.028Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `adc76d33-3485-4bed-a084-7ebed4c25df6`) — `every 6 hour(s)`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `16b91430-33df-48a0-ae0b-166e7afd2973`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `217c13f2-9a9e-42a7-b502-7d2fc2fe905d`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "EMSFiles" (id `27110f04-2cda-492e-9d89-c6585b4e9b58`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "EMSBatchData" (id `46dd2b0b-250b-4e28-a44f-a1acb88eea3c`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "EMSAchData" (id `65b99bae-5354-42ef-91ca-14b35b5172a2`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `a05f18e2-e479-4c57-8dc9-b6584744d0f7`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "EMSFiles" (id `27110f04-2cda-492e-9d89-c6585b4e9b58`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "EMSBatchData" (id `46dd2b0b-250b-4e28-a44f-a1acb88eea3c`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "EMSAchData" (id `65b99bae-5354-42ef-91ca-14b35b5172a2`)

### Slack channels

- [[../resources/slack-channels/c077w62bd7w|ops_alerts]] (id `C077W62BD7W`) — op `channel` — node "Slack" (id `16b91430-33df-48a0-ae0b-166e7afd2973`)
- [[../resources/slack-channels/c077w62bd7w|ops_alerts]] (id `C077W62BD7W`) — op `channel` — node "Slack1" (id `217c13f2-9a9e-42a7-b502-7d2fc2fe905d`)
- [[../resources/slack-channels/c077w62bd7w|ops_alerts]] (id `C077W62BD7W`) — op `channel` — node "Slack2" (id `a05f18e2-e479-4c57-8dc9-b6584744d0f7`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
