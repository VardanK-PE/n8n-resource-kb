# Tech Stack

This product has no traditional frontend/backend split. It is a **knowledge base composed of markdown files**, with sync driven by an existing CLI assistant (Claude Code) talking to two MCP servers.

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
- **MCP tools used**:
  - `n8n-mcp` — fetches workflow definitions, schemas, and metadata from the n8n instance. Skills already present in this environment: `n8n-mcp-tools-expert`, `n8n-node-configuration`, `n8n-workflow-patterns`, `n8n-expression-syntax`, `n8n-validation-expert`.
  - `obsidian` MCP — reads, writes, lists, and searches notes in the vault (`mcp__obsidian__read_note`, `write_note`, `patch_note`, `search_notes`, `list_directory`, `get_frontmatter`, `update_frontmatter`, etc.).

## Change Detection

- **Per-workflow fingerprint** stored in the workflow note's frontmatter. Includes:
  - `last_modified` from n8n
  - A stable hash over the node list, connection topology, and per-node resource references (credentials, URLs, queries, etc.)
- On refresh, the engine compares the current n8n fingerprint against the one in the note. If they differ, the auto block is regenerated and a changelog entry is written.
- **No full JSON snapshots in MVP** — fingerprint + diff-to-prior-state is sufficient for structured changelog generation.

## Database

N/A — there is no database. The vault and the live n8n instance together hold all state.

## Other

- **Optional git** — committing the vault gives durable history of both auto-generated content and manual annotations. Recommended but not required.
- **No CI/CD** for this product itself; refresh is interactive.
