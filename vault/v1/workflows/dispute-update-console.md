---
n8n_id: "8H0XdRETMCwVl3p8"
instance: v1
name: "Dispute - Update Console"
status: inactive
last_modified: 2026-02-09T17:52:27.640Z
tags: []
fingerprint: "1930daabc3b7410933f32d33a662e1dbd6f805b90a9b11abedc0b1b73b03d5dd"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Dispute - Update Console

## Summary

- **Status:** inactive
- **n8n ID:** `8H0XdRETMCwVl3p8`
- **Nodes:** 22
- **Last modified:** 2026-02-09T17:52:27.640Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `5f2c05b5-ee02-49c3-9e3d-9adff67d64e8`)
- **manual** — node "When clicking ‘Execute workflow’" (id `b1738427-d8be-43e1-92b1-722f4ee0c6b4`)

## Depends on

### Credentials

- [[../resources/credentials/l1fdqv2gyxyjgim6|PE Staging Sandbox]] (`httpBearerAuth`, id `l1fDQv2GYxYjgim6`) — node "Sandbox Staging Update Transaction" (id `ba32c713-3bb4-46af-9070-8ce2f316206e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `e0207710-0912-4d9f-8b3f-48ec2c9ed93b`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Prod Update Transaction" (id `f7dae2d9-ccd8-4765-89bb-29bd1a68a31b`)

### HTTP URLs

- *(dynamic URL)* — `PATCH {{ $json.pe_console_base_url }}/api/transaction/{{ $json.transaction_id }}/dispute` — node "Sandbox Staging Update Transaction" (id `ba32c713-3bb4-46af-9070-8ce2f316206e`)
- *(dynamic URL)* — `PATCH {{ $json.pe_console_base_url }}/api/transaction/{{ $json.transaction_id }}/dispute` — node "Prod Update Transaction" (id `f7dae2d9-ccd8-4765-89bb-29bd1a68a31b`)

### Google Drive

- [[../resources/google-drive/1oebuwamgl9xeud0rozqnj7kyls0u7t-9|ECS Exemption From (0 TEST).pdf]] (`file`, id `1OEbuWamgL9xEuD0ROzqnJ7KyLS0u7t_9`) — op `download` — node "Download file" (id `e0207710-0912-4d9f-8b3f-48ec2c9ed93b`)

## Used by (workflows)

- [[dispute-case-handler|Dispute - Case Handler]] — node "Call 'Dispute - Update Console'" (id `ff98e292-34e3-4364-b4d9-122e28270972`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Call 'Dispute - Update Console'1" (id `dc4c6b7e-8524-40bc-858e-d9dee5fddfe8`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Call 'Dispute - Update Console'2" (id `32dd26b7-de5c-412d-8455-4fd8d4876a8c`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Call 'Dispute - Update Console'4" (id `9a0ea660-7ac2-4ce6-b9c9-0d97f28d521b`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Call 'Dispute - Update Console'5" (id `f5777e1b-19ab-4da9-8cb3-01bb91ab4eb4`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Update Pre-Arb 3" (id `225ec923-9c1d-4297-9495-88821c1497f5`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Update copy request" (id `6f0842e2-0633-4919-83e9-a4b8a7874862`)
- [[dispute-case-handler|Dispute - Case Handler]] — node "Update credit advice" (id `67f57dbd-9f18-421d-92bf-4bc77c9de3ec`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
