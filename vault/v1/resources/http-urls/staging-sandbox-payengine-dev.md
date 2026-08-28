---
type: http-url
resource_id: "staging-sandbox.payengine.dev"
current_name: "staging-sandbox.payengine.dev"
aliases: ["staging-sandbox.payengine.dev"]
auto_generated_at: 2026-08-19T19:25:44Z
---

<!-- auto:start -->

# staging-sandbox.payengine.dev

- **Resource id (canonical):** `staging-sandbox.payengine.dev`
- **Current name:** staging-sandbox.payengine.dev
- **Host:** `staging-sandbox.payengine.dev`

## Used by

- [[../../workflows/edit-curbwaste-statements|Edit Curbwaste statements]] — `POST https://staging-sandbox.payengine.dev/api/merchant/{{ $json.mid }}/statements` — node "Sandbox Staging Upload Statements" (id `dd08824d-48da-4dba-9fb3-61d6739bb85a`)
- [[../../workflows/elavon-dispute|Elavon Dispute]] — `GET https://staging-sandbox.payengine.dev/api/transaction/{{$json.dispute_id}}/dispute` — node "HTTP Request1" (id `e8dce8b2-6f0d-4609-9630-567a8941a79f`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
