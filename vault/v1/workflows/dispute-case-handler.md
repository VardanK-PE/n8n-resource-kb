---
n8n_id: "CmcIqdaZ986kB61s"
instance: v1
name: "Dispute - Case Handler"
status: inactive
last_modified: 2026-04-21T17:06:40.192Z
tags: []
fingerprint: "eda9ef89ddc85fd468b971b82da4afd78566a114b816bf665d777c11d4217ea2"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Dispute - Case Handler

## Summary

- **Status:** inactive
- **n8n ID:** `CmcIqdaZ986kB61s`
- **Nodes:** 90
- **Last modified:** 2026-04-21T17:06:40.192Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `82749778-81fb-4eff-a53a-ac9ccef2f63f`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `d375e783-d44f-4976-9b8f-7c582da8827e`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `65a5e3df-66f9-49ed-a33e-6e541df288ee`)

### Google Drive

- *(dynamic)* — op `download` — node "Download file" (id `65a5e3df-66f9-49ed-a33e-6e541df288ee`)

### Data tables (n8n)

- [[../resources/data-tables/da1d723wdyigobvw|Dispute - Merchant Responses]] (id `DA1d723WDyIGoBVW`) — op `update` — node "Update row(s)3" (id `1c3b8d7a-454d-4e48-a5bd-493dcea7be78`)
- [[../resources/data-tables/da1d723wdyigobvw|Dispute - Merchant Responses]] (id `DA1d723WDyIGoBVW`) — op `get` — node "Get row(s)" (id `51adc6eb-df8e-4eac-a0be-a6d11423a762`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `update` — node "Update row(s)" (id `7c8c8c7d-5104-46b4-8ea0-ff9fa60f1d31`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `get` — node "Get Pending Attachments" (id `82a30a5c-56ab-47fd-bd3e-7692a6d2d5bc`)
- [[../resources/data-tables/bp4di8haidhokx7y|Dispute - Elavon Attachments]] (id `BP4Di8haiDhOKX7Y`) — op `update` — node "Update row(s)2" (id `da9aa254-df87-488e-8fe2-b7403995277b`)

### Sub-workflows (Execute Workflow calls)

- [[email-get-email-thread|Email - Get email thread]] (n8n_id `jJq7apxtmeis8y7Y`) — node "Get merchant email thread" (id `1630bddb-c0dd-4ce5-971c-f21515a56e82`)
- [[dispute-update-console|Dispute - Update Console]] (n8n_id `8H0XdRETMCwVl3p8`) — node "Update Pre-Arb 3" (id `225ec923-9c1d-4297-9495-88821c1497f5`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Create base message" (id `288af449-2ef4-4784-b989-fa31bb44fd58`)
- [[dispute-update-console|Dispute - Update Console]] (n8n_id `8H0XdRETMCwVl3p8`) — node "Call 'Dispute - Update Console'2" (id `32dd26b7-de5c-412d-8455-4fd8d4876a8c`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `5f4777a2-a2f4-490d-9116-b800b0d882ca`)
- [[dispute-update-console|Dispute - Update Console]] (n8n_id `8H0XdRETMCwVl3p8`) — node "Update credit advice" (id `67f57dbd-9f18-421d-92bf-4bc77c9de3ec`)
- [[dispute-update-console|Dispute - Update Console]] (n8n_id `8H0XdRETMCwVl3p8`) — node "Update copy request" (id `6f0842e2-0633-4919-83e9-a4b8a7874862`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'2" (id `710547a0-c0fb-44b0-a21e-9f65fc7b0bf4`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Create base message1" (id `77d0df26-4cfe-42b2-93ed-e34070a0d15a`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'4" (id `7cd694f0-295d-4e1f-ab3f-7982925d3c2c`)
- [[dispute-resolve-chargeback-transaction-info|Dispute - Resolve Chargeback Transaction Info]] (n8n_id `c4k0seLSEFK7ZEO5`) — node "Resolve case transactions - elavon" (id `883137a4-fb26-4978-baa6-849c0506eb7e`)
- [[dispute-update-console|Dispute - Update Console]] (n8n_id `8H0XdRETMCwVl3p8`) — node "Call 'Dispute - Update Console'4" (id `9a0ea660-7ac2-4ce6-b9c9-0d97f28d521b`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'3" (id `d41e893f-68a6-497d-bc69-6561e3b26fca`)
- [[dispute-update-console|Dispute - Update Console]] (n8n_id `8H0XdRETMCwVl3p8`) — node "Call 'Dispute - Update Console'1" (id `dc4c6b7e-8524-40bc-858e-d9dee5fddfe8`)
- [[dispute-resolve-chargeback-transaction-info|Dispute - Resolve Chargeback Transaction Info]] (n8n_id `c4k0seLSEFK7ZEO5`) — node "Resolve case transactions - merchant" (id `de78e652-5f2e-4b1b-b4e0-79302f369884`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'1" (id `efff0176-1bf5-415a-8d8e-7bdf619e05b7`)
- [[dispute-update-console|Dispute - Update Console]] (n8n_id `8H0XdRETMCwVl3p8`) — node "Call 'Dispute - Update Console'5" (id `f5777e1b-19ab-4da9-8cb3-01bb91ab4eb4`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Create base message2" (id `f98556be-bb2f-4d7c-a256-c9b6a02e67ea`)
- [[dispute-update-console|Dispute - Update Console]] (n8n_id `8H0XdRETMCwVl3p8`) — node "Call 'Dispute - Update Console'" (id `ff98e292-34e3-4364-b4d9-122e28270972`)

## Used by (workflows)

- [[dispute-main-processor|Dispute - Main Processor]] — node "Call 'Dispute - Case Handler'" (id `aa41a7be-68db-4b5b-8b90-f443de40c7b8`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
