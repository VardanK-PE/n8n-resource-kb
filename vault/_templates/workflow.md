---
n8n_id: "<n8n workflow id>"
name: "<human-readable workflow name>"
status: active            # active | inactive | deleted
last_modified: 2026-01-01T00:00:00Z
tags: []
fingerprint: "<sha-256 hex; see agent-os/standards/sync/fingerprint.md>"
auto_generated_at: 2026-01-01T00:00:00Z
---

<!-- auto:start -->

# <workflow name>

## Summary

- **Status:** active
- **Node count:** N
- **Last modified (n8n):** 2026-01-01T00:00:00Z

## Triggers

- [[../resources/triggers/<slug>]] — type `<webhook|schedule|…>`, node "<node name>" (id `<node-id>`)

## Depends on

### Credentials

- [[../resources/credentials/<slug>]] — node "<node name>" (id `<node-id>`)

### Services

- [[../resources/services/<slug>]] — node "<node name>" (id `<node-id>`)

### Databases

- [[../resources/databases/<slug>]] — node "<node name>" (id `<node-id>`); tables: `<t1>, <t2>`

### LLM models

- [[../resources/llm-models/<slug>]] — node "<node name>" (id `<node-id>`)

### HTTP URLs

- [[../resources/http-urls/<host-slug>]] — node "<node name>" (id `<node-id>`); path `<method> <path>`

### Env vars

- [[../resources/env-vars/<slug>]] — node "<node name>" (id `<node-id>`)

### Custom nodes

- [[../resources/custom-nodes/<slug>]] — node "<node name>" (id `<node-id>`)

### Workflows (sub-workflow calls)

- [[<workflow-slug>]] — node "<Execute Workflow node name>" (id `<node-id>`)

## Used by (workflows)

- [[<calling-workflow-slug>]] — node "<calling Execute Workflow node name>" (id `<node-id>`)

## Unmapped node references

(only populated when a node yields a resource not covered by sync/resource-taxonomy.md)

- Node type `<n8n type string>`, node "<node name>" (id `<node-id>`) — <what was unmapped>

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
