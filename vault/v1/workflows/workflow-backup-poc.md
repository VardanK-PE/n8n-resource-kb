---
n8n_id: "OszFdkYQqIOX3AID"
name: "Workflow backup POC"
status: inactive
last_modified: 2025-09-19T15:23:56.825Z
tags: []
fingerprint: "6dc2c60d0d3c802b16cba4cd360af10a84cd61688097115285551e5ebd5da747"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Workflow backup POC

## Summary

- **Status:** inactive
- **n8n ID:** `OszFdkYQqIOX3AID`
- **Nodes:** 12
- **Last modified:** 2025-09-19T15:23:56.825Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `16f651e1-69b0-474f-8932-f8158307be1e`)
- **schedule** — node "Schedule Trigger" (id `2c478683-0077-4efe-93bc-5224ea047f17`) — `daily at 3:00`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get folders" (id `0c517a95-bd36-4c43-ad6e-952493c68a49`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create new folder" (id `2bb43d4d-a173-40b8-a7c1-2d9da33650f8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "delete folder" (id `5494162e-6fd8-4e55-8d2f-3b9dd029802d`)
- [[../resources/credentials/wwm73d114letbuus|n8n-service-account Google Service Account account]] (`googleApi`, id `wwm73D114LETBUUS`) — node "Upload workflow" (id `d65e48ba-ee8f-49b8-bf1c-f852edd08d48`)
- [[../resources/credentials/vjyobgaeh30bqna6|n8nio-pg]] (`n8nApi`, id `vJyOBgaEh30bQnA6`) — node "Get many workflows" (id `da9953a6-1d45-4e6b-bb0b-918c157db203`)

### Google Drive

- [[../resources/google-drive/root|/ (Root folder)]] (`folder`, id `root`) — op `?` — node "Create new folder" (id `2bb43d4d-a173-40b8-a7c1-2d9da33650f8`)
- *(dynamic)* — op `?` — node "Upload workflow" (id `d65e48ba-ee8f-49b8-bf1c-f852edd08d48`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
