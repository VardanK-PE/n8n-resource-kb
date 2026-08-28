---
n8n_id: "jWRuCkZC6fXG9Sp4"
instance: v1
name: "Closed By Elavon: Merchant status monitoring"
status: inactive
last_modified: 2025-11-16T15:03:41.086Z
tags: []
fingerprint: "8430ba5567b2c51ed391c31d36835d857155222cbfcdf831475f4adda45f1334"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Closed By Elavon: Merchant status monitoring

## Summary

- **Status:** inactive
- **n8n ID:** `jWRuCkZC6fXG9Sp4`
- **Nodes:** 16
- **Last modified:** 2025-11-16T15:03:41.086Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `71126c7a-40dc-49da-805d-d26b17a9d2d3`) — `daily at 8:00`
- **manual** — node "When clicking ‘Execute workflow’" (id `b24a7dd7-21f5-466f-bafe-224d38b56ce9`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks1" (id `3bee0435-e802-45cc-ab39-30083525d3eb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `420be47d-7635-46b6-ac7f-6d10bded8fa7`)
- [[../resources/credentials/gc45raivyrnqugiw|PE Automations Servie Account 2]] (`googleApi`, id `gc45RaIvyrNqUgiw`) — node "Create sheet" (id `fcded0ae-b84c-430f-a5c2-8624595f9bc9`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks1" (id `3bee0435-e802-45cc-ab39-30083525d3eb`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get row(s) in sheet" (id `420be47d-7635-46b6-ac7f-6d10bded8fa7`)
- [[../resources/google-sheets/|]] (id ``) — op `create`, tab `null` — node "Create sheet" (id `fcded0ae-b84c-430f-a5c2-8624595f9bc9`)

### Data tables (n8n)

- [[../resources/data-tables/l62ngzosdxe1ef3j|Merchants activity status]] (id `l62nGzOSDXe1eF3J`) — op `upsert` — node "Upsert row(s)" (id `69fef705-31be-4383-9509-5b9b99635275`)
- [[../resources/data-tables/l62ngzosdxe1ef3j|Merchants activity status]] (id `l62nGzOSDXe1eF3J`) — op `get` — node "Get row(s)" (id `98026c1a-6ad8-4467-ae33-829c4fce58d5`)

### Sub-workflows (Execute Workflow calls)

- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `2fb455a4-6828-49ed-a83f-d0a5cfbf70f5`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
