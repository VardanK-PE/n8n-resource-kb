---
n8n_id: "IEzAJUkv41KuLjCB"
instance: v1
name: "Forte Gateway Auto-submitter V2"
status: active
last_modified: 2026-08-27T19:53:32.105Z
tags: []
fingerprint: "1a0b74f7c9105e316098ee579f0975056b7dda6754b2ec1b29c3064585855413"
auto_generated_at: 2026-08-28T21:13:05Z
---

<!-- auto:start -->

# Forte Gateway Auto-submitter V2

## Summary

- **Status:** active
- **n8n ID:** `IEzAJUkv41KuLjCB`
- **Nodes:** 89
- **Last modified:** 2026-08-27T19:53:32.105Z

## Triggers

- **schedule** — node "Schedule Gateway Creator" (id `138d6b4b-9dfe-4556-a1df-d42efd58adf0`) — `every 1 hour(s)`
- **schedule** — node "Schedule no ACH in PAPI" (id `3b6a3c38-c77d-48b9-ba0e-ed6548536728`) — `daily at 9:00, daily at 15:00`
- **schedule** — node "Schedule conflicting gateways" (id `52cc7faf-2560-45a0-b5ba-f80ff98984ed`) — `every 1 hour(s)`
- **manual** — node "When clicking ‘Execute workflow’" (id `5e7347a8-6a1e-4428-9420-7c3aad7bc98b`)
- **schedule** — node "Schedule mismatched applications" (id `62be42b9-ad94-4938-a1de-6d38c59c2eb3`) — `daily at 9:00, daily at 15:00`
- **schedule** — node "Schedule approved applications" (id `8e99841a-8caa-471c-8800-1e4a5405ff70`) — `unconfigured`
- **schedule** — node "Schedule misconfigured 3ds" (id `92324b11-fb10-4488-988a-cdc08d31cc96`) — `every 15 minute(s)`
- **error** — node "Error Trigger" (id `ba3c5ee6-5c99-490e-aca9-054d3eca4884`)
- **schedule** — node "Schedule submit merchants to processor" (id `dec216a6-c87c-48dd-91d8-9da8d544cc77`) — `every 15 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `05bbd139-5268-47d7-8d39-f8d0e50148c7`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message3" (id `0840bc29-c99e-41a6-916c-7c50d7cafe41`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `13e84b18-b860-4ec4-915f-c91f58184801`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Update Merchant Status (Submitted For Underwriting)1" (id `20e3c6ed-6105-4193-b4c5-a33f775e0538`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message7" (id `218931d7-7a3f-40d7-a230-64f99128fc7d`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "PE Merchant merchant-onboarding-api-logs" (id `31b23758-51e8-4be6-8141-ae437eb922df`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `352b0ffb-9d2a-4e04-8be5-fe8bb2254c40`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `40eade03-22e8-47c1-b46c-733ccac259d8`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query1" (id `44c1b45d-9664-4191-9d6d-a6598846ee0c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message8" (id `473e5876-8822-4451-bf82-d3a5750374e4`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `492706c3-2765-4a82-8ac2-e50ec724a559`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query2" (id `4f27c1fa-e3bc-4cd0-9495-878cae09d943`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Details3" (id `4f6d6aa7-6a2e-4f68-9990-71c4be85c948`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message11" (id `514c4fa9-407e-47c1-915e-ef698d0c175f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `516a7436-b2d4-4522-889c-012fe234ac4d`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Details4" (id `51cc12ae-31f2-4f25-99e5-31f1dd5f0c65`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "Forte Get Merchant Details" (id `53968add-7d21-4a6c-a811-eea2be8ba12d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "LogAutosubmission" (id `5b62a171-09f8-46b8-8ef9-468e866e6882`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message12" (id `5f7eaca2-0278-4bc2-9b4c-b2072f2bf0df`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Details2" (id `674c2f65-d25c-4c8b-ba78-4554bba40438`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message13" (id `695d5097-e0c9-4f93-a3c7-1424a2a14f73`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "PE Merchant merchant-onboarding-api-logs1" (id `6b96fb98-2dd3-4455-96d6-b27b0dc1807a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message15" (id `72e5fd40-ef31-446e-8421-b29d296a38c6`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `72ff26e5-9b1b-49cf-9a71-148863b15f5e`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "Forte Get Merchant Status" (id `8768fb3e-fb1f-4fb6-8b32-da5b73ce7a3f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `8971ddd4-104d-41e5-a801-41290cef6388`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Processor" (id `95fb6210-cb92-4cc2-bc7a-bf5a99482083`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Update Merchant Status (Submitted For Underwriting)" (id `c0159c52-641f-4e23-82ec-56b7012adc7c`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query3" (id `c5b63900-c58a-4e5a-b0ee-d7a4796925ec`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message10" (id `cbc57496-fa21-4557-acf5-38f6ef974278`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Add Forte Processor" (id `cf081004-c8b1-4ed6-8cc7-c44bab0be129`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message2" (id `cf3cc099-6c29-4faf-b27b-38d2ee314557`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message16" (id `e5cc07dc-52e6-4d68-baea-acbe906bbb66`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Details1" (id `e7c25618-7861-46d7-8cb8-69d218ddb623`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message9" (id `ebb8f53d-fe16-470c-a8fc-2706ab381f3a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `eca1fec9-cfe0-4498-b7ff-cea6460b0a7d`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query4" (id `ed7d3991-63d9-45f5-8ca8-5c993425feb8`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message14" (id `f4cfd48d-c4c6-4556-8e57-0f522b391507`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/master/merchants/{{ $('Filter4').item.json.pe_merchant_id }}/gateway` — node "Update Merchant Status (Submitted For Underwriting)1" (id `20e3c6ed-6105-4193-b4c5-a33f775e0538`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchant-onboarding-api-logs/{{ $('Filter4').item.json.pe_merchant_id }}` — node "PE Merchant merchant-onboarding-api-logs" (id `31b23758-51e8-4be6-8141-ae437eb922df`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details3" (id `4f6d6aa7-6a2e-4f68-9990-71c4be85c948`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details4" (id `51cc12ae-31f2-4f25-99e5-31f1dd5f0c65`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/{{ $json.forte_processor_application_id }}` — node "Forte Get Merchant Details" (id `53968add-7d21-4a6c-a811-eea2be8ba12d`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details2" (id `674c2f65-d25c-4c8b-ba78-4554bba40438`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchant-onboarding-api-logs/{{ $json.pe_merchant_id }}` — node "PE Merchant merchant-onboarding-api-logs1" (id `6b96fb98-2dd3-4455-96d6-b27b0dc1807a`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/{{ $json.application_id }}` — node "Forte Get Merchant Status" (id `8768fb3e-fb1f-4fb6-8b32-da5b73ce7a3f`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants/{{ $json.id }}/processor` — node "Get Merchant Processor" (id `95fb6210-cb92-4cc2-bc7a-bf5a99482083`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.merchant_id }}/status` — node "Update Merchant Status (Submitted For Underwriting)" (id `c0159c52-641f-4e23-82ec-56b7012adc7c`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/master/merchants/{{ $json.data.id }}/processor` — node "Add Forte Processor" (id `cf081004-c8b1-4ed6-8cc7-c44bab0be129`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants?page=1&status=submitted_to_pe&sub_status=a&q=&size=100` — node "Get Merchant Details1" (id `e7c25618-7861-46d7-8cb8-69d218ddb623`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `40eade03-22e8-47c1-b46c-733ccac259d8`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query1" (id `44c1b45d-9664-4191-9d6d-a6598846ee0c`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query2" (id `4f27c1fa-e3bc-4cd0-9495-878cae09d943`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query3" (id `c5b63900-c58a-4e5a-b0ee-d7a4796925ec`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query4" (id `ed7d3991-63d9-45f5-8ca8-5c993425feb8`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator4" (id `154320f0-8da6-4125-b946-3983314136ae`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator2" (id `3fa62a88-0c41-4af5-a518-4d3c6eaa6790`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator" (id `ab42dc47-7374-4bc9-b698-3d9170f6c22f`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator1" (id `b8281abe-041d-45bd-80b8-bac736869a35`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator5" (id `d85b7215-2632-434f-b400-299c48ca3056`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator3" (id `f4f30ad0-ed8b-4350-a7fb-69c8ae68fd08`)

### Google Sheets

- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `appendOrUpdate`, tab `ActiveHearthApplications` — node "Append or update row in sheet" (id `13e84b18-b860-4ec4-915f-c91f58184801`)
- [[../resources/google-sheets/1muzy-keyh2c-ny4c2q-ulao5xf43kgr-k-4057zwoai|AI Automation - Ops Alert]] (id `1muzy-kEYH2C-nY4C2q-ulAo5Xf43kgr_K-4057ZwoAI`) — op `?`, tab `ECS - not in app` — node "Get row(s) in sheet" (id `516a7436-b2d4-4522-889c-012fe234ac4d`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `AutosubmissionLog` — node "LogAutosubmission" (id `5b62a171-09f8-46b8-8ef9-468e866e6882`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `append`, tab `forteGatewayCreationLogs` — node "Append row in sheet" (id `eca1fec9-cfe0-4498-b7ff-cea6460b0a7d`)

### Slack channels

- [[../resources/slack-channels/ops-automation-alert|ops-automation-alert]] (id `ops-automation-alert`) — op `channel` — node "Send a message" (id `05bbd139-5268-47d7-8d39-f8d0e50148c7`)
- [[../resources/slack-channels/ops-automation-alert|ops-automation-alert]] (id `ops-automation-alert`) — op `channel` — node "Send a message3" (id `0840bc29-c99e-41a6-916c-7c50d7cafe41`)
- [[../resources/slack-channels/ops-automation-alert|ops-automation-alert]] (id `ops-automation-alert`) — op `channel` — node "Send a message7" (id `218931d7-7a3f-40d7-a230-64f99128fc7d`)
- [[../resources/slack-channels/ops-automation-alert|ops-automation-alert]] (id `ops-automation-alert`) — op `channel` — node "Send a message6" (id `352b0ffb-9d2a-4e04-8be5-fe8bb2254c40`)
- *(dynamic channel)* — op `channel` — node "Send a message8" (id `473e5876-8822-4451-bf82-d3a5750374e4`)
- [[../resources/slack-channels/ops-automation-alert|ops-automation-alert]] (id `ops-automation-alert`) — op `channel` — node "Send a message4" (id `492706c3-2765-4a82-8ac2-e50ec724a559`)
- [[../resources/slack-channels/c09c901een4|hearth-alerts-internal]] (id `C09C901EEN4`) — op `channel` — node "Send a message11" (id `514c4fa9-407e-47c1-915e-ef698d0c175f`)
- *(dynamic channel)* — op `channel` — node "Send a message12" (id `5f7eaca2-0278-4bc2-9b4c-b2072f2bf0df`)
- [[../resources/slack-channels/ops-automation-alert|ops-automation-alert]] (id `ops-automation-alert`) — op `channel` — node "Send a message13" (id `695d5097-e0c9-4f93-a3c7-1424a2a14f73`)
- [[../resources/slack-channels/ops-automation-alert|ops-automation-alert]] (id `ops-automation-alert`) — op `channel` — node "Send a message15" (id `72e5fd40-ef31-446e-8421-b29d296a38c6`)
- [[../resources/slack-channels/ops-automation-alert|ops-automation-alert]] (id `ops-automation-alert`) — op `channel` — node "Send a message1" (id `72ff26e5-9b1b-49cf-9a71-148863b15f5e`)
- *(dynamic channel)* — op `channel` — node "Send a message5" (id `8971ddd4-104d-41e5-a801-41290cef6388`)
- *(dynamic channel)* — op `channel` — node "Send a message10" (id `cbc57496-fa21-4557-acf5-38f6ef974278`)
- *(dynamic channel)* — op `channel` — node "Send a message2" (id `cf3cc099-6c29-4faf-b27b-38d2ee314557`)
- *(dynamic channel)* — op `channel` — node "Send a message16" (id `e5cc07dc-52e6-4d68-baea-acbe906bbb66`)
- [[../resources/slack-channels/ops-automation-alert|ops-automation-alert]] (id `ops-automation-alert`) — op `channel` — node "Send a message9" (id `ebb8f53d-fe16-470c-a8fc-2706ab381f3a`)
- *(dynamic channel)* — op `channel` — node "Send a message14" (id `f4cfd48d-c4c6-4556-8e57-0f522b391507`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
