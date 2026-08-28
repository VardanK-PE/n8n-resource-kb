---
n8n_id: "s0YYCt4gSCOJCbAl"
name: "VNP Bulk Transactions Processor"
status: active
last_modified: 2026-01-12T21:09:27.244Z
tags: []
fingerprint: "4ca9f243805fe7a70dbbbf691b844a4c1ee73fef5ddd9b546673db40b1848917"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# VNP Bulk Transactions Processor

## Summary

- **Status:** active
- **n8n ID:** `s0YYCt4gSCOJCbAl`
- **Nodes:** 60
- **Last modified:** 2026-01-12T21:09:27.244Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `0a4e133e-1f28-43cf-bbee-b2699803121a`)
- **schedule** — node "Schedule Trigger" (id `28e1f3a6-8a44-4d8b-b9b7-cda468f9fbac`) — `every 1 minute(s)`
- **schedule** — node "Schedule Trigger2" (id `342de82a-fca9-40cb-85eb-e5805df0ae59`) — `daily at 13:10`
- **error** — node "Error Trigger" (id `c7596d12-2a30-4293-a303-25a5bf5151ff`)
- **schedule** — node "Schedule Trigger1" (id `f4026497-b4fd-40b2-b99b-dc7a43c65072`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create GSheet" (id `0832f9a5-5377-4e82-b1e9-92ed8219df68`)
- [[../resources/credentials/vjyobgaeh30bqna6|n8nio-pg]] (`n8nApi`, id `vJyOBgaEh30bQnA6`) — node "Get many executions" (id `0aad090c-19ce-4b8c-94e0-f7d34fdfab89`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `24007e75-d900-4072-943f-d54b4e293c80`)
- [[../resources/credentials/v1uawpenaoqnxu0i|PE PROD PGP Key]] (`pgpCredentialsApi`, id `v1UAWPENaoQnxu0I`) — node "PGP1" (id `24dd3600-53dc-4776-9c56-57c3e16dbfe3`)
- [[../resources/credentials/jznf5gj6ezv9mvmj|VNP PE SFTP]] (`sftp`, id `jZNf5gj6Ezv9MvMJ`) — node "Move to processed Directory" (id `2a8b3f7b-ab05-477b-8e19-810bc3aded69`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `31bb2e83-7a4f-438a-9506-73633c03c3a7`)
- [[../resources/credentials/vjyobgaeh30bqna6|n8nio-pg]] (`n8nApi`, id `vJyOBgaEh30bQnA6`) — node "Delete an execution" (id `3c137fae-0f0f-45d6-9a3a-b8a29e19519b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Search files and folders2" (id `40e6898a-93e1-4e81-9baa-1b6afbc37342`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet1" (id `45618122-0c84-44a1-b7c4-9d7afeefadaa`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `4a15865b-c681-4753-ab96-5e1c6911270c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Search files and folders1" (id `4a4c8690-8034-4c1c-b8c9-ddb01c7a6f05`)
- [[../resources/credentials/wwm73d114letbuus|n8n-service-account Google Service Account account]] (`googleApi`, id `wwm73D114LETBUUS`) — node "Create spreadsheet" (id `4e4f6d1b-69f8-4450-9bf7-a6a66efd1703`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Test Transaction" (id `584330b0-e801-49f4-a8b8-99b9caf761f8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Search files and folders" (id `7fb3f811-6848-4616-8295-2a45d15aa6c8`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `8b1dd1a4-36ee-414e-9f10-d47636cdc1d3`)
- [[../resources/credentials/jznf5gj6ezv9mvmj|VNP PE SFTP]] (`sftp`, id `jZNf5gj6Ezv9MvMJ`) — node "Get the filenames" (id `95842c30-60fa-4f0c-9635-3a4bdfee518a`)
- [[../resources/credentials/jznf5gj6ezv9mvmj|VNP PE SFTP]] (`sftp`, id `jZNf5gj6Ezv9MvMJ`) — node "Move to processing directory" (id `9f30c900-c1e8-4fc1-b4d4-e418b0d4b458`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Move to VNP Folder" (id `a1cef033-82b5-4465-9cf1-57d78657906e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Share file" (id `a2690ba1-a112-49ad-8879-086baffd7574`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `aaca5ecc-f189-43ea-9ac6-25bcf5abb1e6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request" (id `aeb3402c-c195-4eb6-93d9-c75c629b9282`)
- [[../resources/credentials/jznf5gj6ezv9mvmj|VNP PE SFTP]] (`sftp`, id `jZNf5gj6Ezv9MvMJ`) — node "FTP" (id `b059dc40-b5d1-4918-b6e9-a98cbc9b1ded`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `b1e91079-8784-49ab-869c-e55fc0ba62f9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Reservations to Skip" (id `b2914be8-462f-40bb-b37c-fc25e6a13d5c`)
- [[../resources/credentials/jznf5gj6ezv9mvmj|VNP PE SFTP]] (`sftp`, id `jZNf5gj6Ezv9MvMJ`) — node "FTP1" (id `b495fb82-d896-4356-b641-b1cb8b635aa4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `c084ec1b-3cf4-44ce-b9c2-2531eb6fdd1e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Delete a file" (id `d75f1e00-5910-4160-8822-7dcec82aa584`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request1" (id `df2d4200-1053-46c7-b982-216fae3a0dd7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file" (id `e9fb65fb-c811-45c9-9ec7-ae8a808b341f`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Test Card" (id `f8f0f9d3-f145-42c5-bc0c-f73d27207f3a`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/payment/sale` — node "Test Transaction" (id `584330b0-e801-49f4-a8b8-99b9caf761f8`)
- [[../resources/http-urls/www-googleapis-com|www.googleapis.com]] — `POST https://www.googleapis.com/upload/drive/v3/files?uploadType=media` — node "HTTP Request" (id `aeb3402c-c195-4eb6-93d9-c75c629b9282`)
- [[../resources/http-urls/www-googleapis-com|www.googleapis.com]] — `POST https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart` — node "HTTP Request1" (id `df2d4200-1053-46c7-b982-216fae3a0dd7`)
- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/cards` — node "Test Card" (id `f8f0f9d3-f145-42c5-bc0c-f73d27207f3a`)

### Custom / community nodes

- [[../resources/custom-nodes/-xzcutable-n8n-nodes-pgp|@xzcutable/n8n-nodes-pgp]] — type `@xzcutable/n8n-nodes-pgp.pgpNode` — node "PGP1" (id `24dd3600-53dc-4776-9c56-57c3e16dbfe3`)

### Google Sheets

- *(dynamic spreadsheet)* — op `update`, tab `0` — node "Update row in sheet" (id `24007e75-d900-4072-943f-d54b4e293c80`)
- *(dynamic spreadsheet)* — op `append`, tab `0` — node "Append row in sheet1" (id `45618122-0c84-44a1-b7c4-9d7afeefadaa`)
- [[../resources/google-sheets/1hqcuntrajjv1ywtfjwjyviqijawzcoz1oky40ixar5o|transactions_to_skip_20251029_143022.csv]] (id `1hQCUnTRajjv1ywtfJwJyVIqIJAwZCOZ1Oky40ixAR5o`) — op `?`, tab `Sheet1` — node "Reservations to Skip" (id `b2914be8-462f-40bb-b37c-fc25e6a13d5c`)
- *(dynamic spreadsheet)* — op `?`, tab `0` — node "Get row(s) in sheet" (id `c084ec1b-3cf4-44ce-b9c2-2531eb6fdd1e`)

### Google Drive

- *(dynamic)* — op `download` — node "Download file" (id `4a15865b-c681-4753-ab96-5e1c6911270c`)
- *(dynamic)* — op `move` — node "Move to VNP Folder" (id `a1cef033-82b5-4465-9cf1-57d78657906e`)
- [[../resources/google-drive/1rm2cwl05ui-voqagikfpynf1cfngv8gb|VNP ISV Data]] (`folder`, id `1RM2cWL05uI_VoqaGIkfpyNF1cfNgV8GB`) — op `move` — node "Move to VNP Folder" (id `a1cef033-82b5-4465-9cf1-57d78657906e`)
- *(dynamic)* — op `share` — node "Share file" (id `a2690ba1-a112-49ad-8879-086baffd7574`)
- *(dynamic)* — op `deleteFile` — node "Delete a file" (id `d75f1e00-5910-4160-8822-7dcec82aa584`)
- [[../resources/google-drive/root|/ (Root folder)]] (`folder`, id `root`) — op `?` — node "Upload file" (id `e9fb65fb-c811-45c9-9ec7-ae8a808b341f`)

### Slack channels

- [[../resources/slack-channels/c09p9rk9nh1|vnp-merchant-alerts]] (id `C09P9RK9NH1`) — op `channel` — node "Send a message" (id `31bb2e83-7a4f-438a-9506-73633c03c3a7`)
- [[../resources/slack-channels/c09p9rk9nh1|vnp-merchant-alerts]] (id `C09P9RK9NH1`) — op `channel` — node "Send a message1" (id `8b1dd1a4-36ee-414e-9f10-d47636cdc1d3`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `aaca5ecc-f189-43ea-9ac6-25bcf5abb1e6`)
- [[../resources/slack-channels/c09p9rk9nh1|vnp-merchant-alerts]] (id `C09P9RK9NH1`) — op `channel` — node "Send a message6" (id `b1e91079-8784-49ab-869c-e55fc0ba62f9`)

### Sub-workflows (Execute Workflow calls)

- [[vnp-bulk-transactions-processor-perform-sale-with-tokenization-single-shot|VNP Bulk Transactions Processor: Perform Sale with Tokenization (Single Shot)]] (n8n_id `cdfm7KHD1A2WeYfb`) — node "Call VNP Bulk Transaction Perform Sale with Tokenization" (id `2acfb8f0-30e3-4fe9-b74d-cc62403323e7`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
