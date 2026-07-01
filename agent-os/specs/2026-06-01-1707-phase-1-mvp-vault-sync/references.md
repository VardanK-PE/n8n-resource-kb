# References for Phase 1 MVP — n8n → Obsidian Vault Sync

This project has no prior in-repo implementation to mirror. The "reusable code" we depend on is tooling already exposed in the environment — not code in this repository.

## In-environment tooling (reuse — do not reimplement)

### n8n REST API

- **Role:** the n8n side of the sync engine. All workflow data flows through this.
- **Endpoints used:**
  - `GET /api/v1/workflows?limit=100&cursor=<nextCursor>` — paginated list
  - `GET /api/v1/workflows/{id}` — full workflow JSON
- **Auth:** `X-N8N-API-KEY: <token>` header. Token + base URL live in `./.env` (gitignored).
- **Why not n8n-mcp:** the n8n-mcp MCP server is unstable on this instance per the maintainer. The REST API is stable, documented, and covers every Phase 1 need (node introspection isn't required — workflow JSON already contains every `type` + `parameters` + `credentials`).

### `jq` programs under `scripts/jq/`

- **Role:** all workflow-JSON manipulation. Raw JSON is hundreds of KB per workflow and must never reach Claude's context.
- **Key scripts:** `canonical.jq` (fingerprint), `nodes-summary.jq`, `extract-{credentials,http-urls,triggers,subworkflows,databases,llm-models,env-vars,custom-nodes}.jq`.
- **Relevance:** without these, every refresh would blow through the context window on the first complex workflow. See `agent-os/standards/sync/large-workflow-handling.md`.

### n8n-mcp skill bundle (reference docs only, not runtime)

- `n8n-mcp-tools-expert`, `n8n-node-configuration`, `n8n-workflow-patterns`, `n8n-expression-syntax`, `n8n-validation-expert`
- **Use them when** investigating an unfamiliar node type during taxonomy extension. They explain node shape and parameter conventions.
- **Do not use them at runtime** — the runbook calls REST endpoints + `jq` programs only.

### Obsidian MCP server — **not used by this project**

The `mcp__obsidian__*` tools in this environment are configured against a different vault (`Data Model/`, `Technical/`, `Specs/` — 20 unrelated notes). This project's vault lives at `./vault/` in this repo and is accessed via plain file I/O (`Read`, `Write`, `Edit`, `Bash`).

The manual-annotation-preservation contract (capability 5) is enforced by:

- `Read` the existing note → capture the `<!-- manual:* -->` region verbatim
- `Edit` with exact-match `old_string` = the existing auto block including markers; `new_string` = the new auto block. The manual block is never in the edit window so it cannot be touched.
- `Write` only for brand-new notes. Never on an existing path.

## In-repo references

### `agent-os/product/roadmap.md`

- **Relevance:** authoritative source for the 5-capability scope. All implementation tasks trace back to a numbered roadmap item.

### `agent-os/product/mission.md`

- **Relevance:** describes the user intents the vault must answer ("which workflows use X?", "what does Y touch?", impact analysis, incident response). Drives the design of CLAUDE.md's intent router.

### `agent-os/product/tech-stack.md`

- **Relevance:** confirms there is no separate runtime. Justifies the conversational-only invocation model — the "sync engine" is Claude + MCP tools, not a service.
