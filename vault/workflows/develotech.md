---
n8n_id: "kYETAiiluoWDyZHO"
name: "Develotech"
status: inactive
last_modified: 2026-02-20T16:53:41.939Z
tags: []
fingerprint: "4c0dffc3347a03090dbcf29e5bec84af1622fb8f158adbfebda483303be87d04"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Develotech

## Summary

- **Status:** inactive
- **n8n ID:** `kYETAiiluoWDyZHO`
- **Nodes:** 45
- **Last modified:** 2026-02-20T16:53:41.939Z

## Triggers

- **other** — node "MCP Server Trigger" (id `1276ad48-2a66-4f3e-a0c0-5505c1bb3e8b`) — GET `250df83b-c455-48cb-9fe1-9c989225b6ca`
- **schedule** — node "Schedule Trigger1" (id `2de77d05-4259-4dfd-bc81-3f056b63c8af`) — `every 1 minute(s)`
- **execute-workflow** — node "When Executed by Another Workflow" (id `735f23bf-0656-4d6a-aa15-6d7a018ba0d5`)
- **manual** — node "When clicking ‘Execute workflow’" (id `7c4f71f1-4a0a-47d3-a6e9-a852e8278367`)
- **schedule** — node "Schedule Trigger" (id `f9691b74-7bae-468b-8a8b-2dc5b487501a`) — `every 1 second(s)`

## Depends on

### Credentials

