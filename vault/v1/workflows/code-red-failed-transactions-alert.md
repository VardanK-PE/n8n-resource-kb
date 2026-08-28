---
n8n_id: "TWU7t9XCJ7sNEOl1"
name: "Code Red / Failed Transactions alert"
status: inactive
last_modified: 2026-04-13T17:43:16.025Z
tags: []
fingerprint: "b742f412e4ffae1a1fb06b846b989de0ab31b78b76c2b4a74339d21ead684e34"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Code Red / Failed Transactions alert

## Summary

- **Status:** inactive
- **n8n ID:** `TWU7t9XCJ7sNEOl1`
- **Nodes:** 9
- **Last modified:** 2026-04-13T17:43:16.025Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `01d8d9cf-b7d6-4117-89cd-0b61ee3dd409`) — `every 30 minute(s)`
- **schedule** — node "Schedule Trigger1" (id `6805e789-c0ee-43b4-9eff-ab2e873e9ef4`) — `unconfigured`
- **manual** — node "When clicking ‘Execute workflow’" (id `74ffd531-47eb-4715-8483-f776eccfda21`)

## Depends on

### Credentials

- [[../resources/credentials/ikbo9ffkgfj1bzcs|AWS SDK Wrapper Credentials PE PROD]] (`awsSdkWrapperCredentialsApi`, id `IKBO9fFKgfj1BzcS`) — node "CloudwatchGetQueryResults" (id `06e21541-7d17-47ea-b263-70bb265d08c4`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `1925dd7d-626a-40b8-9203-06364bd1c565`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `1925dd7d-626a-40b8-9203-06364bd1c565`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-aws-sdk-v3|n8n-nodes-aws-sdk-v3]] — type `n8n-nodes-aws-sdk-v3.AWSSDKWrapper` — node "CloudwatchGetQueryResults" (id `06e21541-7d17-47ea-b263-70bb265d08c4`)

### Data tables (n8n)

- [[../resources/data-tables/ftns17vqyzc0ci8m|Intrastructure Monitoring - API Calls]] (id `FTns17VQYzC0ci8m`) — op `get` — node "Get row(s)" (id `0ff13372-3281-4ed6-8550-b80988842bfc`)
- [[../resources/data-tables/ftns17vqyzc0ci8m|Intrastructure Monitoring - API Calls]] (id `FTns17VQYzC0ci8m`) — op `deleteRows` — node "Delete row(s)" (id `20eff393-c7f4-4b4c-b558-e3128e1a790a`)
- [[../resources/data-tables/ftns17vqyzc0ci8m|Intrastructure Monitoring - API Calls]] (id `FTns17VQYzC0ci8m`) — op `?` — node "Insert row" (id `d452d2a4-d260-46f5-8ef3-da3891f9798c`)
- [[../resources/data-tables/ftns17vqyzc0ci8m|Intrastructure Monitoring - API Calls]] (id `FTns17VQYzC0ci8m`) — op `rowNotExists` — node "If row does not exist" (id `e48c6423-6bfb-4efd-b1de-a9d7d09d1b3b`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
