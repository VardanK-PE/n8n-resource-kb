---
n8n_id: "NAzTAEmqdaFoKHId"
name: "PayEngineAI Bot (v1) Backup 2025-08-30"
status: inactive
last_modified: 2025-08-31T04:07:55.548Z
tags:
  - "backups"
fingerprint: "cd6f2381a390a047eb3d6bd30e59085715a839c413301c29dc95fa837c0f3a8e"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PayEngineAI Bot (v1) Backup 2025-08-30

## Summary

- **Status:** inactive
- **n8n ID:** `NAzTAEmqdaFoKHId`
- **Nodes:** 159
- **Last modified:** 2025-08-31T04:07:55.548Z

## Triggers

- **webhook** — node "Incoming response" (id `37e138ea-e6fa-479d-80ea-0d34f9b42b34`) — POST `241cebc7-568b-499a-9fdb-eb1020b420ac`
- **webhook** — node "Incoming /secops-change" (id `453b5966-baa0-4958-a8fc-afbe6dd3102e`) — POST `06a59506-8196-4959-861c-820a95a4e8ee`
- **error** — node "Error Trigger" (id `5021787a-91a9-4571-aa1c-741b1aa6c2f3`)
- **execute-workflow** — node "Execute Workflow Trigger" (id `598474d5-3a37-4e5a-9105-090380f8c159`)
- **schedule** — node "Schedule Trigger" (id `62bff007-1fa3-4ede-90f9-15cfa6003092`) — `every 65 second(s)`
- **manual** — node "When clicking "Execute Workflow"" (id `7247f995-b2ea-4bbb-8b54-a3159d11a581`)
- **schedule** — node "Schedule Trigger1" (id `b928dbeb-6e73-4267-a4ad-e8781fbd60da`) — `every 1 minute(s)`
- **webhook** — node "Slashcommand" (id `c5968b7a-20c6-44bb-a24b-19c42c9c1659`) — POST `4cf8fc62-6f8e-4c81-80ce-ee7628740028`
- **other** — node "On new manual Chat Message" (id `da21f284-2d00-44f6-a252-b294dc8cda2b`)
- **webhook** — node "Webhook" (id `eeb805a9-08be-44ae-88c2-b3fe3e98cc0a`) — POST `45778b07-b89e-4ffa-9920-7ff3971d7264`
- **webhook** — node "app_mention" (id `f2a0e3fc-3c6b-4ba4-bf66-edb09935acb0`) — POST `3a2f2c81-1106-4575-970c-1bf7beb012be`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant/Partner Details Lookup" (id `0245d163-1918-4494-b579-319e375f12a4`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox (bk 2025-08-30)" (id `0927470f-76cc-40de-8950-8e4cc4fb705d`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox2" (id `0cae8c77-0938-4ff1-a4ee-ac4513dfd952`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `160e3069-f498-4460-b699-ab41ca403610`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model2" (id `1de3a37b-68fc-43c2-b974-9416ed0f6788`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Direct Reply Drafts in PE Inbox" (id `1f584e9e-6cd6-4bba-b158-195ddd0f9d43`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Success Message2" (id `23beb50a-52f3-42ec-b351-13baf4765efe`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `24224ed2-f9aa-45cf-91cd-070f5d688a1c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `2ac3b5bb-2f8c-465a-a197-55f94b2bb683`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Elavon Declined ACHs" (id `2d55c15a-5e3a-479e-88e4-5f8dbbce660a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Posting a Form" (id `316b800c-98db-46c2-b441-3bcc077fbc7d`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Add label to message" (id `32460ca7-620c-4fb2-8e76-e3bfeae0103b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get a document" (id `40cd59ca-ec23-4340-b82e-e92c59b91574`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `42ac9288-7f84-4d18-a08d-49b06b9a4993`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state" (id `4315d407-a9f0-44f7-9187-f934378c18dd`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack4" (id `44a47669-c5b5-467d-b9ca-af3fdf1e8908`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack10" (id `4bf58dd4-9783-481b-b0c5-732b58a4f706`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `4c970b00-efb0-4c6a-b68a-e73ac038bd55`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `5ac7cd43-4843-4b67-82c0-e735755ebc11`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create Draft In Heart Inbox1" (id `5b6f1739-2b79-47d7-a079-260808f6fc2a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack11" (id `67b537a1-5003-4e8d-bd1f-43fc75e0f9cc`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `6bcd2cd0-8d90-43a1-a327-9ea0f4c723c6`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `7797b876-15b3-419d-aad6-1b495da3769c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `868640f9-dca1-400c-980b-a92dc2b598b2`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "PE Slack1" (id `888aab0c-a867-4bfe-9b47-228117138da3`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `8b35b0f6-1170-44ab-b62a-450075b698c4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Subprompt Updater1" (id `8cd77556-6ae3-4b8e-b541-4326196ebdb7`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file1" (id `8dcc445c-7058-4f4f-9a21-99b16b2cbe38`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Add label to message1" (id `8e7e247a-63ee-4226-97bb-3e1a8ea3b979`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack6" (id `90b27141-261a-47e5-9640-87ffad01f316`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download AI Prompt" (id `931ed6a3-8f08-42b9-92b0-fb7763925527`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon" (id `937f5fe9-174b-4f2a-bd46-6a77aab58b59`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Assistant" (id `94e0492f-4a96-41bf-9355-4a132bb5156e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets6" (id `9598e29e-f168-4336-8afc-7f9e34e9fadc`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `9906b823-dba8-4d90-99ab-716b90694524`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth" (id `997b4905-3f0a-40a2-9d42-3c2d52f9533e`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Partner Account Lookup" (id `9c9e0e25-c0fb-465a-a43a-8b4e52ab7c04`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model" (id `9d5954c1-08c4-4f23-a841-bdfcd5bbbedc`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (without attachment)" (id `9de96e19-a9fb-4d3f-adaf-6ae98d198750`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Merchant Reply" (id `9f13b941-ad2c-431a-b038-e435357f4bfe`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `a00f5ca1-7c63-4c18-9985-5556b609930c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Execution Logger" (id `a25c866d-cd70-4aa5-b680-6b1e888e9770`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model1" (id `b00becfe-fa6b-431e-b31f-f7ca14ede9a4`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack3" (id `b3c6a58f-dde5-4f71-b108-fed980fe0a11`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `b7308385-503b-4e07-896f-304424b34620`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `bbeedcb7-605b-42f9-b579-bf7d3f1234cd`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox" (id `c01b7744-16a3-4b4d-8732-c9fffa2abca7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "SubPrompts1" (id `c1926ecf-af2e-44ae-9017-094b4c722cb8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `ce73678b-5613-4d87-b42a-2a64e704c829`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE_Merchants" (id `db89d16a-ffae-4373-90e2-c0b5458da1e6`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file" (id `dcb4164c-6bd8-453a-9604-8d15584393b5`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `dd02e1e4-fe7f-4b65-ac7e-eefacfeb839e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `dee6b0f3-cb63-492f-a5f0-086c68d1b1ee`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send "new email received" notification" (id `e226d28c-b88f-4a6b-af34-cb442c4466f2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `e2784fe9-f66c-4a20-90fa-86663b5e2739`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state1" (id `e3032fa8-6f1f-4e88-aaea-71a11ee75e27`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Partner Specific Instructions" (id `e59f2eef-b4ae-45dc-b6ee-2dd1d6893c4c`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox1 (bk 2025-08-30)" (id `e6914ae9-2289-4bd5-b4b9-b835bae5214e`)
- [[../resources/credentials/6iq3hrw7e8hxpeoa|PE Support Gmail Account (support@payengine.co)]] (`gmailOAuth2`, id `6Iq3hRW7e8hxpEOa`) — node "Merchants Inbox1" (id `f32359bf-f314-465e-bafb-89649a666e3b`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model2" (id `f3b989a6-f63b-4109-9003-e681c04520c1`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack5" (id `f8b82242-b676-439b-aac0-9c1897d749fa`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (with attachment)" (id `fc205fce-6b19-4cc9-9c9d-8ff8a37f9db9`)

### HTTP URLs

- [[../resources/http-urls/slack-com|slack.com]] — `POST https://slack.com/api/views.open` — node "Posting a Form" (id `316b800c-98db-46c2-b441-3bcc077fbc7d`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant/Partner Details Lookup" (id `0245d163-1918-4494-b579-319e375f12a4`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `9906b823-dba8-4d90-99ab-716b90694524`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Partner Account Lookup" (id `9c9e0e25-c0fb-465a-a43a-8b4e52ab7c04`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `dd02e1e4-fe7f-4b65-ac7e-eefacfeb839e`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model2" (id `1de3a37b-68fc-43c2-b974-9416ed0f6788`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model" (id `6bcd2cd0-8d90-43a1-a327-9ea0f4c723c6`)
- [[../resources/llm-models/openai-unspecified|openai / ?]] — node "OpenAI Assistant" (id `94e0492f-4a96-41bf-9355-4a132bb5156e`)
- [[../resources/llm-models/openai-gpt-4|openai / gpt-4]] — node "OpenAI Chat Model" (id `9d5954c1-08c4-4f23-a841-bdfcd5bbbedc`)
- [[../resources/llm-models/openai-o3-pro|openai / o3-pro]] — node "OpenAI Chat Model1" (id `b00becfe-fa6b-431e-b31f-f7ca14ede9a4`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model1" (id `b7308385-503b-4e07-896f-304424b34620`)
- [[../resources/llm-models/openai-gpt-5|openai / gpt-5]] — node "OpenAI Chat Model2" (id `f3b989a6-f63b-4109-9003-e681c04520c1`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-yaml|n8n-nodes-yaml]] — type `n8n-nodes-yaml.yaml` — node "YAML" (id `3f226f96-042e-459d-b984-1d06c8235645`)

### Google Sheets

- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets5" (id `160e3069-f498-4460-b699-ab41ca403610`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `appendOrUpdate`, tab `EmailLogs` — node "Google Sheets1" (id `2ac3b5bb-2f8c-465a-a197-55f94b2bb683`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `ElavonDeclinedACH` — node "Log Elavon Declined ACHs" (id `2d55c15a-5e3a-479e-88e4-5f8dbbce660a`)
- [[../resources/google-sheets/14fmhaamqlgpq5blxfkns4yisa7juvcmkcmmdknl4g1o|PayEngineAIBotLogs]] (id `14fmhaamQlGPQ5BLxfKNS4yISA7jUvcMkCmmDKNL4g1o`) — op `append`, tab `MentionLogs` — node "Google Sheets" (id `42ac9288-7f84-4d18-a08d-49b06b9a4993`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Update row in sheet" (id `4c970b00-efb0-4c6a-b68a-e73ac038bd55`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `SubPrompts` — node "Subprompt Updater1" (id `8cd77556-6ae3-4b8e-b541-4326196ebdb7`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets6" (id `9598e29e-f168-4336-8afc-7f9e34e9fadc`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `EmailLogs` — node "Google Sheets2" (id `a00f5ca1-7c63-4c18-9985-5556b609930c`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `AIExecutionHistory` — node "Execution Logger" (id `a25c866d-cd70-4aa5-b680-6b1e888e9770`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `SubPrompts` — node "SubPrompts1" (id `c1926ecf-af2e-44ae-9017-094b4c722cb8`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `EmailLogs` — node "Google Sheets4" (id `ce73678b-5613-4d87-b42a-2a64e704c829`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets3" (id `e2784fe9-f66c-4a20-90fa-86663b5e2739`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partnerSpceficInstructions` — node "Get Partner Specific Instructions" (id `e59f2eef-b4ae-45dc-b6ee-2dd1d6893c4c`)

### Google Drive

- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download file" (id `24224ed2-f9aa-45cf-91cd-070f5d688a1c`)
- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download AI Prompt" (id `931ed6a3-8f08-42b9-92b0-fb7763925527`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Success Message2" (id `23beb50a-52f3-42ec-b351-13baf4765efe`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state" (id `4315d407-a9f0-44f7-9187-f934378c18dd`)
- *(dynamic channel)* — op `channel` — node "Slack10" (id `4bf58dd4-9783-481b-b0c5-732b58a4f706`)
- *(dynamic channel)* — op `channel` — node "Slack2" (id `5ac7cd43-4843-4b67-82c0-e735755ebc11`)
- *(dynamic channel)* — op `channel` — node "Slack11" (id `67b537a1-5003-4e8d-bd1f-43fc75e0f9cc`)
- *(dynamic channel)* — op `channel` — node "Send a message" (id `7797b876-15b3-419d-aad6-1b495da3769c`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `868640f9-dca1-400c-980b-a92dc2b598b2`)
- *(dynamic channel)* — op `channel` — node "PE Slack1" (id `888aab0c-a867-4bfe-9b47-228117138da3`)
- [[../resources/slack-channels/c06c4lcjadv|payengine-ai-tests]] (id `C06C4LCJADV`) — op `channel` — node "Slack" (id `8b35b0f6-1170-44ab-b62a-450075b698c4`)
- *(dynamic channel)* — op `channel` — node "Slack6" (id `90b27141-261a-47e5-9640-87ffad01f316`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send a message6" (id `bbeedcb7-605b-42f9-b579-bf7d3f1234cd`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send "new email received" notification" (id `e226d28c-b88f-4a6b-af34-cb442c4466f2`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state1" (id `e3032fa8-6f1f-4e88-aaea-71a11ee75e27`)
- *(dynamic channel)* — op `channel` — node "Slack5" (id `f8b82242-b676-439b-aac0-9c1897d749fa`)

### Google Docs

- [[../resources/google-docs/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA]] (id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `get` — node "Get a document" (id `40cd59ca-ec23-4340-b82e-e92c59b91574`)

### Sub-workflows (Execute Workflow calls)

- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Read Emails1" (id `25ff1f78-f492-4316-b5fc-55ef94fe9d11`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Execute Workflow1" (id `27e77f96-9c9d-4481-b41e-5e1803d26b07`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Create Draft In Merchants Inbox1" (id `ad27c598-735a-4fcc-b444-8de972174e3d`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Execute Workflow" (id `d93bfe4c-814d-47fb-8ce3-ea776e59a5c5`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
