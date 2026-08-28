---
n8n_id: "YvKojPnHEEmamM0A"
instance: v1
name: "Critical Workflow Activity Monitoring"
status: active
last_modified: 2025-12-19T17:10:00.472Z
tags: []
fingerprint: "de37ba62616216664d706863d2ec7ed48914620204b9f51176c1c0b5528ab779"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Critical Workflow Activity Monitoring

## Summary

- **Status:** active
- **n8n ID:** `YvKojPnHEEmamM0A`
- **Nodes:** 13
- **Last modified:** 2025-12-19T17:10:00.472Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `0a174f76-71a0-44f5-b347-a030a1a966c7`)
- **error** — node "Error Trigger" (id `4b701072-7feb-4890-a9db-354fac40026b`)
- **schedule** — node "Schedule Trigger" (id `e4462a2c-86d3-49ba-8f0a-1b6d95359528`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Workflow details1" (id `620268b8-a61c-4cc5-a2e3-880e0fc5fd1d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Workflow details" (id `7dae8f9f-19ed-4ea9-8054-eabfc114d72e`)
- [[../resources/credentials/vjyobgaeh30bqna6|n8nio-pg]] (`n8nApi`, id `vJyOBgaEh30bQnA6`) — node "Get many workflows" (id `8f1dea48-85ae-4689-bfd0-301d18390abc`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `942faeaf-efee-4270-9501-e7170733efde`)
- [[../resources/credentials/vjyobgaeh30bqna6|n8nio-pg]] (`n8nApi`, id `vJyOBgaEh30bQnA6`) — node "Get a workflow" (id `c4da7817-cb89-4e24-99a7-16d495b43346`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `cabce65c-93f7-4284-a785-5b507152faca`)

### Google Sheets

- [[../resources/google-sheets/1um4swqm37tusmrqtrrcb-1mh7j3bgmn9zb2hdahixzw|Workflow Activity Monitoring]] (id `1UM4SWqM37TusMRqTRrcB_1mh7J3bgmn9zb2hdAHIxZw`) — op `appendOrUpdate`, tab `Critical Infrastrucure` — node "Get Workflow details1" (id `620268b8-a61c-4cc5-a2e3-880e0fc5fd1d`)
- [[../resources/google-sheets/1um4swqm37tusmrqtrrcb-1mh7j3bgmn9zb2hdahixzw|Workflow Activity Monitoring]] (id `1UM4SWqM37TusMRqTRrcB_1mh7J3bgmn9zb2hdAHIxZw`) — op `?`, tab `Critical Infrastrucure` — node "Get Workflow details" (id `7dae8f9f-19ed-4ea9-8054-eabfc114d72e`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Send a message4" (id `942faeaf-efee-4270-9501-e7170733efde`)
- [[../resources/slack-channels/c077w62bd7w|ops_alerts]] (id `C077W62BD7W`) — op `channel` — node "Send a message6" (id `cabce65c-93f7-4284-a785-5b507152faca`)

### Sub-workflows (Execute Workflow calls)

- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `1a736db8-23fb-47f4-b880-3c4ce26e2400`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
