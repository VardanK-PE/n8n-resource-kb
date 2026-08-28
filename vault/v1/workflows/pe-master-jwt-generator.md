---
n8n_id: "wPVryk5tt2miLmOV"
instance: v1
name: "PE Master JWT Generator"
status: inactive
last_modified: 2026-01-16T17:23:41.164Z
tags: []
fingerprint: "c9a930c0286c49d30dc318b93949f8a65d27c9b5e683dee8a1c47f66d5600f97"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PE Master JWT Generator

## Summary

- **Status:** inactive
- **n8n ID:** `wPVryk5tt2miLmOV`
- **Nodes:** 8
- **Last modified:** 2026-01-16T17:23:41.164Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `af79dd5a-b7d3-45ba-8e51-82a9075c2ce0`)

## Depends on

### Credentials

- [[../resources/credentials/gpttftxjlozfb2xw|Test Master Bearer Auth]] (`httpBearerAuth`, id `gPttFTXJLozFB2xW`) — node "Test Master API (get merchants endpoint)" (id `25590fdb-6600-4750-bc6d-6bdb55cc6e12`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "JWT" (id `3b24a79c-99c3-43ea-b8af-b0824f1e4e59`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "JWT1" (id `64207553-440b-4ade-8698-2c0ac7240e6c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `81ccf62c-108e-48f7-8173-95ea8adab0be`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants?page=1&status=submitted_to_pe&sub_status=a&account=4c971cc5-4664-4286-8a98-e9e327c768d3&q=&size=100` — node "Test Master API (get merchants endpoint)" (id `25590fdb-6600-4750-bc6d-6bdb55cc6e12`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
