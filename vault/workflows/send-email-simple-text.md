---
n8n_id: "Zr3vF0LVpsPrzHVY"
name: "Send Email: Simple Text"
status: inactive
last_modified: 2025-11-10T16:50:28.486Z
tags: []
fingerprint: "7da560e821e166f6a0e6d15e21b942bd46d9ffbb0a3a73f33b27c05a8d76c153"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Send Email: Simple Text

## Summary

- **Status:** inactive
- **n8n ID:** `Zr3vF0LVpsPrzHVY`
- **Nodes:** 44
- **Last modified:** 2025-11-10T16:50:28.486Z

## Triggers

- **error** — node "Error Trigger" (id `9fd13713-7706-46fb-8147-fd58b37ef522`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `f5aad205-49bf-40b0-908f-7d0adc2ba65d`)

## Depends on

### Credentials

- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send email from Hearth inbox" (id `090edfd2-15df-4faa-91e2-5241db6071af`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send email from Hearth inbox (with Attachments)1" (id `438a309e-4d98-466d-962e-7996b75ef96c`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Send email from Supermove inbox1" (id `4ee0a7ba-4ce8-4a1a-8e0e-a96b3b429296`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send email from PE inbox (with Attachments)" (id `653eb86c-b72d-439b-b125-a248de2e3bd3`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send email from Hearth inbox1" (id `697c1335-a2ec-44ae-8eec-fa714bcbaade`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Send email from Supermove inbox" (id `6aea1f4c-5ca0-46e4-881c-f8a7dd65bc1f`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Send email from Supermove inbox (with Attachments)" (id `75ee955a-3ed3-4bab-8e24-2a81e5f9b300`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send email from Hearth inbox (with Attachments)" (id `793caad4-a1f7-4db5-b048-6905c07d3ac1`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Send email from Supermove inbox (with Attachments)1" (id `8d8ee29e-f7b2-4930-a4c3-b08cce67fb13`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send email from PE inbox (with Attachments)1" (id `bc16d322-47fa-4388-8821-da1bee6a7bdb`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `d3521b6e-4f76-4da3-9963-2ecb2503ba00`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send email from PE inbox" (id `e4315cab-8aab-4290-a411-987f6abbe1b7`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send email from PE inbox1" (id `e466b77f-845f-4106-9dae-be713cae7b63`)

### Slack channels

- [[../resources/slack-channels/c0998514tkp|elavon-loss-prevention-alerts]] (id `C0998514TKP`) — op `channel` — node "Send a message5" (id `d3521b6e-4f76-4da3-9963-2ecb2503ba00`)

### Sub-workflows (Execute Workflow calls)

- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Email sent notification" (id `0e08c302-6b80-4024-887c-d53a8ca71b89`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Email send failed notification" (id `226881ce-92c8-4aae-81d9-8e9b31142bd8`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Email skipped notification" (id `5b9bbf02-921f-4955-bf5c-54ec0524145c`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Email not provided notification" (id `b1a6ef78-bfd6-4990-bf75-9d90fd372291`)

## Used by (workflows)

- [[elavon-ach-enrollment-project|Elavon ACH Enrollment Project]] — node "Call 'Send Email: Simple Text'" (id `442e49e4-e51f-49b0-a732-913812f0e92c`)
- [[elavon-ach-enrollment-project|Elavon ACH Enrollment Project]] — node "Call 'Send Email: Simple Text'1" (id `f6b8f1dc-fb9b-44ef-95a1-ca3ff4599046`)
- [[pci-saq-notifications|PCI SAQ Notifications]] — node "Send PCI SAQ email" (id `ccf6b1f2-3084-44c3-bf3c-9ee1dbff3632`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
