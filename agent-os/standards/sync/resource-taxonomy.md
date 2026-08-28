# Standard: Resource Taxonomy (n8n node → vault resource mapping)

This standard defines how the refresh procedure converts each n8n node into one or more resource references. The taxonomy is **open**: when refresh encounters a node that yields a resource not listed here, it logs a `taxonomy_gap` in that day's changelog rather than dropping the data.

## v1 categories

| Category | Vault path |
|---|---|
| `credential` | `resources/credentials/` |
| `service` | `resources/services/` |
| `database` | `resources/databases/` |
| `trigger` | `resources/triggers/` |
| `llm-model` | `resources/llm-models/` |
| `http-url` | `resources/http-urls/` (host-grouped) |
| `env-var` | `resources/env-vars/` |
| `custom-node` | `resources/custom-nodes/` |
| `workflow` | `workflows/` (workflows are first-class resources; note dirs are all under `vault/<instance>/`) |

## v1 node-type → resource extraction rules

### HTTP

- **Node:** `n8n-nodes-base.httpRequest`
- **Resources emitted:**
  - `http-url`: parse the `url` parameter; group by host. Record the path + method in the body of the host note.
  - `credential` (if the node has a `credentials` reference)

### Databases

- **Nodes:** `n8n-nodes-base.postgres`, `n8n-nodes-base.mysql`, `n8n-nodes-base.mongodb`, `n8n-nodes-base.mssql`, `n8n-nodes-base.snowflake`, `n8n-nodes-base.redshift`, `n8n-nodes-base.questdb`, `n8n-nodes-base.timescaledb`
- **Resources emitted:**
  - `database`: keyed by `(engine, host, database)`. Body lists distinct tables (parsed from query / `table` param) and a representative query snippet.
  - `credential`

### Triggers

- **Nodes:**
  - `n8n-nodes-base.webhook` → `trigger` (type `webhook`), record `path` + HTTP method
  - `n8n-nodes-base.scheduleTrigger` / `.cronTrigger` → `trigger` (type `schedule`), record `cron_expression`
  - `n8n-nodes-base.emailReadImap`, `.errorTrigger`, `.executeWorkflowTrigger`, any `*Trigger` → `trigger` (type derived from node name)

### Sub-workflows

- **Node:** `n8n-nodes-base.executeWorkflow`
- **Resources emitted:**
  - `workflow` reference — link to the called workflow's note. Both sides receive entries:
    - The calling workflow's "Depends on → Workflows" lists the callee
    - The callee's "Used by → Workflows" lists the caller (with calling node name + ID)

### LLM models

- **Nodes:** any `@n8n/n8n-nodes-langchain.lm*`, `@n8n/n8n-nodes-langchain.embeddings*`, `@n8n/n8n-nodes-langchain.chatModel*`, `@n8n/n8n-nodes-langchain.openAi`, etc.
- **Resources emitted:**
  - `llm-model`: `(provider, model)` pair (e.g., `openai / gpt-4o`, `anthropic / claude-sonnet-4-6`). Keyed by `provider-model` slug.
  - `credential`

### Credentials (cross-cutting)

Any node that references a credential (via the `credentials` field on the node) emits a `credential` resource keyed by the credential name. The credential's note records its `credential_type`.

### Env vars (cross-cutting)

Scan every node parameter for `$env.X` expressions. Each unique `X` becomes an `env-var` resource. Use the `n8n-expression-syntax` skill for parsing when in doubt.

### Custom / community nodes

Any node whose `type` does **not** start with `n8n-nodes-base.` or `@n8n/` is a custom node. Emit a `custom-node` resource keyed by the npm package name (everything before the last `.` in `type`).

## Open-taxonomy rule

When refresh sees a node that:

- Has parameters or credentials it cannot map to one of the categories above, **or**
- Belongs to a known package but isn't matched by any rule

…it must:

1. Still record the node's basic info in the workflow note's auto block under a "Unmapped node references" sub-section.
2. Append a `taxonomy_gap` entry to that day's changelog, naming the node type and what was unmapped.
3. Never silently drop the data.

This is how the taxonomy grows: by reviewing changelog gaps and extending this file.

## Slugification rules for resource names

- `credentials`: use the credential name from n8n verbatim, slugified
- `http-url`: hostname, lowercased; e.g., `api.example.com` → `api-example-com`
- `database`: `<engine>-<host>-<database>` slugified
- `llm-model`: `<provider>-<model>` slugified
- `env-var`: variable name, slugified (preserve underscores → hyphens)
- `custom-node`: npm package name slugified

## Why "open" matters

n8n's node ecosystem expands constantly. A closed taxonomy would silently lose data the first time a new node type appears. Logging gaps in the changelog keeps the taxonomy honest and gives the maintainer one place to review what needs to be added.
