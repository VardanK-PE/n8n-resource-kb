---
n8n_id: "WZ3gVX06CoEoAmzr"
instance: v1
name: "Daily Onboarding Alerts"
status: active
last_modified: 2024-10-25T17:19:11.739Z
tags: []
fingerprint: "4e508dad407127980af2effff7e0205ce267131724de0609250cb743fd989cca"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Daily Onboarding Alerts

## Summary

- **Status:** active
- **n8n ID:** `WZ3gVX06CoEoAmzr`
- **Nodes:** 10
- **Last modified:** 2024-10-25T17:19:11.739Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `b85d7f1b-0c74-4a78-b472-ed2ff6c08e7a`) — `daily at 6:00, daily at 11:00, daily at 15:00, daily at 17:00`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack Message with Pending Applications" (id `4a218d88-d712-483b-97b9-fc9b5cc6ecb1`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack Message with Applications Pending Additional Info" (id `8141d433-fdeb-4602-98bd-903f10827538`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Pending Applications" (id `91b6aa5a-8aa7-400e-8976-a67492060cec`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Pending Applications" (id `91b6aa5a-8aa7-400e-8976-a67492060cec`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "FormattedText" (id `51b1d062-beb6-423b-acd9-cfd87ed94902`)

### Slack channels

- [[../resources/slack-channels/c076s747zaa|onboarding-daily-reports]] (id `C076S747ZAA`) — op `channel` — node "Slack Message with Pending Applications" (id `4a218d88-d712-483b-97b9-fc9b5cc6ecb1`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
