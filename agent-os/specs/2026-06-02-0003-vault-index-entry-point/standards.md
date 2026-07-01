# Standards for vault/index.md

The following standards apply to this work. Excerpts and notes below; canonical text lives in the linked files.

---

## notes/auto-manual-blocks

**File:** `agent-os/standards/notes/auto-manual-blocks.md`

Relevant excerpt:

> Every note in the vault has two clearly delimited regions:
> - **Auto block** — generated and overwritten by the refresh procedure. Never edit by hand.
> - **Manual block** — human-authored. The refresh procedure must **never** touch it.

Markers (exact strings):

```markdown
<!-- auto:start -->
…
<!-- auto:end -->

<!-- manual:start -->
…
<!-- manual:end -->
```

Ordering: auto block before manual block. Frontmatter above both.

**How it applies to `vault/index.md`:** the file uses the standard layout. The auto block holds About / Sections / Last refreshed; the manual block is an empty stub on initial creation. Refresh uses `Edit` (not `Write`) when the file already exists, with the existing auto block as `old_string` so the manual block is never inside the replacement window.

---

## notes/frontmatter-schema

**File:** `agent-os/standards/notes/frontmatter-schema.md`

Relevant excerpt (refresh-owned keys):

> Refresh-owned keys (any note type): `n8n_id`, `fingerprint`, `last_modified`, `status`, `auto_generated_at`, `type`.

This spec adds a new note type — `index` — to the schema:

```yaml
---
type: index
auto_generated_at: 2026-06-02T00:03:00Z
---
```

Unlike workflows and resources, the index has no name/slug — there is exactly one canonical path (`vault/index.md`). Unlike changelogs, the index *does* carry a manual block.

---

## sync/refresh-procedure

**File:** `agent-os/standards/sync/refresh-procedure.md`

Relevant excerpts:

> #### 4f. Write or patch the note
>
> - **New note:** use the `Write` tool with the full file content (frontmatter + auto block + empty manual stub).
> - **Existing note:** use the `Edit` tool. `old_string` is the current auto-block region (including the `<!-- auto:start -->` and `<!-- auto:end -->` markers) verbatim; `new_string` is the regenerated auto-block region with the same markers. Then issue a second `Edit` against the frontmatter block to update `fingerprint`, `last_modified`, `status`, `auto_generated_at`, and the n8n-sourced subset of `tags`.
>
> **Never use `Write` on an existing note** — it overwrites the whole file and would clobber the manual block.

And the idempotency guarantee:

> ## Idempotency
>
> Running refresh twice in a row, with no n8n-side change between runs, must produce:
> - Zero file modifications (every fingerprint matches)
> - No changelog file
> - A summary reporting "0 added, 0 modified, 0 removed"

**How it applies:** the new Step 6.5 follows the Step 4f write rule (Write for new, Edit for existing) and only runs when the refresh produced semantic change — keeping the idempotency guarantee intact.

---

## sync/changelog-format

**File:** `agent-os/standards/sync/changelog-format.md`

Not modified by this spec, but referenced for symmetry: the index is *not* a changelog (no immutable history, no per-run sections, no taxonomy-gap entries). It's a single live snapshot of vault structure. The changelog continues to be the authoritative record of *what changed*; the index is the authoritative record of *what currently exists*.
