---
n8n_id: "VQPaemuwy6FdMa9L"
instance: v1
name: "Slack - Create a base message"
status: inactive
last_modified: 2025-11-09T10:51:05.362Z
tags: []
fingerprint: "7a087273b0d415e6318dda8d918dc9d0d1c327e08abd556a23906d7bb0b0a985"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Slack - Create a base message

## Summary

- **Status:** inactive
- **n8n ID:** `VQPaemuwy6FdMa9L`
- **Nodes:** 12
- **Last modified:** 2025-11-09T10:51:05.362Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `e87dfaf9-d3af-4453-b83b-297fb52fb3f9`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Create a base message2" (id `1f4ef060-7180-49c1-b941-b699a8e7ff6e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Create a base message" (id `e0e65431-e8ad-4a9a-b14a-3145b24bdc16`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Create a base message1" (id `ee39b47a-92d1-4ce5-9632-b078b89ae0a7`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Create a base message2" (id `1f4ef060-7180-49c1-b941-b699a8e7ff6e`)
- *(dynamic channel)* — op `channel` — node "Create a base message" (id `e0e65431-e8ad-4a9a-b14a-3145b24bdc16`)
- *(dynamic channel)* — op `channel` — node "Create a base message1" (id `ee39b47a-92d1-4ce5-9632-b078b89ae0a7`)

## Used by (workflows)

- [[billing-system-generate-invoices-for-billing-period|Billing System - Generate Invoices for Billing Period]] — node "Call 'Slack - Create a base message'" (id `2f225f5f-3611-4687-863b-52c69aa0a090`)
- [[chargebacks-response-expiration-monitoring|[Deprecated] Chargebacks: Response expiration monitoring]] — node "Slack - Create a base message for 7 days" (id `4de705b8-b6d3-4be0-a52e-a810a8cd1e70`)
- [[chargebacks-response-expiration-monitoring|[Deprecated] Chargebacks: Response expiration monitoring]] — node "Slack - Create a base message for today" (id `79bdf65e-a2bf-4818-bc3e-8127c6cee2a9`)
- [[closed-by-elavon-merchant-status-monitoring|Closed By Elavon: Merchant status monitoring]] — node "Call 'Slack - Create a base message'" (id `2fb455a4-6828-49ed-a83f-d0a5cfbf70f5`)
- [[corksy-open-batch-monitoring|Corksy open batch monitoring]] — node "Call 'Slack - Create a base message'1" (id `7a21fa32-7378-4419-980b-cd3513e1c39a`)
- [[disable-ach-gateway-main-logic|Disable ACH Gateway - Main Logic]] — node "Create a base message" (id `d14e6a9b-58cc-41ec-8227-e91a0eb3085c`)
- [[disable-ach-gateway-main-logic|Disable ACH Gateway - Main Logic]] — node "Create a base message1" (id `739cdbfb-a3a1-4230-b8db-510df342d7f8`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Create base message" (id `288af449-2ef4-4784-b989-fa31bb44fd58`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Create base message1" (id `77d0df26-4cfe-42b2-93ed-e34070a0d15a`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Create base message2" (id `f98556be-bb2f-4d7c-a256-c9b6a02e67ea`)
- [[dispute-merchant-response-monitoring|Dispute - Merchant Response Monitoring]] — node "Call 'Slack - Create a base message'" (id `b86037ca-32f5-4340-8b88-b827a933e5b4`)
- [[dispute-monitor-missed-notifications|Dispute - Monitor missed notifications]] — node "Call 'Slack - Create a base message'" (id `5e56b956-b6e7-4e7d-9a18-5d007e4d6d80`)
- [[dispute-send-details-to-processor|Dispute - Send details to processor]] — node "Create a base message1" (id `3a471b15-f3d8-4f5e-9541-2c9a605fbc4d`)
- [[elavon-ach-enrollment-project|Elavon ACH Enrollment Project]] — node "Create Base Messages (approved forms)" (id `ac6f692e-a122-49e4-b352-8553d99fd34c`)
- [[elavon-dispute|Elavon Dispute]] — node "Create a base message" (id `0bccb684-4934-4a1c-a05d-79304bd2a8fc`)
- [[elavon-disputes-reporting|Elavon Disputes Reporting]] — node "Call 'Slack - Create a base message'" (id `b01b3634-96c5-4f7e-a03f-013165495d04`)
- [[failed-ach-notifications|Failed ACH notifications]] — node "Call 'Slack - Create a base message'" (id `70084f49-a6b7-4586-9546-869b91e731a1`)
- [[generate-merchant-report|Generate Merchant Report]] — node "Call 'Slack - Create a base message'" (id `4b4e5e0f-646d-45cb-b54b-8e42bb4a6123`)
- [[global-open-batch-monitoring-copy|Global open batch monitoring copy]] — node "Call 'Slack - Create a base message'" (id `cc14f6e1-3c48-423f-b335-898c5dcf3705`)
- [[global-open-batch-monitoring-copy|Global open batch monitoring copy]] — node "Call 'Slack - Create a base message'1" (id `0ab773fc-a413-4db0-83d0-9f2b27e26567`)
- [[global-open-batch-monitoring-copy|Global open batch monitoring copy]] — node "Call 'Slack - Create a base message'2" (id `44a06f23-2ad2-4a2d-b510-779fb3348378`)
- [[heath-merchants-forte-next-day-funding-ndf-request-emails|Heath Merchants - Forte Next Day Funding (NDF) Request Emails]] — node "Call 'Slack - Create a base message'" (id `fd342657-cc4a-45b9-92b4-39fb77789479`)
- [[ops-expiry|Ops - Expiry]] — node "Slack - Create a base message for 7 days" (id `6da38350-22d9-4fac-aa91-33d8dd07557f`)
- [[ops-expiry|Ops - Expiry]] — node "Slack - Create a base message for today" (id `0fdfe2dd-1217-44bc-be75-9c86116ed7ec`)
- [[payengineai-bot-v1-1-feb-26-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] — node "Call 'Slack - Create a base message'" (id `0f9ab653-22cd-47d6-9f7a-44278179ba4b`)
- [[payengineai-bot-v1-1-feb-26-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] — node "Call 'Slack - Create a base message'1" (id `4c2efbe1-352b-4624-935a-d6764c31e920`)
- [[payengineai-bot-v1-1-feb-26-2026-saot95eapiyc8s56|PayEngineAI Bot (v1.1) - Feb 26 2026]] — node "Call 'Slack - Create a base message'" (id `6b63778a-2f8a-4ca2-86d1-8b97843b8e67`)
- [[payengineai-bot-v1-1-feb-26-2026-saot95eapiyc8s56|PayEngineAI Bot (v1.1) - Feb 26 2026]] — node "Call 'Slack - Create a base message'1" (id `73043feb-a0f5-4053-b837-d4046e9c35d0`)
- [[pci-monitoring|PCI Monitoring]] — node "Call 'Slack - Create a base message'" (id `07ba278c-57c1-4196-9295-b98e793ba75b`)
- [[pci-monitoring|PCI Monitoring]] — node "Call 'Slack - Create a base message'1" (id `c4600e65-5ceb-46fc-8ca0-b678d993f204`)
- [[pci-monitoring-LdXwJbJl|PCI Monitoring]] — node "Call 'Slack - Create a base message'" (id `07ba278c-57c1-4196-9295-b98e793ba75b`)
- [[pci-monitoring-LdXwJbJl|PCI Monitoring]] — node "Call 'Slack - Create a base message'1" (id `c4600e65-5ceb-46fc-8ca0-b678d993f204`)
- [[pci-saq-notifications|PCI SAQ Notifications]] — node "Create a base message" (id `fadc41a0-abbf-413c-9989-ee81b271da4a`)
- [[pci-saq-notifications|PCI SAQ Notifications]] — node "Create error base" (id `ab55cbe7-dcf6-4676-b863-9e9f5fed573e`)
- [[pci-submission-status-monitoring|PCI Submission Status Monitoring]] — node "Call 'Slack - Create a base message'" (id `a0b28517-4f1d-4003-8363-430f847f2436`)
- [[pci-submission-status-monitoring|PCI Submission Status Monitoring]] — node "Call 'Slack - Create a base message'1" (id `63217260-76b9-435b-8a1c-86511560d12f`)
- [[pci-submission-status-monitoring|PCI Submission Status Monitoring]] — node "Call 'Slack - Create a base message'2" (id `4069984e-2f38-49e3-b656-035431da5040`)
- [[pci-submission-status-monitoring|PCI Submission Status Monitoring]] — node "Call 'Slack - Create a base message'3" (id `8ccc95c4-46f6-4b2a-a0fc-c4923b3f10b9`)
- [[platform-fee-monitoring|Platform Fee monitoring]] — node "Send base message" (id `f892c871-5be7-4688-b416-581079bb9b40`)
- [[upload-monthly-ach-statements-to-pe|Upload monthly ACH statements to PE]] — node "Create the base message" (id `bf21e4ac-5e06-4287-8be0-a8ea176eee32`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
