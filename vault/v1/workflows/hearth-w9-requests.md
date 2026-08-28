---
n8n_id: "b0uBiVZv2sahzDbt"
instance: v1
name: "Hearth W9 Requests"
status: inactive
last_modified: 2025-11-21T17:35:19.860Z
tags: []
fingerprint: "281b9a1b6cd77277545a8011319e3182c38f73c54ab2e4d8dbd1f74e1ed6812e"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Hearth W9 Requests

## Summary

- **Status:** inactive
- **n8n ID:** `b0uBiVZv2sahzDbt`
- **Nodes:** 13
- **Last modified:** 2025-11-21T17:35:19.860Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `857b8322-06a9-45e9-ac9f-3d2cf9f3164f`)

## Depends on

### Credentials

- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Get many messages" (id `6c1a92a5-0c2f-4d81-b572-2d662426ad82`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Get many messages1" (id `82f41898-d299-4b8a-95d9-17b06c99c7e7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `a4d20324-0c6d-422c-8ec2-15b3d320151d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `a5164cb0-2b3c-4095-b8d6-d5e33e914118`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet1" (id `becc9c3c-e5cf-4e79-8663-56f65b829410`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `dc3ce12d-d7ca-4cca-af76-d16def4b57cc`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `eee2c0c5-6a19-4778-a066-507e75b02332`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `eee2c0c5-6a19-4778-a066-507e75b02332`)

### Google Sheets

- [[../resources/google-sheets/1swpg9e6oppao-bvxztiuwp3swnuvz-ox0ljaqbvuues|PE Hearth Reports (shared)]] (id `1SwPG9E6OPPAO_BvXZTIuWp3SwnUvZ-OX0LJAQbvUues`) — op `?`, tab `W-9 Requests` — node "Get row(s) in sheet" (id `a4d20324-0c6d-422c-8ec2-15b3d320151d`)
- [[../resources/google-sheets/1swpg9e6oppao-bvxztiuwp3swnuvz-ox0ljaqbvuues|PE Hearth Reports (shared)]] (id `1SwPG9E6OPPAO_BvXZTIuWp3SwnUvZ-OX0LJAQbvUues`) — op `update`, tab `W-9 Requests` — node "Update row in sheet" (id `a5164cb0-2b3c-4095-b8d6-d5e33e914118`)
- [[../resources/google-sheets/1swpg9e6oppao-bvxztiuwp3swnuvz-ox0ljaqbvuues|PE Hearth Reports (shared)]] (id `1SwPG9E6OPPAO_BvXZTIuWp3SwnUvZ-OX0LJAQbvUues`) — op `appendOrUpdate`, tab `W-9 Requests` — node "Append or update row in sheet1" (id `becc9c3c-e5cf-4e79-8663-56f65b829410`)
- [[../resources/google-sheets/1swpg9e6oppao-bvxztiuwp3swnuvz-ox0ljaqbvuues|PE Hearth Reports (shared)]] (id `1SwPG9E6OPPAO_BvXZTIuWp3SwnUvZ-OX0LJAQbvUues`) — op `appendOrUpdate`, tab `W-9 Requests` — node "Append or update row in sheet" (id `dc3ce12d-d7ca-4cca-af76-d16def4b57cc`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
