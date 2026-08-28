---
n8n_id: "ZJDrkKBETCaZcnob"
instance: v1
name: "Dispute - Monitor missed notifications"
status: inactive
last_modified: 2026-02-23T15:15:34.626Z
tags: []
fingerprint: "d0cfbdde2ac0479ba0df5c82a6cca2caa9ed34306342da3975abbadb16435827"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Dispute - Monitor missed notifications

## Summary

- **Status:** inactive
- **n8n ID:** `ZJDrkKBETCaZcnob`
- **Nodes:** 11
- **Last modified:** 2026-02-23T15:15:34.626Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `0310e15a-b820-4e7d-bab2-dfde33dd19b9`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `15ec7f3a-d007-4b16-a222-021bd3a7ba0b`)

## Depends on

### Data tables (n8n)

- [[../resources/data-tables/nkrufqkkpszwq07b|Dispute - Awaiting Processor Response]] (id `NkRUfQkkpsZWq07b`) — op `get` — node "Get row(s)" (id `25e28f91-8cea-4dc1-8a59-96bb438e37c8`)

### Sub-workflows (Execute Workflow calls)

- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `5e56b956-b6e7-4e7d-9a18-5d007e4d6d80`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `98b6ea52-78d7-4f05-b429-6acf7a1f0427`)

## Used by (workflows)

- [[dispute-main-processor|Dispute - Main Processor]] — node "Call 'Dispute - Monitor missed notifications'" (id `86af3e22-fb91-47e1-a776-a41c9887386b`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
