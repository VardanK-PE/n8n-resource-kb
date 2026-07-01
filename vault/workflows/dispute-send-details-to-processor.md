---
n8n_id: "HkjjRt4gR01DJ4tH"
name: "Dispute - Send details to processor"
status: inactive
last_modified: 2026-01-05T19:55:15.162Z
tags: []
fingerprint: "3895f3740c126d276b7e52cb8c496fcb006f84c99199f646980f7e502750e267"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Dispute - Send details to processor

## Summary

- **Status:** inactive
- **n8n ID:** `HkjjRt4gR01DJ4tH`
- **Nodes:** 35
- **Last modified:** 2026-01-05T19:55:15.162Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `1c8ca858-e96a-454b-92a5-6ebea0f1225f`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `65023f73-ced8-45df-996e-778f6abb63b3`)

## Depends on

### Credentials

- [[../resources/credentials/mla6ntr86w0mqqdf|PE AWS Account (Prod)]] (`aws`, id `mLa6NtR86w0mqQDF`) — node "Download a file3" (id `73800768-45fc-4d36-aaab-7fa40e01aa2c`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `7a4e19df-aec5-4a1d-b1d6-367cfa7a63f0`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `7a4e19df-aec5-4a1d-b1d6-367cfa7a63f0`)

### Data tables (n8n)

- [[../resources/data-tables/nkrufqkkpszwq07b|Dispute - Awaiting Processor Response]] (id `NkRUfQkkpsZWq07b`) — op `get` — node "Get row(s)" (id `5a8a504b-8e97-407e-bd18-174fa78d0cef`)
- [[../resources/data-tables/nkrufqkkpszwq07b|Dispute - Awaiting Processor Response]] (id `NkRUfQkkpsZWq07b`) — op `rowNotExists` — node "If row does not exist" (id `756811dd-9ba3-48bd-a265-dfd49335c791`)
- [[../resources/data-tables/nkrufqkkpszwq07b|Dispute - Awaiting Processor Response]] (id `NkRUfQkkpsZWq07b`) — op `get` — node "Get row(s)1" (id `a12d9b22-0762-4c44-8443-b2a6c028e385`)
- [[../resources/data-tables/nkrufqkkpszwq07b|Dispute - Awaiting Processor Response]] (id `NkRUfQkkpsZWq07b`) — op `upsert` — node "Upsert row(s)" (id `a8901de3-4d90-4ec2-b004-91b206b36352`)
- [[../resources/data-tables/nkrufqkkpszwq07b|Dispute - Awaiting Processor Response]] (id `NkRUfQkkpsZWq07b`) — op `update` — node "Update row(s)" (id `eea2f7ed-eb4b-409e-8b05-e1db89e97e43`)

### AWS S3 buckets

- *(dynamic bucket)* — op `?` — node "Download a file3" (id `73800768-45fc-4d36-aaab-7fa40e01aa2c`)

### Sub-workflows (Execute Workflow calls)

- [[send-email-html|Send Email: HTML]] (n8n_id `H9qPciXCz00KxAyF`) — node "Call 'Send Email: HTML'" (id `32d9eda0-dac1-4143-a797-d25c1bbffd92`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Create a base message1" (id `3a471b15-f3d8-4f5e-9541-2c9a605fbc4d`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'2" (id `668993d5-da75-4ecd-afd6-d8fe1809b99d`)

## Used by (workflows)

- [[dispute-main-processor|Dispute - Main Processor]] — node "Call 'Dispute - Send details to processor'" (id `0d7ccc15-22c8-4372-96ab-cebf4c59e29a`)
- [[dispute-main-processor|Dispute - Main Processor]] — node "Call 'Dispute - Send details to processor'1" (id `188f2c51-021b-48c6-ba2b-d440ba0b40d4`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
