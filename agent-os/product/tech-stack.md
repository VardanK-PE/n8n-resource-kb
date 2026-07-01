# Tech Stack

This product has no traditional frontend/backend split. It is a **knowledge base composed of markdown files**, with sync driven by an existing CLI assistant (Claude Code) talking to the n8n REST API and writing markdown directly.

## Storage / "Frontend"

- **Obsidian vault** — local markdown files with YAML frontmatter and `[[wikilinks]]`. Obsidian itself is the human browsing UI.
- **File layout**:
  - `workflows/<workflow-name>.md` — one note per n8n workflow.
  - `resources/<type>/<resource-name>.md` — one note per unique resource (credentials, services, databases, llm-models, http-urls, triggers, env-vars, custom-nodes).
  - `changelogs/YYYY-MM-DD.md` — one note per refresh date describing what changed.
- **Note structure**: every note has an auto-generated block (rewritten on refresh) and a manual-annotation block (never touched by refresh), separated by explicit markers.

## Data Source / "Backend"

- **n8n instance** — REST API is the source of truth. The vault is fully derived from it (modulo manual annotations).
- No separate backing database. Workflow state, resource extraction, and change detection are computed at refresh time.

## Sync Engine

- **Claude Code** (this CLI) is the sync engine. There is no standalone service to deploy. Refresh runs on-demand when the user triggers it through Claude.
- **Tooling used**:
  - **n8n REST API** via `curl` + `jq` — the source of truth for n8n state. Auth from `.env` (`N8N_API_URL`, `N8N_API_KEY`). Endpoints: `GET /api/v1/workflows`, `GET /api/v1/workflows/{id}`.
  - **`jq` programs under `scripts/jq/`** — every workflow-JSON extraction goes through these pre-written scripts rather than inline `jq`. Full workflow JSON is cached under `vault/_cache/workflows/<id>.json` (gitignored) and read only through `jq` projections, never loaded whole into context.
  - **Plain file I/O** — `Read` for existing notes, `Write` for new notes, and `Edit` (exact-match against the auto block) for updates, so the manual-annotation block is never clobbered.
- **Not used at runtime**: the `n8n-mcp` MCP server (unstable on this instance) and the `obsidian` MCP server (points at an unrelated vault). The n8n-focused skills (`n8n-mcp-tools-expert`, `n8n-node-configuration`, `n8n-workflow-patterns`, `n8n-expression-syntax`, `n8n-validation-expert`) remain useful as **reference docs** when investigating an unfamiliar node.

## Change Detection

- **Per-workflow fingerprint** stored in the workflow note's frontmatter. Includes:
  - `last_modified` from n8n
  - A stable hash over the node list, connection topology, and per-node resource references (credentials, URLs, queries, etc.)
- On refresh, the engine compares the current n8n fingerprint against the one in the note. If they differ, the auto block is regenerated and a changelog entry is written.
- **No full JSON snapshots in MVP** — fingerprint + diff-to-prior-state is sufficient for structured changelog generation.

## Database

N/A — there is no database. The vault and the live n8n instance together hold all state.

## Other

- **git** — this repo is the durability layer, giving history of both auto-generated content and manual annotations. The vault, tooling, and docs are tracked; credentials, `.mcp.json`, and `vault/_cache/` are gitignored (see `.gitignore` and `README.md`).
- **No CI/CD** for this product itself; refresh is interactive.
