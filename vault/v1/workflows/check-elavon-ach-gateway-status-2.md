---
n8n_id: "WaRNwwXwbHcPmYTk"
instance: v1
name: "Check Elavon ACH gateway status 2"
status: inactive
last_modified: 2026-04-15T19:12:52.748Z
tags: []
fingerprint: "134c42143ae29369eafcc85c5f05fbc62cc69805df9b6fa708c756fdb6110e0d"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Check Elavon ACH gateway status 2

## Summary

- **Status:** inactive
- **n8n ID:** `WaRNwwXwbHcPmYTk`
- **Nodes:** 17
- **Last modified:** 2026-04-15T19:12:52.748Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `0b4a4632-f6fd-480b-9968-fae3b3b69a1b`)
- **manual** — node "When clicking ‘Execute workflow’" (id `473a7462-8ae6-43d5-8ba9-fa12daed44ac`)

## Depends on

### Credentials

- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Prod - Get ACH state" (id `3326a9ed-6946-4e5e-a719-5e048052ad40`)
- [[../resources/credentials/l1fdqv2gyxyjgim6|PE Staging Sandbox]] (`httpBearerAuth`, id `l1fDQv2GYxYjgim6`) — node "Stage - Get ACH state" (id `5118a558-e1b3-476d-be70-6c0bf4195f75`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Prod - Get ACH state" (id `3326a9ed-6946-4e5e-a719-5e048052ad40`)
- *(dynamic URL)* — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Stage - Get ACH state" (id `5118a558-e1b3-476d-be70-6c0bf4195f75`)

## Used by (workflows)

- [[disable-ach-gateway-main-logic|Disable ACH Gateway - Main Logic]] — node "Call 'Check Elavon ACH gateway status'1" (id `199b1e81-4a9d-45fd-9455-3c022c626389`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
