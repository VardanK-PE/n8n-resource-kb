---
n8n_id: "SAot95eAPiyc8s56"
instance: v1
name: "PayEngineAI Bot (v1.1) - Feb 26 2026"
status: inactive
last_modified: 2026-06-12T14:34:30.758Z
tags: []
fingerprint: "e48afa010962707d5c2652e967f504f76e1e66932167aaa0e4f08a950fc3dc1a"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PayEngineAI Bot (v1.1) - Feb 26 2026

## Summary

- **Status:** inactive
- **n8n ID:** `SAot95eAPiyc8s56`
- **Nodes:** 210
- **Last modified:** 2026-06-12T14:34:30.758Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `0f26761a-5b1c-4a7e-962f-b6725d3d2a60`) — `every 65 second(s)`
- **schedule** — node "Schedule Trigger2" (id `1317dfc4-f5d4-467a-a199-c7c7bf06aee6`) — `every 2 month(s)`
- **execute-workflow** — node "When Executed by Another Workflow" (id `15e527a3-35e9-4255-8d25-a49873eb3f44`)
- **error** — node "Error Trigger" (id `255014ef-162e-48f7-aa01-cbd78183db4b`)
- **webhook** — node "Webhook" (id `3f2ed506-572d-492a-9157-6bc4df58e2a6`) — POST `d55c5f6c-2cd2-4610-b73c-5314459be894`
- **other** — node "On new manual Chat Message" (id `45a36500-54dd-4125-bd08-a261aa883c58`)
- **schedule** — node "Schedule Trigger3" (id `4832ddd0-7b11-4a9b-b91f-4d4c2f943353`) — `every 4 hour(s)`
- **webhook** — node "Incoming /secops-change" (id `4b3ad0de-9c0b-4de5-b33d-6e11585376ea`) — POST `2fc3f1d5-e64d-455d-aa95-d9bb80973864`
- **manual** — node "When clicking "Execute Workflow"" (id `6a37de7f-1f82-4dfb-af40-59f7004825fc`)
- **webhook** — node "Incoming response" (id `776ad560-182a-40c4-924c-0cc3275dbec6`) — POST `42dee094-34db-43c0-861d-8c5738145bac`
- **webhook** — node "app_mention" (id `a175d058-aee9-49a3-b388-94fee6be3d50`) — POST `dc0beaa5-3d3d-4d18-a259-15a74383978a`
- **webhook** — node "Slashcommand" (id `d6b85f35-a5db-4239-bf87-0af609d6497e`) — POST `cac903db-d2d7-4505-82f5-1d2fdee3e8a3`
- **schedule** — node "Schedule Trigger1" (id `d7ca2912-37a4-4925-8ca7-3f89fd274a07`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `0d1ceded-8fe7-4266-93fb-58ef921fc219`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Assistant" (id `0ed2805b-34ec-4852-b0b6-44884577a647`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox (bk 2025-08-30)" (id `0f832a45-5ee0-4b89-91a8-63f1d6e717a7`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model" (id `111983bb-b952-4883-bc71-b7937801cca2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `1711c25b-5555-4384-ad5c-39bce0ff60a1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Partner Specific Instructions" (id `1affcea2-fe3f-4fba-9f1c-736bdedee10b`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon" (id `1b43e4d3-3946-4fa7-8218-56b410e7a2fa`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state" (id `1c9bb451-d7f6-497c-a68b-3d6f664b3dcd`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `1f4003ea-a0cf-454f-b1e7-82e184d3ea0e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "SubPrompts1" (id `22b70219-5a22-4fa7-b435-cce98804ca29`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove Inbox" (id `23743809-5fd3-46f8-b107-7dd7b8f4849e`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `246f9f1f-f663-42be-8ea0-54e2dcf70dcf`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "Forte Rejected Reason Lookup" (id `24d9d4d0-95fc-443c-ae5c-7d4228d54bb0`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Forte Rejected Reason Lookup" (id `24d9d4d0-95fc-443c-ae5c-7d4228d54bb0`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Add label to message2" (id `36432972-0f12-44d8-80a6-6e468221557b`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `3bb8d920-a75d-4be6-906c-cca644ff712d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Elavon Declined ACHs" (id `3c938ab8-be51-42a9-9429-88f5a767429b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get items to archive" (id `422c7c62-2eff-4b6a-a8fc-f143324d3814`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `454c6a5c-5fce-4f85-9b88-81d6bb202143`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "PE Slack1" (id `48aff8cd-8e7c-427c-8cec-311b40b0602a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `4c0d3d2c-ab85-42b9-8a93-941e34d37dc6`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send "new email received" notification" (id `4e4185a6-2e8e-4f57-a2de-1493a48475e8`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model3" (id `51503bc4-191b-4551-bc41-ccfb348202be`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `5563dfa9-8d07-4339-8867-baf1197dddae`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE_Merchants" (id `56d64a4e-01f7-466a-8029-cde82f012b3f`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `5a0e0da6-a3f5-4c05-83be-602385225e6c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get a document" (id `5dd8d18b-b734-4268-8e09-6885447fa1e9`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox1 (bk 2025-08-30)" (id `62b489fd-dcd5-4330-9f0a-d93c8477ad7d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `6771770f-f310-48d1-aaac-46825d5f46a5`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Success Message2" (id `68f7ee47-25aa-4e90-9d83-7bb8e26cebe4`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (without attachment)" (id `6a45727d-0674-4795-b99d-15746572e735`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox2" (id `6b0ffc11-750e-43f3-8dd1-e208b29352b6`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant/Partner Details Lookup from PE DB" (id `6fdaf84d-2a4f-4268-808a-7c9009a11afe`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model5" (id `78ec033c-b9b8-4c8b-9f03-c70c9baee8ba`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `7ac2abf6-43d1-4cb9-a841-809df6445225`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox2" (id `7b0ca178-e2c6-461b-9668-7fcb5b3e31d4`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model4" (id `7b64d0d7-c2bd-41da-9719-71644e7cfb58`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file" (id `7c487467-c5a2-47e1-855a-5ce0ca2e4521`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model2" (id `7c9d8a5e-2345-408d-b46c-0ab3fe426e1c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `7ce9ab44-7741-48bf-94b3-abaa7e81b7e6`)
- [[../resources/credentials/godp5gdyjaspv2fj|Anthropic (spartak@platformfactory.io) n8n 2026]] (`anthropicApi`, id `Godp5GdYJAspV2fj`) — node "Anthropic (spartak@platformfactory.io)" (id `7d453111-109c-4982-901c-7f4d40860f83`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model2" (id `7f34ddd6-fd61-44fd-9b7b-9a97c7f12a98`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Delete rows or columns from sheet" (id `7fb2e5d7-448d-4196-972e-c15e4b47f4dc`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack11" (id `8366c1a4-ee87-4c81-8271-b17bb78ff5cf`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove" (id `90a79fdc-76e6-482e-94f3-313c22aaf819`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Add label to message1" (id `91734eb5-0e23-4aa2-bc8e-7180a578bdea`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model1" (id `9429ff37-c81e-471d-8fe2-b092d1fba18b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `97d4ef2d-c107-4490-aa49-31135906156f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack6" (id `98e1c3d4-797c-4ffd-9474-2b479d878c28`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth" (id `98e886ac-d5e3-41f1-a25f-5cf769d264d2`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file1" (id `9c895654-adac-4771-99b4-1b26836d9fde`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Create Draft In Supermove Inbox" (id `a674284d-197a-4b7e-a638-c87b71c19ea8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create archive" (id `a6a6a06c-3bdf-4131-b5f9-cef06f27c63d`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon1" (id `a6afc618-f727-47e1-b076-da3d800b3ea4`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox1" (id `adbaae81-9a3b-4fb6-a7e3-0d26884f62c2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets7" (id `b283eb2d-42a4-4675-b52a-2e2d3ce552e9`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (with attachment)" (id `b6ac15c4-fe2d-426e-a244-78878f4cd94e`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create Draft In Heart Inbox1" (id `b7cb9547-7a33-4a9c-b3e0-5347b1291d46`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Merchant Reply" (id `ba80b3f6-65e7-4a6d-abbb-b4ca1bf01ab2`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox" (id `bc0b6996-8867-42a1-a73a-090667bb0811`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `bda1177d-44d3-47c9-9f04-badbada53b4e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Execution Logger" (id `c1da9a19-3df6-44c9-baed-e8d8fa2ba33a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack4" (id `c4745035-57c8-49bf-ab2d-32ef992d0b6a`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Direct Reply Drafts in PE Inbox" (id `c7daee2e-d767-445c-99a2-5647b931469f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download AI Prompt" (id `c953feaf-da2e-4eda-8347-0fd75731d011`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack5" (id `cc4da83f-a157-4cd4-878c-98da25caa581`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Posting a Form" (id `cd1e3bb7-09bb-43bb-93c8-1cd5cd019d00`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets6" (id `cd83534a-f35c-4fc2-8585-758e6b0347ee`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `d09d0a2b-c152-4665-b55c-00e1699a0bb7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Subprompt Updater1" (id `d368d0ab-ab9f-417f-97df-e99b4572ae11`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Partner Account Lookup" (id `d3f8ed73-48e0-4266-856f-94374d66c3a0`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `dbc565bc-c38f-4799-8de0-954f72b216c4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `dca8fe13-4c12-4dd6-8222-f347dbd98a80`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack10" (id `dd564b61-20fe-4dc4-83ac-9054e6f2c844`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack3" (id `de5ef981-4411-4199-bab2-9ca24744d86d`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth1" (id `e4afb53d-e2fa-4e78-88cf-dba32edbc04b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets8" (id `ea34f923-de9d-4978-af9b-842723123e79`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state1" (id `ec7f6906-c06f-4c11-b06f-93f066370a8a`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `efdf84db-bd9d-4821-a1b1-7bd3bd259b04`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic (Spartak@gmail.com)" (id `f305836d-6ccd-4948-a613-2b311a0c36c4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `f319b7a1-9757-4ef3-802f-1962e57bb4b0`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Add label to message" (id `fcc49bbe-70e3-4732-8688-2c54461fbf25`)

### HTTP URLs

- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/app_{{ $fromAI('ForteApplicationID', ``, 'string') }}` — node "Forte Rejected Reason Lookup" (id `24d9d4d0-95fc-443c-ae5c-7d4228d54bb0`)
- [[../resources/http-urls/slack-com|slack.com]] — `POST https://slack.com/api/views.open` — node "Posting a Form" (id `cd1e3bb7-09bb-43bb-93c8-1cd5cd019d00`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `246f9f1f-f663-42be-8ea0-54e2dcf70dcf`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `5a0e0da6-a3f5-4c05-83be-602385225e6c`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant/Partner Details Lookup from PE DB" (id `6fdaf84d-2a4f-4268-808a-7c9009a11afe`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Partner Account Lookup" (id `d3f8ed73-48e0-4266-856f-94374d66c3a0`)

### LLM models

- [[../resources/llm-models/openai-unspecified|openai / ?]] — node "OpenAI Assistant" (id `0ed2805b-34ec-4852-b0b6-44884577a647`)
- [[../resources/llm-models/openai-gpt-4|openai / gpt-4]] — node "OpenAI Chat Model" (id `111983bb-b952-4883-bc71-b7937801cca2`)
- [[../resources/llm-models/openai-gpt-5|openai / gpt-5]] — node "OpenAI Chat Model3" (id `51503bc4-191b-4551-bc41-ccfb348202be`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model" (id `5563dfa9-8d07-4339-8867-baf1197dddae`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model5" (id `78ec033c-b9b8-4c8b-9f03-c70c9baee8ba`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model4" (id `7b64d0d7-c2bd-41da-9719-71644e7cfb58`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model2" (id `7c9d8a5e-2345-408d-b46c-0ab3fe426e1c`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-5-20250929|anthropic / claude-sonnet-4-5-20250929]] — node "Anthropic (spartak@platformfactory.io)" (id `7d453111-109c-4982-901c-7f4d40860f83`)
- [[../resources/llm-models/openai-gpt-5|openai / gpt-5]] — node "OpenAI Chat Model2" (id `7f34ddd6-fd61-44fd-9b7b-9a97c7f12a98`)
- [[../resources/llm-models/openai-o3-pro|openai / o3-pro]] — node "OpenAI Chat Model1" (id `9429ff37-c81e-471d-8fe2-b092d1fba18b`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-5-20250929|anthropic / claude-sonnet-4-5-20250929]] — node "Anthropic Chat Model1" (id `efdf84db-bd9d-4821-a1b1-7bd3bd259b04`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-5-20250929|anthropic / claude-sonnet-4-5-20250929]] — node "Anthropic (Spartak@gmail.com)" (id `f305836d-6ccd-4948-a613-2b311a0c36c4`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-yaml|n8n-nodes-yaml]] — type `n8n-nodes-yaml.yaml` — node "YAML" (id `e93a0293-9f4b-4ecb-bd8f-d18f8faf4531`)

### Google Sheets

- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `update`, tab `EmailLogs` — node "Update row in sheet" (id `1711c25b-5555-4384-ad5c-39bce0ff60a1`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partnerSpceficInstructions` — node "Get Partner Specific Instructions" (id `1affcea2-fe3f-4fba-9f1c-736bdedee10b`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `?`, tab `SubPrompts` — node "SubPrompts1" (id `22b70219-5a22-4fa7-b435-cce98804ca29`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `append`, tab `ElavonDeclinedACH` — node "Log Elavon Declined ACHs" (id `3c938ab8-be51-42a9-9429-88f5a767429b`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `?`, tab `EmailLogs` — node "Get items to archive" (id `422c7c62-2eff-4b6a-a8fc-f143324d3814`)
- [[../resources/google-sheets/14fmhaamqlgpq5blxfkns4yisa7juvcmkcmmdknl4g1o|PayEngineAIBotLogs]] (id `14fmhaamQlGPQ5BLxfKNS4yISA7jUvcMkCmmDKNL4g1o`) — op `append`, tab `MentionLogs` — node "Google Sheets" (id `454c6a5c-5fce-4f85-9b88-81d6bb202143`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `update`, tab `EmailLogs` — node "Google Sheets5" (id `4c0d3d2c-ab85-42b9-8a93-941e34d37dc6`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `append`, tab `={{ $('Edit Fields19').first().json.archive_name }}` — node "Append row in sheet" (id `6771770f-f310-48d1-aaac-46825d5f46a5`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `appendOrUpdate`, tab `EmailLogs` — node "Google Sheets1" (id `7ac2abf6-43d1-4cb9-a841-809df6445225`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `delete`, tab `EmailLogs` — node "Delete rows or columns from sheet" (id `7fb2e5d7-448d-4196-972e-c15e4b47f4dc`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `?`, tab `EmailLogs` — node "Google Sheets2" (id `97d4ef2d-c107-4490-aa49-31135906156f`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `create`, tab `null` — node "Create archive" (id `a6a6a06c-3bdf-4131-b5f9-cef06f27c63d`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `appendOrUpdate`, tab `EmailLogs` — node "Google Sheets7" (id `b283eb2d-42a4-4675-b52a-2e2d3ce552e9`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `append`, tab `AIExecutionHistory` — node "Execution Logger" (id `c1da9a19-3df6-44c9-baed-e8d8fa2ba33a`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `update`, tab `EmailLogs` — node "Google Sheets6" (id `cd83534a-f35c-4fc2-8585-758e6b0347ee`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `append`, tab `SubPrompts` — node "Subprompt Updater1" (id `d368d0ab-ab9f-417f-97df-e99b4572ae11`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `?`, tab `EmailLogs` — node "Google Sheets4" (id `dca8fe13-4c12-4dd6-8222-f347dbd98a80`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `?`, tab `EmailLogs` — node "Google Sheets8" (id `ea34f923-de9d-4978-af9b-842723123e79`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `update`, tab `EmailLogs` — node "Google Sheets3" (id `f319b7a1-9757-4ef3-802f-1962e57bb4b0`)

### Google Drive

- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download file" (id `0d1ceded-8fe7-4266-93fb-58ef921fc219`)
- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download AI Prompt" (id `c953feaf-da2e-4eda-8347-0fd75731d011`)

### Slack channels

- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state" (id `1c9bb451-d7f6-497c-a68b-3d6f664b3dcd`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `1f4003ea-a0cf-454f-b1e7-82e184d3ea0e`)
- *(dynamic channel)* — op `channel` — node "PE Slack1" (id `48aff8cd-8e7c-427c-8cec-311b40b0602a`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send "new email received" notification" (id `4e4185a6-2e8e-4f57-a2de-1493a48475e8`)
- *(dynamic channel)* — op `channel` — node "Success Message2" (id `68f7ee47-25aa-4e90-9d83-7bb8e26cebe4`)
- *(dynamic channel)* — op `channel` — node "Slack2" (id `7ce9ab44-7741-48bf-94b3-abaa7e81b7e6`)
- *(dynamic channel)* — op `channel` — node "Slack11" (id `8366c1a4-ee87-4c81-8271-b17bb78ff5cf`)
- *(dynamic channel)* — op `channel` — node "Slack6" (id `98e1c3d4-797c-4ffd-9474-2b479d878c28`)
- [[../resources/slack-channels/c06c4lcjadv|payengine-ai-tests]] (id `C06C4LCJADV`) — op `channel` — node "Slack" (id `bda1177d-44d3-47c9-9f04-badbada53b4e`)
- *(dynamic channel)* — op `channel` — node "Slack5" (id `cc4da83f-a157-4cd4-878c-98da25caa581`)
- *(dynamic channel)* — op `channel` — node "Send a message" (id `d09d0a2b-c152-4665-b55c-00e1699a0bb7`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send a message6" (id `dbc565bc-c38f-4799-8de0-954f72b216c4`)
- *(dynamic channel)* — op `channel` — node "Slack10" (id `dd564b61-20fe-4dc4-83ac-9054e6f2c844`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state1" (id `ec7f6906-c06f-4c11-b06f-93f066370a8a`)

### Google Docs

- [[../resources/google-docs/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA]] (id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `get` — node "Get a document" (id `5dd8d18b-b734-4268-8e09-6885447fa1e9`)

### Sub-workflows (Execute Workflow calls)

- [[payengineai-bot-v1-1-feb-26-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] (n8n_id `0yjTSaTSRLaCOgvH`) — node "Read Emails1" (id `11f7549b-1d2e-4d7a-978f-6b4b1a37b298`)
- [[payengineai-bot-v1-1-feb-26-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] (n8n_id `0yjTSaTSRLaCOgvH`) — node "Call Onboarding Correspondence Aging Report Tool" (id `310cc45c-3df1-488a-a764-cd7f2d62c6d4`)
- [[payengineai-bot-v1-1-feb-26-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] (n8n_id `0yjTSaTSRLaCOgvH`) — node "Execute Workflow1" (id `43b8ed31-72b1-4302-9ca0-35a8264ecb78`)
- [[onboarding-correspondence-aging|Onboarding Correspondence Aging]] (n8n_id `DjgdzbbtR7fJ4oWX`) — node "Run Correspondence Aging Report" (id `5143dd76-b493-494f-8294-6705adab3692`)
- [[payengineai-bot-v1-1-feb-26-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] (n8n_id `0yjTSaTSRLaCOgvH`) — node "Call PayEngineBot" (id `62637110-e235-42aa-9a03-430217a54e6a`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `6b63778a-2f8a-4ca2-86d1-8b97843b8e67`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'1" (id `73043feb-a0f5-4053-b837-d4046e9c35d0`)
- [[payengineai-bot-v1-1-feb-26-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] (n8n_id `0yjTSaTSRLaCOgvH`) — node "Create Draft In Merchants Inbox1" (id `89bff1a0-36a7-4bc8-b9c3-fc33d0f578f9`)
- [[elavon-ach-exemption-form-generator|Elavon ACH Exemption Form Generator]] (n8n_id `c4rexPHrWGfGDBUP`) — node "Elavon ECS/ACH Max Check Size Generator" (id `b9c2a6b3-cdcf-4c47-b873-3c4ac5037e24`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
