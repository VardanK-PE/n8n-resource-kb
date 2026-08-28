---
n8n_id: "vW224eaYGtanY6Je"
name: "Daily Onboarding Alerts copy SGv1"
status: inactive
last_modified: 2024-06-06T20:03:13.502Z
tags: []
fingerprint: "ac68a3be8f3da82dac1b67252c8ab744a95fbe57df9a85b6b0639bde7d8857f2"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Daily Onboarding Alerts copy SGv1

## Summary

- **Status:** inactive
- **n8n ID:** `vW224eaYGtanY6Je`
- **Nodes:** 4
- **Last modified:** 2024-06-06T20:03:13.502Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `f801e604-be0a-490d-8aa4-c5533f64239d`) — `daily at 6:00, daily at 11:00, daily at 15:00`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Pending Applications" (id `724dddb4-cf1a-4c08-93dd-4765d8a0b505`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `de8c2a7b-294b-4e13-bb60-ffb8188713e7`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Pending Applications" (id `724dddb4-cf1a-4c08-93dd-4765d8a0b505`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "FormattedText" (id `de7c95e0-4c62-4d77-9a35-a36b98edbcc7`)

### Slack channels

- [[../resources/slack-channels/c076s747zaa|onboarding-daily-reports]] (id `C076S747ZAA`) — op `channel` — node "Slack" (id `de8c2a7b-294b-4e13-bb60-ffb8188713e7`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
