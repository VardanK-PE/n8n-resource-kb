---
n8n_id: "7kB7kmRDMjt8K1hc"
instance: v2
name: "Elavon BI - Edit merchant application and send (CCO Enrollment)"
status: inactive
last_modified: 2026-08-28T19:36:26.863Z
tags: []
fingerprint: "1ceca0c5a29b31297fc2f03f4b32b6a63aec9760490d1bb061fe6fc3ae971d3c"
auto_generated_at: 2026-08-28T20:45:46Z
---

<!-- auto:start -->

# Elavon BI - Edit merchant application and send (CCO Enrollment)

## Summary

- **Status:** inactive
- **n8n ID:** `7kB7kmRDMjt8K1hc`
- **Nodes:** 4
- **Last modified:** 2026-08-28T19:36:26.863Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `d9721d26-c2a1-4b8b-bb2b-5e7ab9da6366`)

## Depends on

### Credentials

- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "HTTP Request" (id `e673fe53-920d-4baa-a0c5-c01f32d4ce3d`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/merchant/{{ $json.merchant_id }}/download-signed-document` — node "HTTP Request" (id `e673fe53-920d-4baa-a0c5-c01f32d4ce3d`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
