# Vault entry point (`vault/index.md`)

## Context

The vault under `./vault/` has no front door. Someone opening it in Obsidian (or Claude landing in it cold) gets dropped at the file tree with 202 workflow notes + 17 resource subdirectories + an empty changelogs folder and no narrative for how it's organized or how to navigate it. CLAUDE.md describes the layout for the agent, but the **vault itself** has no orientation note. We want a single `vault/index.md` that:

- Tells a human reader what this vault is and how it's structured
- Surfaces live counts per section (workflows, resources by type, changelogs)
- Wikilinks down into the top-level sections
- Survives refreshes via the standard auto/manual block contract
- Is referenced from `CLAUDE.md` so the agent always knows it exists

This is small surface area; the bulk of the work is wiring the new note type into the refresh procedure and frontmatter schema so it stays current without breaking the idempotency guarantee.

## Decisions (confirmed via /shape-spec)

| | |
|---|---|
| **Filename** | `vault/index.md` |
| **Scope** | Orient + navigate — section links, counts, how-to. No per-workflow enumeration. |
| **Lifecycle** | Auto + manual blocks. Refresh rewrites the auto block; manual block is hand-authored. |

---

## Task 1 — Save spec documentation

Create the spec folder with:

- **plan.md** — this plan, copied verbatim
- **shape.md** — the three decisions above, plus the questions that were asked and answered during `/shape-spec`
- **standards.md** — the relevant excerpts from `notes/auto-manual-blocks.md`, `notes/frontmatter-schema.md`, `sync/refresh-procedure.md`, `sync/changelog-format.md` (since we're touching all four)
- **references.md** — point at `vault/_templates/workflow.md` (template pattern), `agent-os/standards/sync/refresh-procedure.md` (where the new step lands), and the existing spec `agent-os/specs/2026-06-01-1707-phase-1-mvp-vault-sync/` (the convention this is following)
- `visuals/` — empty (no mockups)

## Task 2 — Define the `index` note type

### 2a. Add a template at `vault/_templates/index.md`

Mirror the layout of `vault/_templates/workflow.md`. Frontmatter is minimal — `type: index` + `auto_generated_at`. The auto block holds the orient/navigate sections; the manual block is an empty stub. Sections in the auto block:

- **About** — one paragraph, what this vault is. Static prose generated once per refresh from a fixed string.
- **Sections** — three groups:
  - `[[workflows]]` with count + a one-line description
  - `Resources` — one bullet per `vault/resources/<type>/` directory, each with its count, listed in alphabetical order so new categories surface automatically
  - `[[changelogs]]` with count
- **Last refreshed** — `auto_generated_at` timestamp restated in the body for human visibility.

The auto block must **not** enumerate individual workflows or resources (that's what the section folders already show in Obsidian's file explorer).

### 2b. Extend `agent-os/standards/notes/frontmatter-schema.md`

Add a short subsection for the new note type, after the changelog section:

```yaml
---
type: index             # the literal string "index"
auto_generated_at: 2026-06-02T00:03:00Z
---
```

Note that the index has exactly one canonical path (`vault/index.md`), so no name/slug field is needed. Mention that the index, like changelogs, has only the auto block driven by refresh — but unlike changelogs, it **does** carry a manual block (a place for hand-written orientation prose the maintainer wants visible on the front page).

## Task 3 — Wire index regeneration into the refresh procedure

Edit `agent-os/standards/sync/refresh-procedure.md`. Add a new **Step 6.5 — Update `vault/index.md`** between Step 6 (workflow-as-resource bidirectionality) and Step 7 (write the changelog). Spec for the step:

**Inputs:** the in-memory categorization from Step 3 (added / modified / removed / unchanged counts) plus a filesystem walk of `vault/resources/*/` to enumerate categories and counts.

**Computation:**

```sh
# Counts come from disk, not n8n state — index reflects the vault.
workflows=$(ls vault/workflows/*.md 2>/dev/null | wc -l | tr -d ' ')
for d in vault/resources/*/; do
  cat=$(basename "$d")
  cnt=$(ls "$d"*.md 2>/dev/null | wc -l | tr -d ' ')
  # …assemble into the auto block
done
changelogs=$(ls vault/changelogs/*.md 2>/dev/null | wc -l | tr -d ' ')
```

**Write rule** (mirrors Step 4f):

- If `vault/index.md` does not exist → `Write` the full file (frontmatter + auto block + empty manual stub).
- If it exists → `Read` it, capture the manual block verbatim, `Edit` the auto block region (exact-match `old_string`), then `Edit` the `auto_generated_at` frontmatter line. Never use `Write` on the existing file.

**Idempotency guard:** only update the index when **at least one** of the run's `added | modified | removed` counters is non-zero or a resource note was created/removed. If the run was a pure no-op, leave `vault/index.md` untouched — matches the existing rule "Running refresh twice in a row, with no n8n-side change, must produce zero file modifications."

## Task 4 — Reference the entry point from `CLAUDE.md`

Two edits in `CLAUDE.md`:

1. **`## Vault location` block** — add `vault/index.md` at the top of the bulleted layout list, with the line *"entry point: section overview, live counts, navigation links — refresh keeps the auto block current"*.
2. **`## Where to read more` block** — add `vault/index.md` as the first bullet, before `agent-os/product/...`, so the agent's first navigation hop into the vault is the index.

Do not introduce a new standards file — this is a pointer change, not a new contract. The contract lives in `notes/auto-manual-blocks.md` (already covers it) + the new index-type section added to `frontmatter-schema.md` in Task 2.

## Task 5 — Generate the initial `vault/index.md`

Refresh isn't running in this conversation, so produce the first version inline using the same algorithm Task 3 specs:

1. Enumerate `vault/workflows/*.md`, `vault/resources/*/*.md`, `vault/changelogs/*.md` via `ls` (excluding `.gitkeep`).
2. Render the auto block per the template from Task 2a.
3. `Write` the file (it does not yet exist — `Write` is the correct tool here, per the auto-manual-blocks contract).
4. Verify by re-reading the file and confirming the section counts match the `ls` output.

---

## Verification

End-to-end checks once tasks are executed:

- `ls vault/index.md` exists and is non-empty.
- `Read vault/index.md` shows: frontmatter with `type: index` + `auto_generated_at`; the auto block enumerates every directory under `vault/resources/` with a count that matches `ls vault/resources/<type>/*.md | wc -l`; an empty manual stub follows the auto block; markers are `<!-- auto:start --> … <!-- auto:end -->` and `<!-- manual:start --> … <!-- manual:end -->` exactly.
- `grep -n 'vault/index.md' CLAUDE.md` returns two hits (vault-location list + where-to-read-more list).
- Opening the vault in Obsidian and clicking `index.md` lands on a navigable page with working wikilinks into `workflows/`, each resource subfolder, and `changelogs/`.
- Dry-run the Task 3 idempotency rule on paper: a refresh with `added=0, modified=0, removed=0` must skip the index update. (No real refresh needed here — just confirm the spec text in `refresh-procedure.md` says so.)
- Add a manual line inside `<!-- manual:start --> … <!-- manual:end -->`, then mentally walk through Step 6.5: the manual line survives because `Edit` only replaces the auto-block region.
