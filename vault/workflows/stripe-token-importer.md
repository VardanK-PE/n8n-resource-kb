---
n8n_id: "MvyvwKEhjRBkaiNH"
name: "Stripe Token Importer"
status: active
last_modified: 2025-11-25T01:54:57.824Z
tags: []
fingerprint: "b585c3899e9d9f4ffb1ffc745ee65bc14ee5f48a7d336493508b807988fe64c2"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Stripe Token Importer

## Summary

- **Status:** active
- **n8n ID:** `MvyvwKEhjRBkaiNH`
- **Nodes:** 48
- **Last modified:** 2025-11-25T01:54:57.824Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `8f7b7e17-be3e-4d26-9c4b-397b1a38982d`) — `daily at 13:30`
- **execute-workflow** — node "When Executed by Another Workflow" (id `d0e644bd-7be3-49b0-8098-2691b60973d5`)
- **manual** — node "When clicking ‘Execute workflow’" (id `d5410fa5-b23a-43bb-8222-e2b6768366f1`)

## Depends on

### Credentials

- [[../resources/credentials/cy32sqxfif41jywm|Prod: PayEngine sftp (for direct connection)]] (`sftp`, id `cY32sQxfiF41jYwm`) — node "FTP1" (id `64b46028-18e4-4001-bd73-3a9c9727c17a`)
- [[../resources/credentials/cy32sqxfif41jywm|Prod: PayEngine sftp (for direct connection)]] (`sftp`, id `cY32sQxfiF41jYwm`) — node "FTP2" (id `a50469b6-3c4d-4bdc-93fc-c3de2efec98b`)
- [[../resources/credentials/roockqldv1dgljtd|VNP Partner API Basic Auth Headr]] (`httpHeaderAuth`, id `ROOckQldV1dglJTd`) — node "Create Token w/ Private Key" (id `dc626c28-ec13-46d1-8933-0f4739fb0d77`)
- [[../resources/credentials/cy32sqxfif41jywm|Prod: PayEngine sftp (for direct connection)]] (`sftp`, id `cY32sQxfiF41jYwm`) — node "FTP" (id `e1ef4f37-eee5-447c-afd6-657e1fa6bccf`)

### HTTP URLs

- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/bank-accounts` — node "Create Bank Token w/ Public Key" (id `7fb00550-94ee-437c-be6f-c6335c44b2f5`)
- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/cards` — node "Create CC Token w/ Private Key" (id `d37a4489-6f96-49bb-8bf7-d0a555b191d9`)
- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/cards` — node "Create Token w/ Private Key" (id `dc626c28-ec13-46d1-8933-0f4739fb0d77`)

### Data tables (n8n)

- [[../resources/data-tables/pibsj85emd1r3rms|StripeTokenImports]] (id `piBSJ85eMd1r3Rms`) — op `?` — node "Success_entry" (id `0bc4a914-83f5-4682-9ebf-82c9609c5385`)
- [[../resources/data-tables/pibsj85emd1r3rms|StripeTokenImports]] (id `piBSJ85eMd1r3Rms`) — op `get` — node "Get row(s)1" (id `37f3de3e-7f40-4c88-a0cb-aa93e05b83cc`)
- [[../resources/data-tables/pibsj85emd1r3rms|StripeTokenImports]] (id `piBSJ85eMd1r3Rms`) — op `get` — node "Get Exiting Imports" (id `3d17e6c3-7bf2-471d-b8c4-a7f2b27d14bb`)
- [[../resources/data-tables/pibsj85emd1r3rms|StripeTokenImports]] (id `piBSJ85eMd1r3Rms`) — op `?` — node "Error_Entry" (id `b5cecd69-1211-4d7a-b072-88d596e2d69a`)
- [[../resources/data-tables/pibsj85emd1r3rms|StripeTokenImports]] (id `piBSJ85eMd1r3Rms`) — op `rowExists` — node "If row exists" (id `d59d0c81-88a4-491d-8ab6-eb2ecc9ebd1f`)
- [[../resources/data-tables/pibsj85emd1r3rms|StripeTokenImports]] (id `piBSJ85eMd1r3Rms`) — op `rowNotExists` — node "If row does not exist" (id `ddb8080b-3e0a-48c6-97b2-2b581e95e49b`)

### Sub-workflows (Execute Workflow calls)

- [[stripe-token-importer|Stripe Token Importer]] (n8n_id `MvyvwKEhjRBkaiNH`) — node "Call 'Stripe Token Importer'" (id `330deb51-2ae9-4c25-aa2d-a721fe6a6be2`)

## Used by (workflows)

- [[stripe-token-importer|Stripe Token Importer]] — node "Call 'Stripe Token Importer'" (id `330deb51-2ae9-4c25-aa2d-a721fe6a6be2`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
