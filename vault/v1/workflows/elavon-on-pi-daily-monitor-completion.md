---
n8n_id: "yPLpPO9vvfhOXV7W"
name: "Elavon: On PI Daily Monitor Completion"
status: inactive
last_modified: 2025-11-16T18:41:56.045Z
tags: []
fingerprint: "ed27952fde73a8fc8042143fdb94b66c735e324a07611c3eba9d618a56bec097"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Elavon: On PI Daily Monitor Completion

## Summary

- **Status:** inactive
- **n8n ID:** `yPLpPO9vvfhOXV7W`
- **Nodes:** 7
- **Last modified:** 2025-11-16T18:41:56.045Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `209060cc-0823-4b78-adaa-5b4e1e755d05`)

## Depends on

### Sub-workflows (Execute Workflow calls)

- [[update-pi-items-with-pe-details|Update PI items with PE Details]] (n8n_id `GXtdNPhHxKiailuk`) — node "Add MID partner info" (id `1eda6a8e-35a2-4892-aacd-030c93a9f2cb`)
- [[update-pi-items-with-pe-details|Update PI items with PE Details]] (n8n_id `GXtdNPhHxKiailuk`) — node "Add chargeback partner info" (id `3beb36da-32bb-4875-af49-eded8c810f91`)
- [[update-pi-items-with-pe-details|Update PI items with PE Details]] (n8n_id `GXtdNPhHxKiailuk`) — node "Set newly added entries date created" (id `8d256e60-6da9-423e-9c2e-cdefad43a130`)
- [[elavon-disputes-send-hearth-notifications|Elavon Disputes - Send Hearth Notifications]] (n8n_id `8YHh1wSkFjN6tExy`) — node "Send Hearth notifications" (id `e63f6782-154c-4a9c-9d47-ecdf014a2fd2`)

## Used by (workflows)

- [[elavon-bi-automation-daily-monitor|Elavon BI Automation (Daily Monitor)]] — node "Notify on daily monitor completion" (id `382a37f4-5785-4d08-8b8b-a10c5bd76403`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
