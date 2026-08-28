---
n8n_id: "nCPycKmA1ZTwh2p6"
name: "PayEngineAI Bot (v1) BK-2025-09-20"
status: inactive
last_modified: 2025-09-20T16:07:37.092Z
tags:
  - "backups"
fingerprint: "31794fddd39cdf11ab2638d93c48bdf5b60c2f33fe3e62fa2e8f884563238c1f"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PayEngineAI Bot (v1) BK-2025-09-20

## Summary

- **Status:** inactive
- **n8n ID:** `nCPycKmA1ZTwh2p6`
- **Nodes:** 180
- **Last modified:** 2025-09-20T16:07:37.092Z

## Triggers

- **manual** — node "When clicking "Execute Workflow"" (id `284a1370-95d0-4e75-b883-2b96f45113b2`)
- **webhook** — node "app_mention" (id `40abd6c3-da0d-418c-a272-9fd132b082d7`) — POST `8c42d4eb-9f43-46d1-af12-6c939b2c279b`
- **error** — node "Error Trigger" (id `68b23fff-a757-4969-9e92-43a8cbd287f7`)
- **other** — node "On new manual Chat Message" (id `6cd12728-ecde-4487-afed-69244d993eec`)
- **webhook** — node "Incoming /secops-change" (id `71dc9e5d-f616-4936-bb87-06b90ace3358`) — POST `1ee41ab1-4d73-4386-9272-eb2322729407`
- **execute-workflow** — node "Execute Workflow Trigger" (id `86c9e0f6-5141-4fd5-bacd-a51620f9577c`)
- **schedule** — node "Schedule Trigger1" (id `94633a32-0101-4760-9c95-cf974fe81e19`) — `every 1 minute(s)`
- **webhook** — node "Webhook" (id `94d2ebf3-b46e-42ec-89c4-75121ece8b90`) — POST `215b53ad-5cf3-442a-a5b2-70bd03193038`
- **webhook** — node "Slashcommand" (id `9cdd1f46-f868-44ff-b20b-9a30aa01a9d2`) — POST `05622fc0-1017-4937-a955-85f733155303`
- **schedule** — node "Schedule Trigger" (id `ab9264b7-9246-437f-9d55-95cba6c1ab41`) — `every 65 second(s)`
- **webhook** — node "Incoming response" (id `bef91353-98f7-4b60-969f-f43b563aa9ba`) — POST `54621fe8-8f6b-47be-a728-d04288bbf0c9`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `04ff8b39-9fd0-463e-9c0a-a458e626bd4e`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (without attachment)" (id `05d414c0-9bd5-4f6b-b9b9-4acb9541ee0d`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove Inbox" (id `094bc022-200f-49f9-b6b9-8baa6679c560`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state1" (id `17c5fc5b-6562-4087-bd39-03d82d96e7e5`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove" (id `1cb030cb-77ca-4e70-b0fb-910005274137`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Add label to message2" (id `240901b0-177b-44c2-9114-016369e6dee6`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack3" (id `24275fcf-cbfd-4034-a89f-a23266fca890`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get a document" (id `2d7b655c-e0f4-4c74-bfae-eb3207a8b566`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Elavon Declined ACHs" (id `30f24199-e8e9-49c2-98d6-5562bb93c0da`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "PE Slack1" (id `318d2cb5-353f-4c93-9aff-d61299f529ec`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model1" (id `3e09bd7f-2bb9-4250-8e7c-85acf1224cc9`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `3e6049d4-853e-49ac-af90-7dbc0b1d531d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file" (id `402e1b5c-f2fb-47b5-ac4f-882f427d3a3f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `407f377b-3039-45af-82c7-0ea6bf7fdfab`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Partner Account Lookup" (id `40af9063-5a53-4ffc-a082-c0bbcce675ec`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download AI Prompt" (id `48cc8c60-c1bd-4856-96e2-ed61ab730c90`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create Draft In Heart Inbox1" (id `498c87a0-43f8-44c6-b7e7-8c65d7ec9b90`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets6" (id `549535de-5262-4da3-b1ab-0273d028dcc7`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model" (id `5c0eca56-a955-47b1-ae75-d68c01c63e5e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Subprompt Updater1" (id `5f69217c-07e0-45da-8432-46c768fcf48e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack5" (id `63302c4b-c81f-4222-844e-d80ff1626466`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox (bk 2025-08-30)" (id `63ad54e1-f477-4a52-882f-304975e366a4`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `6750b2c2-5f5b-4f5d-92d5-9044bddc130d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file1" (id `6db6746c-0510-40eb-a8f7-a0ec3c29370b`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant/Partner Details Lookup from PE DB" (id `6e5d07ca-dc96-419c-b142-a6c9d98bc476`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (with attachment)" (id `72fbe508-8c5f-4aab-9633-5b9eefe70562`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon1" (id `763f620b-f864-4c87-b1b3-1991e3fcb6ed`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state" (id `76908a26-b1d1-4314-b28a-db7c70e8375b`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Merchant Reply" (id `7e99b8e8-973e-40a1-871d-0eee1cd16a76`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Create Draft In Supermove Inbox" (id `7ead14e4-45a1-4219-9452-61d8a551fa69`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack11" (id `7f367150-5b10-4a46-be26-de2b09a8d327`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Success Message2" (id `7f3da13c-7ca4-486e-830f-3872e8d8799d`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox2" (id `824ded54-86e1-48a5-8d17-76b9cb0f930c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `85864ea3-bf68-4b3b-81c7-c26b36c80adf`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `86732ef6-cf10-4618-a5d2-3609978ce200`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Add label to message" (id `8c8233ba-bce2-469e-9d50-d101fc77ac1a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `90475416-4c4c-4955-8f2b-3321570bdf0d`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon" (id `a6a7fa3a-9611-4250-92c6-342219742251`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model2" (id `a7835f73-eb11-453b-b444-98cb2d27ea73`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `a91224ac-5ed5-4d75-bc4f-73731cc51cfc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `a92509ed-0e79-4060-a87f-103ac9d18f54`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `aa051c86-f581-4919-8d8b-57becc8633e6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `abbb86e9-d8d6-4bf2-b2c5-159b44916975`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack4" (id `ac3ea7e4-8cb0-4091-aa84-7be699771610`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `b0f8311a-b96e-4778-8d01-717489e4c48e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Posting a Form" (id `b2de53e7-62a9-48de-8f8f-0c829fda24f2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Partner Specific Instructions" (id `b90b9f17-a869-4ad5-963d-95bb46c2163c`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE_Merchants" (id `c06ea939-e5b1-4db3-bf2d-0a6737be1611`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth" (id `c2b18abd-7874-44cc-bd66-4d3a18d1f00c`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth1" (id `c2bc4a29-3aad-413e-92ca-622c094bcaf1`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `c85213ec-bab4-49af-8c8c-7d552ef9ff9a`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `cdadb8dd-a9be-4aa3-83a8-4d3e3382f854`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `cdbe914f-b703-4436-b283-615ff287dbc9`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack6" (id `d7a89290-d4f8-42b1-80c1-ed4d8520d448`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model2" (id `d92f6ecb-ca05-4287-b8df-b0546421fdef`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack10" (id `da965bc5-34b2-4202-9dc7-5acbdc67b57e`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Direct Reply Drafts in PE Inbox" (id `da98bda5-6b0d-414f-9a67-6ad80d74d2c2`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send "new email received" notification" (id `df3489f9-8aed-40f6-8070-534097d63132`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Add label to message1" (id `e2c5f703-3ab3-4907-be35-d3c4cc43a14f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "SubPrompts1" (id `eb406f62-c0bd-47ec-8b65-7504e474e303`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Execution Logger" (id `fa1f4fc2-42e4-4b72-8642-83a7ebf01da0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `faa472ec-cf76-44e8-a26e-63524f734924`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox" (id `fb22dfe1-388d-45d6-8268-1193bc95a5e1`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox1 (bk 2025-08-30)" (id `fbb06752-5713-420b-af8e-4c5269a45bdc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `fc478f23-601c-4d79-8922-5409ced01261`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Assistant" (id `fdb013b7-0097-49f8-b1c6-4106ba5754b3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `fe93aab6-7d27-41ce-a9be-f0cde14a23fe`)

### HTTP URLs

- [[../resources/http-urls/slack-com|slack.com]] — `POST https://slack.com/api/views.open` — node "Posting a Form" (id `b2de53e7-62a9-48de-8f8f-0c829fda24f2`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `04ff8b39-9fd0-463e-9c0a-a458e626bd4e`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Partner Account Lookup" (id `40af9063-5a53-4ffc-a082-c0bbcce675ec`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant/Partner Details Lookup from PE DB" (id `6e5d07ca-dc96-419c-b142-a6c9d98bc476`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `c85213ec-bab4-49af-8c8c-7d552ef9ff9a`)

### LLM models

- [[../resources/llm-models/openai-o3-pro|openai / o3-pro]] — node "OpenAI Chat Model1" (id `3e09bd7f-2bb9-4250-8e7c-85acf1224cc9`)
- [[../resources/llm-models/openai-gpt-4|openai / gpt-4]] — node "OpenAI Chat Model" (id `5c0eca56-a955-47b1-ae75-d68c01c63e5e`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model1" (id `6750b2c2-5f5b-4f5d-92d5-9044bddc130d`)
- [[../resources/llm-models/openai-gpt-5|openai / gpt-5]] — node "OpenAI Chat Model2" (id `a7835f73-eb11-453b-b444-98cb2d27ea73`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model" (id `cdadb8dd-a9be-4aa3-83a8-4d3e3382f854`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model2" (id `d92f6ecb-ca05-4287-b8df-b0546421fdef`)
- [[../resources/llm-models/openai-unspecified|openai / ?]] — node "OpenAI Assistant" (id `fdb013b7-0097-49f8-b1c6-4106ba5754b3`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-yaml|n8n-nodes-yaml]] — type `n8n-nodes-yaml.yaml` — node "YAML" (id `a6980d67-157e-45e2-b26f-46a1d8976a23`)

### Google Sheets

- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `ElavonDeclinedACH` — node "Log Elavon Declined ACHs" (id `30f24199-e8e9-49c2-98d6-5562bb93c0da`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets6" (id `549535de-5262-4da3-b1ab-0273d028dcc7`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `SubPrompts` — node "Subprompt Updater1" (id `5f69217c-07e0-45da-8432-46c768fcf48e`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets5" (id `85864ea3-bf68-4b3b-81c7-c26b36c80adf`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `EmailLogs` — node "Google Sheets4" (id `a92509ed-0e79-4060-a87f-103ac9d18f54`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Update row in sheet" (id `abbb86e9-d8d6-4bf2-b2c5-159b44916975`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `EmailLogs` — node "Google Sheets2" (id `b0f8311a-b96e-4778-8d01-717489e4c48e`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partnerSpceficInstructions` — node "Get Partner Specific Instructions" (id `b90b9f17-a869-4ad5-963d-95bb46c2163c`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `SubPrompts` — node "SubPrompts1" (id `eb406f62-c0bd-47ec-8b65-7504e474e303`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `AIExecutionHistory` — node "Execution Logger" (id `fa1f4fc2-42e4-4b72-8642-83a7ebf01da0`)
- [[../resources/google-sheets/14fmhaamqlgpq5blxfkns4yisa7juvcmkcmmdknl4g1o|PayEngineAIBotLogs]] (id `14fmhaamQlGPQ5BLxfKNS4yISA7jUvcMkCmmDKNL4g1o`) — op `append`, tab `MentionLogs` — node "Google Sheets" (id `faa472ec-cf76-44e8-a26e-63524f734924`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `appendOrUpdate`, tab `EmailLogs` — node "Google Sheets1" (id `fc478f23-601c-4d79-8922-5409ced01261`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets3" (id `fe93aab6-7d27-41ce-a9be-f0cde14a23fe`)

### Google Drive

- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download file" (id `407f377b-3039-45af-82c7-0ea6bf7fdfab`)
- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download AI Prompt" (id `48cc8c60-c1bd-4856-96e2-ed61ab730c90`)

### Slack channels

- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state1" (id `17c5fc5b-6562-4087-bd39-03d82d96e7e5`)
- *(dynamic channel)* — op `channel` — node "PE Slack1" (id `318d2cb5-353f-4c93-9aff-d61299f529ec`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send a message6" (id `3e6049d4-853e-49ac-af90-7dbc0b1d531d`)
- *(dynamic channel)* — op `channel` — node "Slack5" (id `63302c4b-c81f-4222-844e-d80ff1626466`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state" (id `76908a26-b1d1-4314-b28a-db7c70e8375b`)
- *(dynamic channel)* — op `channel` — node "Slack11" (id `7f367150-5b10-4a46-be26-de2b09a8d327`)
- *(dynamic channel)* — op `channel` — node "Success Message2" (id `7f3da13c-7ca4-486e-830f-3872e8d8799d`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `86732ef6-cf10-4618-a5d2-3609978ce200`)
- *(dynamic channel)* — op `channel` — node "Send a message" (id `90475416-4c4c-4955-8f2b-3321570bdf0d`)
- [[../resources/slack-channels/c06c4lcjadv|payengine-ai-tests]] (id `C06C4LCJADV`) — op `channel` — node "Slack" (id `a91224ac-5ed5-4d75-bc4f-73731cc51cfc`)
- *(dynamic channel)* — op `channel` — node "Slack2" (id `cdbe914f-b703-4436-b283-615ff287dbc9`)
- *(dynamic channel)* — op `channel` — node "Slack6" (id `d7a89290-d4f8-42b1-80c1-ed4d8520d448`)
- *(dynamic channel)* — op `channel` — node "Slack10" (id `da965bc5-34b2-4202-9dc7-5acbdc67b57e`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send "new email received" notification" (id `df3489f9-8aed-40f6-8070-534097d63132`)

### Google Docs

- [[../resources/google-docs/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA]] (id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `get` — node "Get a document" (id `2d7b655c-e0f4-4c74-bfae-eb3207a8b566`)

### Sub-workflows (Execute Workflow calls)

- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Execute Workflow" (id `0f54a8a9-4ad0-4f79-bc83-cfdac39c2afe`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Create Draft In Merchants Inbox1" (id `5d7ae694-08f6-4d87-8a24-529468f3146b`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Read Emails1" (id `bc4b869a-d0fe-45ca-b5cd-5e00b3edabc7`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Execute Workflow1" (id `bd47b027-a4c9-44f0-a662-55fa56b2c54b`)
- [[elavon-ach-exemption-form-generator|Elavon ACH Exemption Form Generator]] (n8n_id `c4rexPHrWGfGDBUP`) — node "Elavon ECS/ACH Max Check Size Generator" (id `bd7be718-93ed-4c9f-9287-6a4d062a5d81`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
