# Standard: Reverse Lookup (runbook)

This is the runbook Claude follows when the user asks any of:

- "what uses <X>?"
- "what depends on <X>?"
- "what touches <X>?"
- "which workflows use the <X> credential / service / database / model / URL?"

It returns the list of `(workflow, node-name, node-id)` triples that touch the named resource — answering "what breaks if I change / rotate / remove this?".

## Procedure

### Step 1 — Resolve the resource

The user may name the resource exactly (`hubspot-prod`) or partially (`hubspot`). Resolve in this order:

1. **Exact slug match** in any `vault/resources/<type>/<slug>.md`. Use `Bash` (`ls vault/resources/*/`) to enumerate; exact-match the user's term (slugified) against the note filename.
2. **Frontmatter `name` exact match** via `Bash` (`grep -rl '^name: "<term>"' vault/resources/`) or by reading candidates and parsing frontmatter.
3. **Partial match** via `Bash` (`grep -rli '<term>' vault/resources/` or `find vault/resources -iname '*<term>*'`). If multiple notes match, ask the user to disambiguate. Do not guess.

If no match: report "no resource matches `<term>` in the vault" and suggest a refresh if the resource was added recently.

### Step 2 — Read the resource note

Use the `Read` tool. Parse:

- Frontmatter (type, name, type-specific keys)
- The reverse-lookup list inside the auto block — every `[[../workflows/<slug>]]` entry along with the node name and node ID

### Step 3 — Report

Format the response as:

```
<resource-type> "<resource-name>" is used by:

- [[workflows/<slug-1>]] — node "<node-name-1>" (id <node-id-1>)
- [[workflows/<slug-2>]] — node "<node-name-2>" (id <node-id-2>)
- …

(N total usages across M workflows)
```

If the resource note shows `0 current usages`, report that — it means the resource was previously used but no longer is, and the note is preserved for historical / manual-annotation reasons.

### Step 4 — Workflow-as-resource case

If the user asks "what uses workflow `X`?", the resource note **is** the workflow note (`vault/workflows/<slug>.md`). Use its "Used by (workflows)" section in the auto block. Same response shape.

## Freshness caveat

The reverse-lookup reflects the **last refresh**. If the user expresses doubt the vault is current, suggest "refresh the vault first" before relying on the answer. Do not auto-refresh on every lookup — that's wasteful and the user may be intentionally querying historical state.

## What this runbook does **not** do

- Does not modify any note
- Does not call n8n-mcp (it operates entirely on the vault)
- Does not re-extract resources — it trusts the auto block written by the most recent refresh
- Does not use the `mcp__obsidian__*` tools — those point at a different vault in this environment
