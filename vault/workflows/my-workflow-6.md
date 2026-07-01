---
n8n_id: "tXu5oNM9CkUVIKZ2"
name: "My workflow 6"
status: inactive
last_modified: 2026-04-16T20:08:16.076Z
tags: []
fingerprint: "6e0d51423afdfde5e05d18b76d23b26834013eec08ea5a7b7f21e2e16d7e67ab"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# My workflow 6

## Summary

- **Status:** inactive
- **n8n ID:** `tXu5oNM9CkUVIKZ2`
- **Nodes:** 6
- **Last modified:** 2026-04-16T20:08:16.076Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `81684e37-9a89-425c-9408-140032449c15`)

## Depends on

### Credentials

- [[../resources/credentials/e72zxlrqrweyxf18|Elavon Basic Auth]] (`httpHeaderAuth`, id `E72ZxLRqrWEyxF18`) — node "Get OAuth Token" (id `35bb6352-9a1a-4f30-9ccb-8961ae1edae5`)

### HTTP URLs

- [[../resources/http-urls/sandbox-elavonapi-com|sandbox.elavonapi.com]] — `POST https://sandbox.elavonapi.com/service/dispute-management/v2/disputes/search` — node "HTTP Request2" (id `10d1807a-4c7c-47da-a4d1-eb19b58c0243`)
- [[../resources/http-urls/sandbox-elavonapi-com|sandbox.elavonapi.com]] — `POST https://sandbox.elavonapi.com/service/v2/disputes/search` — node "HTTP Request" (id `16e26b54-b46d-41e4-b67b-d56b9688c909`)
- [[../resources/http-urls/sandbox-elavonapi-com|sandbox.elavonapi.com]] — `POST https://sandbox.elavonapi.com/oauth2/client-credentials/v2/token` — node "Get OAuth Token" (id `35bb6352-9a1a-4f30-9ccb-8961ae1edae5`)
- [[../resources/http-urls/sandbox-elavonapi-com|sandbox.elavonapi.com]] — `GET https://sandbox.elavonapi.com/service/v2/disputes` — node "HTTP Request1" (id `fa764c03-25e8-4c47-b817-6fbf5ac2da5a`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
