---
n8n_id: "LtFlmLE3illZ7fsL"
name: "Service-Titan Failed Payments (sandox)"
status: active
last_modified: 2025-04-23T22:29:08.591Z
tags: []
fingerprint: "f8acf0c844a682920a7752cc104e9869c7933df1c7dc3c025eaf277cc12c0b44"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Service-Titan Failed Payments (sandox)

## Summary

- **Status:** active
- **n8n ID:** `LtFlmLE3illZ7fsL`
- **Nodes:** 4
- **Last modified:** 2025-04-23T22:29:08.591Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `16b57589-f0d7-42bb-ba1f-1d8e5a0ea0d1`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `5868be9f-817e-4586-a757-42eca7da66ee`)
- [[../resources/credentials/6gbwfpl6n9qz81ho|Postgres Sandbox-Live]] (`postgres`, id `6GBwfPL6n9QZ81ho`) — node "Postgres" (id `7039d945-251a-4291-8b29-ab6948421c15`)

### Databases

- [[../resources/databases/postgres-6gbwfpl6n9qz81ho|postgres (via Postgres Sandbox-Live)]] — op `executeQuery` — node "Postgres" (id `7039d945-251a-4291-8b29-ab6948421c15`)

### Slack channels

- [[../resources/slack-channels/c08pgszkedr|st-payment-failures-sandbox]] (id `C08PGSZKEDR`) — op `channel` — node "Slack" (id `5868be9f-817e-4586-a757-42eca7da66ee`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
