---
n8n_id: "U3EyWwhZtcf2tMh5"
name: "Slack - Send notification"
status: inactive
last_modified: 2025-11-09T13:20:01.702Z
tags: []
fingerprint: "bedf850d17f42baf07d0ec3be71035b021a37f76d3ac8dc04b222468065cc398"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Slack - Send notification

## Summary

- **Status:** inactive
- **n8n ID:** `U3EyWwhZtcf2tMh5`
- **Nodes:** 9
- **Last modified:** 2025-11-09T13:20:01.702Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `a2479bfa-3195-4b2b-9b04-3c51b3393c91`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Hearth: Send a message" (id `088f3232-1cc3-4f20-b709-071e8959cb97`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Supermove: Send a message" (id `791ac0d5-0eac-471f-8809-87463a18f315`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "PE: Send a message" (id `918d01b7-b21f-45e2-af01-2eca59db18e0`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Hearth: Send a message" (id `088f3232-1cc3-4f20-b709-071e8959cb97`)
- *(dynamic channel)* — op `channel` — node "Supermove: Send a message" (id `791ac0d5-0eac-471f-8809-87463a18f315`)
- *(dynamic channel)* — op `channel` — node "PE: Send a message" (id `918d01b7-b21f-45e2-af01-2eca59db18e0`)

## Used by (workflows)

- [[chargebacks-response-expiration-monitoring|Chargebacks: Response expiration monitoring]] — node "Call 'Slack - Send notification'" (id `9c16336d-fcdc-43ed-8d83-99d370462938`)
- [[chargebacks-response-expiration-monitoring|Chargebacks: Response expiration monitoring]] — node "Call 'Slack - Send notification'1" (id `2555d8cf-ace6-4992-ac0b-80c25de6e8fd`)
- [[corksy-open-batch-monitoring|Corksy open batch monitoring]] — node "Call 'Slack - Send notification'" (id `56c7f65b-79f2-4b97-8c67-e24640789d55`)
- [[critical-workflow-activity-monitoring|Critical Workflow Activity Monitoring]] — node "Call 'Slack - Send notification'" (id `1a736db8-23fb-47f4-b880-3c4ce26e2400`)
- [[disable-ach-gateway-main-logic|Disable ACH Gateway - Main Logic]] — node "Call 'Slack - Send notification'" (id `55c9c155-3e40-426a-ba0a-d6bd3d41257d`)
- [[disable-ach-gateway-main-logic|Disable ACH Gateway - Main Logic]] — node "Call 'Slack - Send notification'1" (id `775881ec-519c-4594-af58-e04b0fd317a8`)
- [[disable-ach-gateway-main-logic|Disable ACH Gateway - Main Logic]] — node "Call 'Slack - Send notification'2" (id `d81b9ea2-0644-4da3-836e-fb03d7b02efa`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Call 'Slack - Send notification'" (id `5f4777a2-a2f4-490d-9116-b800b0d882ca`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Call 'Slack - Send notification'1" (id `efff0176-1bf5-415a-8d8e-7bdf619e05b7`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Call 'Slack - Send notification'2" (id `710547a0-c0fb-44b0-a21e-9f65fc7b0bf4`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Call 'Slack - Send notification'3" (id `d41e893f-68a6-497d-bc69-6561e3b26fca`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Call 'Slack - Send notification'4" (id `7cd694f0-295d-4e1f-ab3f-7982925d3c2c`)
- [[dispute-merchant-response-monitoring|Dispute - Merchant Response Monitoring]] — node "Call 'Slack - Send notification'" (id `43dfbe48-cad6-4465-944c-8efd611e9007`)
- [[dispute-monitor-missed-notifications|Dispute - Monitor missed notifications]] — node "Call 'Slack - Send notification'" (id `98b6ea52-78d7-4f05-b429-6acf7a1f0427`)
- [[dispute-send-details-to-processor|Dispute - Send details to processor]] — node "Call 'Slack - Send notification'2" (id `668993d5-da75-4ecd-afd6-d8fe1809b99d`)
- [[elavon-ach-enrollment-project|Elavon ACH Enrollment Project]] — node "Call 'Slack - Send notification'" (id `797c42aa-6a1e-489a-ba59-d46a3e27b8e8`)
- [[elavon-dispute|Elavon Dispute]] — node "Call 'Slack - Send notification'" (id `d9cb0b33-45f7-40e4-bd2a-a2a9c9a4e30b`)
- [[elavon-dispute|Elavon Dispute]] — node "Call 'Slack - Send notification'1" (id `82045f43-f769-4a71-8b90-ca3c6451ec35`)
- [[elavon-dispute|Elavon Dispute]] — node "Send" (id `7217d6da-615d-4ff7-b923-fb665de95505`)
- [[elavon-disputes-reporting|Elavon Disputes Reporting]] — node "Call 'Slack - Send notification'" (id `edd491ac-6dfe-4aab-ab83-845a14a0a20a`)
- [[elavon-disputes-reporting|Elavon Disputes Reporting]] — node "Call 'Slack - Send notification'1" (id `496ef260-f3f3-469e-8dd3-ea7bff9aa5dd`)
- [[elavon-disputes-reporting|Elavon Disputes Reporting]] — node "Call 'Slack - Send notification'2" (id `23151017-febc-45d9-a314-c6b0ac82b316`)
- [[generate-a-list-of-pci-non-compliant-merchants|Generate a list of PCI non compliant merchants]] — node "Call 'Slack - Send notification'" (id `2082fe1b-446e-4188-b402-b1c44602d96c`)
- [[pci-monitoring-LdXwJbJl|PCI Monitoring]] — node "Call 'Slack - Send notification'" (id `3c67f410-4e17-437c-ae87-a252a96461ba`)
- [[pci-saq-notifications|PCI SAQ Notifications]] — node "Report failed PCI SAQ notification" (id `92e8c1eb-db0d-403d-b5a1-87c65fbeb3b7`)
- [[platform-fee-monitoring|Platform Fee monitoring]] — node "Call 'Slack - Send notification'" (id `1cd30bd0-dbf0-4986-8708-4fdefd87491d`)
- [[send-email-html|Send Email: HTML]] — node "Email not provided notification" (id `af693ff9-3fc9-4be2-8d91-ac164fff5083`)
- [[send-email-html|Send Email: HTML]] — node "Email send failed notification" (id `b6cf7891-af9c-4860-8a1e-dc11e9cae71c`)
- [[send-email-html|Send Email: HTML]] — node "Email sent notification" (id `f461e202-f24e-479e-a3b9-83ad1b3cd554`)
- [[send-email-html|Send Email: HTML]] — node "Email skipped notification" (id `7dc7368c-1db5-456d-9339-66a9270cf14f`)
- [[send-email-simple-text|Send Email: Simple Text]] — node "Email not provided notification" (id `b1a6ef78-bfd6-4990-bf75-9d90fd372291`)
- [[send-email-simple-text|Send Email: Simple Text]] — node "Email send failed notification" (id `226881ce-92c8-4aae-81d9-8e9b31142bd8`)
- [[send-email-simple-text|Send Email: Simple Text]] — node "Email sent notification" (id `0e08c302-6b80-4024-887c-d53a8ca71b89`)
- [[send-email-simple-text|Send Email: Simple Text]] — node "Email skipped notification" (id `5b9bbf02-921f-4955-bf5c-54ec0524145c`)
- [[upload-monthly-ach-statements-to-pe|Upload monthly ACH statements to PE]] — node "Call 'Slack - Send notification'2" (id `d4f9e62c-c681-4eff-9c63-01b067048dc3`)
- [[upload-monthly-ach-statements-to-pe|Upload monthly ACH statements to PE]] — node "Report on missing ACH table" (id `d9c70f69-76b8-4dc8-9894-b5aec7eff553`)
- [[upload-monthly-ach-statements-to-pe|Upload monthly ACH statements to PE]] — node "Send API failure notification" (id `a16dd925-aecc-409d-956d-1a3bafeda1e5`)
- [[upload-monthly-ach-statements-to-pe|Upload monthly ACH statements to PE]] — node "Send success notification" (id `0e76f9c0-99f7-4a0f-abe0-d573e7d1e22a`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
