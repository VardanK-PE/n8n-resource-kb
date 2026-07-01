---
n8n_id: "MgUymrWWSzLhoUxF"
name: "Check Elavon ACH gateway status"
status: inactive
last_modified: 2026-03-19T19:05:24.035Z
tags: []
fingerprint: "7798dbb2bcc170b4cae1a36361a5d6e16c3faa0f2b5b3dce1db16da967a5a48d"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Check Elavon ACH gateway status

## Summary

- **Status:** inactive
- **n8n ID:** `MgUymrWWSzLhoUxF`
- **Nodes:** 16
- **Last modified:** 2026-03-19T19:05:24.035Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `543d0361-18c2-4e04-b5be-bcd598a7bb49`)
- **manual** — node "When clicking ‘Execute workflow’" (id `5f8f0aec-eacb-467d-a441-060e38caffef`)

## Depends on

### Credentials

- [[../resources/credentials/l1fdqv2gyxyjgim6|PE Staging Sandbox]] (`httpBearerAuth`, id `l1fDQv2GYxYjgim6`) — node "Stage - Get ACH state" (id `31a57470-0a71-4a95-a499-65844a0d1f24`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Prod - Get ACH state" (id `e544a98f-d3eb-447b-8d9b-46988137bf32`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Stage - Get ACH state" (id `31a57470-0a71-4a95-a499-65844a0d1f24`)
- *(dynamic URL)* — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Prod - Get ACH state" (id `e544a98f-d3eb-447b-8d9b-46988137bf32`)

## Used by (workflows)

- [[disable-ach-gateway-main-logic|Disable ACH Gateway - Main Logic]] — node "Call 'Check Elavon ACH gateway status'" (id `6dd09ced-1166-41c6-9df6-4a7ef83a01fd`)
- [[hearth-merchant-capabilities-status|Hearth Merchant Capabilities Status]] — node "Call 'Check ACH gateway status'" (id `07260b91-2fbb-4ef6-9960-d27f183e2816`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
