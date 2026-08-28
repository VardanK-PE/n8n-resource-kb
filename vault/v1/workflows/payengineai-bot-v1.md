---
n8n_id: "Y1VduzBZY22iN5CY"
name: "PayEngineAI Bot (v1)"
status: inactive
last_modified: 2026-02-26T16:11:30.356Z
tags: []
fingerprint: "65b342d24291de40758b81e484356ad0d23398ec640bc8df2672961585c027b5"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PayEngineAI Bot (v1)

## Summary

- **Status:** inactive
- **n8n ID:** `Y1VduzBZY22iN5CY`
- **Nodes:** 192
- **Last modified:** 2026-02-26T16:11:30.356Z

## Triggers

- **webhook** — node "Slashcommand" (id `31ea1755-ef27-45c6-85fd-34fac9ebafe4`) — POST `b7593f23-c973-4bc8-876f-75a56d6d3169`
- **schedule** — node "Schedule Trigger" (id `4cf86345-48ad-4821-80fc-38f6778d7ee4`) — `every 65 second(s)`
- **webhook** — node "Incoming response" (id `62229ec6-d7b8-401d-b96b-c16f03681af4`) — POST `aaaaaaa-1675-4e9e-b7b9-bbbbbbbbb`
- **other** — node "On new manual Chat Message" (id `68ee61ed-0c23-4dac-886e-072733bd7c15`)
- **webhook** — node "Incoming /secops-change" (id `92a1bfce-d71a-471e-80e6-73b5fd6214e0`) — POST `ccccccccc-6d04-4ea1-8be0-dddddddd`
- **execute-workflow** — node "When Executed by Another Workflow" (id `97b317bd-7410-4ab7-838b-c5054519ffc4`)
- **schedule** — node "Schedule Trigger1" (id `a8ac4a84-0b5e-4fe8-a61d-c163280118d5`) — `every 1 minute(s)`
- **webhook** — node "Webhook" (id `b20a4c1d-13c0-44e5-8ba6-447fb00bd020`) — POST `slack-payengineai`
- **webhook** — node "app_mention" (id `b8081f09-6a8a-4db1-915f-e4fdc7989786`) — POST `a23aead4-bc40-48f2-acda-889fd523bd70`
- **manual** — node "When clicking "Execute Workflow"" (id `c6ec144f-20b9-4add-886b-ce3e0f14d7a9`)
- **error** — node "Error Trigger" (id `db1aaf6a-4751-4eb8-8be2-0d1c3978e26d`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `00d8454f-660f-424b-96e6-811a3f0ba024`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `02b7dcd3-6dee-4af1-a6df-7b13b9e80ddc`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `035701a5-e2b9-4b08-9299-5f820ce6b432`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox" (id `08483841-b16e-4767-b074-0bea3c6514db`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth1" (id `08781180-b627-4dbd-8fe2-cfc36a6dc441`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create Draft In Heart Inbox1" (id `09e03e4c-d911-48dd-95cf-3b27268c144f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `0fbecfbd-a0ce-4d5f-af6f-cdaa514b64da`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `11c2f667-27b7-4816-885e-ffc07b9a5c77`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Add label to message2" (id `14f30742-a5f9-4666-9f5f-36a08a4ea14c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download AI Prompt" (id `160f15aa-26d0-4601-8ffa-f3ff56c78d16`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `1b481f9d-491e-4c2f-8de0-3bcb4885ac56`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Partner Account Lookup" (id `21eca9cf-58da-4f47-b39a-c68800f694ab`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `24c39dde-b952-4772-afab-498ebc9f61ad`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model" (id `2961b842-8c6f-4450-a331-40b02a2757f1`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Add label to message" (id `2c5e5a85-f02c-4dcd-92c4-b711108b1aa5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `2c9ec225-a209-4a79-b27f-f4dad47e5dcc`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "PE Slack1" (id `30fec379-56a9-4be4-be37-439826567e85`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox (bk 2025-08-30)" (id `36ea8eed-794f-4e0c-97b3-3585c43e630f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Execution Logger" (id `3e69c73d-95a0-4ac0-8b23-3c6af0490c7e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get a document" (id `4098cd4c-5e22-49fa-8a83-23d96ed57e58`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model4" (id `43450ed1-b6f1-4d00-b08a-8db0a09f7c9f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state" (id `48116c23-b78f-409d-9d41-e8c8db86af60`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack4" (id `482ffbf4-7acd-4bc1-9e77-7f099c74ac90`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox2" (id `4a105fc6-ee97-46d1-af3b-9ec6d75f8ece`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack5" (id `4fffc8fd-e145-4bce-a71c-b71762f089d9`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Assistant" (id `516fc160-47e9-4e84-afec-163cbb41ac57`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove Inbox" (id `56817d61-027b-41ba-a9b6-7c49561e5259`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE_Merchants" (id `56b4edfc-5fd6-4bea-b092-6f65dbec82a9`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model3" (id `58f2c9c0-1f7f-400a-8b46-0ebfc4466c9e`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Add label to message1" (id `5ee081a7-cd73-43dc-9227-ebec8768119e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file" (id `616b20be-bd94-4c6f-b144-a2483e640948`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth" (id `681e1531-9866-439b-b5aa-ac2486ddd1c7`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file1" (id `68a3965f-4d65-40ea-b81f-3adf15937a2f`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Supermove" (id `69071a81-e7b9-4bb3-884f-49a41b7f147e`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `696df600-5e48-498b-9807-f816b0224e3a`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox1 (bk 2025-08-30)" (id `6984fa58-872d-45e9-a7d7-9ab7a11d43da`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Direct Reply Drafts in PE Inbox" (id `6fe99640-4d17-4af8-b7ba-483e93a94527`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `73afabd4-1518-4f54-bde2-484e9e724a0c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `74b7ccd7-c487-4e5f-ad4e-f77fb7ebef4a`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `7b696a2b-a9b2-45c2-b95d-8d95d72c4753`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack10" (id `7ee1d36d-035e-4fe6-932c-dc485c3019e9`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Merchant Reply" (id `802a43ae-43b4-4f3d-86a1-9ecc40af663c`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model2" (id `81c126a4-7d0b-491a-bc01-cd38cd200425`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `828c9a75-69c6-4f31-9433-6e1934a7b396`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state1" (id `83b8ae8c-589a-4c7f-8ab4-0d1766bfb745`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox2" (id `85a37a89-baad-4674-ad2d-e9e0bf9d0a73`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Success Message2" (id `8891b723-0ebc-408f-a9cd-c97cedd10c25`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model2" (id `91938b95-e841-459f-8029-c8e280d9380e`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon1" (id `935c8694-6eed-464c-b251-dcb21e435f0a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Partner Specific Instructions" (id `95a085b8-5583-43b1-bf70-5ec189b59efa`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Posting a Form" (id `9713522c-cf3d-4c54-b834-77f9bc62da99`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `9cbb5074-3e98-44bb-9c32-446e94c02178`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "Forte Rejected Reason Lookup" (id `9e20f883-3058-4988-a985-5ca3f6de0c25`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Forte Rejected Reason Lookup" (id `9e20f883-3058-4988-a985-5ca3f6de0c25`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Elavon Declined ACHs" (id `a2afdba2-bdb6-4802-be3d-044425836ec6`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant/Partner Details Lookup from PE DB" (id `a7b4dbb9-5a16-4507-bea9-b22d219d6ee2`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (without attachment)" (id `a99194fc-aed7-4eb4-bf91-cedad8e59f83`)
- [[../resources/credentials/godp5gdyjaspv2fj|Anthropic (spartak@platformfactory.io)]] (`anthropicApi`, id `Godp5GdYJAspV2fj`) — node "Anthropic (spartak@platformfactory.io)" (id `ab8f5546-9a18-4b17-8093-fa768f52bc92`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model5" (id `b23e0a2e-bb06-4b75-806a-c7ff6ca936e8`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI Chat Model1" (id `b757fdd3-b655-43e9-9049-42067f47f436`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Subprompt Updater1" (id `c2320ec3-fb93-45e4-8213-6aacb610b917`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack6" (id `c380aa16-2af5-4a02-895f-29c001fbe178`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox1" (id `c675df37-bab0-4a35-b769-ee063ab1d710`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `d4af44c5-ce9c-46ba-9132-cdeb3f36a5d5`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Create Draft In Supermove Inbox" (id `dec96315-32aa-4451-8e89-27911be15ab1`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `df241bd1-f71b-4293-9c06-d8c77342faaf`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack11" (id `e05bcfc5-65a8-48f7-b05a-7783d8d21f1c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `e6d9c413-f42a-4038-805f-ec9cd440b1c4`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic (Spartak@gmail.com)" (id `eb6268b5-04a7-4144-8120-44811f38a6cb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "SubPrompts1" (id `eeaa9beb-fc3f-451c-bc69-c76396628091`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack3" (id `eed4d042-a4c8-4cc7-bb55-4f3cb7cd614a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `f3f78418-3de9-4e3c-aeeb-f6cae52557f6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets6" (id `f482cc90-4405-4520-9be8-ed040292189d`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Request From Elavon" (id `f95ef03d-003d-4388-974c-1507ec0ff26f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send "new email received" notification" (id `f9d0ed50-0f35-4f88-b90c-719431b22f8d`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create Draft (with attachment)" (id `fa7339ef-1031-408b-ba5a-a1262975d871`)

### HTTP URLs

- [[../resources/http-urls/slack-com|slack.com]] — `POST https://slack.com/api/views.open` — node "Posting a Form" (id `9713522c-cf3d-4c54-b834-77f9bc62da99`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/app_{{ $fromAI('ForteApplicationID', ``, 'string') }}` — node "Forte Rejected Reason Lookup" (id `9e20f883-3058-4988-a985-5ca3f6de0c25`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `035701a5-e2b9-4b08-9299-5f820ce6b432`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Partner Account Lookup" (id `21eca9cf-58da-4f47-b39a-c68800f694ab`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant/Partner Details Lookup from PE DB" (id `a7b4dbb9-5a16-4507-bea9-b22d219d6ee2`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `d4af44c5-ce9c-46ba-9132-cdeb3f36a5d5`)

### LLM models

- [[../resources/llm-models/openai-gpt-4|openai / gpt-4]] — node "OpenAI Chat Model" (id `2961b842-8c6f-4450-a331-40b02a2757f1`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model4" (id `43450ed1-b6f1-4d00-b08a-8db0a09f7c9f`)
- [[../resources/llm-models/openai-unspecified|openai / ?]] — node "OpenAI Assistant" (id `516fc160-47e9-4e84-afec-163cbb41ac57`)
- [[../resources/llm-models/openai-gpt-5|openai / gpt-5]] — node "OpenAI Chat Model3" (id `58f2c9c0-1f7f-400a-8b46-0ebfc4466c9e`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model1" (id `696df600-5e48-498b-9807-f816b0224e3a`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model" (id `7b696a2b-a9b2-45c2-b95d-8d95d72c4753`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model2" (id `81c126a4-7d0b-491a-bc01-cd38cd200425`)
- [[../resources/llm-models/openai-gpt-5|openai / gpt-5]] — node "OpenAI Chat Model2" (id `91938b95-e841-459f-8029-c8e280d9380e`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-5-20250929|anthropic / claude-sonnet-4-5-20250929]] — node "Anthropic (spartak@platformfactory.io)" (id `ab8f5546-9a18-4b17-8093-fa768f52bc92`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model5" (id `b23e0a2e-bb06-4b75-806a-c7ff6ca936e8`)
- [[../resources/llm-models/openai-o3-pro|openai / o3-pro]] — node "OpenAI Chat Model1" (id `b757fdd3-b655-43e9-9049-42067f47f436`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-5-20250929|anthropic / claude-sonnet-4-5-20250929]] — node "Anthropic (Spartak@gmail.com)" (id `eb6268b5-04a7-4144-8120-44811f38a6cb`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-yaml|n8n-nodes-yaml]] — type `n8n-nodes-yaml.yaml` — node "YAML" (id `851a6d2b-7a02-4189-b05e-226959d963cc`)

### Google Sheets

- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `EmailLogs` — node "Google Sheets2" (id `00d8454f-660f-424b-96e6-811a3f0ba024`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets5" (id `02b7dcd3-6dee-4af1-a6df-7b13b9e80ddc`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Update row in sheet" (id `11c2f667-27b7-4816-885e-ffc07b9a5c77`)
- [[../resources/google-sheets/14fmhaamqlgpq5blxfkns4yisa7juvcmkcmmdknl4g1o|PayEngineAIBotLogs]] (id `14fmhaamQlGPQ5BLxfKNS4yISA7jUvcMkCmmDKNL4g1o`) — op `append`, tab `MentionLogs` — node "Google Sheets" (id `2c9ec225-a209-4a79-b27f-f4dad47e5dcc`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `AIExecutionHistory` — node "Execution Logger" (id `3e69c73d-95a0-4ac0-8b23-3c6af0490c7e`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partnerSpceficInstructions` — node "Get Partner Specific Instructions" (id `95a085b8-5583-43b1-bf70-5ec189b59efa`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `EmailLogs` — node "Google Sheets4" (id `9cbb5074-3e98-44bb-9c32-446e94c02178`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `ElavonDeclinedACH` — node "Log Elavon Declined ACHs" (id `a2afdba2-bdb6-4802-be3d-044425836ec6`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `SubPrompts` — node "Subprompt Updater1" (id `c2320ec3-fb93-45e4-8213-6aacb610b917`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets3" (id `e6d9c413-f42a-4038-805f-ec9cd440b1c4`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `SubPrompts` — node "SubPrompts1" (id `eeaa9beb-fc3f-451c-bc69-c76396628091`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `appendOrUpdate`, tab `EmailLogs` — node "Google Sheets1" (id `f3f78418-3de9-4e3c-aeeb-f6cae52557f6`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `EmailLogs` — node "Google Sheets6" (id `f482cc90-4405-4520-9be8-ed040292189d`)

### Google Drive

- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download AI Prompt" (id `160f15aa-26d0-4601-8ffa-f3ff56c78d16`)
- [[../resources/google-drive/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|Virtual Merchant Account Manager AI Promp]] (`file`, id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `download` — node "Download file" (id `1b481f9d-491e-4c2f-8de0-3bcb4885ac56`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Send a message4" (id `0fbecfbd-a0ce-4d5f-af6f-cdaa514b64da`)
- *(dynamic channel)* — op `channel` — node "PE Slack1" (id `30fec379-56a9-4be4-be37-439826567e85`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state" (id `48116c23-b78f-409d-9d41-e8c8db86af60`)
- *(dynamic channel)* — op `channel` — node "Slack5" (id `4fffc8fd-e145-4bce-a71c-b71762f089d9`)
- [[../resources/slack-channels/c06c4lcjadv|payengine-ai-tests]] (id `C06C4LCJADV`) — op `channel` — node "Slack" (id `73afabd4-1518-4f54-bde2-484e9e724a0c`)
- *(dynamic channel)* — op `channel` — node "Slack2" (id `74b7ccd7-c487-4e5f-ad4e-f77fb7ebef4a`)
- *(dynamic channel)* — op `channel` — node "Slack10" (id `7ee1d36d-035e-4fe6-932c-dc485c3019e9`)
- *(dynamic channel)* — op `channel` — node "Send a message" (id `828c9a75-69c6-4f31-9433-6e1934a7b396`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Skipping trigger due to active processing state1" (id `83b8ae8c-589a-4c7f-8ab4-0d1766bfb745`)
- *(dynamic channel)* — op `channel` — node "Success Message2" (id `8891b723-0ebc-408f-a9cd-c97cedd10c25`)
- *(dynamic channel)* — op `channel` — node "Slack6" (id `c380aa16-2af5-4a02-895f-29c001fbe178`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send a message6" (id `df241bd1-f71b-4293-9c06-d8c77342faaf`)
- *(dynamic channel)* — op `channel` — node "Slack11" (id `e05bcfc5-65a8-48f7-b05a-7783d8d21f1c`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send "new email received" notification" (id `f9d0ed50-0f35-4f88-b90c-719431b22f8d`)

### Google Docs

- [[../resources/google-docs/1njxtxgp6ga9e2umquemks5bzysisex0gttdruhtezqa|1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA]] (id `1NjXTXGP6Ga9E2UmQUEMKS5bZYSiSEx0GTtDRuHTEZQA`) — op `get` — node "Get a document" (id `4098cd4c-5e22-49fa-8a83-23d96ed57e58`)

### Sub-workflows (Execute Workflow calls)

- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Create Draft In Merchants Inbox1" (id `057bb9f3-7bc7-4d39-8624-b072b586b399`)
- [[onboarding-correspondence-aging|Onboarding Correspondence Aging]] (n8n_id `DjgdzbbtR7fJ4oWX`) — node "Run Correspondence Aging Report" (id `564bd1d8-8eee-4518-b2e5-9c867fa0ac33`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Call Onboarding Correspondence Aging Report Tool" (id `8f470ca1-6bdf-4f5e-ae9a-24047c7ccac3`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Read Emails1" (id `9cf29a3f-8128-462b-876c-58654060c1bf`)
- [[elavon-ach-exemption-form-generator|Elavon ACH Exemption Form Generator]] (n8n_id `c4rexPHrWGfGDBUP`) — node "Elavon ECS/ACH Max Check Size Generator" (id `d2654b32-5b57-42e0-9c5b-ad31902dbe5e`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Execute Workflow1" (id `e61971a3-fb8f-49ac-8d67-e00f51e879f1`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] (n8n_id `Y1VduzBZY22iN5CY`) — node "Execute Workflow" (id `ee1a4d17-92f0-4578-9f97-4927a069827e`)

## Used by (workflows)

- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] — node "Call Onboarding Correspondence Aging Report Tool" (id `8f470ca1-6bdf-4f5e-ae9a-24047c7ccac3`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] — node "Create Draft In Merchants Inbox1" (id `057bb9f3-7bc7-4d39-8624-b072b586b399`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] — node "Execute Workflow" (id `ee1a4d17-92f0-4578-9f97-4927a069827e`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] — node "Execute Workflow1" (id `e61971a3-fb8f-49ac-8d67-e00f51e879f1`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] — node "Read Emails1" (id `9cf29a3f-8128-462b-876c-58654060c1bf`)
- [[payengineai-bot-v1-backup-2025-08-30|PayEngineAI Bot (v1) Backup 2025-08-30]] — node "Create Draft In Merchants Inbox1" (id `ad27c598-735a-4fcc-b444-8de972174e3d`)
- [[payengineai-bot-v1-backup-2025-08-30|PayEngineAI Bot (v1) Backup 2025-08-30]] — node "Execute Workflow" (id `d93bfe4c-814d-47fb-8ce3-ea776e59a5c5`)
- [[payengineai-bot-v1-backup-2025-08-30|PayEngineAI Bot (v1) Backup 2025-08-30]] — node "Execute Workflow1" (id `27e77f96-9c9d-4481-b41e-5e1803d26b07`)
- [[payengineai-bot-v1-backup-2025-08-30|PayEngineAI Bot (v1) Backup 2025-08-30]] — node "Read Emails1" (id `25ff1f78-f492-4316-b5fc-55ef94fe9d11`)
- [[payengineai-bot-v1-backup-2025-09-02|PayEngineAI Bot (v1) Backup 2025-09-02]] — node "Create Draft In Merchants Inbox1" (id `bf311c8e-ce6f-48a4-a81d-29c7bb0bb2b4`)
- [[payengineai-bot-v1-backup-2025-09-02|PayEngineAI Bot (v1) Backup 2025-09-02]] — node "Execute Workflow" (id `5303317c-33fc-4051-9747-772f0561ede7`)
- [[payengineai-bot-v1-backup-2025-09-02|PayEngineAI Bot (v1) Backup 2025-09-02]] — node "Execute Workflow1" (id `edac15fc-fdfc-4c55-8f04-1d23f5fed416`)
- [[payengineai-bot-v1-backup-2025-09-02|PayEngineAI Bot (v1) Backup 2025-09-02]] — node "Read Emails1" (id `a50442df-aaf0-49a3-a95c-075e159ff716`)
- [[payengineai-bot-v1-backup-2025-09-06|PayEngineAI Bot (v1) Backup 2025-09-06]] — node "Create Draft In Merchants Inbox1" (id `57bc4ac5-f189-44fc-80ef-6bd76a0c392a`)
- [[payengineai-bot-v1-backup-2025-09-06|PayEngineAI Bot (v1) Backup 2025-09-06]] — node "Execute Workflow" (id `75fcce89-a4e2-4da2-841c-6ced72044b6b`)
- [[payengineai-bot-v1-backup-2025-09-06|PayEngineAI Bot (v1) Backup 2025-09-06]] — node "Execute Workflow1" (id `eb46f65e-8f28-4a63-a750-69e568fa497a`)
- [[payengineai-bot-v1-backup-2025-09-06|PayEngineAI Bot (v1) Backup 2025-09-06]] — node "Read Emails1" (id `c6b74237-f29e-4896-b8ee-ab4ef49b064c`)
- [[payengineai-bot-v1-bk-2025-09-04|PayEngineAI Bot (v1) BK 2025-09-04]] — node "Create Draft In Merchants Inbox1" (id `b080ea44-58a9-4753-bc49-ef2b1dddf7e9`)
- [[payengineai-bot-v1-bk-2025-09-04|PayEngineAI Bot (v1) BK 2025-09-04]] — node "Execute Workflow" (id `745cabe0-f204-4f46-b427-482dc2599c62`)
- [[payengineai-bot-v1-bk-2025-09-04|PayEngineAI Bot (v1) BK 2025-09-04]] — node "Execute Workflow1" (id `13366e4f-a446-4b43-ae67-8eec7846d4c8`)
- [[payengineai-bot-v1-bk-2025-09-04|PayEngineAI Bot (v1) BK 2025-09-04]] — node "Read Emails1" (id `32b7de17-ca76-4a75-a458-bfe0b93078ef`)
- [[payengineai-bot-v1-bk-2025-09-20|PayEngineAI Bot (v1) BK-2025-09-20]] — node "Create Draft In Merchants Inbox1" (id `5d7ae694-08f6-4d87-8a24-529468f3146b`)
- [[payengineai-bot-v1-bk-2025-09-20|PayEngineAI Bot (v1) BK-2025-09-20]] — node "Execute Workflow" (id `0f54a8a9-4ad0-4f79-bc83-cfdac39c2afe`)
- [[payengineai-bot-v1-bk-2025-09-20|PayEngineAI Bot (v1) BK-2025-09-20]] — node "Execute Workflow1" (id `bd47b027-a4c9-44f0-a662-55fa56b2c54b`)
- [[payengineai-bot-v1-bk-2025-09-20|PayEngineAI Bot (v1) BK-2025-09-20]] — node "Read Emails1" (id `bc4b869a-d0fe-45ca-b5cd-5e00b3edabc7`)
- [[pe-ai-agents|PE AI Agents]] — node "Execute Workflow1" (id `0b08eb25-8c69-4c96-85ba-1237458d5915`)
- [[pe-ai-agents|PE AI Agents]] — node "PayEnginePE Bot" (id `30da42d3-ea10-4824-88fd-54906ccd4dee`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
