---
n8n_id: "gzYwe04hbZzgdUGb"
name: "Forte Gateway Autosubmitter"
status: inactive
last_modified: 2026-08-18T18:24:14.280Z
tags: []
fingerprint: "a0ad37b3b9acad8dde96f602995abd7dfa47981373a472ea24594c851db0075b"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Forte Gateway Autosubmitter

## Summary

- **Status:** inactive
- **n8n ID:** `gzYwe04hbZzgdUGb`
- **Nodes:** 111
- **Last modified:** 2026-08-18T18:24:14.280Z

## Triggers

- **schedule** — node "Schedule Trigger3" (id `050131ac-0143-4e07-9cb0-347d78614e43`) — `every 1 hour(s)`
- **schedule** — node "Schedule Trigger6" (id `0d542948-9fa3-4ffd-94e1-5c94b416f913`) — `every 15 minute(s)`
- **error** — node "Error Trigger" (id `2a9535a4-7a19-490d-a7a3-26c0dc41b44e`)
- **schedule** — node "Schedule Trigger" (id `2e59555b-6834-4671-91c1-ec84928dbd2d`) — `unconfigured`
- **schedule** — node "Schedule Trigger2" (id `5934377d-6232-4ab2-bee1-d131fba18b39`) — `daily at 9:00, daily at 15:00`
- **manual** — node "When clicking ‘Execute workflow’" (id `a6f4c8b3-228f-44d5-81f8-4d0f9ae9e22c`)
- **schedule** — node "Schedule Trigger5" (id `bff5cb6a-c59f-4b12-89fd-43920fa10498`) — `daily at 9:00, daily at 15:00`
- **schedule** — node "Schedule Trigger4" (id `c4cb8b75-a4c9-459c-bf65-62704d0800b1`) — `every 1 hour(s)`
- **schedule** — node "Schedule Trigger1" (id `d2197907-d7bd-4bd2-96bf-f518d3327ceb`) — `every 15 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "Forte Get Merchant Details" (id `0005bb7d-e37e-4169-80c3-fc42754e5f07`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Processor2" (id `0c06ce4e-7203-457e-8d8d-c279ffa40a37`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Details1" (id `15a0142e-fdef-4c6b-8b30-4ab09e50b759`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query3" (id `1f7d253c-260a-4044-8902-548451897f5b`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "GetFundingTransactionsFromForte" (id `274e62f0-265d-4c0c-bb2c-7f9d816b84be`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message3" (id `2f4637ba-7fa7-4389-bb56-32928ab0e632`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "LogAutosubmission" (id `35db04b0-813f-4cf3-be2f-4f66ff16fa38`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `3bc94248-6c6a-411b-b4ea-c9992671b094`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message7" (id `3bfe55b6-a05c-4d27-9ac2-e61eb9e4ead3`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Details3" (id `45e63418-a6e7-4c1b-b94c-34aa50bd3d5b`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "PE Merchant merchant-onboarding-api-logs1" (id `4a490fef-56b5-4f56-b545-e73129e71ed9`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message11" (id `54e13a58-f2da-493c-a3fd-90bcb51bace1`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Details5" (id `5d45cd20-cb1d-4b21-b71f-3eb86d017691`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `62616995-8129-4b1f-87f8-916ad58bc70c`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query1" (id `651aab80-db09-4f3f-b230-d659c0771bca`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `6a518f80-4195-48f1-9cff-548defb75c1a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message9" (id `840d691e-c9ac-4f59-ad50-e4d74be2d341`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Details" (id `86362c4a-b42c-48c5-a03d-29f78aafc488`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Processor" (id `89bcc04d-d115-4c80-8300-6439747f20b6`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message8" (id `8beeffa6-e59b-4951-96ff-8bafbf1cf7f4`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `91c24966-5f5a-42ca-a159-a1478492acd3`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query2" (id `9764a14a-3530-490d-845b-06659d21469b`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Processor3" (id `9892bb42-3cd0-44fc-89e9-be0a8b53b024`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "GetFundingTransactionsFromForte1" (id `9ac60bf0-f56a-4013-9aae-64ac49ecf755`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `9d3ad34b-e8b4-4397-85b1-0eed05b9f7bb`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message2" (id `9d423f4c-bec8-4f2f-9b40-c47a75f9d0a2`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Details6" (id `aa1dafc5-b4a5-461d-bb13-cd4b8ed6111f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `abf17224-2ee0-41b5-b2ec-5d9676a77bbe`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Processor1" (id `bb8d18e3-9eb4-4d6b-933f-90fd12484473`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Update Merchant Status (Submitted For Underwriting)1" (id `c2573670-e5bc-4091-9214-f2933ae70919`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Update Merchant Status (Submitted For Underwriting)" (id `c3284fd1-a476-465c-b36d-6af625d36257`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Details4" (id `c857f13a-4ec8-4598-a619-fcb28b17ba8f`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Account Merchants2" (id `c858169b-b4f1-41e6-973d-2246b4f5e85f`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "Forte Get Merchant Status" (id `c8c84f95-376e-4770-822e-0c27691e10af`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message12" (id `c8d48bef-68a2-49bd-80ae-29b421610552`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message10" (id `cdf91887-a68c-498f-b73b-a1a3c726244a`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "PE Merchant Gateways" (id `d009137d-2c4c-4a47-ac77-ca138bb0e80f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `d266dc93-f3e1-4f96-bcfe-9e76f6760609`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Details2" (id `d61a8dc7-b434-4545-87b5-3710e375a33e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `db23b121-36f3-4013-9d4c-da06f9077803`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query4" (id `dc05b888-45dd-4903-b5d5-a76373864375`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Account Merchants3" (id `f0b2cb59-d720-4e2b-aa42-5427bfe23218`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Add Forte Processor" (id `f26558e9-1129-4abf-80fa-7b8f815341a8`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "PE Merchant merchant-onboarding-api-logs" (id `fd521c4d-2f94-412c-ab4a-38ad1104da5a`)

### HTTP URLs

- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/{{ $json.forte_processor_application_id }}` — node "Forte Get Merchant Details" (id `0005bb7d-e37e-4169-80c3-fc42754e5f07`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants/{{ $json.id }}/gateway` — node "Get Merchant Processor2" (id `0c06ce4e-7203-457e-8d8d-c279ffa40a37`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants?page=1&status=submitted_to_pe&sub_status=a&account=4c971cc5-4664-4286-8a98-e9e327c768d3&q=&size=100` — node "Get Merchant Details1" (id `15a0142e-fdef-4c6b-8b30-4ab09e50b759`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/{{ $json.data.find(d => d.processor_id === 'forte')?.application_id }}` — node "GetFundingTransactionsFromForte" (id `274e62f0-265d-4c0c-bb2c-7f9d816b84be`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details3" (id `45e63418-a6e7-4c1b-b94c-34aa50bd3d5b`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchant-onboarding-api-logs/{{ $json.pe_merchant_id }}` — node "PE Merchant merchant-onboarding-api-logs1" (id `4a490fef-56b5-4f56-b545-e73129e71ed9`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details5" (id `5d45cd20-cb1d-4b21-b71f-3eb86d017691`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants?page=1&status=submitted_to_pe&sub_status=a&account=4c971cc5-4664-4286-8a98-e9e327c768d3&q=&size=100` — node "Get Merchant Details" (id `86362c4a-b42c-48c5-a03d-29f78aafc488`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants/{{ $json.id }}/processor` — node "Get Merchant Processor" (id `89bcc04d-d115-4c80-8300-6439747f20b6`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants/{{ $json.data[0].merchant_id }}/processor` — node "Get Merchant Processor3" (id `9892bb42-3cd0-44fc-89e9-be0a8b53b024`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/org_444639/locations` — node "GetFundingTransactionsFromForte1" (id `9ac60bf0-f56a-4013-9aae-64ac49ecf755`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details6" (id `aa1dafc5-b4a5-461d-bb13-cd4b8ed6111f`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants/{{ $json.id }}/processor` — node "Get Merchant Processor1" (id `bb8d18e3-9eb4-4d6b-933f-90fd12484473`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/master/merchants/{{ $('Filter4').item.json.pe_merchant_id }}/gateway` — node "Update Merchant Status (Submitted For Underwriting)1" (id `c2573670-e5bc-4091-9214-f2933ae70919`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.merchant_id }}/status` — node "Update Merchant Status (Submitted For Underwriting)" (id `c3284fd1-a476-465c-b36d-6af625d36257`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details4" (id `c857f13a-4ec8-4598-a619-fcb28b17ba8f`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Account Merchants2" (id `c858169b-b4f1-41e6-973d-2246b4f5e85f`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/{{ $json.application_id }}` — node "Forte Get Merchant Status" (id `c8c84f95-376e-4770-822e-0c27691e10af`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants/{{ $json.pe_merchant_id }}/gateway
` — node "PE Merchant Gateways" (id `d009137d-2c4c-4a47-ac77-ca138bb0e80f`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details2" (id `d61a8dc7-b434-4545-87b5-3710e375a33e`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Account Merchants3" (id `f0b2cb59-d720-4e2b-aa42-5427bfe23218`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/master/merchants/{{ $json.data.id }}/processor` — node "Add Forte Processor" (id `f26558e9-1129-4abf-80fa-7b8f815341a8`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchant-onboarding-api-logs/{{ $('Filter4').item.json.pe_merchant_id }}` — node "PE Merchant merchant-onboarding-api-logs" (id `fd521c4d-2f94-412c-ab4a-38ad1104da5a`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query3" (id `1f7d253c-260a-4044-8902-548451897f5b`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query1" (id `651aab80-db09-4f3f-b230-d659c0771bca`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `91c24966-5f5a-42ca-a159-a1478492acd3`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query2" (id `9764a14a-3530-490d-845b-06659d21469b`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query4" (id `dc05b888-45dd-4903-b5d5-a76373864375`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator" (id `19ec3214-39a0-4fcf-a4e8-0bb41dfab94a`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator2" (id `31cbc70f-63a4-47fb-9c99-5eab194a1e9c`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator3" (id `511b3efd-7650-4bc6-94a3-94e24482c84c`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator1" (id `f7af4583-2c49-41f1-927a-7aa19e93b44e`)

### Google Sheets

- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `AutosubmissionLog` — node "LogAutosubmission" (id `35db04b0-813f-4cf3-be2f-4f66ff16fa38`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `appendOrUpdate`, tab `ActiveHearthApplications` — node "Append or update row in sheet" (id `abf17224-2ee0-41b5-b2ec-5d9676a77bbe`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `append`, tab `forteGatewayCreationLogs` — node "Append row in sheet" (id `db23b121-36f3-4013-9d4c-da06f9077803`)

### Slack channels

- [[../resources/slack-channels/c09c901een4|hearth-alerts-internal]] (id `C09C901EEN4`) — op `channel` — node "Send a message3" (id `2f4637ba-7fa7-4389-bb56-32928ab0e632`)
- *(dynamic channel)* — op `channel` — node "Send a message5" (id `3bc94248-6c6a-411b-b4ea-c9992671b094`)
- [[../resources/slack-channels/c09c901een4|hearth-alerts-internal]] (id `C09C901EEN4`) — op `channel` — node "Send a message7" (id `3bfe55b6-a05c-4d27-9ac2-e61eb9e4ead3`)
- [[../resources/slack-channels/c09c901een4|hearth-alerts-internal]] (id `C09C901EEN4`) — op `channel` — node "Send a message11" (id `54e13a58-f2da-493c-a3fd-90bcb51bace1`)
- [[../resources/slack-channels/c09c901een4|hearth-alerts-internal]] (id `C09C901EEN4`) — op `channel` — node "Send a message6" (id `62616995-8129-4b1f-87f8-916ad58bc70c`)
- [[../resources/slack-channels/c09c901een4|hearth-alerts-internal]] (id `C09C901EEN4`) — op `channel` — node "Send a message" (id `6a518f80-4195-48f1-9cff-548defb75c1a`)
- [[../resources/slack-channels/c09c901een4|hearth-alerts-internal]] (id `C09C901EEN4`) — op `channel` — node "Send a message9" (id `840d691e-c9ac-4f59-ad50-e4d74be2d341`)
- *(dynamic channel)* — op `channel` — node "Send a message8" (id `8beeffa6-e59b-4951-96ff-8bafbf1cf7f4`)
- [[../resources/slack-channels/c09c901een4|hearth-alerts-internal]] (id `C09C901EEN4`) — op `channel` — node "Send a message4" (id `9d3ad34b-e8b4-4397-85b1-0eed05b9f7bb`)
- *(dynamic channel)* — op `channel` — node "Send a message2" (id `9d423f4c-bec8-4f2f-9b40-c47a75f9d0a2`)
- *(dynamic channel)* — op `channel` — node "Send a message12" (id `c8d48bef-68a2-49bd-80ae-29b421610552`)
- *(dynamic channel)* — op `channel` — node "Send a message10" (id `cdf91887-a68c-498f-b73b-a1a3c726244a`)
- [[../resources/slack-channels/c09c901een4|hearth-alerts-internal]] (id `C09C901EEN4`) — op `channel` — node "Send a message1" (id `d266dc93-f3e1-4f96-bcfe-9e76f6760609`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
