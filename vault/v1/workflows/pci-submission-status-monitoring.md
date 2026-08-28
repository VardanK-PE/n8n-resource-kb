---
n8n_id: "Tu8F1opFql4cJquG"
name: "PCI Submission Status Monitoring"
status: active
last_modified: 2026-08-03T20:21:40.929Z
tags: []
fingerprint: "ba58f99238a9a0e9e03c5cc40a9aa71e314c12a9d4e5478453a5af7063d2d2e6"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PCI Submission Status Monitoring

## Summary

- **Status:** active
- **n8n ID:** `Tu8F1opFql4cJquG`
- **Nodes:** 17
- **Last modified:** 2026-08-03T20:21:40.929Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `15d02bfc-207a-49f9-a290-74f9340a8fed`) — `unconfigured`
- **manual** — node "When clicking ‘Execute workflow’" (id `a6552eb8-e747-45bc-9619-cc35c15ac3ee`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `68f513fd-eed4-4204-ae0d-0b89e9f98c19`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get row(s) in sheet" (id `68f513fd-eed4-4204-ae0d-0b89e9f98c19`)

### Sub-workflows (Execute Workflow calls)

- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'2" (id `4069984e-2f38-49e3-b656-035431da5040`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'1" (id `63217260-76b9-435b-8a1c-86511560d12f`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'3" (id `8ccc95c4-46f6-4b2a-a0fc-c4923b3f10b9`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `a0b28517-4f1d-4003-8363-430f847f2436`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
