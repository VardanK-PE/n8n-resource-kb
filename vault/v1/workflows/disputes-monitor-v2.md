---
n8n_id: "GmvzheDuY80pBHyy"
instance: v1
name: "Disputes Monitor V2"
status: inactive
last_modified: 2025-09-30T18:54:38.591Z
tags: []
fingerprint: "d47cbb2a62242adae4ca15a4570496d8e4c9544adbb8173e3350a823106788e4"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Disputes Monitor V2

## Summary

- **Status:** inactive
- **n8n ID:** `GmvzheDuY80pBHyy`
- **Nodes:** 72
- **Last modified:** 2025-09-30T18:54:38.591Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `3d7d7ede-fb99-444f-a1bc-dcbd6d16b0c9`)
- **manual** — node "When clicking ‘Execute workflow’" (id `824cc3c4-ba32-46c2-906d-5be70eb93460`)
- **schedule** — node "Schedule Trigger" (id `d702b7da-4eb6-4d8a-92e9-9ec7f0cb04ce`) — `every 1 hour(s)`
- **webhook** — node "Webhook" (id `ede4aeab-f879-49e6-bde1-c7f66571b3a8`) — GET `7a330012-4d7d-4d2a-8583-4d9722963932`

## Depends on

### Credentials

- [[../resources/credentials/wwm73d114letbuus|n8n-service-account Google Service Account account]] (`googleApi`, id `wwm73D114LETBUUS`) — node "Google Vision" (id `000bcdbb-b99a-4dde-9d47-b6512839fc06`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive" (id `045b0a8b-ab22-4fe1-af19-7034fe3d905d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `05b6cab2-5dde-41e6-9e6f-f55fd2825b67`)
- [[../resources/credentials/xvxjtkyqxpbm4zqg|Browserless (http://pf-prod-ecs-task-container-browserless:3000)]] (`httpQueryAuth`, id `xvXjTKYQxpBm4zQg`) — node "HTTP Request2" (id `093f0885-e94c-4403-84d3-1ff958a7a92a`)
- [[../resources/credentials/k6tv0fwwyxa8mcft|N8N 1Pass Connect Server Auth]] (`httpBearerAuth`, id `k6tV0FwwyXa8mcFt`) — node "1Pass Connect Server" (id `179bc73c-6b43-4cd8-92ef-82e6fd655c85`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail5" (id `19b918ab-87cd-407f-82b2-82903d75ad8c`)
- [[../resources/credentials/xvxjtkyqxpbm4zqg|Browserless (http://pf-prod-ecs-task-container-browserless:3000)]] (`httpQueryAuth`, id `xvXjTKYQxpBm4zQg`) — node "HTTP Request1" (id `2b25b5be-19f3-4bfa-bdbb-c36e7ef37dc5`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `2ee2778f-1e36-4027-8acc-687673cde2a9`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "DisputesAwaitingDetails1" (id `3312469b-d7c0-4a0a-8406-b09080e06122`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail6" (id `3fb65236-1d47-457b-b69a-8c2d852976a6`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail7" (id `4754709c-b80d-4342-b4f0-e5bc3aede31d`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail" (id `4886f093-bbc9-455b-bee9-2c7979d07d5c`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Logs" (id `4d269d36-2504-4324-b512-d0d681d7bd80`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `4ec36d48-f6e0-4429-ba2e-1d9a67a84534`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "DisputesAwaitingDetails" (id `5a29f77f-14d4-421a-8e29-c44508655886`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail8" (id `5d907f9a-9148-4c5e-b077-c415eaa85988`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail3" (id `7cd7befd-b2fa-4a77-b0b6-79493438b050`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail10" (id `8d4215db-c290-4f4b-b1bd-a85aa9bbdbd3`)
- [[../resources/credentials/xvxjtkyqxpbm4zqg|Browserless (http://pf-prod-ecs-task-container-browserless:3000)]] (`httpQueryAuth`, id `xvXjTKYQxpBm4zQg`) — node "HTTP Request" (id `9422714e-dfa8-41cf-9f4e-0d3674df72ea`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `acc29c5f-5aa0-4728-988d-9ec06621224b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `b1015aa6-5685-4ca3-93ad-d76fc238ac64`)
- [[../resources/credentials/3rcscrwjlewffwlr|n8n account]] (`n8nApi`, id `3RcscrwJleWFfWlR`) — node "n8n" (id `b18e3c65-40fb-48ae-9da5-4d0f5d30d660`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail2" (id `c22cc0f1-1e77-48f0-86f8-feab78b5b6db`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "AllDisputes" (id `c293aa97-1805-425a-ab35-f64528842ae9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `d16f7096-de1c-4285-91b2-672e6b5c6a74`)
- [[../resources/credentials/xvxjtkyqxpbm4zqg|Browserless (http://pf-prod-ecs-task-container-browserless:3000)]] (`httpQueryAuth`, id `xvXjTKYQxpBm4zQg`) — node "HTTP Request3" (id `d972f5f5-530c-4748-bae1-af375b67f425`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail1" (id `dedc8778-3997-465e-89b8-7f6f081d623a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive2" (id `df35822b-d126-4880-af37-5ca2d54f616e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets6" (id `e64eb059-49b6-444f-88db-f127747d216b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `f068c3a3-89ae-4595-bcef-54a39a573e3e`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail9" (id `f817a1b2-7df5-485a-a6df-5c436b718f63`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail4" (id `fcf45f97-cc29-49ed-935a-eb37468fa335`)

### HTTP URLs

- [[../resources/http-urls/vision-googleapis-com|vision.googleapis.com]] — `POST https://vision.googleapis.com/v1/files:annotate` — node "Google Vision" (id `000bcdbb-b99a-4dde-9d47-b6512839fc06`)
- [[../resources/http-urls/pf-prod-ecs-task-container-browserless-3000|pf-prod-ecs-task-container-browserless:3000]] — `POST http://pf-prod-ecs-task-container-browserless:3000/function` — node "HTTP Request2" (id `093f0885-e94c-4403-84d3-1ff958a7a92a`)
- *(dynamic URL)* — `GET ` — node "1Pass Connect Server" (id `179bc73c-6b43-4cd8-92ef-82e6fd655c85`)
- [[../resources/http-urls/pf-prod-ecs-task-container-browserless-3000|pf-prod-ecs-task-container-browserless:3000]] — `POST http://pf-prod-ecs-task-container-browserless:3000/screenshot` — node "HTTP Request1" (id `2b25b5be-19f3-4bfa-bdbb-c36e7ef37dc5`)
- [[../resources/http-urls/pf-prod-ecs-task-container-browserless-3000|pf-prod-ecs-task-container-browserless:3000]] — `POST http://pf-prod-ecs-task-container-browserless:3000/screenshot` — node "HTTP Request" (id `9422714e-dfa8-41cf-9f4e-0d3674df72ea`)
- [[../resources/http-urls/pf-prod-ecs-task-container-browserless-3000|pf-prod-ecs-task-container-browserless:3000]] — `POST http://pf-prod-ecs-task-container-browserless:3000/function` — node "HTTP Request3" (id `d972f5f5-530c-4748-bae1-af375b67f425`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "DisputesAwaitingDetails1" (id `3312469b-d7c0-4a0a-8406-b09080e06122`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Logs" (id `4d269d36-2504-4324-b512-d0d681d7bd80`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "DisputesAwaitingDetails" (id `5a29f77f-14d4-421a-8e29-c44508655886`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "AllDisputes" (id `c293aa97-1805-425a-ab35-f64528842ae9`)

### Google Sheets

- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `update`, tab `emails` — node "Google Sheets4" (id `05b6cab2-5dde-41e6-9e6f-f55fd2825b67`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `appendOrUpdate`, tab `emails` — node "Google Sheets" (id `4ec36d48-f6e0-4429-ba2e-1d9a67a84534`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `appendOrUpdate`, tab `emails` — node "Google Sheets2" (id `acc29c5f-5aa0-4728-988d-9ec06621224b`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `update`, tab `emails` — node "Google Sheets5" (id `b1015aa6-5685-4ca3-93ad-d76fc238ac64`)
- [[../resources/google-sheets/10yahywgavwbz5ln0aehguzxwp-hieevu7ii7ovj55gg|CISCO_MERCHANT_CREDENTIALS]] (id `10yAHYWgAvWBz5ln0aEhGuzxwP_HIeeVu7iI7ovJ55gg`) — op `?`, tab `Sheet1` — node "Google Sheets3" (id `d16f7096-de1c-4285-91b2-672e6b5c6a74`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `appendOrUpdate`, tab `emails` — node "Google Sheets6" (id `e64eb059-49b6-444f-88db-f127747d216b`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Google Sheets1" (id `f068c3a3-89ae-4595-bcef-54a39a573e3e`)

### Google Drive

- [[../resources/google-drive/1-mkjjmvlephu8hzitd8jk-mblzpxyzfk|ELAVON_US]] (`folder`, id `1-MKJJmVLEPhu8HziTD8jk-mblZpXYzFK`) — op `?` — node "Google Drive" (id `045b0a8b-ab22-4fe1-af19-7034fe3d905d`)
- [[../resources/google-drive/1ryhct0qod-uli9gibpvifludvtrf6ze0|DISPUTES_AUTOMATION_SCREENSHOTS]] (`folder`, id `1RYHct0QOD-ULi9GiBPviFlUDVTRF6zE0`) — op `?` — node "Google Drive2" (id `df35822b-d126-4880-af37-5ca2d54f616e`)

### Slack channels

- [[../resources/slack-channels/c092ruaq86q|disputes-automation]] (id `C092RUAQ86Q`) — op `channel` — node "Slack" (id `2ee2778f-1e36-4027-8acc-687673cde2a9`)

### Sub-workflows (Execute Workflow calls)

- [[disputes-monitor-v2|Disputes Monitor V2]] (n8n_id `GmvzheDuY80pBHyy`) — node "Execute Workflow" (id `9777a631-2a24-4deb-8776-391d3e251873`)

## Used by (workflows)

- [[disputes-monitor-v2|Disputes Monitor V2]] — node "Execute Workflow" (id `9777a631-2a24-4deb-8776-391d3e251873`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
