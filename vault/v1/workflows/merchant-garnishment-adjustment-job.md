---
n8n_id: "lkb4rXtsJfBygB5C"
instance: v1
name: "Merchant Garnishment/Adjustment Job"
status: inactive
last_modified: 2025-08-13T17:29:39.224Z
tags: []
fingerprint: "d8368b681b827c36bace12c96c888a590d53c4f4025a320d89560536f86297c2"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Merchant Garnishment/Adjustment Job

## Summary

- **Status:** inactive
- **n8n ID:** `lkb4rXtsJfBygB5C`
- **Nodes:** 14
- **Last modified:** 2025-08-13T17:29:39.224Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `66166738-e0b6-4033-9705-8fc50f134645`) — `daily at 17:30`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `22983a47-d7e6-48d2-8dfb-e7da60973ea5`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `33086dd5-dda0-4249-802b-5ec7698d2195`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `466ea81c-51ee-4633-b6c6-daea735d1eb9`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack5" (id `62d45bd5-a6cc-4d82-afd4-c043f76f76dc`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `739731ee-bc4d-49c5-aff3-14fd929dd823`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `7ae7512a-d198-4f6d-b097-efd38befe4d9`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/payment/ach-credit` — node "HTTP Request" (id `2231892c-46d4-4712-bb8a-aea66a1a6322`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `22983a47-d7e6-48d2-8dfb-e7da60973ea5`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `466ea81c-51ee-4633-b6c6-daea735d1eb9`)

### Slack channels

- [[../resources/slack-channels/c089vqunm1n|merchant-adjustment-alerts]] (id `C089VQUNM1N`) — op `channel` — node "Slack2" (id `33086dd5-dda0-4249-802b-5ec7698d2195`)
- [[../resources/slack-channels/c089vqunm1n|merchant-adjustment-alerts]] (id `C089VQUNM1N`) — op `channel` — node "Slack5" (id `62d45bd5-a6cc-4d82-afd4-c043f76f76dc`)
- [[../resources/slack-channels/c089vqunm1n|merchant-adjustment-alerts]] (id `C089VQUNM1N`) — op `channel` — node "Slack1" (id `739731ee-bc4d-49c5-aff3-14fd929dd823`)
- [[../resources/slack-channels/c089vqunm1n|merchant-adjustment-alerts]] (id `C089VQUNM1N`) — op `channel` — node "Slack" (id `7ae7512a-d198-4f6d-b097-efd38befe4d9`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
