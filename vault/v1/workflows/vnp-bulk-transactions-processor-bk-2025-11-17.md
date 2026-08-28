---
n8n_id: "75YuTt4Jprz6WHM8"
name: "VNP Bulk Transactions Processor BK 2025-11-17"
status: inactive
last_modified: 2025-11-17T16:15:04.657Z
tags: []
fingerprint: "67d76c15e48e51f94cb4ef79a632cfd161aa21298d0d3fd6219324af93694d2c"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# VNP Bulk Transactions Processor BK 2025-11-17

## Summary

- **Status:** inactive
- **n8n ID:** `75YuTt4Jprz6WHM8`
- **Nodes:** 44
- **Last modified:** 2025-11-17T16:15:04.657Z

## Triggers

- **error** — node "Error Trigger" (id `258a860b-3bf5-4e45-8f2e-8d96328e5756`)
- **schedule** — node "Schedule Trigger" (id `43a1dece-b6c2-45a0-b74a-55cd24b93e04`) — `every 1 minute(s)`
- **manual** — node "When clicking ‘Execute workflow’" (id `c580838d-e0f8-4695-b0f5-b6954a20dca5`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Reservations to Skip" (id `17c441de-c2d0-4edc-aa68-2b343ee250d4`)
- [[../resources/credentials/jznf5gj6ezv9mvmj|VNP PE SFTP]] (`sftp`, id `jZNf5gj6Ezv9MvMJ`) — node "FTP" (id `27154a84-e185-4399-8c4e-8c17561ea41c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `2a0679a0-dc04-498b-90b2-f52e135fea88`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Prod Transaction" (id `2dec6fcf-960c-45a1-84db-728f1060b19e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `38fd9bea-a52b-484d-8fb9-6d9020af4fb4`)
- [[../resources/credentials/jznf5gj6ezv9mvmj|VNP PE SFTP]] (`sftp`, id `jZNf5gj6Ezv9MvMJ`) — node "Get the filenames" (id `396adc3e-0bc1-4d6e-b07b-04bee387e751`)
- [[../resources/credentials/wwm73d114letbuus|n8n-service-account Google Service Account account]] (`googleApi`, id `wwm73D114LETBUUS`) — node "Create spreadsheet" (id `3e13c908-02d4-47ca-adb4-4bf4c0f62441`)
- [[../resources/credentials/jznf5gj6ezv9mvmj|VNP PE SFTP]] (`sftp`, id `jZNf5gj6Ezv9MvMJ`) — node "Move to processing directory" (id `5f51d0d6-e8c9-4ca9-a5dc-f2adfde95f43`)
- [[../resources/credentials/vjyobgaeh30bqna6|n8nio-pg]] (`n8nApi`, id `vJyOBgaEh30bQnA6`) — node "Get many executions" (id `6c9e9143-05ce-4047-80e5-c9c40b9717f3`)
- [[../resources/credentials/jznf5gj6ezv9mvmj|VNP PE SFTP]] (`sftp`, id `jZNf5gj6Ezv9MvMJ`) — node "Move to processed Directory" (id `71e9a346-4dd1-41e0-ab08-eb8baab3349d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `9cc83cf1-7a85-4093-9e01-149639ae7e95`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Test Card" (id `a61eeead-ebee-4549-b0bb-ae4694d4600f`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Prod Data" (id `ad40a2c8-cf8e-4eae-9c75-f65e04214adf`)
- [[../resources/credentials/v1uawpenaoqnxu0i|PE PROD PGP Key]] (`pgpCredentialsApi`, id `v1UAWPENaoQnxu0I`) — node "PGP1" (id `d2da2fa4-f6e3-4298-a56a-dfb09fef6651`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file" (id `d5628599-2e0d-4eca-9f8a-da6b0d114c11`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Test Transaction" (id `dfd29563-9af2-484e-b93e-82167268f722`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create GSheet" (id `e2bd9a5c-c305-4b56-975a-ae7705de6454`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `e3294aab-f1a2-4e07-a15e-3da0bbb17bee`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `e558bae8-05e2-44a1-bf01-1538613d5a77`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Move to VNP Folder" (id `e5b332a7-f1b1-4b58-8eeb-4eaf59aa692c`)
- [[../resources/credentials/vjyobgaeh30bqna6|n8nio-pg]] (`n8nApi`, id `vJyOBgaEh30bQnA6`) — node "Delete an execution" (id `ea4e6967-4f79-4f87-8541-d82dff205568`)
- [[../resources/credentials/jznf5gj6ezv9mvmj|VNP PE SFTP]] (`sftp`, id `jZNf5gj6Ezv9MvMJ`) — node "FTP1" (id `fa0a25f1-1fae-4e2d-9593-922f0529cf96`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/payment/sale` — node "Prod Transaction" (id `2dec6fcf-960c-45a1-84db-728f1060b19e`)
- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/cards` — node "Test Card" (id `a61eeead-ebee-4549-b0bb-ae4694d4600f`)
- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/cards` — node "Prod Data" (id `ad40a2c8-cf8e-4eae-9c75-f65e04214adf`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/payment/sale` — node "Test Transaction" (id `dfd29563-9af2-484e-b93e-82167268f722`)

### Custom / community nodes

- [[../resources/custom-nodes/-xzcutable-n8n-nodes-pgp|@xzcutable/n8n-nodes-pgp]] — type `@xzcutable/n8n-nodes-pgp.pgpNode` — node "PGP1" (id `d2da2fa4-f6e3-4298-a56a-dfb09fef6651`)

### Google Sheets

- [[../resources/google-sheets/1hqcuntrajjv1ywtfjwjyviqijawzcoz1oky40ixar5o|transactions_to_skip_20251029_143022.csv]] (id `1hQCUnTRajjv1ywtfJwJyVIqIJAwZCOZ1Oky40ixAR5o`) — op `?`, tab `Sheet1` — node "Reservations to Skip" (id `17c441de-c2d0-4edc-aa68-2b343ee250d4`)
- *(dynamic spreadsheet)* — op `append`, tab `0` — node "Append row in sheet" (id `38fd9bea-a52b-484d-8fb9-6d9020af4fb4`)

### Google Drive

- *(dynamic)* — op `download` — node "Download file" (id `2a0679a0-dc04-498b-90b2-f52e135fea88`)
- [[../resources/google-drive/root|/ (Root folder)]] (`folder`, id `root`) — op `?` — node "Upload file" (id `d5628599-2e0d-4eca-9f8a-da6b0d114c11`)
- *(dynamic)* — op `move` — node "Move to VNP Folder" (id `e5b332a7-f1b1-4b58-8eeb-4eaf59aa692c`)
- [[../resources/google-drive/1rm2cwl05ui-voqagikfpynf1cfngv8gb|VNP ISV Data]] (`folder`, id `1RM2cWL05uI_VoqaGIkfpyNF1cfNgV8GB`) — op `move` — node "Move to VNP Folder" (id `e5b332a7-f1b1-4b58-8eeb-4eaf59aa692c`)

### Slack channels

- [[../resources/slack-channels/c09p9rk9nh1|vnp-merchant-alerts]] (id `C09P9RK9NH1`) — op `channel` — node "Send a message" (id `9cc83cf1-7a85-4093-9e01-149639ae7e95`)
- [[../resources/slack-channels/c09p9rk9nh1|vnp-merchant-alerts]] (id `C09P9RK9NH1`) — op `channel` — node "Send a message6" (id `e3294aab-f1a2-4e07-a15e-3da0bbb17bee`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `e558bae8-05e2-44a1-bf01-1538613d5a77`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
