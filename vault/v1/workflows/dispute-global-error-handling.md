---
n8n_id: "KBN9sWK9juozY766"
instance: v1
name: "Dispute - Global error handling"
status: inactive
last_modified: 2025-12-22T20:29:34.195Z
tags: []
fingerprint: "cdea644ad876d842085e9958ff2384e2fa8c87fd8f7f8e13176ce85eae90fea1"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Dispute - Global error handling

## Summary

- **Status:** inactive
- **n8n ID:** `KBN9sWK9juozY766`
- **Nodes:** 3
- **Last modified:** 2025-12-22T20:29:34.195Z

## Triggers

- **error** — node "Error Trigger" (id `6dbbdf64-c37a-4874-a1d3-0fe009a8840a`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `81dcc222-a177-44ba-92a4-3ceda54c4e08`)

### Slack channels

- [[../resources/slack-channels/c08r8h75n15|dispute-alerts]] (id `C08R8H75N15`) — op `channel` — node "Send a message5" (id `81dcc222-a177-44ba-92a4-3ceda54c4e08`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
