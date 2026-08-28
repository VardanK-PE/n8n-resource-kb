---
n8n_id: "114H81oKKk4EXteM"
instance: v1
name: "Email - Get emails by filter"
status: inactive
last_modified: 2025-12-22T16:55:21.363Z
tags: []
fingerprint: "137e63133e5f1042623cb9cdc8565fe3651e1fe92636eeb912ad7581ebb1645b"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Email - Get emails by filter

## Summary

- **Status:** inactive
- **n8n ID:** `114H81oKKk4EXteM`
- **Nodes:** 9
- **Last modified:** 2025-12-22T16:55:21.363Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `bf5b61e3-cfff-4baf-a1de-789d4a1b1fca`)

## Depends on

### Credentials

- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages1" (id `71780f5c-a765-4c2c-8389-5ad5b5f2eff9`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Get many messages" (id `a85bd977-9801-45ac-9680-9aaa847520f6`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Get many messages2" (id `bbe23376-0fec-418c-b0ec-aeb2888ed597`)

## Used by (workflows)

- [[dispute-merchant-response-monitoring|Dispute - Merchant Response Monitoring]] — node "Get Hearth Merchant Emails" (id `41459dea-ce7b-42b6-b670-0ba8eef9e6ef`)
- [[dispute-merchant-response-monitoring|Dispute - Merchant Response Monitoring]] — node "Get PE Merchant Emails" (id `23a1c23b-880a-4084-a716-67a707edf321`)
- [[dispute-merchant-response-monitoring|Dispute - Merchant Response Monitoring]] — node "Get Supermove Merchant Emails" (id `56d5b54a-7ec6-44cc-b106-bc60d293286c`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
