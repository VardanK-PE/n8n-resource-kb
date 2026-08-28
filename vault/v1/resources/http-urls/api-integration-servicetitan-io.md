---
type: http-url
instance: v1
resource_id: "api-integration.servicetitan.io"
current_name: "api-integration.servicetitan.io"
aliases: ["api-integration.servicetitan.io"]
auto_generated_at: 2026-08-19T19:25:44Z
---

<!-- auto:start -->

# api-integration.servicetitan.io

- **Resource id (canonical):** `api-integration.servicetitan.io`
- **Current name:** api-integration.servicetitan.io
- **Host:** `api-integration.servicetitan.io`

## Used by

- [[../../workflows/develotech|Develotech ServiceTitan]] — `GET https://api-integration.servicetitan.io/jpm/v2/tenant/1692561827/jobs/{{ $json.id }}/notes` — node "Get job note" (id `0fbb703e-67b2-4df4-b730-7e4679f5e0f1`)
- [[../../workflows/develotech|Develotech ServiceTitan]] — `GET https://api-integration.servicetitan.io/jpm/v2/tenant/1692561827/jobs` — node "Get Jobs" (id `d6702fa6-207d-4537-b7c2-f58e47d2e4a8`)
- [[../../workflows/develotech|Develotech ServiceTitan]] — `GET https://api-integration.servicetitan.io/settings/v2/tenant/1692561827/technicians` — node "Get Technicians" (id `950e6d83-b0ad-4ff0-acf2-ea73ed734b48`)
- [[../../workflows/develotech|Develotech ServiceTitan]] — `GET https://api-integration.servicetitan.io{{ $('When Executed by Another Workflow').item.json.url_path }}` — node "Get Technicians1" (id `a202ac42-eda9-4b34-b225-02e330c5c3dd`)
- [[../../workflows/develotech|Develotech ServiceTitan]] — `GET https://api-integration.servicetitan.io{{ $fromAI('EndpointPath', `The path that should be appended to 'https://api-integration.servicetitan.io/''`, 'string') }}` — node "ST API Request tool" (id `b7028213-ea52-4cd8-99a1-b6e915159e21`)
- [[../../workflows/develotech|Develotech ServiceTitan]] — `POST https://api-integration.servicetitan.io/jpm/v2/tenant/1692561827/jobs/{{ $('Loop Over Items').item.json.id }}/notes` — node "Post a note to job" (id `43b60aff-6bce-4ed9-92d8-a9c879d5aaa3`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
