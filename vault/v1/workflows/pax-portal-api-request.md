---
n8n_id: "T0yGFQaEQnHpmPdt"
instance: v1
name: "PAX Portal API Request"
status: inactive
last_modified: 2026-05-27T16:02:45.340Z
tags: []
fingerprint: "227f93d493e00c1cc8a55fe4169950775ef3298cee0ac21808fc7e93248135f5"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PAX Portal API Request

## Summary

- **Status:** inactive
- **n8n ID:** `T0yGFQaEQnHpmPdt`
- **Nodes:** 8
- **Last modified:** 2026-05-27T16:02:45.340Z

## Triggers

- **execute-workflow** — node "PAXStore API Request" (id `3a61a4dd-82c4-44b6-a678-c713907359be`)

## Depends on

### Sub-workflows (Execute Workflow calls)

- [[pax-portal-access-token-manager|PAX Portal Access Token Manager]] (n8n_id `pY05hGyMJwslcwoH`) — node "Access Token1" (id `7b7e813b-3212-4a6b-a8ba-38db77c4804d`)

## Used by (workflows)

- [[pax-device-monitoring|PAX Device Monitoring]] — node "GET /current-user" (id `a5209929-6698-42d7-b38d-6f8a5a29c1f7`)
- [[pax-device-monitoring|PAX Device Monitoring]] — node "GET /p-market-web/v1/common/system-config" (id `4105b336-3d81-43c1-b270-11750b6b3f6e`)
- [[pax-device-monitoring|PAX Device Monitoring]] — node "GET /p-market-web/v1/common/system-config1" (id `ab28bd2b-f699-4456-aa07-213f3799864d`)
- [[pax-device-monitoring|PAX Device Monitoring]] — node "GET /resellers/tree" (id `36977806-6618-4345-beaa-99f8bd27ef94`)
- [[pax-device-monitoring|PAX Device Monitoring]] — node "GET /terminals/list" (id `efbaf083-72c3-40ce-b996-572263c36ced`)
- [[pax-device-monitoring|PAX Device Monitoring]] — node "GET /terminals/list Count" (id `0ef5e90b-3264-4991-a50d-2a3b42dde139`)
- [[pax-terminal-details-sync|PAX Terminal Details Sync]] — node "GET /installed-apks" (id `e7fcf556-538c-478f-9699-042a95bfce82`)
- [[pax-terminal-details-sync|PAX Terminal Details Sync]] — node "GET /installed-firmware" (id `a9ae5669-168a-4a29-adc4-4f3e966d05d0`)
- [[pax-terminal-details-sync|PAX Terminal Details Sync]] — node "GET /param" (id `e514ac11-3dc9-4e51-ac49-ebcfe024aa3d`)
- [[pax-terminal-details-sync|PAX Terminal Details Sync]] — node "GET /terminals/{terminal}" (id `6e60c8fc-b760-4fd7-b69c-4d56ed4009a4`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
