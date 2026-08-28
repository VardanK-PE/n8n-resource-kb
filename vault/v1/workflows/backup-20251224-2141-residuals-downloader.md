---
n8n_id: "WOh7XTA5yAW7zqPI"
instance: v1
name: "[BACKUP 20251224_2141] Residuals Downloader"
status: inactive
last_modified: 2025-12-25T05:41:20.281Z
tags: []
fingerprint: "b928f3cf3d719127a6b08a7a4782fc3a99b926c3a55b09150e3b7fbc5586365b"
auto_generated_at: 2026-08-28T21:31:11Z
---

<!-- auto:start -->

# [BACKUP 20251224_2141] Residuals Downloader

## Summary

- **Status:** inactive
- **n8n ID:** `WOh7XTA5yAW7zqPI`
- **Nodes:** 17
- **Last modified:** 2025-12-25T05:41:20.281Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `cef772c8-0307-4048-ad9f-c4ce456b920a`)

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
