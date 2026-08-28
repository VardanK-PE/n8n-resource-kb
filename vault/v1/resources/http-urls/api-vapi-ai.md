---
type: http-url
instance: v1
resource_id: "api.vapi.ai"
current_name: "api.vapi.ai"
aliases: ["api.vapi.ai"]
auto_generated_at: 2026-08-28T21:31:11Z
---

<!-- auto:start -->

# api.vapi.ai

- **Resource id (canonical):** `api.vapi.ai`
- **Current name:** api.vapi.ai
- **Host:** `api.vapi.ai`

## Used by

- [[../../workflows/vapi-server|VAPI Server]] — `GET https://api.vapi.ai/call` — node "Get Calls" (id `6376b445-df93-4da8-857c-1a68010aa75c`)
- [[../../workflows/vapi-server|VAPI Server]] — `GET https://api.vapi.ai/call/{{ $('Switch').item.json.body.message.call.id }}` — node "Get Call Details" (id `6bac8068-e856-496e-965a-5aa1c8ee4d7c`)
- [[../../workflows/vapi-server|VAPI Server]] — `GET https://api.vapi.ai/call/{{ $('Switch').item.json.body.message.call.id }}` — node "Get Call Details1" (id `19b766fd-f9db-49c1-a915-1f234ddeb212`)
- [[../../workflows/vapi-server|VAPI Server]] — `PATCH https://api.vapi.ai/call/{{ $('Switch').item.json.body.message.call.id }}` — node "Update Call Name" (id `59975dfb-bf2e-444e-8f92-2ac2ce6c3848`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
