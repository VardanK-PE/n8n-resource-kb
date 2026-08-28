---
n8n_id: "WL8tb0vHsgM1D4Je"
instance: v1
name: "Dispute - Main Processor"
status: active
last_modified: 2026-04-20T18:35:24.533Z
tags: []
fingerprint: "d04b5b3660d0df88c5b65b665c8a9d77c3a047fff801523c2ab97fdb4f79fe0d"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Dispute - Main Processor

## Summary

- **Status:** active
- **n8n ID:** `WL8tb0vHsgM1D4Je`
- **Nodes:** 11
- **Last modified:** 2026-04-20T18:35:24.533Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `00c34969-05a1-4ca7-8a5b-d6db771ca0db`) — `every 15 minute(s)`
- **schedule** — node "Schedule Trigger2" (id `79e30cf2-f79f-47e6-b9ca-56dff2860ed8`) — `every 15 minute(s)`
- **schedule** — node "Schedule Trigger1" (id `b2e3dd4f-2c45-4edf-992c-61a1d579ec71`) — `daily at 7:00`

## Depends on

### Sub-workflows (Execute Workflow calls)

- [[dispute-send-details-to-processor|Dispute - Send details to processor]] (n8n_id `HkjjRt4gR01DJ4tH`) — node "Call 'Dispute - Send details to processor'" (id `0d7ccc15-22c8-4372-96ab-cebf4c59e29a`)
- [[dispute-send-details-to-processor|Dispute - Send details to processor]] (n8n_id `HkjjRt4gR01DJ4tH`) — node "Call 'Dispute - Send details to processor'1" (id `188f2c51-021b-48c6-ba2b-d440ba0b40d4`)
- [[dispute-process-elavon-attachments|Dispute - Process Elavon attachments]] (n8n_id `7Bxmbj0pKRQHzNC6`) — node "Call 'Dispute - Process orphaned email attachments'" (id `724f0d5d-cfd9-426d-a5bb-fa75b07c9a32`)
- [[dispute-monitor-missed-notifications|Dispute - Monitor missed notifications]] (n8n_id `ZJDrkKBETCaZcnob`) — node "Call 'Dispute - Monitor missed notifications'" (id `86af3e22-fb91-47e1-a776-a41c9887386b`)
- [[dispute-process-elavon-attachments|Dispute - Process Elavon attachments]] (n8n_id `7Bxmbj0pKRQHzNC6`) — node "Call 'Dispute - Process orphaned email attachments'2" (id `8c6e967b-51ed-48ba-afd5-9a6975413ba7`)
- [[dispute-case-handler|Dispute - Case Handler]] (n8n_id `CmcIqdaZ986kB61s`) — node "Call 'Dispute - Case Handler'" (id `aa41a7be-68db-4b5b-8b90-f443de40c7b8`)
- [[dispute-process-elavon-attachments|Dispute - Process Elavon attachments]] (n8n_id `7Bxmbj0pKRQHzNC6`) — node "Call 'Dispute - Process orphaned email attachments'3" (id `b22bac98-fae0-491c-8e87-144885c5b83c`)
- [[dispute-process-elavon-attachments|Dispute - Process Elavon attachments]] (n8n_id `7Bxmbj0pKRQHzNC6`) — node "Call 'Dispute - Process orphaned email attachments'1" (id `c2299fc3-3560-4a0f-9d3d-749a730ee9b0`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
