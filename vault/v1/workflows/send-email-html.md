---
n8n_id: "H9qPciXCz00KxAyF"
name: "Send Email: HTML"
status: inactive
last_modified: 2025-11-10T16:50:49.504Z
tags: []
fingerprint: "9117930a5126c0702d64cf0721bb1184b259075b28516ce3ad110ab61017571c"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Send Email: HTML

## Summary

- **Status:** inactive
- **n8n ID:** `H9qPciXCz00KxAyF`
- **Nodes:** 44
- **Last modified:** 2025-11-10T16:50:49.504Z

## Triggers

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

- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Email skipped notification" (id `7dc7368c-1db5-456d-9339-66a9270cf14f`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Email not provided notification" (id `af693ff9-3fc9-4be2-8d91-ac164fff5083`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Email send failed notification" (id `b6cf7891-af9c-4860-8a1e-dc11e9cae71c`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Email sent notification" (id `f461e202-f24e-479e-a3b9-83ad1b3cd554`)

## Used by (workflows)

- [[auto-email-elavon-to-change-the-merchant-email|Auto-email Elavon to change the merchant email]] — node "Call 'Send Email'" (id `c9cd9161-98f4-4473-ad5f-a044f5e93bcd`)
- [[dispute-process-elavon-attachments|Dispute - Process Elavon attachments]] — node "Call 'Send Email'" (id `246581ca-9fba-4f13-95ad-20bbba563757`)
- [[dispute-send-details-to-processor|Dispute - Send details to processor]] — node "Call 'Send Email: HTML'" (id `32d9eda0-dac1-4143-a797-d25c1bbffd92`)
- [[elavon-dispute|Elavon Dispute]] — node "Call 'Send Email'" (id `058b9d38-d986-4039-95a4-51db8cf9c3a6`)
- [[failed-ach-notifications|Failed ACH notifications]] — node "Call 'Send Email'" (id `193b21d1-a19e-4ba8-a07a-372287b8b351`)
- [[heath-merchants-forte-next-day-funding-ndf-request-emails|Heath Merchants - Forte Next Day Funding (NDF) Request Emails]] — node "Call 'Send Email: HTML'" (id `136b1c8b-a363-4778-bed3-77dd755dba3b`)
- [[pci-monitoring|PCI Monitoring]] — node "Call 'Send Email: HTML'" (id `4ac9adb7-1ddb-461e-8cf7-1cef81f8c292`)
- [[pci-monitoring-LdXwJbJl|PCI Monitoring]] — node "Call 'Send Email: HTML'" (id `4ac9adb7-1ddb-461e-8cf7-1cef81f8c292`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
