---
n8n_id: "MgUymrWWSzLhoUxF"
name: "Check Elavon ACH gateway status"
status: inactive
last_modified: 2026-07-23T18:21:12.108Z
tags: []
fingerprint: "4e1968b77003002296a09e543f7aadba49e3b23c51696f116b98bd7e5101e402"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Check Elavon ACH gateway status

## Summary

- **Status:** inactive
- **n8n ID:** `MgUymrWWSzLhoUxF`
- **Nodes:** 19
- **Last modified:** 2026-07-23T18:21:12.108Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `6944a734-f2b5-4c33-bd7f-1bafc9addb55`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `b5d01b63-89e2-4eda-9dc3-cb5579823e63`)

## Depends on

### Credentials

- [[../resources/credentials/l1fdqv2gyxyjgim6|PE Staging Sandbox]] (`httpBearerAuth`, id `l1fDQv2GYxYjgim6`) — node "Stage - Get ACH state" (id `5aa17965-ec99-4a04-83a0-3063af51bea6`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Prod - Get ACH state" (id `ae67c7da-35cc-4edd-81ad-718a63b567db`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Stage - Get ACH state" (id `5aa17965-ec99-4a04-83a0-3063af51bea6`)
- *(dynamic URL)* — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Prod - Get ACH state" (id `ae67c7da-35cc-4edd-81ad-718a63b567db`)

## Used by (workflows)

- [[disable-ach-gateway-main-logic|Disable ACH Gateway - Main Logic]] — node "Call 'Check Elavon ACH gateway status'" (id `6dd09ced-1166-41c6-9df6-4a7ef83a01fd`)
- [[disable-ach-gateway-main-logic|Disable ACH Gateway - Main Logic]] — node "Call 'Check Elavon ACH gateway status'2" (id `c843631c-55dd-436e-bcde-5d1d09117a66`)
- [[hearth-merchant-capabilities-status|Hearth Merchant Capabilities Status]] — node "Call 'Check ACH gateway status'" (id `07260b91-2fbb-4ef6-9960-d27f183e2816`)
- [[hearth-merchants-with-rejected-elavon-ach-but-enabled-gateway|Hearth - Merchants with rejected Elavon ACH but enabled Gateway]] — node "Call 'Check Elavon ACH gateway status'" (id `ff1667f4-f3ef-44d4-a962-73eb9209c453`)
- [[hearth-merchants-with-rejected-elavon-ach-but-enabled-gateway|Hearth - Merchants with rejected Elavon ACH but enabled Gateway]] — node "Call 'Check Elavon ACH gateway status'1" (id `be1ead95-8974-46ad-a10c-641915277950`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
