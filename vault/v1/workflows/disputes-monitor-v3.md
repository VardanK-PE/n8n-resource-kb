---
n8n_id: "KnfVEBen0SWqKIyS"
instance: v1
name: "Disputes Monitor V3"
status: active
last_modified: 2026-02-24T13:20:59.311Z
tags: []
fingerprint: "8beb706a8054af9380361096b04215cb5374a887a971d61d570190557b528529"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Disputes Monitor V3

## Summary

- **Status:** active
- **n8n ID:** `KnfVEBen0SWqKIyS`
- **Nodes:** 34
- **Last modified:** 2026-02-24T13:20:59.311Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `02a2b5ac-2156-4ed7-87b3-36d96c211563`)
- **manual** — node "When clicking ‘Execute workflow’" (id `8c4cf7be-3a91-43a8-a95e-5b0292db779e`)
- **schedule** — node "Schedule Trigger1" (id `b4bb7742-4a3a-429c-8a75-6991d973a756`) — `every 15 minute(s)`
- **error** — node "Error Trigger" (id `c31682c5-5c0e-4cde-9ba6-0d0187c6fc1c`)

## Depends on

### Credentials

- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get a message" (id `1c7d74cc-2d5d-4cbd-b9a3-e2179c6ccd67`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages" (id `2ecbcc35-ab2a-4315-acd3-2039f35ad894`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AllDisputes" (id `3e992c58-d0ac-4ecf-882d-3d10765ea387`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets8" (id `4433df79-880b-45d5-8991-922d69287b93`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `6576dd47-6e61-4dbb-8c01-a90bf0e24f9c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `703ba5c9-6f4d-413c-b89b-8fc917306df4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets7" (id `88abbef4-8c1e-4734-b3c9-1e411628513b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets12" (id `ab534bf6-c30a-4900-bc04-e061aa901f0a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload to GD" (id `bb3c3f6e-03cb-47fd-9928-f67e8e9b3766`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `c605fe65-e1a9-49b0-90e6-6f5ed756371e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets10" (id `ca98f7ef-09de-4b46-98d3-d61a2e56494a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets11" (id `d2e33898-528b-4e37-a7ca-bdcd296c6e74`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets9" (id `e9cb31ca-11ea-4808-95fe-32f57efa5abc`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AllDisputes" (id `3e992c58-d0ac-4ecf-882d-3d10765ea387`)

### Google Sheets

- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Google Sheets8" (id `4433df79-880b-45d5-8991-922d69287b93`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `appendOrUpdate`, tab `emails` — node "Google Sheets7" (id `88abbef4-8c1e-4734-b3c9-1e411628513b`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `update`, tab `emails` — node "Google Sheets12" (id `ab534bf6-c30a-4900-bc04-e061aa901f0a`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `appendOrUpdate`, tab `emails` — node "Google Sheets10" (id `ca98f7ef-09de-4b46-98d3-d61a2e56494a`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `appendOrUpdate`, tab `emails` — node "Google Sheets11" (id `d2e33898-528b-4e37-a7ca-bdcd296c6e74`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Google Sheets9" (id `e9cb31ca-11ea-4808-95fe-32f57efa5abc`)

### Google Drive

- [[../resources/google-drive/1-mkjjmvlephu8hzitd8jk-mblzpxyzfk|ELAVON_US]] (`folder`, id `1-MKJJmVLEPhu8HziTD8jk-mblZpXYzFK`) — op `?` — node "Upload to GD" (id `bb3c3f6e-03cb-47fd-9928-f67e8e9b3766`)

### Slack channels

- [[../resources/slack-channels/c077w62bd7w|ops_alerts]] (id `C077W62BD7W`) — op `channel` — node "Send a message" (id `6576dd47-6e61-4dbb-8c01-a90bf0e24f9c`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `703ba5c9-6f4d-413c-b89b-8fc917306df4`)
- [[../resources/slack-channels/c09pc6hkhpy|payengine-ai-alerts]] (id `C09PC6HKHPY`) — op `channel` — node "Send a message6" (id `c605fe65-e1a9-49b0-90e6-6f5ed756371e`)

### Sub-workflows (Execute Workflow calls)

- [[disputes-monitor-v3|Disputes Monitor V3]] (n8n_id `KnfVEBen0SWqKIyS`) — node "Execute Workflow1" (id `c6cf81fe-3bed-47da-ad14-ad4df9e1bc29`)

## Used by (workflows)

- [[disputes-monitor-v3|Disputes Monitor V3]] — node "Execute Workflow1" (id `c6cf81fe-3bed-47da-ad14-ad4df9e1bc29`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
