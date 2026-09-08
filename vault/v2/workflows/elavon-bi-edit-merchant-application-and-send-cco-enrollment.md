---
n8n_id: "7kB7kmRDMjt8K1hc"
instance: v2
name: "Elavon BI - Edit merchant application and send (CCO Enrollment)"
status: inactive
last_modified: 2026-09-03T18:41:38.527Z
tags: []
fingerprint: "b067ba4066e8d6d83e338684762e2da4b1e634d97c64c8c4a12d0efc960201e5"
auto_generated_at: 2026-09-08T19:19:58Z
---

<!-- auto:start -->

# Elavon BI - Edit merchant application and send (CCO Enrollment)

## Summary

- **Status:** inactive
- **n8n ID:** `7kB7kmRDMjt8K1hc`
- **Nodes:** 10
- **Last modified:** 2026-09-03T18:41:38.527Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `d9721d26-c2a1-4b8b-bb2b-5e7ab9da6366`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Eligibility + merchant data" (id `5a942ad4-bff0-4009-bba8-e31f87423879`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "HTTP Request" (id `e673fe53-920d-4baa-a0c5-c01f32d4ce3d`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/merchant/{{ $('Edit Fields').first().json.merchant_id }}/download-signed-document` — node "HTTP Request" (id `e673fe53-920d-4baa-a0c5-c01f32d4ce3d`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Eligibility + merchant data" (id `5a942ad4-bff0-4009-bba8-e31f87423879`)

### Data tables (n8n)

- [[../resources/data-tables/bbk0o87cch8t5vzq|Elavon MCC and Commodity Codes]] (id `bbk0O87cCh8t5vzQ`) — op `get` — node "Get commodity code" (id `a8c0446d-145b-4403-a7cc-ba035790ac48`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
