# Phase 1 MVP — Shaping Notes

## Scope

Deliver all five Phase 1 / MVP capabilities from `agent-os/product/roadmap.md` in a single spec:

1. **Workflow inventory + resource extraction** — one note per workflow in `vault/workflows/<name>.md` with frontmatter (`n8n_id`, `name`, `status`, `last_modified`, `tags`, `fingerprint`) and a structured body listing every resource the workflow uses, each tagged with the node name **and** node ID.
2. **Resource pages with reverse lookup** — one note per unique resource under `vault/resources/<type>/<name>.md`. Each lists every `(workflow, node-name, node-id)` triple that touches it.
3. **Workflows-as-resources** — workflow notes themselves carry a reverse-lookup section listing every other workflow that calls them via Execute-Workflow. Sub-workflow dependencies are bidirectional.
4. **Refresh + structured changelog** — on-demand refresh that fetches current n8n state, diffs against the stored per-workflow fingerprint, rewrites only the auto block, and emits `vault/changelogs/YYYY-MM-DD.md` describing changes in human terms.
5. **Manual annotations preserved** — every note has an auto-generated block and a manual-annotation block. Refresh only rewrites the auto block; human-authored content survives every refresh.

## Decisions

- **One spec covers all 5 capabilities.** They are tightly coupled (resource notes depend on workflow extraction; changelog depends on fingerprint; manual-block contract spans every note type) — splitting them would require duplicate scaffolding.
- **Vault lives inside the repo at `./vault/`.** Co-located with `agent-os/` so git history captures both auto-generated state and manual annotations together.
- **n8n-mcp is treated as already configured.** No setup task — plan assumes the MCP server is wired and authenticated.
- **Conversational invocation only.** No slash commands, no skills, no settings hooks. Behavior is captured in `CLAUDE.md` (intent router) and runbook files under `agent-os/standards/sync/`. The user just talks to Claude; Claude routes the intent.
- **Standards are the durable spec.** Templates and `CLAUDE.md` reference them rather than duplicating their content. Anything load-bearing — frontmatter shape, fingerprint algorithm, taxonomy mapping, refresh procedure — lives once, under `agent-os/standards/`.
- **Workflow notes are never hard-deleted.** When a workflow disappears from n8n, the note's status becomes `deleted` but the file (and any manual annotations) survives. Manual blocks are the source of truth for human context and must never be clobbered.
- **Open taxonomy.** When refresh encounters a node yielding a resource not in `sync/resource-taxonomy.md`, it is flagged as a `taxonomy_gap` in that day's changelog rather than silently dropped.

## Context

- **Visuals:** None. Output shape is markdown notes; no UI mockups needed.
- **References:**
  - `agent-os/product/mission.md` — the "why" (impact analysis, incident response, audits)
  - `agent-os/product/roadmap.md` — the 5-capability MVP scope
  - `agent-os/product/tech-stack.md` — confirms no traditional runtime; sync is conversational via MCP tools
  - **No prior implementation** — greenfield. The codebase contains only product docs and the agent-os scaffolding.
- **Product alignment:** Plan implements Phase 1 exactly as defined in the roadmap; nothing from Phase 2 (scheduled sync, full JSON snapshots, dashboards, multi-env, ownership, push refresh, cross-instance dedup) is in scope.

## Standards Applied

- `notes/auto-manual-blocks` — every note in the vault has guarded auto/manual sections; this is the contract that protects manual annotations across refreshes
- `notes/frontmatter-schema` — uniform frontmatter shape so refresh/diff/lookup operations work consistently across workflow and resource notes
- `sync/resource-taxonomy` — defines the v1 node-type → resource-category mapping and the open-taxonomy rule
- `sync/fingerprint` — stable per-workflow hash used for change detection
- `sync/refresh-procedure` — end-to-end runbook for "refresh the vault"
- `sync/reverse-lookup` — runbook for "what uses X?" intents
- `sync/changelog-format` — required structure for `changelogs/YYYY-MM-DD.md` notes
