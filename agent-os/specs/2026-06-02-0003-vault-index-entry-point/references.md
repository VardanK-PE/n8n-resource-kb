# References for vault/index.md

## Similar Implementations

### Workflow note template

- **Location:** `vault/_templates/workflow.md`
- **Relevance:** the index template follows the same skeleton — frontmatter, `<!-- auto:start -->` block with H1 + H2 sections, `<!-- manual:start -->` empty stub.
- **Key patterns to borrow:**
  - Section header style (`## Summary`, `## Triggers`, …)
  - Comment markers placed flush left, with blank lines on either side
  - Manual block contains an HTML comment explaining what goes there

### Resource note templates

- **Location:** `vault/_templates/resource-*.md`
- **Relevance:** confirms the convention that the auto block holds machine-generated content (reverse-lookup tables for resources, counts/links for the index) and the manual block holds free-form maintainer prose.

### Prior spec

- **Location:** `agent-os/specs/2026-06-01-1707-phase-1-mvp-vault-sync/`
- **Relevance:** establishes the spec-folder convention (`plan.md` + `shape.md` + `standards.md` + `references.md` + `visuals/`). This spec follows the same layout for discoverability.

## Standards that drive implementation

- `agent-os/standards/notes/auto-manual-blocks.md` — the guarded-block contract; load-bearing for the manual block surviving refresh.
- `agent-os/standards/notes/frontmatter-schema.md` — extended with the new `index` type.
- `agent-os/standards/sync/refresh-procedure.md` — gets Step 6.5 added.

## Repo-level pointers

- `CLAUDE.md` — the agent's intent-router. Updated to point at `vault/index.md` from both the Vault location and Where to read more sections.
- `vault/_cache/` — gitignored cache; counts are computed from disk (vault/workflows/, vault/resources/<type>/, vault/changelogs/), not from the cache, because the index reflects vault state, not n8n state.
