---
n8n_id: "3fMuBNt6axo0xTjZ"
instance: v2
name: "Gmail - Send HTML Email"
status: active
last_modified: 2026-08-31T18:37:01.212Z
tags: []
fingerprint: "27680666fe9fd5098f77bfff6bb8d3cc19a2926de8aeba2072ba98cf4a2cb9af"
auto_generated_at: 2026-09-08T19:19:58Z
---

<!-- auto:start -->

# Gmail - Send HTML Email

## Summary

- **Status:** active
- **n8n ID:** `3fMuBNt6axo0xTjZ`
- **Nodes:** 47
- **Last modified:** 2026-08-31T18:37:01.212Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `845839a7-7451-48c9-b33b-51a31a1da691`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `8c36e47c-3c6e-41be-8bb5-ae8ecc1cfa82`)
- **error** — node "Error Trigger" (id `9dea4e08-75b4-4b08-8ba2-312e8f8605c8`)

## Depends on

### Credentials

- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send email from PE inbox" (id `004961f0-2247-4b58-b06b-735d78e28aea`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `0e55b9f4-32ec-40a4-893c-80745754288e`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Send email from Supermove inbox" (id `2bc30932-0ff3-456f-a076-ad5cc65e8a2b`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send email from PE inbox1" (id `3c3b692d-4e0d-4df7-8ac6-97601672bc32`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send email from Hearth inbox1" (id `7a13228d-645c-46cb-8b9e-9545db9330bb`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Send email from Supermove inbox (with Attachments)" (id `a287a549-0345-461c-943d-ca538100f133`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send email from Hearth inbox (with Attachments)1" (id `b351aa35-de27-4e18-b91e-a2d5c77ea0a0`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Send email from Supermove inbox (with Attachments)1" (id `b51ad562-93f8-4acc-8751-0914f7db4057`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send email from PE inbox (with Attachments)" (id `d3869a1c-6a9b-4e9f-ace5-f8859c99ff7b`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send email from PE inbox (with Attachments)1" (id `d9b336f8-1336-4f3b-beb5-488dac26d554`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send email from Hearth inbox (with Attachments)" (id `ec082b4f-f747-41a2-a7c6-48bcae00e923`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send email from Hearth inbox" (id `ec74786b-3eb9-480a-8be6-47ac88c331d5`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Send email from Supermove inbox1" (id `f3553a43-cd54-43a8-8255-9118d7f42f52`)

### Slack channels

- [[../resources/slack-channels/c0998514tkp|elavon-loss-prevention-alerts]] (id `C0998514TKP`) — op `channel` — node "Send a message5" (id `0e55b9f4-32ec-40a4-893c-80745754288e`)

### Sub-workflows (Execute Workflow calls)

- [[gmail-send-html-email|Gmail - Send HTML Email]] (n8n_id `3fMuBNt6axo0xTjZ`) — node "Call 'Gmail - Send HTML Email'" (id `0be9d77b-7190-4f01-b483-fa62871c9c88`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `3u0JNKt3eNJrK4rq`) — node "Call 'Slack - Create a base message'" (id `1006d16e-dfdd-4a95-b4c2-0525bbdafa72`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `fMgQKiyw6jrmjIWq`) — node "Email skipped notification" (id `7dc7368c-1db5-456d-9339-66a9270cf14f`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `fMgQKiyw6jrmjIWq`) — node "Email not provided notification" (id `af693ff9-3fc9-4be2-8d91-ac164fff5083`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `fMgQKiyw6jrmjIWq`) — node "Email send failed notification" (id `b6cf7891-af9c-4860-8a1e-dc11e9cae71c`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `fMgQKiyw6jrmjIWq`) — node "Email sent notification" (id `f461e202-f24e-479e-a3b9-83ad1b3cd554`)

## Used by (workflows)

- [[gmail-send-html-email|Gmail - Send HTML Email]] — node "Call 'Gmail - Send HTML Email'" (id `0be9d77b-7190-4f01-b483-fa62871c9c88`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
