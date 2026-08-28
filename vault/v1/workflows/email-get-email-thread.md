---
n8n_id: "jJq7apxtmeis8y7Y"
instance: v1
name: "Email - Get email thread"
status: inactive
last_modified: 2026-01-01T19:15:32.738Z
tags: []
fingerprint: "2132e5fa6a508147714434bda1931455ba3b0ca77e960d7074ebfebe4496a38c"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Email - Get email thread

## Summary

- **Status:** inactive
- **n8n ID:** `jJq7apxtmeis8y7Y`
- **Nodes:** 17
- **Last modified:** 2026-01-01T19:15:32.738Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `6ebf631f-e655-4232-812b-f98c46ae54ba`)

## Depends on

### Credentials

- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get a message2" (id `07168ead-342f-4683-9028-b6eb1ba87f35`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Get a message1" (id `32d8edda-47ab-4dbc-9ca7-e1564b7518f3`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get a thread1" (id `9bbf106c-21e0-4798-9244-09750a71a093`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Get a message" (id `9cb2497a-907b-42c5-ba23-18fa3e2f17e9`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Get a thread2" (id `b1148baf-0344-4f74-a20b-046190989cd5`)
- [[../resources/credentials/cde3nulqqlnaaarl|Supermove Gmail Account]] (`gmailOAuth2`, id `cdE3NULqqLnAaaRL`) — node "Get a thread" (id `cb99a2ef-8632-41a4-9d24-61dc21e1769d`)

### Sub-workflows (Execute Workflow calls)

- [[email-get-email-thread|Email - Get email thread]] (n8n_id `jJq7apxtmeis8y7Y`) — node "Call 'Email - Get email thread'" (id `a64ae396-8adf-4d2d-9d82-80331fe4ae44`)

## Used by (workflows)

- [[dispute-case-handler|Dispute - Case Handler]] — node "Get merchant email thread" (id `1630bddb-c0dd-4ce5-971c-f21515a56e82`)
- [[dispute-merchant-response-monitoring|Dispute - Merchant Response Monitoring]] — node "Call 'Email - Get email thread'" (id `49d2a468-938a-4837-9fe2-78a35cf41c05`)
- [[email-get-email-thread|Email - Get email thread]] — node "Call 'Email - Get email thread'" (id `a64ae396-8adf-4d2d-9d82-80331fe4ae44`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
