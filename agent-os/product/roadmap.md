# Product Roadmap

## Phase 1: MVP

The first usable version is the smallest thing that answers "which workflows use X?" and "what does workflow Y touch?" with node-level precision, refreshable on demand.

### MVP capabilities

1. **Workflow inventory + resource extraction.** Pull all workflows from the n8n instance via the n8n REST API. Generate one Obsidian note per workflow (`workflows/<workflow-name>.md`) with:
   - Frontmatter: `n8n_id`, `name`, `status` (active/inactive), `last_modified`, `tags`, `fingerprint` (hash used for change detection).
   - Body: a structured list of every resource the workflow uses, grouped by type. Each entry records the **node name and node ID** that uses it. When multiple nodes use the same resource inside a workflow, all of them are listed.

2. **Resource pages with reverse lookup.** Generate one note per unique resource, organized by type:
   - `resources/credentials/<name>.md`
   - `resources/services/<name>.md`
   - `resources/databases/<name>.md` (with tables/queries surfaced underneath)
   - `resources/triggers/<name>.md` (webhooks, schedules)
   - `resources/llm-models/<name>.md`
   - `resources/http-urls/<host-or-url>.md`
   - `resources/env-vars/<name>.md`
   - `resources/custom-nodes/<name>.md`

   Each resource note lists every `(workflow, node-name, node-id)` triple that uses it — answering "what breaks if I rotate / change / remove this?"

3. **Workflows-as-resources.** Workflow notes themselves act as their own "resource pages": each carries a reverse-lookup section listing every other workflow whose Execute-Workflow node calls it, with the calling node's name + ID. Sub-workflow dependencies are bidirectional in the vault.

4. **Refresh + structured changelog.** A Claude-driven, on-demand refresh that:
   - Fetches current workflow state from n8n (via `n8n-mcp` tools).
   - Compares against the per-workflow fingerprint stored in the existing note's frontmatter.
   - Writes a dated changelog note (`changelogs/YYYY-MM-DD.md`) describing what changed in human terms — e.g. "added HTTP node `Get Customer` targeting `api.example.com`", "schedule changed from `0 * * * *` to `0 9 * * *`", "removed credential `hubspot-prod`".
   - Updates the affected workflow and resource notes in place.

5. **Manual annotations preserved.** Each note has a clearly marked auto-generated block and a manual-annotation block. Refresh rewrites only the auto block; human-authored fields (owner, criticality, runbook URL, business purpose, free-form notes) survive every refresh.

### Resource taxonomy for v1

- Credentials & external services
- Databases, tables & queries
- Triggers: webhooks, schedules, event triggers
- Workflows (as sub-workflow dependencies via Execute Workflow)
- LLM models (with model name + provider)
- HTTP request URLs (grouped by host)
- Environment variables & n8n static data
- Custom / community nodes

Taxonomy is **open**: when refresh encounters a node type that produces a resource not in the taxonomy, it is flagged in the changelog so the taxonomy can grow.

## Phase 2: Post-Launch

Candidates for after MVP — not committed, to be re-prioritized once the vault is in real use:

- **Scheduled sync** (cron) alongside the on-demand refresh, for unattended freshness.
- **Full workflow JSON snapshots** stored in `snapshots/` for forensic diffing between any two points in time (beyond the structured changelog).
- **Dashboards & query views** — generated index/dashboard notes like "all workflows touching production credentials", "workflows by criticality", "stale workflows" (using Dataview or generated markdown indexes).
- **Multi-environment support** — distinguish workflows across dev / staging / prod n8n instances in the same vault.
- **Ownership & criticality classification** — surfaced in changelog priority and dashboards.
- **Webhook-based push refresh** — if n8n can be wired to ping a refresh endpoint on save, replace polling with push.
- **Cross-instance dedup** — when the same logical credential / service exists across environments, link the per-env resource notes to a shared concept page.
