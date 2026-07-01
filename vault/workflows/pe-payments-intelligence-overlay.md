---
n8n_id: "tcYnixnPq9S8UPQl"
name: "PE Payments Intelligence Overlay"
status: active
last_modified: 2025-10-15T13:07:28.967Z
tags: []
fingerprint: "183a707cd019bbf824c909f21a3dde3dcc840d092f3590e7c0129a6fbdb01c36"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PE Payments Intelligence Overlay

## Summary

- **Status:** active
- **n8n ID:** `tcYnixnPq9S8UPQl`
- **Nodes:** 41
- **Last modified:** 2025-10-15T13:07:28.967Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `567e046f-ad5e-40aa-b1bd-c2200a6dd5c3`)
- **manual** — node "When clicking ‘Execute workflow’" (id `6bdb900c-58be-44bf-8332-46efaf34611f`)
- **webhook** — node "Webhook" (id `80494801-e541-4297-9014-54442fe186ab`) — ["POST"] `e5eb3746-e09a-49e2-a07d-ad730f4a6f15`
- **other** — node "When chat message received" (id `886ee9f7-356b-4fbb-9de6-2d8e53047a04`)
- **webhook** — node "Webhook1" (id `b9729ab6-8ad8-4d45-ad22-801426f0046d`) — GET `e5eb3746-e09a-49e2-a07d-ad730f4a6f15`
- **other** — node "MCP Server Trigger" (id `eeb2cc2f-ab69-4fe3-8699-e409013df7f4`) — GET `103b9843-cf37-4ce1-8d17-f71ac9be32a4`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Add or Append Context Store Item" (id `3d45d40e-2be5-48b1-ae29-226f83016bd7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Instructions for JavaScript Execution Tool" (id `909bfeca-5705-4082-8449-92a920a42fa3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get a document in Google Docs" (id `a2640b76-e556-4282-9ad9-15987f71514a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Instructions for Using Browser JavaScript Execution Tool2" (id `c045bdf0-42c3-46c6-b9f1-83fd6181c5c4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Context Store Item" (id `c418fba1-1d34-4d12-8e03-b0f0214f6bc8`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `cbbd76c1-2c30-4a17-801c-889ac74615c4`)
- [[../resources/credentials/jizht82aeuvnkqed|Centrifugo HMAC Secret Key]] (`jwtAuth`, id `JizHT82aEUvnKQEd`) — node "JWT" (id `d3215dec-5f82-4915-8eaf-eb00807243f0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Agent Context Store Items List" (id `ee2a83ac-916a-4623-a1cc-fdc358c3f152`)

### HTTP URLs

- [[../resources/http-urls/centrifugo-payengine-dev|centrifugo.payengine.dev]] — `POST https://centrifugo.payengine.dev/api/publish` — node "Command1" (id `38f2618a-f9c8-4ccf-bf82-3d58907128a9`)
- [[../resources/http-urls/centrifugo-payengine-dev|centrifugo.payengine.dev]] — `POST https://centrifugo.payengine.dev/api/publish` — node "Command" (id `6d3d707a-776e-4d6e-9588-35208338b3bf`)
- [[../resources/http-urls/www-googleapis-com|www.googleapis.com]] — `GET https://www.googleapis.com/drive/v3/files/1EInFusCRzH3z8GC0fRa4r4hpGeFolnnzklJEPoc5_n8/export?mimeType=text/plain` — node "Instructions for JavaScript Execution Tool" (id `909bfeca-5705-4082-8449-92a920a42fa3`)
- *(dynamic URL)* — `GET ` — node "HTTP Request1" (id `aca95584-06ca-41e2-9154-834a1f81f699`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model" (id `cbbd76c1-2c30-4a17-801c-889ac74615c4`)

### Google Sheets

- [[../resources/google-sheets/1lt0myokcmxpa9rrqxvptagovf6ffxeih0zuojhyenua|PE Payments Intelligence Overlay]] (id `1Lt0MyOkCMXpA9RRQXVptAgoVF6ffXEIh0ZUOjHyENUA`) — op `appendOrUpdate`, tab `agent_context_store` — node "Add or Append Context Store Item" (id `3d45d40e-2be5-48b1-ae29-226f83016bd7`)
- [[../resources/google-sheets/1lt0myokcmxpa9rrqxvptagovf6ffxeih0zuojhyenua|PE Payments Intelligence Overlay]] (id `1Lt0MyOkCMXpA9RRQXVptAgoVF6ffXEIh0ZUOjHyENUA`) — op `?`, tab `agent_context_store` — node "Get Context Store Item" (id `c418fba1-1d34-4d12-8e03-b0f0214f6bc8`)
- [[../resources/google-sheets/1lt0myokcmxpa9rrqxvptagovf6ffxeih0zuojhyenua|PE Payments Intelligence Overlay]] (id `1Lt0MyOkCMXpA9RRQXVptAgoVF6ffXEIh0ZUOjHyENUA`) — op `?`, tab `agent_context_store` — node "Agent Context Store Items List" (id `ee2a83ac-916a-4623-a1cc-fdc358c3f152`)

### Google Drive

- [[../resources/google-drive/1einfuscrzh3z8gc0fra4r4hpgefolnnzkljepoc5-n8|PE Payments Intelligence Overlay ]] (`file`, id `1EInFusCRzH3z8GC0fRa4r4hpGeFolnnzklJEPoc5_n8`) — op `download` — node "Instructions for Using Browser JavaScript Execution Tool2" (id `c045bdf0-42c3-46c6-b9f1-83fd6181c5c4`)

### Google Docs

- [[../resources/google-docs/1einfuscrzh3z8gc0fra4r4hpgefolnnzkljepoc5-n8|1EInFusCRzH3z8GC0fRa4r4hpGeFolnnzklJEPoc5_n8]] (id `1EInFusCRzH3z8GC0fRa4r4hpGeFolnnzklJEPoc5_n8`) — op `get` — node "Get a document in Google Docs" (id `a2640b76-e556-4282-9ad9-15987f71514a`)

### Sub-workflows (Execute Workflow calls)

- [[pe-payments-intelligence-overlay|PE Payments Intelligence Overlay]] (n8n_id `tcYnixnPq9S8UPQl`) — node "Browser JavaScript Execution Tool 2" (id `1195a914-a594-4af9-aa4f-20147657fd36`)
- [[pe-payments-intelligence-overlay|PE Payments Intelligence Overlay]] (n8n_id `tcYnixnPq9S8UPQl`) — node "Call 'PE Payments Intelligence Overlay'" (id `185770f7-5b7c-4def-ade2-4ee84514c761`)
- [[pe-payments-intelligence-overlay|PE Payments Intelligence Overlay]] (n8n_id `tcYnixnPq9S8UPQl`) — node "Browser JavaScript Execution Tool" (id `21cdca59-f78c-4cb6-a006-e49d6455f82d`)
- [[pe-payments-intelligence-overlay|PE Payments Intelligence Overlay]] (n8n_id `tcYnixnPq9S8UPQl`) — node "User Browser Command Response" (id `6b6be6d6-3c59-4e24-b7b7-6cd3d75e8898`)
- [[pe-payments-intelligence-overlay|PE Payments Intelligence Overlay]] (n8n_id `tcYnixnPq9S8UPQl`) — node "Browser JavaScript Execution Tool2" (id `db9c72b6-98ad-4840-a071-c90e83dd19ea`)

## Used by (workflows)

- [[pe-payments-intelligence-overlay|PE Payments Intelligence Overlay]] — node "Browser JavaScript Execution Tool" (id `21cdca59-f78c-4cb6-a006-e49d6455f82d`)
- [[pe-payments-intelligence-overlay|PE Payments Intelligence Overlay]] — node "Browser JavaScript Execution Tool 2" (id `1195a914-a594-4af9-aa4f-20147657fd36`)
- [[pe-payments-intelligence-overlay|PE Payments Intelligence Overlay]] — node "Browser JavaScript Execution Tool2" (id `db9c72b6-98ad-4840-a071-c90e83dd19ea`)
- [[pe-payments-intelligence-overlay|PE Payments Intelligence Overlay]] — node "Call 'PE Payments Intelligence Overlay'" (id `185770f7-5b7c-4def-ade2-4ee84514c761`)
- [[pe-payments-intelligence-overlay|PE Payments Intelligence Overlay]] — node "User Browser Command Response" (id `6b6be6d6-3c59-4e24-b7b7-6cd3d75e8898`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
