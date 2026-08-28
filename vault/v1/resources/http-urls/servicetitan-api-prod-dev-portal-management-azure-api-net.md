---
type: http-url
instance: v1
resource_id: "servicetitan-api-prod-dev-portal.management.azure-api.net"
current_name: "servicetitan-api-prod-dev-portal.management.azure-api.net"
aliases: ["servicetitan-api-prod-dev-portal.management.azure-api.net"]
auto_generated_at: 2026-08-28T21:31:11Z
---

<!-- auto:start -->

# servicetitan-api-prod-dev-portal.management.azure-api.net

- **Resource id (canonical):** `servicetitan-api-prod-dev-portal.management.azure-api.net`
- **Current name:** servicetitan-api-prod-dev-portal.management.azure-api.net
- **Host:** `servicetitan-api-prod-dev-portal.management.azure-api.net`

## Used by

- [[../../workflows/develotech-servicetitan|Develotech ServiceTitan]] — `GET https://servicetitan-api-prod-dev-portal.management.azure-api.net/subscriptions/sid/resourceGroups/rgid/providers/Microsoft.ApiManagement/service/sid/apis?expandApiVersionSet=true&$top=500&$skip=0&$filter=isCurrent%20eq%20true&skipWorkspaces=true&api-version=2022-04-01-preview` — node "API Categories" (id `b299e84c-bc7e-4d27-be64-ceedfaaf6334`)
- [[../../workflows/develotech-servicetitan|Develotech ServiceTitan]] — `GET https://servicetitan-api-prod-dev-portal.management.azure-api.net/subscriptions/sid/resourceGroups/rgid/providers/Microsoft.ApiManagement/service/sid/apis?expandApiVersionSet=true&$top=500&$skip=0&$filter=isCurrent%20eq%20true&skipWorkspaces=true&api-version=2022-04-01-preview` — node "HTTP Request1" (id `4fe85372-26c4-4f65-84f4-e7c20cb19627`)
- [[../../workflows/develotech-servicetitan|Develotech ServiceTitan]] — `GET https://servicetitan-api-prod-dev-portal.management.azure-api.net/subscriptions/sid/resourceGroups/rgid/providers/Microsoft.ApiManagement/service/sid{{ $json.operation.id }}?api-version=2022-04-01-preview` — node "HTTP Request3" (id `9447cd61-e13c-402e-b1f6-66d1b89a2a1e`)
- [[../../workflows/develotech-servicetitan|Develotech ServiceTitan]] — `GET https://servicetitan-api-prod-dev-portal.management.azure-api.net{{ $fromAI('URL', `The value[].id should be looked up and passed in from API Categoreis tools`, 'string') }}/operationsByTags?includeNotTaggedOperations=true&$top=500&$skip=0&api-version=2022-04-01-preview` — node "API Category Endpoints" (id `46e1c85c-9800-4e3b-b614-aecc5cbc46cf`)
- [[../../workflows/develotech-servicetitan|Develotech ServiceTitan]] — `GET https://servicetitan-api-prod-dev-portal.management.azure-api.net{{ $fromAI('URL', `The value[].tag.operation.id should be looked up and passed in from API Categoreis tools`, 'string') }}/operationsByTags?includeNotTaggedOperations=true&$top=500&$skip=0&api-version=2022-04-01-preview` — node "API Category Endpoint Details" (id `85618699-fb1a-4f08-aa00-db6cdfbbce80`)
- [[../../workflows/develotech-servicetitan|Develotech ServiceTitan]] — `GET https://servicetitan-api-prod-dev-portal.management.azure-api.net{{ $json.id }}/operationsByTags?includeNotTaggedOperations=true&$top=500&$skip=0&api-version=2022-04-01-preview` — node "HTTP Request2" (id `dad96699-2ac0-467d-a2b6-ab8933abf494`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
