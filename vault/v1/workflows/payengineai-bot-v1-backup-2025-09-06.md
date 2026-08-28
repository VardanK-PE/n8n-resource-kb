---
n8n_id: "neoME1ujm6wUh7QS"
instance: v1
name: "PayEngineAI Bot (v1) Backup 2025-09-06"
status: inactive
last_modified: 2025-09-06T17:41:46.473Z
tags:
  - "backups"
fingerprint: "461c4c70eb0f52ff7f7ee2e083fcc6bfb39408fec13fccb453df1caf27d92a27"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PayEngineAI Bot (v1) Backup 2025-09-06

## Summary

- **Status:** inactive
- **n8n ID:** `neoME1ujm6wUh7QS`
- **Nodes:** 179
- **Last modified:** 2025-09-06T17:41:46.473Z

## Triggers

- **other** — node "On new manual Chat Message" (id `06b15b25-8393-432a-8347-ea672b118154`)
- **execute-workflow** — node "Execute Workflow Trigger" (id `26fa6b49-eb04-4af8-95a3-1e20f52ba2b9`)
- **webhook** — node "Webhook" (id `27f7ceb5-2cd6-4600-94bd-38d6afb6e0b5`) — POST `02d1a40d-05c2-4d05-8c6f-86d520828ebd`
- **error** — node "Error Trigger" (id `28e07ea9-6887-49d1-a51e-d9f1814baf17`)
- **webhook** — node "Incoming response" (id `4869d15d-a058-4142-ac6f-2edda28cb737`) — POST `339bc7d5-32f7-4f3f-9a15-8c8e1d3ff20a`
- **webhook** — node "app_mention" (id `4bfc8403-2972-4856-a328-fa5f461605a4`) — POST `06648f9b-4b6a-4005-a620-1b9abefdde2c`
- **schedule** — node "Schedule Trigger" (id `8770384f-628a-4be9-a8e0-8c9118929e56`) — `every 65 second(s)`
- **schedule** — node "Schedule Trigger1" (id `a1a35c18-c132-443a-bd4e-b344ff79458d`) — `every 1 minute(s)`
- **manual** — node "When clicking "Execute Workflow"" (id `a34240b3-044c-4739-99c2-4ee6127a8eda`)
- **webhook** — node "Slashcommand" (id `b4f8cc4c-2524-4407-9278-897cf210a87b`) — POST `8956b213-b341-47e9-8df7-02cfe614beed`
- **webhook** — node "Incoming /secops-change" (id `e46ce65a-008b-4d5f-9791-3d307213f506`) — POST `7067487f-96fd-4ed0-9c23-c4999d065b67`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `02c6a02a-d85d-4124-a9ef-252dadad91f6`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Success Message2" (id `055376f5-edf2-4e04-b372-6179d4520986`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox" (id `0cab4c0f-81c0-4e24-bc94-c308afb976a3`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model2" (id `0d3faa3b-3e09-45d9-8c68-4412c9c135b9`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Add label to message2" (id `16fbe7db-5174-4438-94e2-1fb781682e9c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `18b75e21-53c0-488e-bc2f-23710299463e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `2911c09d-fef0-4c2e-b793-a031c2f7a322`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `32047d18-7695-4e00-b201-17e714cec46b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `32a8b50b-6250-4756-b2a2-92651a0caec2`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Create Draft In Supermove Inbox" (id `38447717-b946-4170-bcfb-06b9c7712604`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack5" (id `3ca7efb7-b4e6-42c6-afd4-bba956ef0942`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `4004fbc3-0345-4148-9e42-d306d8ece76d`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant/Partner Details Lookup" (id `40af0e2d-7519-4065-93a0-a8f28a772c43`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Posting a Form" (id `41468ec3-0b81-4401-aafd-40b77f3f121f`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox1 (bk 2025-08-30)" (id `41dd89b1-7696-432c-9b94-2e7efb35eedc`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove" (id `456b186a-4d99-448f-8bc5-830016e66a40`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets6" (id `50b02c50-fe43-4a6e-9bf4-903e8bfec84b`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack11" (id `539c8053-6031-4dd0-873f-594febcea32a`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model1" (id `552b3c19-c02b-4e2f-9cc6-6a5f3c7fab40`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox (bk 2025-08-30)" (id `58accaf1-8e21-4228-8274-642cc4339178`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (with attachment)" (id `592d8d96-f83a-414e-9a11-cc807396765d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Partner Specific Instructions" (id `5d36f24e-27fe-4db7-b11e-1078905abc34`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file1" (id `63b44cfe-cb06-4ba5-8a5d-daadc39aade1`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack6" (id `64004c84-1df3-4aef-aefb-a42b150ca343`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Execution Logger" (id `6611aeb4-425e-49e4-8a7c-edbd82dcf162`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create Draft In Heart Inbox1" (id `6be3ab73-7675-42d2-a2e8-8760788d7a49`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Elavon Declined ACHs" (id `6e08027f-e7d2-4c3a-9fae-1d16a26b6166`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (without attachment)" (id `6f3e350c-249e-4836-8df6-1b98957d756f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack3" (id `7befbff0-6350-4f97-bec8-86f100c168a8`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model" (id `7e4ca5f5-7f5a-4b81-89f8-e520b565c581`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Subprompt Updater1" (id `7ff94148-8984-4237-8576-5f58174a70be`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state1" (id `8075307f-3ac9-44e0-81ec-704569e4cc30`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Add label to message" (id `832f0ff0-fba6-4240-beb0-f5ee21e22bf4`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `86f73f70-4e8d-4040-8d76-c114506132c4`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack10" (id `8c91752c-9ca2-4788-bf43-06845a870d8d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file" (id `8d831c0f-7519-42d8-8170-aaa8c4fd874f`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox2" (id `90f91126-ad3b-4abb-a011-c0672fc496b4`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `917d70c9-3265-4c87-976a-4ef9a087d04e`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon" (id `95c87e36-f9e8-47be-8226-1c94eddf2a67`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Add label to message1" (id `981dde46-3222-4e65-8323-86369c7bd7b2`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model2" (id `98a7c716-d872-47d6-bf45-557b9e269648`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack4" (id `9d2a017a-c0ab-42dc-871d-7e4c1349c539`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download AI Prompt" (id `a12467d1-d7e4-4fa6-8375-b28e9106c0d8`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE_Merchants" (id `a3a585db-3771-46b6-bebd-b485dc995228`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Merchant Reply" (id `aaa8d5dd-0f59-45b7-8eaa-03ea38db15b6`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove Inbox" (id `af269286-1184-4621-8032-bfbc7bc10345`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state" (id `b74a33a2-4b42-4d2f-9c38-1683db757b73`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get a document" (id `b7ce95ee-553f-422d-81ff-256bfdc3a2f5`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `ba937e8e-c7c8-4ab7-ba88-0206ae04a871`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon1" (id `cab50644-d7d5-42ee-a510-ca2827207f0a`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `cc2947c2-4d2c-4481-b9b6-7b02928738cd`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send "new email received" notification" (id `cd02bbc7-adc4-4106-a0e8-1438f609ac90`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth1" (id `cf3c937b-f331-4791-8dc1-a083ffa00938`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `d269a363-e5eb-465c-89a8-6f4d2a837add`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `d301b19f-13ff-420f-b64c-614d4fc0b806`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "SubPrompts1" (id `d60273a1-0319-4528-bada-1ecc0e4cefd7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `d6acddf5-97b3-49be-a1a9-f58520f4a005`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Direct Reply Drafts in PE Inbox" (id `d7e5b248-e727-44cc-b07a-9165610003d3`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Partner Account Lookup" (id `d838a61e-0bb8-407a-85a5-e4df90c636c7`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth" (id `d9357f00-7f15-4b44-899c-f7877d34a004`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `db5fffab-c038-49a9-9556-b0ba589983ae`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "PE Slack1" (id `e81e13ca-7838-4b8c-bcce-6cb3be269a94`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Assistant" (id `ef8d3d85-e438-4fdb-9994-6c9a541dfb4a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `efd6d2d7-82c1-413e-ad38-30dd21069d91`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `f365d2ab-01fe-4df5-810b-d10ffd9dbb12`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `f87df22b-c2ca-41c0-8e4d-792f48dc7600`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `fab8da6c-f40a-408b-98ef-0401b54bb4af`)

### HTTP URLs

- [[../resources/http-urls/slack-com|slack.com]] — `POST https://slack.com/api/views.open` — node "Posting a Form" (id `41468ec3-0b81-4401-aafd-40b77f3f121f`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant/Partner Details Lookup" (id `40af0e2d-7519-4065-93a0-a8f28a772c43`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `86f73f70-4e8d-4040-8d76-c114506132c4`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `d269a363-e5eb-465c-89a8-6f4d2a837add`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Partner Account Lookup" (id `d838a61e-0bb8-407a-85a5-e4df90c636c7`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model2" (id `0d3faa3b-3e09-45d9-8c68-4412c9c135b9`)
- [[../resources/llm-models/openai-o3-pro|openai / o3-pro]] — node "OpenAI Chat Model1" (id `552b3c19-c02b-4e2f-9cc6-6a5f3c7fab40`)
- [[../resources/llm-models/openai-gpt-4|openai / gpt-4]] — node "OpenAI Chat Model" (id `7e4ca5f5-7f5a-4b81-89f8-e520b565c581`)
- [[../resources/llm-models/openai-gpt-5|openai / gpt-5]] — node "OpenAI Chat Model2" (id `98a7c716-d872-47d6-bf45-557b9e269648`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model" (id `cc2947c2-4d2c-4481-b9b6-7b02928738cd`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model1" (id `db5fffab-c038-49a9-9556-b0ba589983ae`)
- [[../resources/llm-models/openai-unspecified|openai / ?]] — node "OpenAI Assistant" (id `ef8d3d85-e438-4fdb-9994-6c9a541dfb4a`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-yaml|n8n-nodes-yaml]] — type `n8n-nodes-yaml.yaml` — node "YAML" (id `f8e3a3bc-1545-4006-90d8-848bd5c887af`)

### Google Sheets

- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets5" (id `18b75e21-53c0-488e-bc2f-23710299463e`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `EmailLogs` — node "Google Sheets4" (id `32a8b50b-6250-4756-b2a2-92651a0caec2`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Update row in sheet" (id `4004fbc3-0345-4148-9e42-d306d8ece76d`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets6" (id `50b02c50-fe43-4a6e-9bf4-903e8bfec84b`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partnerSpceficInstructions` — node "Get Partner Specific Instructions" (id `5d36f24e-27fe-4db7-b11e-1078905abc34`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `AIExecutionHistory` — node "Execution Logger" (id `6611aeb4-425e-49e4-8a7c-edbd82dcf162`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `ElavonDeclinedACH` — node "Log Elavon Declined ACHs" (id `6e08027f-e7d2-4c3a-9fae-1d16a26b6166`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `SubPrompts` — node "Subprompt Updater1" (id `7ff94148-8984-4237-8576-5f58174a70be`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `EmailLogs` — node "Google Sheets2" (id `d301b19f-13ff-420f-b64c-614d4fc0b806`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `SubPrompts` — node "SubPrompts1" (id `d60273a1-0319-4528-bada-1ecc0e4cefd7`)
- [[../resources/google-sheets/14fmhaamqlgpq5blxfkns4yisa7juvcmkcmmdknl4g1o|PayEngineAIBotLogs]] (id `14fmhaamQlGPQ5BLxfKNS4yISA7jUvcMkCmmDKNL4g1o`) — op `append`, tab `MentionLogs` — node "Google Sheets" (id `d6acddf5-97b3-49be-a1a9-f58520f4a005`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `appendOrUpdate`, tab `EmailLogs` — node "Google Sheets1" (id `f365d2ab-01fe-4df5-810b-d10ffd9dbb12`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets3" (id `fab8da6c-f40a-408b-98ef-0401b54bb4af`)

### Google Drive

- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download file" (id `2911c09d-fef0-4c2e-b793-a031c2f7a322`)
- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download AI Prompt" (id `a12467d1-d7e4-4fa6-8375-b28e9106c0d8`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Success Message2" (id `055376f5-edf2-4e04-b372-6179d4520986`)
- [[../resources/slack-channels/c06c4lcjadv|payengine-ai-tests]] (id `C06C4LCJADV`) — op `channel` — node "Slack" (id `32047d18-7695-4e00-b201-17e714cec46b`)
- *(dynamic channel)* — op `channel` — node "Slack5" (id `3ca7efb7-b4e6-42c6-afd4-bba956ef0942`)
- *(dynamic channel)* — op `channel` — node "Slack11" (id `539c8053-6031-4dd0-873f-594febcea32a`)
- *(dynamic channel)* — op `channel` — node "Slack6" (id `64004c84-1df3-4aef-aefb-a42b150ca343`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state1" (id `8075307f-3ac9-44e0-81ec-704569e4cc30`)
- *(dynamic channel)* — op `channel` — node "Slack10" (id `8c91752c-9ca2-4788-bf43-06845a870d8d`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `917d70c9-3265-4c87-976a-4ef9a087d04e`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state" (id `b74a33a2-4b42-4d2f-9c38-1683db757b73`)
- *(dynamic channel)* — op `channel` — node "Send a message" (id `ba937e8e-c7c8-4ab7-ba88-0206ae04a871`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send "new email received" notification" (id `cd02bbc7-adc4-4106-a0e8-1438f609ac90`)
- *(dynamic channel)* — op `channel` — node "PE Slack1" (id `e81e13ca-7838-4b8c-bcce-6cb3be269a94`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send a message6" (id `efd6d2d7-82c1-413e-ad38-30dd21069d91`)
- *(dynamic channel)* — op `channel` — node "Slack2" (id `f87df22b-c2ca-41c0-8e4d-792f48dc7600`)

### Google Docs

- [[../resources/google-docs/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA]] (id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `get` — node "Get a document" (id `b7ce95ee-553f-422d-81ff-256bfdc3a2f5`)

### Sub-workflows (Execute Workflow calls)

- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Create Draft In Merchants Inbox1" (id `57bc4ac5-f189-44fc-80ef-6bd76a0c392a`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Execute Workflow" (id `75fcce89-a4e2-4da2-841c-6ced72044b6b`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Read Emails1" (id `c6b74237-f29e-4896-b8ee-ab4ef49b064c`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Execute Workflow1" (id `eb46f65e-8f28-4a63-a750-69e568fa497a`)
- [[elavon-ach-exemption-form-generator|Elavon ACH Exemption Form Generator]] (n8n_id `c4rexPHrWGfGDBUP`) — node "Elavon ECS/ACH Max Check Size Generator" (id `edf4d488-5b8c-49ae-aaf6-0b69ec647354`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
