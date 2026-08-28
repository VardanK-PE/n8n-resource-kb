---
n8n_id: "QBg9aLdfqR3kLqVB"
instance: v1
name: "PayEngineAI Bot (v1) BK 2025-09-04"
status: inactive
last_modified: 2025-09-05T04:32:20.799Z
tags:
  - "backups"
fingerprint: "c57e132c26341cfc51c3be45026e37c924e8e20c140e06d285f06c57e889d713"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PayEngineAI Bot (v1) BK 2025-09-04

## Summary

- **Status:** inactive
- **n8n ID:** `QBg9aLdfqR3kLqVB`
- **Nodes:** 179
- **Last modified:** 2025-09-05T04:32:20.799Z

## Triggers

- **manual** — node "When clicking "Execute Workflow"" (id `016ff552-b9ee-41dc-ac60-3b6e68f68685`)
- **schedule** — node "Schedule Trigger" (id `41671996-4a5b-48ca-a389-a945328fc3b0`) — `every 65 second(s)`
- **webhook** — node "Webhook" (id `43cd3e92-2179-489f-87df-7d0133fc6317`) — POST `7dd7fece-b652-4bda-b17b-3a32f112eb31`
- **error** — node "Error Trigger" (id `526ea025-77c0-45a8-9c6b-e86ce0d43ae2`)
- **webhook** — node "Incoming /secops-change" (id `544edd45-8569-4628-8f96-e7daded2177c`) — POST `d5f8a4b0-b7dd-4b09-9c90-018b2c7b0616`
- **schedule** — node "Schedule Trigger1" (id `70fa2efd-cb03-44ed-b2c9-6fe50ddd6467`) — `every 1 minute(s)`
- **webhook** — node "app_mention" (id `7bbd50e0-59f9-44d1-94bb-37e554776632`) — POST `bf2cbe72-2b3a-4bf8-ad03-078b1c1c2d31`
- **other** — node "On new manual Chat Message" (id `7deb6628-369e-4cee-a33a-103360cef5ee`)
- **execute-workflow** — node "Execute Workflow Trigger" (id `8aa4be8c-ef5b-4f3d-8265-37db1ea03090`)
- **webhook** — node "Slashcommand" (id `9d027832-8de3-43fc-b1c2-3a5c26d39cbd`) — POST `174acfe2-e7a6-485a-83a5-f91b0ede8ccd`
- **webhook** — node "Incoming response" (id `d5163212-ef2e-4960-80fb-d9d2ccdffaa9`) — POST `c0766615-fef9-4a1f-8ea0-43050ba922b6`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Posting a Form" (id `01372a25-07c6-4a29-b8db-31eabbc6e9d4`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send "new email received" notification" (id `080fc74d-0f66-4bd4-9f16-e6a1960d9911`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Subprompt Updater1" (id `0aafbb89-627b-4156-8d04-4de92871bbe4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `0ce3ff7c-4945-487a-9498-424fc0cc346b`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (with attachment)" (id `0f4745d9-4678-4311-9017-6da8e27d7534`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack3" (id `1129ecd5-ea9e-4c62-84a5-08caaa82883d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack4" (id `14cecdd1-7420-4e47-a503-f3710143d4f8`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create Draft In Heart Inbox1" (id `1659b09a-9d50-41e7-9a15-ac9a363efe2a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack5" (id `1a711360-ccfc-4a36-b965-83724c2c0521`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Assistant" (id `20e97812-a7d2-402f-8903-e2d6a1ab8623`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `26d7730d-7c9a-49fd-b8ae-e26086b41ace`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state" (id `27164864-ce53-4e75-974a-4fe678ce7a93`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE_Merchants" (id `2d1a52cf-a060-4ef8-b10e-ac455b1ffcdc`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file" (id `2efecf82-6c56-4897-91e0-c2a13506bdfc`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model2" (id `313c9469-ca83-4b59-bd9e-3efe90493c93`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `37a59d70-8f04-4943-a017-436e2457dd3f`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Partner Account Lookup" (id `3ee76dfc-a6fc-428c-963a-e0709d6678c0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `4381351f-d2a2-4dd6-932a-838b3fc67eb0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `4447b408-d7e2-42d8-a49d-647032f1e074`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove Inbox" (id `4c2bf5c1-e625-4efe-928a-c3c1f140035a`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon1" (id `4fdb473b-0596-4f8b-90ab-8cd740fbe1e6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `5191b9ae-67b3-4b8e-b350-1fedcf025cdf`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox1 (bk 2025-08-30)" (id `52d3a7a5-5ba9-40d3-8476-6efe062d926c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get a document" (id `58dbbd90-c52f-4fe5-aac4-86efaa9828ea`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Add label to message1" (id `6097e78e-c21b-46de-9cfc-593b890fd20f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack10" (id `609818ea-f8ee-482f-8b79-7e67105a7e1e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack11" (id `623e54f5-ed6b-4be8-96e5-65ee8fd9482a`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `63d521d2-10f8-4f9e-9901-b2b1c5cbccf2`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model2" (id `64b3be6a-a96b-4d18-a721-8e0e4bef42d0`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `650e1236-66a5-4e5c-89d0-3e458bf5c5d4`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model1" (id `6b896087-f53c-4aa4-bd59-7bbb8478b12f`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox2" (id `7247fc2d-4a9f-4eae-8928-3a2ca6459996`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `75bf0754-c420-4ce4-9879-0a27aa170ca6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `7765c28c-18fa-41e7-8b95-ac8833119ddd`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Success Message2" (id `78402fa7-33cd-41a9-bf9c-2bdfb4640cd2`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Direct Reply Drafts in PE Inbox" (id `79e57fc3-9fb3-4952-aae7-396b18102c08`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file1" (id `7a8dbf0d-078b-420d-8ef4-ad9976b05d8e`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth" (id `7b101975-2dd3-4798-a2d9-c7b0c51ed67c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `7fdf4417-f11a-4b63-af63-2eed0b12bcc6`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack6" (id `89e0a0f6-e261-4c0e-9cb8-b50b4a152f26`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Add label to message2" (id `8ca246ee-c959-4e51-ab7d-9a4202e4416a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `91a06fa0-ad1f-484c-9985-428fafd53794`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model" (id `93cf26e9-a6d8-4d6e-98a6-b213931ae917`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "SubPrompts1" (id `94a274f1-10be-42ca-ad1c-0de00f0d4761`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `95585e45-bc69-4fc1-8410-97ec870b59e3`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `9841337e-4702-4916-97f0-eaa008c18811`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox (bk 2025-08-30)" (id `9cc848cf-d9c9-4b33-9777-a8b37b7edc4f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download AI Prompt" (id `a2179de8-db40-4807-8696-2a782d8ff597`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Execution Logger" (id `ad54cc83-fd1e-4d13-b28a-3114df2064ee`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (without attachment)" (id `b24c85e6-aadb-4f44-8b82-bd50f3642dc8`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Merchant Reply" (id `b5f5fa79-a81e-4ce5-958c-7493ee70b158`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Elavon Declined ACHs" (id `b8982182-1bd5-42a2-b744-93c1abd90305`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `bac20ce0-0b2e-404b-baf4-2e9b0bab3170`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Add label to message" (id `c1dfd55d-ea18-4a0b-9d4d-f1dabe70dd41`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox" (id `cad7c737-6378-430c-b1c0-cf24e8ed4424`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state1" (id `d0b6cdce-2ea8-43d0-9ec7-b4efbcf5b56e`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant/Partner Details Lookup" (id `d30d7ea8-8ba3-40d7-965d-faab3661d0ad`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets6" (id `d329439c-25a7-4bfe-9020-4af2f71be73a`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove" (id `d5a47458-44af-459f-ba4c-9d3d955301ea`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `d629233b-9ee7-4edf-96f4-3679dba74b5d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `d7013c8d-4093-4ea0-b5f5-ef40e449fd19`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon" (id `dca1fcff-60fd-449a-914d-48ea8a32cf04`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `e3c12a65-7cc5-4f2f-8e4f-04a3e0d1a59a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "PE Slack1" (id `eda2b19b-92bf-441d-99c0-1d1674506f15`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth1" (id `f6bb1030-9e4e-42f6-8727-0f1305d79da2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Partner Specific Instructions" (id `fa77e713-24e4-48d2-a4e5-fa8db2fe7a3e`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Create Draft In Supermove Inbox" (id `fbb2d287-67c4-46a7-a494-8aa2bc5d9ee1`)

### HTTP URLs

- [[../resources/http-urls/slack-com|slack.com]] — `POST https://slack.com/api/views.open` — node "Posting a Form" (id `01372a25-07c6-4a29-b8db-31eabbc6e9d4`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Partner Account Lookup" (id `3ee76dfc-a6fc-428c-963a-e0709d6678c0`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `63d521d2-10f8-4f9e-9901-b2b1c5cbccf2`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant/Partner Details Lookup" (id `d30d7ea8-8ba3-40d7-965d-faab3661d0ad`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `e3c12a65-7cc5-4f2f-8e4f-04a3e0d1a59a`)

### LLM models

- [[../resources/llm-models/openai-unspecified|openai / ?]] — node "OpenAI Assistant" (id `20e97812-a7d2-402f-8903-e2d6a1ab8623`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model2" (id `313c9469-ca83-4b59-bd9e-3efe90493c93`)
- [[../resources/llm-models/openai-gpt-5|openai / gpt-5]] — node "OpenAI Chat Model2" (id `64b3be6a-a96b-4d18-a721-8e0e4bef42d0`)
- [[../resources/llm-models/openai-o3-pro|openai / o3-pro]] — node "OpenAI Chat Model1" (id `6b896087-f53c-4aa4-bd59-7bbb8478b12f`)
- [[../resources/llm-models/openai-gpt-4|openai / gpt-4]] — node "OpenAI Chat Model" (id `93cf26e9-a6d8-4d6e-98a6-b213931ae917`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model" (id `bac20ce0-0b2e-404b-baf4-2e9b0bab3170`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model1" (id `d629233b-9ee7-4edf-96f4-3679dba74b5d`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-yaml|n8n-nodes-yaml]] — type `n8n-nodes-yaml.yaml` — node "YAML" (id `7ba101fc-660b-462c-82bb-a748ed4db4ec`)

### Google Sheets

- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `SubPrompts` — node "Subprompt Updater1" (id `0aafbb89-627b-4156-8d04-4de92871bbe4`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets5" (id `0ce3ff7c-4945-487a-9498-424fc0cc346b`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `appendOrUpdate`, tab `EmailLogs` — node "Google Sheets1" (id `37a59d70-8f04-4943-a017-436e2457dd3f`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `EmailLogs` — node "Google Sheets4" (id `4381351f-d2a2-4dd6-932a-838b3fc67eb0`)
- [[../resources/google-sheets/14fmhaamqlgpq5blxfkns4yisa7juvcmkcmmdknl4g1o|PayEngineAIBotLogs]] (id `14fmhaamQlGPQ5BLxfKNS4yISA7jUvcMkCmmDKNL4g1o`) — op `append`, tab `MentionLogs` — node "Google Sheets" (id `5191b9ae-67b3-4b8e-b350-1fedcf025cdf`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Update row in sheet" (id `75bf0754-c420-4ce4-9879-0a27aa170ca6`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets3" (id `7765c28c-18fa-41e7-8b95-ac8833119ddd`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `SubPrompts` — node "SubPrompts1" (id `94a274f1-10be-42ca-ad1c-0de00f0d4761`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `EmailLogs` — node "Google Sheets2" (id `95585e45-bc69-4fc1-8410-97ec870b59e3`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `AIExecutionHistory` — node "Execution Logger" (id `ad54cc83-fd1e-4d13-b28a-3114df2064ee`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `ElavonDeclinedACH` — node "Log Elavon Declined ACHs" (id `b8982182-1bd5-42a2-b744-93c1abd90305`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets6" (id `d329439c-25a7-4bfe-9020-4af2f71be73a`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partnerSpceficInstructions` — node "Get Partner Specific Instructions" (id `fa77e713-24e4-48d2-a4e5-fa8db2fe7a3e`)

### Google Drive

- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download file" (id `4447b408-d7e2-42d8-a49d-647032f1e074`)
- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download AI Prompt" (id `a2179de8-db40-4807-8696-2a782d8ff597`)

### Slack channels

- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send "new email received" notification" (id `080fc74d-0f66-4bd4-9f16-e6a1960d9911`)
- *(dynamic channel)* — op `channel` — node "Slack5" (id `1a711360-ccfc-4a36-b965-83724c2c0521`)
- [[../resources/slack-channels/c06c4lcjadv|payengine-ai-tests]] (id `C06C4LCJADV`) — op `channel` — node "Slack" (id `26d7730d-7c9a-49fd-b8ae-e26086b41ace`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state" (id `27164864-ce53-4e75-974a-4fe678ce7a93`)
- *(dynamic channel)* — op `channel` — node "Slack10" (id `609818ea-f8ee-482f-8b79-7e67105a7e1e`)
- *(dynamic channel)* — op `channel` — node "Slack11" (id `623e54f5-ed6b-4be8-96e5-65ee8fd9482a`)
- *(dynamic channel)* — op `channel` — node "Send a message" (id `650e1236-66a5-4e5c-89d0-3e458bf5c5d4`)
- *(dynamic channel)* — op `channel` — node "Success Message2" (id `78402fa7-33cd-41a9-bf9c-2bdfb4640cd2`)
- *(dynamic channel)* — op `channel` — node "Slack6" (id `89e0a0f6-e261-4c0e-9cb8-b50b4a152f26`)
- *(dynamic channel)* — op `channel` — node "Slack2" (id `91a06fa0-ad1f-484c-9985-428fafd53794`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `9841337e-4702-4916-97f0-eaa008c18811`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state1" (id `d0b6cdce-2ea8-43d0-9ec7-b4efbcf5b56e`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send a message6" (id `d7013c8d-4093-4ea0-b5f5-ef40e449fd19`)
- *(dynamic channel)* — op `channel` — node "PE Slack1" (id `eda2b19b-92bf-441d-99c0-1d1674506f15`)

### Google Docs

- [[../resources/google-docs/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA]] (id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `get` — node "Get a document" (id `58dbbd90-c52f-4fe5-aac4-86efaa9828ea`)

### Sub-workflows (Execute Workflow calls)

- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Execute Workflow1" (id `13366e4f-a446-4b43-ae67-8eec7846d4c8`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Read Emails1" (id `32b7de17-ca76-4a75-a458-bfe0b93078ef`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Execute Workflow" (id `745cabe0-f204-4f46-b427-482dc2599c62`)
- [[elavon-ach-exemption-form-generator|Elavon ACH Exemption Form Generator]] (n8n_id `c4rexPHrWGfGDBUP`) — node "Elavon ECS/ACH Max Check Size Generator" (id `91438807-f109-4d1e-b087-870203660ebf`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Create Draft In Merchants Inbox1" (id `b080ea44-58a9-4753-bc49-ef2b1dddf7e9`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
