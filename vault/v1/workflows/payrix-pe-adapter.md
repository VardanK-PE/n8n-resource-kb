---
n8n_id: "hjNxdCntNuRL1THI"
instance: v1
name: "Payrix > PE Adapter"
status: active
last_modified: 2024-10-25T17:20:06.200Z
tags:
  - "emulators"
fingerprint: "c193c59b247593b92f43479c4244f86c6c8abf03157fe74d3428cb3c9a41cbe9"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Payrix > PE Adapter

## Summary

- **Status:** active
- **n8n ID:** `hjNxdCntNuRL1THI`
- **Nodes:** 29
- **Last modified:** 2024-10-25T17:20:06.200Z

## Triggers

- **webhook** — node "Inbound Request" (id `e60d3643-a55f-4899-a228-a29a33ef892b`) — POST `647cd28c-08ff-4791-b3db-cbcd35b890db`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres account]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Lookup PE MID" (id `59ccd8cc-7e28-48d6-9668-b42b0d7f285f`)

### HTTP URLs

- [[../resources/http-urls/webhook-site|webhook.site]] — `POST https://webhook.site/bd53ecd5-374e-4ba6-80c7-257cd72dfd25` — node "HTTP Request1" (id `20152038-4d70-4793-94d4-1e67f9170f26`)
- [[../resources/http-urls/test-api-payrix-com|test-api.payrix.com]] — `={{ $json.body.method }} https://test-api.payrix.com{{ $json.body.path }}` — node "Catchall Forwarder" (id `51ad1564-2d61-450b-8272-88168344d011`)
- [[../resources/http-urls/api-payrix-com|api.payrix.com]] — `={{ $json.body.method }} https://api.payrix.com/{{ $json.body.path }}` — node "PayFrameCodeRaw" (id `dee5cc42-4c93-4079-9451-612c66987760`)
- [[../resources/http-urls/test-api-payrix-com|test-api.payrix.com]] — `={{ $json.body.method }} https://test-api.payrix.com{{ $json.body.path }}` — node "HTTP Request" (id `fbe07337-5c5e-453a-975d-d4d3a3b0cea9`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres account)]] — op `executeQuery` — node "Lookup PE MID" (id `59ccd8cc-7e28-48d6-9668-b42b0d7f285f`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
