---
n8n_id: "OpUQfwveuLHARiR5"
name: "Residuals Downloader"
status: active
last_modified: 2025-12-25T18:41:07.159Z
tags: []
fingerprint: "bc170be47f64ff48200e31f56cb90511c1d81de8bb8f3812cbbad82892dcdebb"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Residuals Downloader

## Summary

- **Status:** active
- **n8n ID:** `OpUQfwveuLHARiR5`
- **Nodes:** 18
- **Last modified:** 2025-12-25T18:41:07.159Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `cef772c8-0307-4048-ad9f-c4ce456b920a`)
- **webhook** — node "Webhook Trigger" (id `ff483881-a245-4624-9b28-1a0151b7860d`) — POST `residuals-download`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create Parent Folder" (id `0878fcdf-4034-4eff-b78f-7204010fde01`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create Sources Folder" (id `1a4bf617-6219-4bbe-8756-73f2359e9ede`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get a message" (id `3024d1f6-f57b-42f9-bc26-0d36699b0c58`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail" (id `41e13e48-8359-4352-92e8-2d03fb1199dd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file" (id `5ba0be0a-37f9-49b6-8c15-0a0abf1b5409`)

### Google Drive

- [[../resources/google-drive/1qbvieb-iqf7pp1tndtqm4yyilboj6chh|PF Residual Reports V2]] (`folder`, id `1qBviEB_iqF7pP1TndtQM4YYILBoj6cHh`) — op `?` — node "Create Parent Folder" (id `0878fcdf-4034-4eff-b78f-7204010fde01`)
- *(dynamic)* — op `?` — node "Create Sources Folder" (id `1a4bf617-6219-4bbe-8756-73f2359e9ede`)
- *(dynamic)* — op `?` — node "Upload file" (id `5ba0be0a-37f9-49b6-8c15-0a0abf1b5409`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
