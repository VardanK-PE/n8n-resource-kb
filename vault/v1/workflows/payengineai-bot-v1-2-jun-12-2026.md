---
n8n_id: "0yjTSaTSRLaCOgvH"
instance: v1
name: "PayEngineAI Bot (v1.2) - Jun 12 2026"
status: active
last_modified: 2026-08-27T18:47:41.259Z
tags: []
fingerprint: "9a3e0ba64f7baa68a0a1edc0bf536ffb87392ee3e3e7e3b48cc8019ea908fd1b"
auto_generated_at: 2026-08-28T21:13:05Z
---

<!-- auto:start -->

# PayEngineAI Bot (v1.2) - Jun 12 2026

## Summary

- **Status:** active
- **n8n ID:** `0yjTSaTSRLaCOgvH`
- **Nodes:** 208
- **Last modified:** 2026-08-27T18:47:41.259Z

## Triggers

- **schedule** — node "Schedule Trigger3" (id `00bfd1c5-8fc2-4c00-a2b7-7bfa0f2be497`) — `every 4 hour(s)`
- **webhook** — node "Incoming response" (id `4b57d810-2243-47f7-9da9-22c43c200c23`) — POST `aaaaaaa-1675-4e9e-b7b9-bbbbbbbbb`
- **webhook** — node "Incoming /secops-change" (id `50d80a68-4a6b-452a-9c70-6383e2c11c69`) — POST `ccccccccc-6d04-4ea1-8be0-dddddddd`
- **execute-workflow** — node "When Executed by Another Workflow" (id `5305ade1-1b27-4c4f-b186-e10f1631e1a4`)
- **webhook** — node "app_mention" (id `5c7683fb-bb49-4d8f-9b5b-a11a8ee87d8b`) — POST `a23aead4-bc40-48f2-acda-889fd523bd70`
- **webhook** — node "Webhook" (id `7658601a-b109-4b88-b57c-f7c5824c1111`) — POST `slack-payengineai`
- **other** — node "On new manual Chat Message" (id `a05dc82b-e9bf-4ae1-8798-c13016ada7fe`)
- **error** — node "Error Trigger" (id `a258e95c-587d-4426-ac57-e812cbc93e28`)
- **webhook** — node "Slashcommand" (id `a571f4e8-c76c-4737-ad3c-24600f5650ea`) — POST `b7593f23-c973-4bc8-876f-75a56d6d3169`
- **schedule** — node "Schedule Trigger" (id `ca19a350-b966-4522-bede-84109dd6395e`) — `every 65 second(s)`
- **manual** — node "When clicking "Execute Workflow"" (id `cc1451d2-8fd9-4a16-b18c-855ffcb48093`)
- **schedule** — node "Schedule Trigger1" (id `d44b7d6e-631b-40bb-b35c-c2be627acf79`) — `every 1 minute(s)`
- **schedule** — node "Schedule Trigger2" (id `e3273c1d-a668-4a80-93b0-2b4896d3f622`) — `every 2 month(s)`

## Depends on

### Credentials

- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox2" (id `08502166-11f6-4d7b-a6e8-e9eff7f40cca`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack6" (id `13102bdd-9be6-4a1a-9946-46f1a986f1d8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download AI Prompt" (id `1b7a101a-0905-415e-92d1-e3a0d585fa44`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `1b845199-575e-4e8a-b995-a4b66dea77e0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `1e0b1aa5-53ca-4c76-bf75-94ca0d15730d`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth" (id `22105189-1294-456f-939b-956c390be3da`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `259a75f8-3afc-4f1f-9b4c-5439bb202ab0`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model5" (id `2632de6e-fb3f-444d-b514-23337335e0ee`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `27b4368b-1058-4a1c-92cc-2b9cdbcccafa`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Add label to message2" (id `2d330f0e-103c-4940-95d0-6bc332db92af`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `2fe9c994-6537-4f4a-861d-692473cf81b0`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox (bk 2025-08-30)" (id `326f5115-a5b2-49d2-b73a-5e3a9f4117a6`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox1" (id `34ae73dc-ea84-4b9f-ae7e-75ecc05d5acc`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `352db74f-376e-4bf7-9ef6-641d4c0351b2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets8" (id `358ada98-e5c6-4d7b-8349-44efc630dbf6`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state1" (id `3cbf2d2c-2001-447f-b5e8-946d58fdf16d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file1" (id `42836858-544e-4508-a153-7d35bbf67b33`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant/Partner Details Lookup from PE DB" (id `434f16f6-3416-4fab-9bf3-185ab6d58d20`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model3" (id `44f10172-5a18-4d69-b899-4a1b64f79c77`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Partner Account Lookup" (id `4900bbb9-a4a7-45ef-9f6a-72973a469193`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth1" (id `4b57bd0c-c0ae-42cc-89bf-9669e4200520`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets6" (id `4d4e0d6f-cf10-4867-92f9-bd939ea1b657`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon1" (id `4f4b4802-5343-4df9-ad2f-a16b7656edc9`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack4" (id `50e23a94-017d-4fa0-86bb-909fe82ecfcf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets7" (id `5504a9a5-0d5b-4e54-8d7c-c7076b89939d`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove" (id `558eb933-14d0-4a19-adee-0d7fdf129a3d`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (with attachment)" (id `5c939b43-4b8e-4410-8881-791fa183185f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Subprompt Updater1" (id `5d30ba6f-9eaf-4e8b-a429-83bc71e2dd1b`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `64c8a548-44c2-4fe7-b97f-3dee6298d590`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Execution Logger - Old" (id `663c9db8-97fa-4147-9b24-76a65602a27e`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Merchant Reply" (id `6b190608-6935-45d7-9b0b-e611aaf7e50c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Posting a Form" (id `6edb8b28-1305-482d-bed6-f447a9487e5f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `767e00f9-7f2c-4435-8a6d-121810d2db31`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get a document" (id `78716a79-9d30-46e5-9a9e-440074ec911c`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic (Spartak@gmail.com)" (id `7a763d1f-ce85-44b4-8aa3-108cab5d0b85`)
- [[../resources/credentials/godp5gdyjaspv2fj|Anthropic (spartak@platformfactory.io) n8n 2026]] (`anthropicApi`, id `Godp5GdYJAspV2fj`) — node "Anthropic (spartak@platformfactory.io)" (id `7a872924-2d67-44bb-bd5c-08e5a90daf7a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Delete rows or columns from sheet" (id `8350eb6d-6d6c-46be-832b-a5d62fbcbd35`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Assistant" (id `8934007c-de07-4ffb-b89f-283383e335fa`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Elavon Declined ACHs" (id `89b93fef-a7b8-4be9-8689-b2ed0187a57d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `8ab3f615-2de2-4991-92d6-2708d7e1d9cb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Execution Logger" (id `8aeb70fd-3369-4188-8ab4-61e2313745e4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Elavon Declined ACHs - Old" (id `8b433619-3fda-499a-99bc-0af99e1cea0c`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model1" (id `8bc36137-d0b3-4dca-966d-51f5c7bc295a`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Add label to message1" (id `8db94aa3-952b-4a71-8c49-7bac944dc2de`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox2" (id `8ff98743-2039-4349-b330-788e1210d63f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `9000b26b-bed1-4e43-8883-776c952c455c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get items to archive" (id `91cffa3d-4d7a-4616-ae39-5b849a8eaf19`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `93d6e6fd-140f-4e25-97dd-cb36c919ceeb`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `97b88372-dfe7-4e8f-82f8-cc6629a68a81`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model" (id `990d91d3-a569-402d-afa1-50e7032fb468`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox" (id `9a8d51e3-a9e8-462a-9b96-17128f0afd64`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state" (id `9dc9dbf1-58aa-440a-8e80-a36e68733723`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE_Merchants" (id `ac05cd38-2ef9-4202-aaec-19d7616eaed4`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (without attachment)" (id `ac709f2c-ba04-4291-aa57-0d240efa3e9b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `b22ee548-c901-491e-9c61-6fdc59dbca39`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `b925e2bb-4f60-4e7b-9964-df5e4fa577cd`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon" (id `b9672d83-0476-4607-ac03-3779b376573f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send "new email received" notification" (id `ba5f2f57-3495-4115-8e1c-8f2ca24bef28`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox1 (bk 2025-08-30)" (id `bb97138c-f3c0-49d6-9fee-21e7cf976b2c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `bd3abf12-41ce-4606-bccf-788fe0ae75d8`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "PE Slack1" (id `bd984fc9-4641-4ece-b097-a78ce6272b66`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Success Message2" (id `bf980404-a286-40cf-ab48-4557446f7065`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "SubPrompts1" (id `c1b2a954-f288-4480-9f5c-069df5bc33e9`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack5" (id `c3ccc1b1-82ab-4889-ac1b-78cb2ca60e53`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `c662623c-6288-48d3-a4f6-2618061c4b05`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Direct Reply Drafts in PE Inbox" (id `cad2dac2-3b0b-4693-87eb-613f7d705574`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "Forte Rejected Reason Lookup" (id `cc83a563-1ae6-4ef4-821d-aea24e55853d`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Forte Rejected Reason Lookup" (id `cc83a563-1ae6-4ef4-821d-aea24e55853d`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Create Draft In Supermove Inbox" (id `cd7f6610-7c95-4d28-b402-5529a43676d4`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create Draft In Heart Inbox1" (id `d0247b67-d990-47d6-b96c-6e484d88db47`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `d131c158-c7cf-4936-9294-6dee29d2e8a6`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Add label to message" (id `d276ac08-8c57-4fa2-8938-7bd6067e6f82`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack11" (id `d7fcadfe-ba25-4df1-b291-c5a52bb1b909`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Partner Specific Instructions" (id `e6e01ec6-02fc-45e2-90ba-8cae7f40d3f8`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `ea51e664-ffad-4d59-ac5b-2e9e021bb36c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack3" (id `f1c02116-2993-4828-8849-4bbdabdac02c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create archive" (id `f26589fb-cd80-4587-9f66-c108aa25bb72`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack10" (id `f740b198-2d2b-4baa-93ae-ee1e9ecbd680`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove Inbox" (id `fefa9961-8e1a-41eb-a3df-77e667bd17ff`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file" (id `ff231897-044f-4dd3-9e72-35f0fbafd566`)

### HTTP URLs

- [[../resources/http-urls/slack-com|slack.com]] — `POST https://slack.com/api/views.open` — node "Posting a Form" (id `6edb8b28-1305-482d-bed6-f447a9487e5f`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/app_{{ $fromAI('ForteApplicationID', ``, 'string') }}` — node "Forte Rejected Reason Lookup" (id `cc83a563-1ae6-4ef4-821d-aea24e55853d`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `352db74f-376e-4bf7-9ef6-641d4c0351b2`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant/Partner Details Lookup from PE DB" (id `434f16f6-3416-4fab-9bf3-185ab6d58d20`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Partner Account Lookup" (id `4900bbb9-a4a7-45ef-9f6a-72973a469193`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `64c8a548-44c2-4fe7-b97f-3dee6298d590`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-5|anthropic / claude-sonnet-5]] — node "Anthropic Chat Model1" (id `259a75f8-3afc-4f1f-9b4c-5439bb202ab0`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model5" (id `2632de6e-fb3f-444d-b514-23337335e0ee`)
- [[../resources/llm-models/openai-gpt-5|openai / gpt-5]] — node "OpenAI Chat Model3" (id `44f10172-5a18-4d69-b899-4a1b64f79c77`)
- [[../resources/llm-models/anthropic-claude-sonnet-5|anthropic / claude-sonnet-5]] — node "Anthropic (Spartak@gmail.com)" (id `7a763d1f-ce85-44b4-8aa3-108cab5d0b85`)
- [[../resources/llm-models/anthropic-claude-sonnet-5|anthropic / claude-sonnet-5]] — node "Anthropic (spartak@platformfactory.io)" (id `7a872924-2d67-44bb-bd5c-08e5a90daf7a`)
- [[../resources/llm-models/openai-unspecified|openai / ?]] — node "OpenAI Assistant" (id `8934007c-de07-4ffb-b89f-283383e335fa`)
- [[../resources/llm-models/openai-o3-pro|openai / o3-pro]] — node "OpenAI Chat Model1" (id `8bc36137-d0b3-4dca-966d-51f5c7bc295a`)
- [[../resources/llm-models/openai-gpt-4|openai / gpt-4]] — node "OpenAI Chat Model" (id `990d91d3-a569-402d-afa1-50e7032fb468`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-yaml|n8n-nodes-yaml]] — type `n8n-nodes-yaml.yaml` — node "YAML" (id `0a09eef1-6c80-4de5-b5b4-f205388f5558`)

### Google Sheets

- [[../resources/google-sheets/14fmhaamqlgpq5blxfkns4yisa7juvcmkcmmdknl4g1o|PayEngineAIBotLogs]] (id `14fmhaamQlGPQ5BLxfKNS4yISA7jUvcMkCmmDKNL4g1o`) — op `append`, tab `MentionLogs` — node "Google Sheets" (id `1b845199-575e-4e8a-b995-a4b66dea77e0`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `appendOrUpdate`, tab `EmailLogs` — node "Google Sheets1" (id `27b4368b-1058-4a1c-92cc-2b9cdbcccafa`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `update`, tab `EmailLogs` — node "Google Sheets5" (id `2fe9c994-6537-4f4a-861d-692473cf81b0`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `?`, tab `EmailLogs` — node "Google Sheets8" (id `358ada98-e5c6-4d7b-8349-44efc630dbf6`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `update`, tab `EmailLogs` — node "Google Sheets6" (id `4d4e0d6f-cf10-4867-92f9-bd939ea1b657`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `appendOrUpdate`, tab `EmailLogs` — node "Google Sheets7" (id `5504a9a5-0d5b-4e54-8d7c-c7076b89939d`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `append`, tab `SubPrompts` — node "Subprompt Updater1" (id `5d30ba6f-9eaf-4e8b-a429-83bc71e2dd1b`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `append`, tab `AIExecutionHistory` — node "Execution Logger - Old" (id `663c9db8-97fa-4147-9b24-76a65602a27e`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `append`, tab `={{ $('Edit Fields19').first().json.archive_name }}` — node "Append row in sheet" (id `767e00f9-7f2c-4435-8a6d-121810d2db31`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `delete`, tab `EmailLogs` — node "Delete rows or columns from sheet" (id `8350eb6d-6d6c-46be-832b-a5d62fbcbd35`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `append`, tab `ElavonDeclinedACH` — node "Log Elavon Declined ACHs" (id `89b93fef-a7b8-4be9-8689-b2ed0187a57d`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `append`, tab `AIExecutionHistory` — node "Execution Logger" (id `8aeb70fd-3369-4188-8ab4-61e2313745e4`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `append`, tab `ElavonDeclinedACH` — node "Log Elavon Declined ACHs - Old" (id `8b433619-3fda-499a-99bc-0af99e1cea0c`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `?`, tab `EmailLogs` — node "Get items to archive" (id `91cffa3d-4d7a-4616-ae39-5b849a8eaf19`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `update`, tab `EmailLogs` — node "Update row in sheet" (id `93d6e6fd-140f-4e25-97dd-cb36c919ceeb`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `?`, tab `EmailLogs` — node "Google Sheets2" (id `b22ee548-c901-491e-9c61-6fdc59dbca39`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `?`, tab `SubPrompts` — node "SubPrompts1" (id `c1b2a954-f288-4480-9f5c-069df5bc33e9`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `?`, tab `EmailLogs` — node "Google Sheets4" (id `c662623c-6288-48d3-a4f6-2618061c4b05`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `update`, tab `EmailLogs` — node "Google Sheets3" (id `d131c158-c7cf-4936-9294-6dee29d2e8a6`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partnerSpceficInstructions` — node "Get Partner Specific Instructions" (id `e6e01ec6-02fc-45e2-90ba-8cae7f40d3f8`)
- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `create`, tab `null` — node "Create archive" (id `f26589fb-cd80-4587-9f66-c108aa25bb72`)

### Google Drive

- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download AI Prompt" (id `1b7a101a-0905-415e-92d1-e3a0d585fa44`)
- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download file" (id `1e0b1aa5-53ca-4c76-bf75-94ca0d15730d`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Slack6" (id `13102bdd-9be6-4a1a-9946-46f1a986f1d8`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state1" (id `3cbf2d2c-2001-447f-b5e8-946d58fdf16d`)
- *(dynamic channel)* — op `channel` — node "Send a message" (id `8ab3f615-2de2-4991-92d6-2708d7e1d9cb`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send a message6" (id `9000b26b-bed1-4e43-8883-776c952c455c`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state" (id `9dc9dbf1-58aa-440a-8e80-a36e68733723`)
- [[../resources/slack-channels/c06c4lcjadv|payengine-ai-tests]] (id `C06C4LCJADV`) — op `channel` — node "Slack" (id `b925e2bb-4f60-4e7b-9964-df5e4fa577cd`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send "new email received" notification" (id `ba5f2f57-3495-4115-8e1c-8f2ca24bef28`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `bd3abf12-41ce-4606-bccf-788fe0ae75d8`)
- *(dynamic channel)* — op `channel` — node "PE Slack1" (id `bd984fc9-4641-4ece-b097-a78ce6272b66`)
- *(dynamic channel)* — op `channel` — node "Success Message2" (id `bf980404-a286-40cf-ab48-4557446f7065`)
- *(dynamic channel)* — op `channel` — node "Slack5" (id `c3ccc1b1-82ab-4889-ac1b-78cb2ca60e53`)
- *(dynamic channel)* — op `channel` — node "Slack11" (id `d7fcadfe-ba25-4df1-b291-c5a52bb1b909`)
- *(dynamic channel)* — op `channel` — node "Slack2" (id `ea51e664-ffad-4d59-ac5b-2e9e021bb36c`)
- *(dynamic channel)* — op `channel` — node "Slack10" (id `f740b198-2d2b-4baa-93ae-ee1e9ecbd680`)

### Google Docs

- [[../resources/google-docs/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA]] (id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `get` — node "Get a document" (id `78716a79-9d30-46e5-9a9e-440074ec911c`)

### Sub-workflows (Execute Workflow calls)

- [[payengineai-bot-v1-2-jun-12-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] (n8n_id `0yjTSaTSRLaCOgvH`) — node "Read Emails1" (id `086d0da1-9831-4cd4-9d3c-f5164afe01b0`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `0f9ab653-22cd-47d6-9f7a-44278179ba4b`)
- [[onboarding-correspondence-aging|Onboarding Correspondence Aging]] (n8n_id `DjgdzbbtR7fJ4oWX`) — node "Run Correspondence Aging Report" (id `25568675-6936-4e80-bb49-e1b3c65db470`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'1" (id `4c2efbe1-352b-4624-935a-d6764c31e920`)
- [[payengineai-bot-v1-2-jun-12-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] (n8n_id `0yjTSaTSRLaCOgvH`) — node "Call PayEngineBot" (id `56bc2196-99c3-4223-9ca3-9ab970fac434`)
- [[payengineai-bot-v1-2-jun-12-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] (n8n_id `0yjTSaTSRLaCOgvH`) — node "Create Draft In Merchants Inbox1" (id `ad52b28d-1dcd-4a9b-b35f-aa24fe185c1b`)
- [[elavon-ach-exemption-form-generator|Elavon ACH Exemption Form Generator]] (n8n_id `c4rexPHrWGfGDBUP`) — node "Elavon ECS/ACH Max Check Size Generator" (id `ce996276-c9a4-4a86-a434-3cde348aa3bc`)
- [[payengineai-bot-v1-2-jun-12-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] (n8n_id `0yjTSaTSRLaCOgvH`) — node "Call Onboarding Correspondence Aging Report Tool" (id `e64d7759-24d4-429f-b13a-b2434c194f30`)
- [[payengineai-bot-v1-2-jun-12-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] (n8n_id `0yjTSaTSRLaCOgvH`) — node "Execute Workflow1" (id `f1a4b9c6-4f86-435f-b0e3-bf602f97e8aa`)

## Used by (workflows)

- [[payengineai-bot-v1-2-jun-12-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] — node "Call Onboarding Correspondence Aging Report Tool" (id `e64d7759-24d4-429f-b13a-b2434c194f30`)
- [[payengineai-bot-v1-2-jun-12-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] — node "Call PayEngineBot" (id `56bc2196-99c3-4223-9ca3-9ab970fac434`)
- [[payengineai-bot-v1-2-jun-12-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] — node "Create Draft In Merchants Inbox1" (id `ad52b28d-1dcd-4a9b-b35f-aa24fe185c1b`)
- [[payengineai-bot-v1-2-jun-12-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] — node "Execute Workflow1" (id `f1a4b9c6-4f86-435f-b0e3-bf602f97e8aa`)
- [[payengineai-bot-v1-2-jun-12-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] — node "Read Emails1" (id `086d0da1-9831-4cd4-9d3c-f5164afe01b0`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
