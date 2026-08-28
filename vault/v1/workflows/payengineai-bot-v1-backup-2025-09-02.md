---
n8n_id: "L0vnaWVsQZMKsDqp"
instance: v1
name: "PayEngineAI Bot (v1) Backup 2025-09-02"
status: inactive
last_modified: 2025-09-03T01:50:15.246Z
tags:
  - "backups"
fingerprint: "5e9a7831c94b8ad6a95f2478f3cf5d9f9357d9f76cd07d404743f7b8477830a4"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PayEngineAI Bot (v1) Backup 2025-09-02

## Summary

- **Status:** inactive
- **n8n ID:** `L0vnaWVsQZMKsDqp`
- **Nodes:** 160
- **Last modified:** 2025-09-03T01:50:15.246Z

## Triggers

- **webhook** — node "app_mention" (id `006be669-b4e4-4975-a159-c3b199702df2`) — POST `6a3d8e9d-19a6-412b-8392-a85eeb78f5a7`
- **schedule** — node "Schedule Trigger" (id `1bc2c81e-18a9-4e92-96a2-e61a89f0dbef`) — `every 65 second(s)`
- **other** — node "On new manual Chat Message" (id `3e1aca27-4186-4dfb-be51-b67afb2dd5ed`)
- **error** — node "Error Trigger" (id `973eff43-bd22-4685-9b50-5110dc38db56`)
- **webhook** — node "Incoming /secops-change" (id `9b9ccb77-0c39-48be-ad78-7498f8f7c5af`) — POST `07ac7eeb-8c5d-4f91-a04d-40b31ce38748`
- **webhook** — node "Slashcommand" (id `9e064f23-6701-4647-8b9f-d9dcfa5b265b`) — POST `9b654874-c5b1-4400-8100-901c1c4695cb`
- **schedule** — node "Schedule Trigger1" (id `afd803ca-7b58-41c3-a85b-138f07675637`) — `every 1 minute(s)`
- **execute-workflow** — node "Execute Workflow Trigger" (id `b3f04c5e-039a-4223-8fd3-c3e829102067`)
- **webhook** — node "Webhook" (id `b96cc53c-302d-4144-bf95-0d29accf05ef`) — POST `8f46fce0-e7b3-47b6-9420-c4c858ef7316`
- **manual** — node "When clicking "Execute Workflow"" (id `be27a64a-2d28-47d8-8067-7bf9967b302a`)
- **webhook** — node "Incoming response" (id `c82858c3-4fb3-47e7-950a-f52f0a148380`) — POST `8504a49b-195e-422f-99c5-c3759e6837ef`

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Posting a Form" (id `0b7f551e-4a6e-4559-b496-aaac11152efd`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model1" (id `0e768f4f-a510-4cac-9426-effa02808ffa`)
- [[../resources/credentials/6iq3hrw7e8hxpeoa|PE Support Gmail Account (support@payengine.co)]] (`gmailOAuth2`, id `6Iq3hRW7e8hxpEOa`) — node "Merchants Inbox1" (id `12f3e665-4c26-4f4d-96a5-59ab87a4d003`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack3" (id `16cacc06-2823-48ac-9636-5148d0fa6324`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get a document" (id `19ee3d29-6dbb-4143-afde-c3180d35f6b8`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model2" (id `1a3a6964-7658-45b4-8a9c-2bc07530d69e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Elavon Declined ACHs" (id `1a444b4b-6f02-4406-9b07-3fd2c7ee2ddf`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `1c871b24-e0bc-4ab4-964d-ebacd5af8c91`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `1f48cef6-394a-409d-9b55-3fdd0a793042`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE_Merchants" (id `26013a4d-f736-495c-a9ea-60d47b86c17c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `2706b996-0251-424c-a3af-7e8bbf9b85d8`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack5" (id `283ca253-0116-49e4-9364-0d156abe58b8`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create Draft In Heart Inbox1" (id `346fd477-2c23-49c8-8daf-5b6dec3909f6`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `39b28e36-2c8c-4868-8f9c-96931ff8e547`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `3af35fed-190a-4d72-9cf7-be112177b901`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download AI Prompt" (id `3f3a162b-02c1-4b6a-98e3-ea571519d7cd`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file" (id `42d4903d-68a3-42b9-a2ee-0affb1ec6fa3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Subprompt Updater1" (id `4402c780-8151-4dba-a47b-711ebe2267ef`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox2" (id `4526cb34-59b3-4559-b688-3b3598535abd`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Merchant Reply" (id `4bd3ef2a-fe91-4576-b89e-1ae678275470`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file1" (id `4e551116-3582-4d73-9441-67cfb3c67c61`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack10" (id `5212c7a7-f2f2-4e4c-b1f4-9bd3b4d2013a`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon" (id `55fc7209-75f9-44a8-b100-589082e5439d`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth" (id `5714a1b2-cd5c-4acc-8306-e19e5a3b082d`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Add label to message1" (id `5b14b4f6-d606-4899-98cb-b8dc841e4ebe`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `6271c77c-77d4-41c7-9c26-c7128d80f8ec`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `68f3685a-4428-431d-9276-e8673560ac5a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack4" (id `698db7ad-fa8f-4957-b63d-26e759e2df3a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets6" (id `6ba2d1ec-d198-4908-97ff-238583502a9b`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Create Draft In Supermove Inbox" (id `70684ee7-96a3-4e18-9b6d-d587c29dd170`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `710d489b-6d02-4d39-b10e-e8f5f8544db6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `71c59e8c-1f27-4849-984b-5303de60b5db`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox (bk 2025-08-30)" (id `7909cc6b-dfe8-42d1-a93f-d04200098e45`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "SubPrompts1" (id `79359e6b-cc55-4841-a471-9bd3bbab367e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send "new email received" notification" (id `7ae46335-28e0-4e18-ac2b-bd38845295c5`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox" (id `856905d0-d1b8-4b52-bb25-6046d9ab7b9d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack6" (id `8712bab8-898a-4ded-a72d-a7d0dedf35a7`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `90488c84-14af-4d38-bb67-ba4fb1fbe8bd`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (with attachment)" (id `9133d3db-793c-4a1c-8f60-8ea616915a44`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "PE Slack1" (id `97efc383-6633-4c60-832b-2f544ff13c10`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant/Partner Details Lookup" (id `9b05e62a-294a-419f-b38d-227eada3b7dd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Partner Specific Instructions" (id `9d05aee6-4281-4249-826e-27503f54c966`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `9d0628c0-c104-4bc5-8398-6a5b269c3080`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Direct Reply Drafts in PE Inbox" (id `9e5c86d0-6b5a-4639-81b9-7998a53b36b2`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Success Message2" (id `a391ef5f-e1b6-464a-907b-7a28982709e7`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `a622897e-faf9-4bd9-a664-b66ca9f5dd05`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Assistant" (id `a99f1713-d40e-4803-993c-654465ec0dec`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `abd12169-290e-4186-9a33-0de79f80a78f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state" (id `ad557354-d280-4e91-b6bc-d82e4068fb14`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Partner Account Lookup" (id `bd4708ba-1444-4aec-82c4-c8bddda1b2a0`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack11" (id `bde5061d-20ca-4db5-8ede-d20c961b3f2f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state1" (id `be29c178-4899-47c7-82bc-ba67a4f16ed1`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model2" (id `d14985da-4614-4657-a043-7d4d71432e9a`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Add label to message" (id `d352fca5-6213-4050-bc6e-31449dc64a25`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `d3db7f72-f1c6-424c-a973-27899cd9fb40`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `d77464a6-7ea6-4a1b-a47f-8c2ac92f1c09`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox1 (bk 2025-08-30)" (id `d7f8cf68-f450-48c5-8682-35edf7c80b83`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (without attachment)" (id `ddc59d37-d464-4fd5-ac8f-3889c4bcbd4a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `e5eb6b62-a296-4ec0-bae4-36a869a75aaa`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `e6f6d8c2-7e46-490b-a6ef-365deb32a98d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Execution Logger" (id `fb67f5ab-7141-42a3-80db-c63a4ade9ec5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `fd48b3af-59c8-4b09-aed2-c7f5909e57d1`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model" (id `ff94dd54-982d-430b-a60f-e675238071fb`)

### HTTP URLs

- [[../resources/http-urls/slack-com|slack.com]] — `POST https://slack.com/api/views.open` — node "Posting a Form" (id `0b7f551e-4a6e-4559-b496-aaac11152efd`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `39b28e36-2c8c-4868-8f9c-96931ff8e547`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant/Partner Details Lookup" (id `9b05e62a-294a-419f-b38d-227eada3b7dd`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `9d0628c0-c104-4bc5-8398-6a5b269c3080`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Partner Account Lookup" (id `bd4708ba-1444-4aec-82c4-c8bddda1b2a0`)

### LLM models

- [[../resources/llm-models/openai-o3-pro|openai / o3-pro]] — node "OpenAI Chat Model1" (id `0e768f4f-a510-4cac-9426-effa02808ffa`)
- [[../resources/llm-models/openai-gpt-5|openai / gpt-5]] — node "OpenAI Chat Model2" (id `1a3a6964-7658-45b4-8a9c-2bc07530d69e`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model" (id `710d489b-6d02-4d39-b10e-e8f5f8544db6`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model1" (id `90488c84-14af-4d38-bb67-ba4fb1fbe8bd`)
- [[../resources/llm-models/openai-unspecified|openai / ?]] — node "OpenAI Assistant" (id `a99f1713-d40e-4803-993c-654465ec0dec`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model2" (id `d14985da-4614-4657-a043-7d4d71432e9a`)
- [[../resources/llm-models/openai-gpt-4|openai / gpt-4]] — node "OpenAI Chat Model" (id `ff94dd54-982d-430b-a60f-e675238071fb`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-yaml|n8n-nodes-yaml]] — type `n8n-nodes-yaml.yaml` — node "YAML" (id `30c0a66c-4b7f-4759-bdba-08036aa4f9d4`)

### Google Sheets

- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `ElavonDeclinedACH` — node "Log Elavon Declined ACHs" (id `1a444b4b-6f02-4406-9b07-3fd2c7ee2ddf`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `SubPrompts` — node "Subprompt Updater1" (id `4402c780-8151-4dba-a47b-711ebe2267ef`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `EmailLogs` — node "Google Sheets4" (id `6271c77c-77d4-41c7-9c26-c7128d80f8ec`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `EmailLogs` — node "Google Sheets2" (id `68f3685a-4428-431d-9276-e8673560ac5a`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets6" (id `6ba2d1ec-d198-4908-97ff-238583502a9b`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Update row in sheet" (id `71c59e8c-1f27-4849-984b-5303de60b5db`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `SubPrompts` — node "SubPrompts1" (id `79359e6b-cc55-4841-a471-9bd3bbab367e`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partnerSpceficInstructions` — node "Get Partner Specific Instructions" (id `9d05aee6-4281-4249-826e-27503f54c966`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets5" (id `abd12169-290e-4186-9a33-0de79f80a78f`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets3" (id `d3db7f72-f1c6-424c-a973-27899cd9fb40`)
- [[../resources/google-sheets/14fmhaamqlgpq5blxfkns4yisa7juvcmkcmmdknl4g1o|PayEngineAIBotLogs]] (id `14fmhaamQlGPQ5BLxfKNS4yISA7jUvcMkCmmDKNL4g1o`) — op `append`, tab `MentionLogs` — node "Google Sheets" (id `e5eb6b62-a296-4ec0-bae4-36a869a75aaa`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `AIExecutionHistory` — node "Execution Logger" (id `fb67f5ab-7141-42a3-80db-c63a4ade9ec5`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `appendOrUpdate`, tab `EmailLogs` — node "Google Sheets1" (id `fd48b3af-59c8-4b09-aed2-c7f5909e57d1`)

### Google Drive

- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download AI Prompt" (id `3f3a162b-02c1-4b6a-98e3-ea571519d7cd`)
- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download file" (id `d77464a6-7ea6-4a1b-a47f-8c2ac92f1c09`)

### Slack channels

- [[../resources/slack-channels/c06c4lcjadv|payengine-ai-tests]] (id `C06C4LCJADV`) — op `channel` — node "Slack" (id `1c871b24-e0bc-4ab4-964d-ebacd5af8c91`)
- *(dynamic channel)* — op `channel` — node "Send a message" (id `2706b996-0251-424c-a3af-7e8bbf9b85d8`)
- *(dynamic channel)* — op `channel` — node "Slack5" (id `283ca253-0116-49e4-9364-0d156abe58b8`)
- *(dynamic channel)* — op `channel` — node "Slack2" (id `3af35fed-190a-4d72-9cf7-be112177b901`)
- *(dynamic channel)* — op `channel` — node "Slack10" (id `5212c7a7-f2f2-4e4c-b1f4-9bd3b4d2013a`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send "new email received" notification" (id `7ae46335-28e0-4e18-ac2b-bd38845295c5`)
- *(dynamic channel)* — op `channel` — node "Slack6" (id `8712bab8-898a-4ded-a72d-a7d0dedf35a7`)
- *(dynamic channel)* — op `channel` — node "PE Slack1" (id `97efc383-6633-4c60-832b-2f544ff13c10`)
- *(dynamic channel)* — op `channel` — node "Success Message2" (id `a391ef5f-e1b6-464a-907b-7a28982709e7`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send a message6" (id `a622897e-faf9-4bd9-a664-b66ca9f5dd05`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state" (id `ad557354-d280-4e91-b6bc-d82e4068fb14`)
- *(dynamic channel)* — op `channel` — node "Slack11" (id `bde5061d-20ca-4db5-8ede-d20c961b3f2f`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state1" (id `be29c178-4899-47c7-82bc-ba67a4f16ed1`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `e6f6d8c2-7e46-490b-a6ef-365deb32a98d`)

### Google Docs

- [[../resources/google-docs/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA]] (id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `get` — node "Get a document" (id `19ee3d29-6dbb-4143-afde-c3180d35f6b8`)

### Sub-workflows (Execute Workflow calls)

- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Execute Workflow" (id `5303317c-33fc-4051-9747-772f0561ede7`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Read Emails1" (id `a50442df-aaf0-49a3-a95c-075e159ff716`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Create Draft In Merchants Inbox1" (id `bf311c8e-ce6f-48a4-a81d-29c7bb0bb2b4`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Execute Workflow1" (id `edac15fc-fdfc-4c55-8f04-1d23f5fed416`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
