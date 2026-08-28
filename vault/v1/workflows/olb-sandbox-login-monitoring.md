---
n8n_id: "Dmc22YVXED9bDeZb"
instance: v1
name: "OLB Sandbox Login Monitoring"
status: active
last_modified: 2024-10-25T17:20:00.921Z
tags: []
fingerprint: "82a175b7549554c1aad27c393220b58788c948ae95f1b9a5e1364af004b3852c"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# OLB Sandbox Login Monitoring

## Summary

- **Status:** active
- **n8n ID:** `Dmc22YVXED9bDeZb`
- **Nodes:** 4
- **Last modified:** 2024-10-25T17:20:00.921Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `8252cedb-478f-442d-b97b-76c400a958c4`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `09c3a496-4304-4a5f-95ad-2ac3ec94f7c2`)
- [[../resources/credentials/6gbwfpl6n9qz81ho|Postgres account 2]] (`postgres`, id `6GBwfPL6n9QZ81ho`) — node "Postgres" (id `0c952a62-4703-4454-ba53-7216bfd8d7df`)

### Databases

- [[../resources/databases/postgres-6gbwfpl6n9qz81ho|postgres (via Postgres account 2)]] — op `executeQuery` — node "Postgres" (id `0c952a62-4703-4454-ba53-7216bfd8d7df`)

### Slack channels

- [[../resources/slack-channels/c0725s1rwu9|partner-monitoring-alerts]] (id `C0725S1RWU9`) — op `channel` — node "Slack" (id `09c3a496-4304-4a5f-95ad-2ac3ec94f7c2`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
