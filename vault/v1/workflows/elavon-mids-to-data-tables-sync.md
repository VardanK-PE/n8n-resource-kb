---
n8n_id: "z06gndFj1h0pcspx"
instance: v1
name: "Elavon MIDs to Data Tables sync"
status: inactive
last_modified: 2026-03-16T18:08:34.761Z
tags: []
fingerprint: "0328e51cbd9ce99528bf67a808100ca9ee220c7b19988984cd5f8a6bab4730ac"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Elavon MIDs to Data Tables sync

## Summary

- **Status:** inactive
- **n8n ID:** `z06gndFj1h0pcspx`
- **Nodes:** 6
- **Last modified:** 2026-03-16T18:08:34.761Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `4c947195-74b7-4c46-805b-43936ec9c1d6`)
- **manual** — node "When clicking ‘Execute workflow’" (id `51406f51-66f4-405a-af39-81d759dc4b17`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `b3fb2875-d863-48ff-b7f2-140f71cfb7c9`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get row(s) in sheet" (id `b3fb2875-d863-48ff-b7f2-140f71cfb7c9`)

### Data tables (n8n)

- [[../resources/data-tables/eefxih6vfsgkmssi|Elavon - MIDs]] (id `EEFXIH6vFSgKmssi`) — op `upsert` — node "Upsert row(s)" (id `56e23460-b942-4a32-b554-6644b3e5808c`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
