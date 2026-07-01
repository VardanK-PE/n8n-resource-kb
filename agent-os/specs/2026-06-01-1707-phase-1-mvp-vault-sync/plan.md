# Phase 1 MVP — n8n → Obsidian Vault Sync

## Context

The `n8n-resources` project exists today as product docs only (`agent-os/product/{mission,roadmap,tech-stack}.md`) with no implementation, no `CLAUDE.md`, and no vault. Phase 1 of the roadmap defines a 5-capability MVP that turns the n8n instance into a Claude-driven, Obsidian-native knowledge base with node-level resource reverse-lookup, structured changelogs, and preserved manual annotations.

This plan delivers all five capabilities in one spec:

1. Workflow inventory + resource extraction (`workflows/<name>.md`)
2. Resource pages with reverse lookup (`resources/<type>/<name>.md`)
3. Workflows-as-resources (bidirectional Execute-Workflow dependencies)
4. Refresh + structured changelog (fingerprint diffing → `changelogs/YYYY-MM-DD.md`)
5. Manual annotations preserved (auto/manual guarded blocks)

**Confirmed constraints (from shaping):**
- All 5 capabilities, one spec
- Vault lives **in the same repo** at `./vault/` so it can be git-committed alongside `agent-os/`
- `n8n-mcp` MCP server is already configured and authenticated
- **Conversational invocation only** — no new slash commands, no new skills. All behavior lives in `CLAUDE.md` + referenced runbooks under `agent-os/standards/sync/`

**Why this shape:** there is no traditional runtime to build. The "implementation" is templates + procedures + a router (`CLAUDE.md`) that Claude follows when the user asks to refresh, lookup, or annotate. The n8n-mcp + obsidian MCP tools (already exposed in this environment) are the engine.

---

## Spec folder

`agent-os/specs/2026-06-01-1707-phase-1-mvp-vault-sync/`

---

## Task 1 — Save spec documentation

Create the spec folder with:

- `plan.md` — copy of this plan
- `shape.md` — scope (all 5 caps), decisions (vault in-repo, conversational only, n8n-mcp pre-configured), references (`agent-os/product/*.md`)
- `standards.md` — links to the standards created in Task 2 (with brief rationale per standard)
- `references.md` — points at the existing n8n-mcp skills (`n8n-mcp-tools-expert`, `n8n-node-configuration`, `n8n-workflow-patterns`, `n8n-validation-expert`, `n8n-expression-syntax`) and obsidian MCP tools as the primary "code" we reuse rather than re-implement
- `visuals/` — empty (no mockups for this work)

---

## Task 2 — Author standards (the source-of-truth for note shape and sync behavior)

These files are the durable specification. Templates and CLAUDE.md reference them. Create under `agent-os/standards/`:

- **`notes/auto-manual-blocks.md`** — defines the guarded-block markers (`<!-- auto:start --> … <!-- auto:end -->` and `<!-- manual:start --> … <!-- manual:end -->`), the invariant that refresh **only rewrites the auto block**, and the conflict-resolution rule when a manual block is missing (insert empty stub).
- **`notes/frontmatter-schema.md`** — YAML frontmatter shape for each note type:
  - Workflow: `n8n_id`, `name`, `status`, `last_modified`, `tags`, `fingerprint`, `auto_generated_at`
  - Resource: `type`, `name`, `auto_generated_at`, plus type-specific keys (e.g., `host` for http-url, `provider` + `model` for llm-model)
  - Changelog: `date`, `workflows_changed`, `resources_added`, `resources_removed`
