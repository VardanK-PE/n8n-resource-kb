# Vault entry point — Shaping Notes

## Scope

Add a single orientation note at `vault/index.md` that serves as the vault's "front door": a short prose intro, live section counts, and wikilinks into `workflows/`, every `resources/<type>/`, and `changelogs/`. It is *not* a per-workflow catalog — Obsidian's file explorer already shows that.

The note participates in the same auto / manual block contract every other vault note follows, so refresh keeps the counts and timestamp current while the maintainer can edit orientation prose without fear of being clobbered.

## Decisions

| Decision | Choice | Why |
|---|---|---|
| Filename | `vault/index.md` | User-chosen (overrode the `Home.md` default mid-conversation). Lowercase + web-style; sits alongside `_templates/`, `_cache/`, etc. |
| Scope | Orient + navigate (sections + counts + how-to) | Full catalog is redundant with Obsidian's file tree and would balloon the file every refresh. Counts are the highest-value live data. |
| Lifecycle | Auto + manual blocks | Matches the existing contract — counts/timestamps must be machine-refreshed, but the maintainer wants a place for hand-written guidance on the front page. |
| Idempotency | Skip update when the run had no semantic change | Required to preserve "two refreshes in a row produce zero file modifications" from `sync/refresh-procedure.md`. |
| Refresh integration | New Step 6.5 in `sync/refresh-procedure.md` (between bidirectionality reconciliation and changelog write) | Index reflects the *post-reconciliation* vault state, so it has to run after Steps 5 + 6. It precedes Step 7 because we want the index updated even if the changelog is being written. |
| Frontmatter | `type: index` + `auto_generated_at` only | The note has exactly one canonical path — no name/slug field needed. |

## /shape-spec Q&A

**Q: What should the vault entry point primarily be?**
→ Orient + navigate. (Not a full catalog; not catalog-only.)

**Q: How should the entry point stay current?**
→ Auto + manual blocks — same contract as every other vault note.

**Q: What should the entry point file be called?**
→ Originally `Home.md`; user followed up with "make it `vault/index.md`" before plan finalization.

## Context

- **Visuals:** None. Markdown-only output; the auto-block sketch in the shape-spec preview is already in the plan.
- **References:**
  - `vault/_templates/workflow.md` — template pattern this index template follows.
  - `agent-os/standards/notes/auto-manual-blocks.md` — the contract.
  - `agent-os/standards/notes/frontmatter-schema.md` — where the new `index` type slots in.
  - `agent-os/standards/sync/refresh-procedure.md` — where Step 6.5 lands.
  - `agent-os/specs/2026-06-01-1707-phase-1-mvp-vault-sync/` — prior spec; the convention this one follows.
- **Product alignment:** Implements the navigation/discoverability surface implied by Phase 1's "the vault is the UI; Obsidian is the browser" line in `agent-os/product/mission.md`. Does not touch the Phase 2 dashboards work (that would be the full-catalog option we explicitly rejected).

## Standards Applied

- `notes/auto-manual-blocks` — index uses the standard guarded-block layout
- `notes/frontmatter-schema` — extended with the new `index` note type
- `sync/refresh-procedure` — new Step 6.5 added; idempotency guard preserved
- `sync/changelog-format` — *not* modified; the index is not a changelog and refresh's existing "any change? then write changelog" rule already covers the cases that would trigger an index update
