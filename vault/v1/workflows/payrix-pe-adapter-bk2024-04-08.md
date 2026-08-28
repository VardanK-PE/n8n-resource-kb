---
n8n_id: "5gleRAOHEDZtmu1S"
name: "Payrix > PE Adapter bk2024-04-08"
status: inactive
last_modified: 2024-04-08T21:30:30.884Z
tags:
  - "emulators"
fingerprint: "85d8f6646303ccc8010c4c3b588f47dbe1f21fc003d7295c9b02d4c2ed5dfe56"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Payrix > PE Adapter bk2024-04-08

## Summary

- **Status:** inactive
- **n8n ID:** `5gleRAOHEDZtmu1S`
- **Nodes:** 29
- **Last modified:** 2024-04-08T21:30:30.884Z

## Triggers

- **webhook** — node "Inbound Request" (id `f18fd94b-47bd-4a2f-a406-63f9fc8ad1ca`) — POST `647cd28c-08ff-4791-b3db-cbcd35b890db`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres account]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Lookup PE MID" (id `d35a6524-60b4-4caf-aa20-57fe709450eb`)

### HTTP URLs

- [[../resources/http-urls/test-api-payrix-com|test-api.payrix.com]] — `={{ $json.body.method }} https://test-api.payrix.com{{ $json.body.path }}` — node "HTTP Request" (id `46a6d4a9-0c26-444a-bd9d-bf7d80be9fb3`)
- [[../resources/http-urls/api-payrix-com|api.payrix.com]] — `={{ $json.body.method }} https://api.payrix.com/{{ $json.body.path }}` — node "PayFrameCodeRaw" (id `ac0c7aed-231a-47b2-8491-0c0e8dc63c33`)
- [[../resources/http-urls/webhook-site|webhook.site]] — `POST https://webhook.site/bd53ecd5-374e-4ba6-80c7-257cd72dfd25` — node "HTTP Request1" (id `c7c66657-a622-422d-bad5-4d7641d911b7`)
- [[../resources/http-urls/test-api-payrix-com|test-api.payrix.com]] — `={{ $json.body.method }} https://test-api.payrix.com{{ $json.body.path }}` — node "Catchall Forwarder" (id `d0055d39-3f1f-4074-a677-354a7b259baf`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres account)]] — op `executeQuery` — node "Lookup PE MID" (id `d35a6524-60b4-4caf-aa20-57fe709450eb`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
