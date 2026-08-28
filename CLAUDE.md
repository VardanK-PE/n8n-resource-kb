# n8n-resources — Claude project router

This repository is a **Claude-driven, Obsidian-native knowledge base** for **two n8n instances** — `v1` (Old) and `v2` (New). The vault under `./vault/` is fully derived from the live instances (modulo manual annotations), kept in sync conversationally through this CLI. Each instance has its own isolated subtree (`vault/v1/`, `vault/v2/`); n8n workflow IDs are only unique within an instance, so the subtrees never share notes or cache. Every read, refresh, and lookup is scoped to an instance alias.

There is no service to deploy, no test suite to run, no build step. The "runtime" is Claude + two MCP servers (`n8n-mcp` for reading n8n, `obsidian` for reading/writing the vault). Your job, when the user gives an intent, is to dispatch to the right runbook in `agent-os/standards/`.

## Vault location

`./vault/` — co-located with this repo. `<INST>` is the instance alias (`v1` | `v2`). Layout:

- `vault/index.md` — **top-level router** (`type: index-router`): lists the instances and links to each per-instance index. Hand-maintained; refresh never regenerates it. Read this first when landing cold.
- `vault/<INST>/index.md` — per-instance **entry point**: section overview, live counts, navigation links for that instance. Refresh keeps its auto block current; the manual block holds hand-written orientation prose.
- `vault/<INST>/workflows/<slug>.md` — one note per n8n workflow in that instance
- `vault/<INST>/resources/<type>/<slug>.md` — one note per unique resource (credentials, services, databases, triggers, llm-models, http-urls, env-vars, custom-nodes)
- `vault/<INST>/changelogs/YYYY-MM-DD.md` — one note per refresh-day that produced change
- `vault/<INST>/_cache/` — gitignored per-instance cache of full workflow JSON (never read raw; see below)
- `vault/_templates/*.md` — shared, instance-agnostic reference templates Claude follows when writing notes (do **not** treat these as live notes)

## Intent → runbook map

| User says | Follow |
|---|---|
| "refresh the vault" / "sync n8n" / "update the vault" | `agent-os/standards/sync/refresh-procedure.md` |
| "what uses X?" / "what depends on X?" / "what touches X?" | `agent-os/standards/sync/reverse-lookup.md` |
| "what changed today?" / "show the changelog" | read `vault/<INST>/changelogs/` (most recent file); ask which instance if unscoped |
| Manual annotation request ("note that X is owned by …") | edit **only** between `<!-- manual:start -->` and `<!-- manual:end -->` markers on the target note — see `agent-os/standards/notes/auto-manual-blocks.md` |

When the intent is ambiguous, ask once. Don't refresh on a lookup-shaped question; don't lookup-and-stop when the user clearly asked for a refresh.

## Hard invariants

These are non-negotiable. Violating them corrupts the vault.

1. **Never hard-delete a workflow note.** When a workflow disappears from n8n, flip `status: deleted` in frontmatter and preserve the file (including its manual block). Hard-deletion loses manual annotations forever.
2. **Never write inside an auto block** except via the refresh procedure. The auto block is for refresh; manual edits must go in the manual block.
3. **Never use the `Write` tool on an existing vault note.** It overwrites the whole file and destroys the manual block. Use `Edit` instead — `old_string` must match the existing auto block (or specific frontmatter line) verbatim so the manual block is never in the replacement window.
4. **Never skip changelog generation when the refresh procedure produced semantic change.** The changelog *is* the audit trail; a missing entry makes Phase 1 useless.
5. **Never fabricate manual-block content.** If a manual block is missing on an existing note (corruption, hand-truncation), insert an **empty stub** and continue. Do not infer what the human might have written.
6. **Never expand the resource taxonomy silently.** When a node yields a resource that doesn't fit `agent-os/standards/sync/resource-taxonomy.md`, log a `taxonomy_gap` in the changelog. The maintainer extends the taxonomy file explicitly.

## Tools to use (and prefer)

- **n8n REST API** via the `scripts/n8n-api.sh <instance> <endpoint>` wrapper (`Bash` + `curl` + `jq`) — the source of truth for n8n state. **First arg is the instance alias** (`v1`|`v2`); the agent only ever passes the alias, never a URL or key. The wrapper validates the alias against an allowlist, then resolves that instance's auth from `.env` (`N8N_API_URL_V1`/`N8N_API_KEY_V1`, `N8N_API_URL_V2`/`N8N_API_KEY_V2`; v1 falls back to legacy unsuffixed vars + `../n8n_claude/.mcp.json`). Never source `.env` directly — it's hook-blocked. Endpoints: `GET /api/v1/workflows`, `GET /api/v1/workflows/{id}`. See `agent-os/standards/sync/refresh-procedure.md`.
- **`jq` programs under `scripts/jq/`** — every workflow-JSON extraction goes through these. Never inline complex `jq` in shell heredocs; compose pre-written scripts.
- Plain file I/O for the vault: `Read`, `Write` (new notes only), `Edit` (existing notes), `Bash` for enumeration (`ls`, `find`, `grep`)
- Skills already available in this environment for n8n knowledge: `n8n-mcp-tools-expert`, `n8n-node-configuration`, `n8n-workflow-patterns`, `n8n-expression-syntax`, `n8n-validation-expert`. Useful as **reference docs** when investigating an unfamiliar node — not a runtime dependency.

**Do not use the `mcp__obsidian__*` tools for this project's vault.** They are configured against a different on-disk vault in this environment. The manual-block contract is enforced through `Read` + `Edit` (exact-match `old_string` against the existing auto block) — see `agent-os/standards/sync/refresh-procedure.md`.

**Do not use the n8n-mcp MCP server** even if it's available — it's unstable on this instance. The REST API covers every Phase 1 need.

**Do not read raw workflow JSON into context.** n8n workflows can run hundreds of KB each. Per `agent-os/standards/sync/large-workflow-handling.md`: cache fetched workflows under `vault/<instance>/_cache/workflows/<id>.json` (gitignored, one cache per instance), then extract via `jq` programs. Never `Read` or `cat` a file under `vault/<instance>/_cache/workflows/` — always go through a `jq` query that returns only the small projection you need.

## Where to read more

- `vault/index.md` — the vault's front door; section counts + wikilinks. Open this first.
- Product context: `agent-os/product/{mission,roadmap,tech-stack}.md`
- Standards (authoritative spec for every operation):
  - `agent-os/standards/notes/auto-manual-blocks.md`
  - `agent-os/standards/notes/frontmatter-schema.md`
  - `agent-os/standards/sync/resource-taxonomy.md`
  - `agent-os/standards/sync/fingerprint.md`
  - `agent-os/standards/sync/refresh-procedure.md`
  - `agent-os/standards/sync/reverse-lookup.md`
  - `agent-os/standards/sync/changelog-format.md`
  - `agent-os/standards/sync/large-workflow-handling.md`
- `scripts/jq/*.jq` — reusable extraction programs that drive every workflow-JSON read
- Current spec: `agent-os/specs/2026-06-01-1707-phase-1-mvp-vault-sync/`