- [[../resources/credentials/cyocscldlc2ybmpm|Freshdesk PESupport]] (`freshdeskApi`, id `CyOCsclDlC2yBMPM`) — node "Get a ticket" (id `139bf34a-3d50-4ac7-a65c-4f7993e1c9de`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `3c6b9c36-ba89-4047-93c7-e036c28dea51`)
- [[../resources/credentials/cyocscldlc2ybmpm|Freshdesk PESupport]] (`freshdeskApi`, id `CyOCsclDlC2yBMPM`) — node "Get many tickets" (id `5fd188ec-78ff-4fb7-8baf-4e8f23721095`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Delete a message" (id `ba98decc-c072-4952-84bf-4d9592fbe5c5`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send a message in Gmail" (id `c250792f-4fd5-4d62-b2e8-9a29ae532808`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send a message" (id `e6cb1f6f-10c3-4ed6-98f6-8ba3b12ca381`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send a message1" (id `e9f067d1-e70e-4646-a3b3-889ebe31c1f8`)

### HTTP URLs

- [[../resources/http-urls/auth-integration-servicetitan-io|auth-integration.servicetitan.io]] — `POST https://auth-integration.servicetitan.io/connect/token ` — node "Obtain Access Token2" (id `01f875d1-6b77-42b0-9700-d543276b227c`)
- [[../resources/http-urls/auth-integration-servicetitan-io|auth-integration.servicetitan.io]] — `POST https://auth-integration.servicetitan.io/connect/token ` — node "Obtain Access Token1" (id `0ee9237d-6fa8-4951-af63-23936711d6c8`)
- [[../resources/http-urls/api-integration-servicetitan-io|api-integration.servicetitan.io]] — `GET https://api-integration.servicetitan.io/jpm/v2/tenant/1692561827/jobs/{{ $json.id }}/notes` — node "Get job note" (id `0fbb703e-67b2-4df4-b730-7e4679f5e0f1`)
- [[../resources/http-urls/api-integration-servicetitan-io|api-integration.servicetitan.io]] — `POST https://api-integration.servicetitan.io/jpm/v2/tenant/1692561827/jobs/{{ $('Loop Over Items').item.json.id }}/notes` — node "Post a note to job" (id `43b60aff-6bce-4ed9-92d8-a9c879d5aaa3`)
- [[../resources/http-urls/servicetitan-api-prod-dev-portal-management-azure-api-net|servicetitan-api-prod-dev-portal.management.azure-api.net]] — `GET https://servicetitan-api-prod-dev-portal.management.azure-api.net{{ $fromAI('URL', `The value[].id should be looked up and passed in from API Categoreis tools`, 'string') }}/operationsByTags?includeNotTaggedOperations=true&$top=500&$skip=0&api-version=2022-04-01-preview` — node "API Category Endpoints" (id `46e1c85c-9800-4e3b-b614-aecc5cbc46cf`)
- [[../resources/http-urls/servicetitan-api-prod-dev-portal-management-azure-api-net|servicetitan-api-prod-dev-portal.management.azure-api.net]] — `GET https://servicetitan-api-prod-dev-portal.management.azure-api.net/subscriptions/sid/resourceGroups/rgid/providers/Microsoft.ApiManagement/service/sid/apis?expandApiVersionSet=true&$top=500&$skip=0&$filter=isCurrent%20eq%20true&skipWorkspaces=true&api-version=2022-04-01-preview` — node "HTTP Request1" (id `4fe85372-26c4-4f65-84f4-e7c20cb19627`)
- [[../resources/http-urls/victorious-field-02b1c0e1e-3-azurestaticapps-net|victorious-field-02b1c0e1e.3.azurestaticapps.net]] — `GET https://victorious-field-02b1c0e1e.3.azurestaticapps.net/api/technicians` — node "HTTP Request" (id `62b70570-e546-4dbe-8e9a-8386e830b211`)
- [[../resources/http-urls/auth-integration-servicetitan-io|auth-integration.servicetitan.io]] — `POST https://auth-integration.servicetitan.io/connect/token ` — node "Obtain Access Token" (id `6dce41e9-0f58-46b7-88ab-3f7a376149a4`)
- [[../resources/http-urls/servicetitan-api-prod-dev-portal-management-azure-api-net|servicetitan-api-prod-dev-portal.management.azure-api.net]] — `GET https://servicetitan-api-prod-dev-portal.management.azure-api.net{{ $fromAI('URL', `The value[].tag.operation.id should be looked up and passed in from API Categoreis tools`, 'string') }}/operationsByTags?includeNotTaggedOperations=true&$top=500&$skip=0&api-version=2022-04-01-preview` — node "API Category Endpoint Details" (id `85618699-fb1a-4f08-aa00-db6cdfbbce80`)
- [[../resources/http-urls/servicetitan-api-prod-dev-portal-management-azure-api-net|servicetitan-api-prod-dev-portal.management.azure-api.net]] — `GET https://servicetitan-api-prod-dev-portal.management.azure-api.net/subscriptions/sid/resourceGroups/rgid/providers/Microsoft.ApiManagement/service/sid{{ $json.operation.id }}?api-version=2022-04-01-preview` — node "HTTP Request3" (id `9447cd61-e13c-402e-b1f6-66d1b89a2a1e`)
- [[../resources/http-urls/api-integration-servicetitan-io|api-integration.servicetitan.io]] — `GET https://api-integration.servicetitan.io/settings/v2/tenant/1692561827/technicians` — node "Get Technicians" (id `950e6d83-b0ad-4ff0-acf2-ea73ed734b48`)
- [[../resources/http-urls/api-integration-servicetitan-io|api-integration.servicetitan.io]] — `GET https://api-integration.servicetitan.io{{ $('When Executed by Another Workflow').item.json.url_path }}` — node "Get Technicians1" (id `a202ac42-eda9-4b34-b225-02e330c5c3dd`)
- [[../resources/http-urls/servicetitan-api-prod-dev-portal-management-azure-api-net|servicetitan-api-prod-dev-portal.management.azure-api.net]] — `GET https://servicetitan-api-prod-dev-portal.management.azure-api.net/subscriptions/sid/resourceGroups/rgid/providers/Microsoft.ApiManagement/service/sid/apis?expandApiVersionSet=true&$top=500&$skip=0&$filter=isCurrent%20eq%20true&skipWorkspaces=true&api-version=2022-04-01-preview` — node "API Categories" (id `b299e84c-bc7e-4d27-be64-ceedfaaf6334`)
- [[../resources/http-urls/api-integration-servicetitan-io|api-integration.servicetitan.io]] — `GET https://api-integration.servicetitan.io{{ $fromAI('EndpointPath', `The path that should be appended to 'https://api-integration.servicetitan.io/''`, 'string') }}` — node "ST API Request tool" (id `b7028213-ea52-4cd8-99a1-b6e915159e21`)
- [[../resources/http-urls/api-integration-servicetitan-io|api-integration.servicetitan.io]] — `GET https://api-integration.servicetitan.io/jpm/v2/tenant/1692561827/jobs` — node "Get Jobs" (id `d6702fa6-207d-4537-b7c2-f58e47d2e4a8`)
- [[../resources/http-urls/servicetitan-api-prod-dev-portal-management-azure-api-net|servicetitan-api-prod-dev-portal.management.azure-api.net]] — `GET https://servicetitan-api-prod-dev-portal.management.azure-api.net{{ $json.id }}/operationsByTags?includeNotTaggedOperations=true&$top=500&$skip=0&api-version=2022-04-01-preview` — node "HTTP Request2" (id `dad96699-2ac0-467d-a2b6-ab8933abf494`)
- [[../resources/http-urls/auth-integration-servicetitan-io|auth-integration.servicetitan.io]] — `POST https://auth-integration.servicetitan.io/connect/token ` — node "Get ST API Bearer Token" (id `e7b0eef8-ab2e-4f5a-9d82-99196d083bb7`)

### Google Drive

- [[../resources/google-drive/1fmlnpnm2enixq1m2pa7nyhlealqe42rigpycyejouek|Test Context Stuff]] (`file`, id `1FMlnpnM2ENIxQ1m2Pa7nYHlEALQE42rIgPYCYEjoUEk`) — op `download` — node "Download file" (id `3c6b9c36-ba89-4047-93c7-e036c28dea51`)

### Sub-workflows (Execute Workflow calls)

- [[develotech|Develotech]] (n8n_id `kYETAiiluoWDyZHO`) — node "servicetitan api request" (id `f4c1b811-e97e-4006-ae24-d7ceb11aa7f0`)

## Used by (workflows)

- [[develotech|Develotech]] — node "servicetitan api request" (id `f4c1b811-e97e-4006-ae24-d7ceb11aa7f0`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
