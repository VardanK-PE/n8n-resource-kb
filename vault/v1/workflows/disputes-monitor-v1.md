---
n8n_id: "QE4hVXVz1d6eNYyN"
name: "Disputes Monitor V1"
status: inactive
last_modified: 2025-06-24T16:28:40.161Z
tags: []
fingerprint: "c88ca8c1e6969a2095fe72845092cb8c364dec0b1bf9034cef932e331b69ab16"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Disputes Monitor V1

## Summary

- **Status:** inactive
- **n8n ID:** `QE4hVXVz1d6eNYyN`
- **Nodes:** 12
- **Last modified:** 2025-06-24T16:28:40.161Z

## Triggers

- **manual** — node "When clicking ‘Test workflow’" (id `1a4d99ae-e3e2-4188-a4ca-4b27a9ea1476`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `00a68643-7a28-4b51-8fd5-aca7c83ab3fb`)
- [[../resources/credentials/mekrtcrubrfnr3ei|PE Atlassian Cloud account]] (`jiraSoftwareCloudApi`, id `MeKRTCrUBRfnR3Ei`) — node "Jira Software1" (id `025cb1f8-1160-4a1f-93e3-cb5e10600bfa`)
- [[../resources/credentials/mekrtcrubrfnr3ei|PE Atlassian Cloud account]] (`jiraSoftwareCloudApi`, id `MeKRTCrUBRfnR3Ei`) — node "Jira Software2" (id `2599aea4-4c52-4407-a289-66b5839b7a86`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `38a82f06-0e9f-4424-85c5-71027895b563`)
- [[../resources/credentials/mekrtcrubrfnr3ei|PE Atlassian Cloud account]] (`jiraSoftwareCloudApi`, id `MeKRTCrUBRfnR3Ei`) — node "Jira Software5" (id `3e581b78-075a-4c92-a84c-fcb227c5071b`)
- [[../resources/credentials/mekrtcrubrfnr3ei|PE Atlassian Cloud account]] (`jiraSoftwareCloudApi`, id `MeKRTCrUBRfnR3Ei`) — node "Jira Software" (id `5ff76517-4121-40e9-8a3f-61780ec927f3`)
- [[../resources/credentials/mekrtcrubrfnr3ei|PE Atlassian Cloud account]] (`jiraSoftwareCloudApi`, id `MeKRTCrUBRfnR3Ei`) — node "HTTP Request" (id `701bd5f4-863b-45ce-9689-76848d44dfa9`)
- [[../resources/credentials/mekrtcrubrfnr3ei|PE Atlassian Cloud account]] (`jiraSoftwareCloudApi`, id `MeKRTCrUBRfnR3Ei`) — node "Jira Software3" (id `8bd9f386-7492-46a9-b3ab-3ae686cd2649`)
- [[../resources/credentials/mekrtcrubrfnr3ei|PE Atlassian Cloud account]] (`jiraSoftwareCloudApi`, id `MeKRTCrUBRfnR3Ei`) — node "HTTP Request1" (id `c75b7e77-0be8-4c87-bdd6-c8ffc6fd2246`)
- [[../resources/credentials/mekrtcrubrfnr3ei|PE Atlassian Cloud account]] (`jiraSoftwareCloudApi`, id `MeKRTCrUBRfnR3Ei`) — node "Jira Software4" (id `e5c6bcb0-9c45-4ffa-bc11-f06e2faa6012`)

### HTTP URLs

- [[../resources/http-urls/payengine-atlassian-net|payengine.atlassian.net]] — `GET https://payengine.atlassian.net/rest/api/2/issue/CS-3?fields=customfield_10010` — node "HTTP Request" (id `701bd5f4-863b-45ce-9689-76848d44dfa9`)
- [[../resources/http-urls/payengine-atlassian-net|payengine.atlassian.net]] — `GET https://payengine.atlassian.net/rest/servicedeskapi/requesttype` — node "HTTP Request1" (id `c75b7e77-0be8-4c87-bdd6-c8ffc6fd2246`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `00a68643-7a28-4b51-8fd5-aca7c83ab3fb`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `38a82f06-0e9f-4424-85c5-71027895b563`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
