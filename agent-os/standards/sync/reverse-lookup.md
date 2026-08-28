# Standard: Reverse Lookup (runbook)

This is the runbook Claude follows when the user asks any of:

- "what uses <X>?"
- "what depends on <X>?"
- "what touches <X>?"
- "which workflows use the <X> credential / service / database / model / URL?"

It returns the list of `(workflow, node-name, node-id)` triples that touch the named resource — answering "what breaks if I change / rotate / remove this?".

## Procedure

### Step 0 — Determine instance scope

The vault holds one isolated subtree per instance (`vault/v1/`, `vault/v2/`). A resource with the same name can exist **independently** in each instance, with different usages.

- **Default: search both instances** and label every hit with its instance (`v1` / `v2`). Cross-instance visibility is the whole point of keeping both subtrees in one vault.
- If the user scopes the question ("in the new instance", "on v1", "the old n8n"), restrict to that subtree.
- Never merge usages from the two instances into one list as if they were the same resource — a `postgres` credential in v1 and one in v2 are different credentials. Group results by instance.

Throughout, `<INST>` ranges over the in-scope instances (`v1`, `v2`, or both).

### Step 1 — Resolve the resource

The user may name the resource exactly (`hubspot-prod`) or partially (`hubspot`). For each in-scope instance, resolve in this order:

1. **Exact slug match** in any `vault/<INST>/resources/<type>/<slug>.md`. Use `Bash` (`ls vault/<INST>/resources/*/`, or `ls vault/*/resources/*/` for both) to enumerate; exact-match the user's term (slugified) against the note filename.
2. **Frontmatter `name` exact match** via `Bash` (`grep -rl '^name: "<term>"' vault/<INST>/resources/`) or by reading candidates and parsing frontmatter.
3. **Partial match** via `Bash` (`grep -rli '<term>' vault/<INST>/resources/` or `find vault/<INST>/resources -iname '*<term>*'`). If multiple notes match, ask the user to disambiguate. Do not guess.

If no match in any in-scope instance: report "no resource matches `<term>` in the vault" (naming which instances were searched) and suggest a refresh if the resource was added recently. If it matches in one instance but not the other, say so.

### Step 2 — Read the resource note

Use the `Read` tool. Parse:

- Frontmatter (type, name, type-specific keys)
- The reverse-lookup list inside the auto block — every `[[../workflows/<slug>]]` entry along with the node name and node ID

### Step 3 — Report

Format the response grouped by instance (omit an instance heading if the query was scoped to a single one):

```
<resource-type> "<resource-name>":

[v1] used by:
- [[v1/workflows/<slug-1>]] — node "<node-name-1>" (id <node-id-1>)
- …

[v2] used by:
- [[v2/workflows/<slug-2>]] — node "<node-name-2>" (id <node-id-2>)
- …

(v1: N1 usages across M1 workflows; v2: N2 usages across M2 workflows)
```

If a resource note shows `0 current usages`, report that — it means the resource was previously used but no longer is, and the note is preserved for historical / manual-annotation reasons.

### Step 4 — Workflow-as-resource case

If the user asks "what uses workflow `X`?", the resource note **is** the workflow note (`vault/<INST>/workflows/<slug>.md`). Use its "Used by (workflows)" section in the auto block. Same response shape. A workflow ID is instance-local, so resolve it within the in-scope instance(s).

## Freshness caveat

The reverse-lookup reflects the **last refresh**. If the user expresses doubt the vault is current, suggest "refresh the vault first" before relying on the answer. Do not auto-refresh on every lookup — that's wasteful and the user may be intentionally querying historical state.

## What this runbook does **not** do

- Does not modify any note
- Does not call n8n-mcp (it operates entirely on the vault)
- Does not re-extract resources — it trusts the auto block written by the most recent refresh
- Does not use the `mcp__obsidian__*` tools — those point at a different vault in this environment
