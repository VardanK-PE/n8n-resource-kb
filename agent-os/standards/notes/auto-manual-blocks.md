# Standard: Auto / Manual Guarded Blocks

Every note in the vault has two clearly delimited regions:

- **Auto block** — generated and overwritten by the refresh procedure. Never edit by hand.
- **Manual block** — human-authored. The refresh procedure must **never** touch it.

This contract is the load-bearing invariant of capability 5 in `agent-os/product/roadmap.md`: manual annotations (owner, criticality, runbook URL, business purpose, free-form notes) must survive every refresh.

## Markers

Use these exact HTML-comment markers. They are stable strings that the refresh procedure pattern-matches against and that Obsidian renders invisibly.

```markdown
<!-- auto:start -->

Auto-generated content here.
Rewritten end-to-end by the refresh procedure.

<!-- auto:end -->

<!-- manual:start -->

Human-authored content here.
Refresh never modifies this region.

<!-- manual:end -->
```

## Ordering

The auto block always comes **before** the manual block in the file body. Frontmatter is its own thing — it sits above both blocks and is governed by `notes/frontmatter-schema.md`.

Full note layout:

```markdown
---
<frontmatter>
---

<!-- auto:start -->
...auto content...
<!-- auto:end -->

<!-- manual:start -->
...manual content...
<!-- manual:end -->
```

## Rules for refresh

1. **Read the existing note first** when one is present (using the `Read` tool). Capture the manual block verbatim before doing anything else.
2. **Use `Edit`** to replace only the auto-block region (the `old_string` is the existing auto block including its markers; `new_string` is the new auto block including markers). Never use `Write` on an existing note — it overwrites the whole file and would destroy the manual block.
3. **If the manual block is missing** (e.g., a corrupted or hand-truncated file), insert an empty manual block stub (`<!-- manual:start -->\n\n<!-- manual:end -->`). Do not infer or fabricate manual content.
4. **If the auto block is missing**, treat the note as not-yet-generated: regenerate the auto block in place above the manual block.

## Rules for manual editing

When the user adds annotations (owner, criticality, etc.):

- Edit **only** between `<!-- manual:start -->` and `<!-- manual:end -->`.
- Never edit inside the auto block; changes will be lost on the next refresh.
- Frontmatter `tags` may be manually extended **only** for keys not produced by refresh; refresh-owned frontmatter keys (`n8n_id`, `fingerprint`, `last_modified`, `status`, `auto_generated_at`) are off-limits to manual editing.

## Rationale

The guarded-block pattern is preferred over a side-car file because:

- A single note is what Obsidian's UI presents — splitting auto and manual into two files breaks the user's mental model.
- Wikilinks and Dataview queries work across the combined note seamlessly.
- A surgical replacement of a delimited region is straightforward with the `Edit` tool when given exact-match `old_string` (= the prior auto block including markers) and `new_string` (= the regenerated auto block).