- **`sync/resource-taxonomy.md`** — the canonical n8n-node-type → resource-category mapping for v1, plus the **open-taxonomy rule**: when a node yields a resource not in the mapping, emit a `taxonomy_gap` entry in the changelog. Minimum coverage:
  - `n8n-nodes-base.httpRequest` → `http-urls` (host-grouped) + `credentials`
  - `n8n-nodes-base.postgres` / `.mysql` / `.mongodb` → `databases` (with tables/queries listed) + `credentials`
  - `n8n-nodes-base.webhook` / `.scheduleTrigger` / `.cronTrigger` → `triggers`
  - `n8n-nodes-base.executeWorkflow` → `workflows` (bidirectional link)
  - `@n8n/n8n-nodes-langchain.lmChat*` and other LLM nodes → `llm-models` + `credentials`
  - Any credential reference on any node → `credentials`
  - `$env.*` expression references → `env-vars`
  - Community / custom node packages → `custom-nodes`
- **`sync/fingerprint.md`** — fingerprint algorithm. Stable hash (SHA-256, hex) over a canonical JSON containing: ordered `[(node_id, node_type, parameters_excluding_position)]`, ordered `connections`, and the per-node extracted resource references. Excludes `position`, `notesInFlow`, UI-only fields. Lives in workflow frontmatter as `fingerprint`.
- **`sync/refresh-procedure.md`** — step-by-step runbook Claude follows on "refresh the vault" / "sync n8n":
  1. List workflows via `n8n-mcp` (n8n_list_workflows or equivalent)
  2. For each workflow: fetch full definition, compute fingerprint, compare with note's stored fingerprint
  3. If new → create workflow note + emit resource references + update resource notes
  4. If changed → diff resources (added/removed), rewrite auto block (preserve manual block via `mcp__obsidian__patch_note`), update affected resource notes, append entry to today's changelog
  5. If deleted in n8n → mark workflow note `status: deleted` (do not hard-delete; preserve manual annotations); update reverse-lookups
  6. End-of-run: write `changelogs/YYYY-MM-DD.md` summarizing all changes in human terms ("added HTTP node 'Get Customer' targeting api.example.com", "schedule changed from `0 * * * *` to `0 9 * * *`")
- **`sync/reverse-lookup.md`** — runbook for "what uses X?" intents. Uses `mcp__obsidian__read_note` on the resource page (or `search_notes` if the resource name is partial) and returns the `(workflow, node-name, node-id)` triples from its auto block.
- **`sync/changelog-format.md`** — required sections per changelog note (Added workflows, Modified workflows, Removed workflows, Resource diffs, Taxonomy gaps) and the human-language rules for diff descriptions.

Also extend `agent-os/standards/index.yml` to register the above.

---

## Task 3 — Create vault skeleton + note templates

Create the directory structure inside the repo:

```
vault/
├── workflows/.gitkeep
├── resources/
│   ├── credentials/.gitkeep
│   ├── services/.gitkeep
│   ├── databases/.gitkeep
│   ├── triggers/.gitkeep
│   ├── llm-models/.gitkeep
│   ├── http-urls/.gitkeep
│   ├── env-vars/.gitkeep
│   └── custom-nodes/.gitkeep
├── changelogs/.gitkeep
└── _templates/
    ├── workflow.md
    ├── resource-credential.md
    ├── resource-service.md
    ├── resource-database.md
    ├── resource-trigger.md
    ├── resource-llm-model.md
    ├── resource-http-url.md
    ├── resource-env-var.md
    ├── resource-custom-node.md
    └── changelog.md
```

Each template embeds:
- The frontmatter shape from `notes/frontmatter-schema.md`
- The auto/manual marker pair from `notes/auto-manual-blocks.md`
- For workflow + resource templates: an "Used by" / "Depends on" reverse-lookup section in the auto block (workflow notes have **both** sections, since workflows are themselves resources)

Templates are read-only references that the runbook in Task 2 instructs Claude to follow when writing notes — not executed by code.

---

## Task 4 — Author `CLAUDE.md` router

Create `CLAUDE.md` at repo root. Keep it short — it's an intent router, not a procedure dump. Content:

- Project purpose (1 paragraph, derived from `mission.md`)
- Vault location (`./vault/`)
- **Intent → runbook map**:
  - "refresh / sync / update the vault" → follow `agent-os/standards/sync/refresh-procedure.md`
  - "what uses / what depends on / what touches <X>" → follow `agent-os/standards/sync/reverse-lookup.md`
  - "what changed today / show changelog" → read `vault/changelogs/`
  - Manual annotation → only edit between `<!-- manual:start -->` / `<!-- manual:end -->` markers; never inside auto blocks
- Hard invariants: never hard-delete a workflow note; never write inside auto blocks except via the refresh procedure; preserve frontmatter ordering; always run the full refresh procedure end-to-end (don't skip changelog generation)
- Pointer to the n8n-mcp skills already available in this environment (so Claude uses `n8n-mcp-tools-expert` etc. for node-shape questions rather than guessing)

---

## Task 5 — End-to-end smoke run + seed the vault

Run the conversational refresh once against the live n8n instance to verify the pipeline:

1. Ask Claude to "refresh the vault" — should produce `workflows/*.md`, `resources/<type>/*.md`, and `changelogs/2026-06-01.md`
2. Spot-check a workflow note: frontmatter complete, fingerprint present, resources listed with node name + node ID, auto/manual blocks both present
3. Spot-check a resource note: reverse-lookup lists every `(workflow, node)` that uses it
4. Spot-check a sub-workflow note: "Used by" section lists Execute-Workflow callers
5. Add a manual annotation to one workflow note (owner, criticality) inside the `<!-- manual:* -->` block
6. Make a trivial change to that workflow in n8n (e.g., toggle a node), refresh again, confirm: (a) the manual annotation survives, (b) the changelog describes the change in human terms, (c) the fingerprint updated
7. Capture any taxonomy gaps surfaced by the run as follow-up items

This is the only "executable" task in the plan — everything before it is authoring durable artifacts.

---

## Critical files to create

| Path | Role |
|---|---|
| `CLAUDE.md` | Intent router |
| `agent-os/standards/notes/auto-manual-blocks.md` | Guarded-block contract |
| `agent-os/standards/notes/frontmatter-schema.md` | Frontmatter shape |
| `agent-os/standards/sync/resource-taxonomy.md` | Node-type → resource mapping |
| `agent-os/standards/sync/fingerprint.md` | Change-detection hash |
| `agent-os/standards/sync/refresh-procedure.md` | Full refresh runbook |
| `agent-os/standards/sync/reverse-lookup.md` | "What uses X?" runbook |
| `agent-os/standards/sync/changelog-format.md` | Changelog note shape |
| `agent-os/standards/index.yml` | Register the above |
| `vault/_templates/*.md` | Per-note-type templates |
| `vault/{workflows,resources/*,changelogs}/.gitkeep` | Directory skeleton |
| `agent-os/specs/2026-06-01-1707-phase-1-mvp-vault-sync/{plan,shape,standards,references}.md` | Spec record |

## Reusable tooling (don't reimplement)

- `n8n-mcp` MCP tools — workflow fetch, node introspection (already configured)
- Skills already loaded: `n8n-mcp-tools-expert`, `n8n-node-configuration`, `n8n-workflow-patterns`, `n8n-validation-expert`, `n8n-expression-syntax` — reference these from the refresh runbook for node-shape questions
- `mcp__obsidian__*` tools — `write_note`, `patch_note` (critical for preserving manual blocks), `read_note`, `search_notes`, `list_directory`, `get_frontmatter`, `update_frontmatter`

## Verification

- After Task 5: `vault/workflows/`, `vault/resources/*/`, and `vault/changelogs/2026-06-01.md` are populated
- Manual annotation survives a second refresh (the core contract of Phase 1)
- Resource note reverse-lookup lists at least one `(workflow, node-name, node-id)` triple
- A sub-workflow note shows bidirectional dependency (both "Depends on" and "Used by")
- Re-running refresh on an unchanged instance produces **no** changelog entry (fingerprint stability)
