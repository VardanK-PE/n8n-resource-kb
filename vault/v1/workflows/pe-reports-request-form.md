---
n8n_id: "7PSj71BcMMboUDkg"
instance: v1
name: "PE Reports Request Form"
status: active
last_modified: 2025-07-18T11:58:58.930Z
tags: []
fingerprint: "ea99bdc4f4ab24567cf7f6696a80b0195f6f4ead1aed3184f2681910caacaa98"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PE Reports Request Form

## Summary

- **Status:** active
- **n8n ID:** `7PSj71BcMMboUDkg`
- **Nodes:** 8
- **Last modified:** 2025-07-18T11:58:58.930Z

## Triggers

- **error** — node "Error Trigger" (id `a48383aa-bd6c-48a2-a640-73dd7c59a679`)
- **form** — node "On form submission" (id `e9c844c5-7397-429f-b6ae-56905a448e09`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `201fd853-acda-4e3f-9f13-5b8d42230554`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `a196b40e-f8b8-4ce7-9a92-33a90a866fd7`)
- [[../resources/credentials/bl0pza3gikxwnnct|ReportGenerationRequestFormBasicAuth]] (`httpBasicAuth`, id `bl0pza3GiKxWNNcT`) — node "On form submission" (id `e9c844c5-7397-429f-b6ae-56905a448e09`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `ee20b596-cb69-46cb-a282-311453339864`)

### Slack channels

- [[../resources/slack-channels/c05db6zerj5|accounts-receivable]] (id `C05DB6ZERJ5`) — op `channel` — node "Slack2" (id `201fd853-acda-4e3f-9f13-5b8d42230554`)
- [[../resources/slack-channels/c05db6zerj5|accounts-receivable]] (id `C05DB6ZERJ5`) — op `channel` — node "Slack" (id `a196b40e-f8b8-4ce7-9a92-33a90a866fd7`)
- [[../resources/slack-channels/c05db6zerj5|accounts-receivable]] (id `C05DB6ZERJ5`) — op `channel` — node "Slack1" (id `ee20b596-cb69-46cb-a282-311453339864`)

### Sub-workflows (Execute Workflow calls)

- [[monthly-ach-reports|Monthly ACH Reports]] (n8n_id `J24a0qIXslRvAe5m`) — node "Execute Workflow" (id `ac9d7695-f6e7-43f0-90e6-a697c1ca0dab`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
