---
type: http-url
resource_id: "console.payengine.dev"
current_name: "console.payengine.dev"
aliases: ["console.payengine.dev"]
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# console.payengine.dev

- **Resource id (canonical):** `console.payengine.dev`
- **Current name:** console.payengine.dev
- **Host:** `console.payengine.dev`

## Used by

- [[../../workflows/gitbook-auth|Gitbook Auth]] — `POST https://console.payengine.dev/api/user/auth` — node "Check Credentials" (id `3ac9ea38-bce8-43e2-aa3c-e62079e99d80`)
- [[../../workflows/gitbook-auth|Gitbook Auth]] — `POST https://console.payengine.dev/api/user/auth` — node "HTTP Request" (id `3e3e4669-1edb-4672-9f89-73c591ba1b43`)
- [[../../workflows/managed-by-spartak-ai-agent-partner-merchant-bulk-import-sync-sandbox|[Managed by Spartak AI Agent] Partner Merchant Bulk Import Sync (SANDBOX)]] — `POST https://console.payengine.dev/api/merchant` — node "Create Merchant" (id `create-merchant`)
- [[../../workflows/managed-by-spartak-ai-agent-partner-merchant-bulk-import-sync-sandbox|[Managed by Spartak AI Agent] Partner Merchant Bulk Import Sync (SANDBOX)]] — `POST https://console.payengine.dev/api/merchant/{{ $('Create Merchant').item.json.data?.id ?? $('Create Merchant').item.json.id }}/gateways` — node "Create Gateway" (id `create-gateway`)
- [[../../workflows/managed-by-spartak-ai-agent-partner-merchant-bulk-import-sync-sandbox|[Managed by Spartak AI Agent] Partner Merchant Bulk Import Sync (SANDBOX)]] — `PATCH https://console.payengine.dev/api/v2/merchant/{{ $('Create Merchant').item.json.data?.id ?? $('Create Merchant').item.json.id }}/status` — node "Activate Merchant" (id `activate-merchant`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
