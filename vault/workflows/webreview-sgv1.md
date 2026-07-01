---
n8n_id: "Lyl6QUD6yIFN6320"
name: "WebReview SGv1"
status: inactive
last_modified: 2024-06-08T23:56:56.861Z
tags: []
fingerprint: "9267cfee76f2257c04ffa3ccdb1d8a14c4769f19c950f896d1c28ea10ab14497"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# WebReview SGv1

## Summary

- **Status:** inactive
- **n8n ID:** `Lyl6QUD6yIFN6320`
- **Nodes:** 4
- **Last modified:** 2024-06-08T23:56:56.861Z

## Triggers

- **webhook** — node "Webhook" (id `01e10e6e-3929-4aa3-9fe0-cf499dc9ae1b`) — POST `b03ac366-e983-480a-b723-67fa3ccc5eaa`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `7ade2d51-265e-4574-9cb8-4458efdbca6a`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Pending Applications" (id `88434bd3-90cc-402d-a7b1-e4d0250bc3ac`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Pending Applications" (id `88434bd3-90cc-402d-a7b1-e4d0250bc3ac`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "FormattedText" (id `121d28c2-2b80-48e7-a960-869571ed1e47`)

### Slack channels

- [[../resources/slack-channels/c076s747zaa|onboarding-daily-reports]] (id `C076S747ZAA`) — op `channel` — node "Slack" (id `7ade2d51-265e-4574-9cb8-4458efdbca6a`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
