---
n8n_id: "OpUQfwveuLHARiR5"
name: "Residuals Downloader"
status: active
last_modified: 2026-07-30T17:14:52.122Z
tags: []
fingerprint: "10ed271c8b06f1b0df2e9438c33909a76968f92517f3bda808ecda0925cbed20"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Residuals Downloader

## Summary

- **Status:** active
- **n8n ID:** `OpUQfwveuLHARiR5`
- **Nodes:** 23
- **Last modified:** 2026-07-30T17:14:52.122Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `cef772c8-0307-4048-ad9f-c4ce456b920a`)
- **webhook** — node "Webhook Trigger" (id `ff483881-a245-4624-9b28-1a0151b7860d`) — POST `residuals-download`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create Parent Folder" (id `0878fcdf-4034-4eff-b78f-7204010fde01`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create Sources Folder" (id `1a4bf617-6219-4bbe-8756-73f2359e9ede`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get a message" (id `3024d1f6-f57b-42f9-bc26-0d36699b0c58`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file" (id `38580511-4fcd-41d0-ab2a-01ebaf52c503`)
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
