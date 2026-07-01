---
n8n_id: "E66SPMxJDH28QBxI"
name: "Disable Elavon ACH gateway for a given merchant"
status: inactive
last_modified: 2026-04-15T19:02:55.688Z
tags: []
fingerprint: "404fb040a9b08487166133c60f73c5624d2a9df466044a4c168d71668ba8d675"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Disable Elavon ACH gateway for a given merchant

## Summary

- **Status:** inactive
- **n8n ID:** `E66SPMxJDH28QBxI`
- **Nodes:** 29
- **Last modified:** 2026-04-15T19:02:55.688Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `0e1b58aa-e713-4341-be38-579a2b1a847f`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `cff70a6d-a159-4be6-bf34-30551331d7b7`)

## Depends on

### Credentials

- [[../resources/credentials/l1fdqv2gyxyjgim6|PE Staging Sandbox]] (`httpBearerAuth`, id `l1fDQv2GYxYjgim6`) — node "Stage - Disable ACH" (id `58d04a8f-ca3f-487f-9f13-3a34815f5d8e`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Prod - Get ACH state" (id `7d4f7571-f267-4b45-aa97-8495dc9c4774`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Prod - Disable ACH" (id `7e9467a1-19e4-4aa4-83ec-72a497950420`)
- [[../resources/credentials/l1fdqv2gyxyjgim6|PE Staging Sandbox]] (`httpBearerAuth`, id `l1fDQv2GYxYjgim6`) — node "Stage - Get ACH state" (id `eefb440e-0106-471c-8a9b-7a208dee9ef6`)

### HTTP URLs

- *(dynamic URL)* — `PATCH {{ $('Set base URL').item.json.pe_console_base_url }}/api/master/merchants/{{ $('Entry Point').first().json.merchantID }}/gateway/{{ $json.id }}` — node "Stage - Disable ACH" (id `58d04a8f-ca3f-487f-9f13-3a34815f5d8e`)
- *(dynamic URL)* — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Prod - Get ACH state" (id `7d4f7571-f267-4b45-aa97-8495dc9c4774`)
- *(dynamic URL)* — `PATCH {{ $('Set base URL').item.json.pe_console_base_url }}/api/master/merchants/{{ $('Entry Point').first().json.merchantID }}/gateway/{{ $json.id }}` — node "Prod - Disable ACH" (id `7e9467a1-19e4-4aa4-83ec-72a497950420`)
- *(dynamic URL)* — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Stage - Get ACH state" (id `eefb440e-0106-471c-8a9b-7a208dee9ef6`)

## Used by (workflows)

- [[disable-ach-gateway-main-logic|Disable ACH Gateway - Main Logic]] — node "Call 'Disable Elavon ACH gateway for a given merchant'" (id `cc07df45-e7fe-44c8-9ad5-7e1b123242a6`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
