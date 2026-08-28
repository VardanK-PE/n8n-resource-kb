# Standard: Workflow Fingerprint

The fingerprint is the stable hash used to answer "did this workflow actually change?" It lives in each workflow note's frontmatter as `fingerprint` and is compared on every refresh.

## Why a fingerprint (and not `last_modified`)

n8n's `updatedAt` ticks on cosmetic edits (node drag, note re-flow). The vault should not emit a changelog entry for every cosmetic edit — only when **semantic** content changes. The fingerprint hashes only the fields that affect what the workflow *does*.

## Algorithm

1. From the workflow JSON, build a canonical object containing only:

   ```jsonc
   {
     "nodes": [
       {
         "id": "<n8n node ID>",
         "name": "<node name>",
         "type": "<node type>",
         "typeVersion": <number>,
         "parameters": <node parameters with UI-only fields stripped>,
         "credentials": <credentials reference object or null>,
         "disabled": <bool>
       },
       …
     ],
     "connections": <workflow.connections object verbatim>,
     "settings": <workflow.settings minus runtime-only fields>,
     "active": <bool>,
     "resources": [
       <every resource reference extracted per agent-os/standards/sync/resource-taxonomy.md, normalized and sorted>
     ]
   }
   ```

2. **Sort `nodes` by `id`** (lexicographic). **Sort `resources`** by `(type, name)`. Connections is keyed by node name; preserve key ordering by sorting object keys alphabetically.

3. Serialize to JSON with:
   - Sorted object keys at every depth
   - No insignificant whitespace
   - `\n` newlines (LF) where present
   - UTF-8 encoding

4. Hash with **SHA-256**. Store as lowercase hex.

## Fields stripped from `parameters`

These never affect semantics, only the UI:

- `position` (canvas coordinates)
- `notesInFlow`
- `notes` *when used as canvas annotations* — keep `notes` if a node uses it as a parameter (rare)
- Any key starting with `_` (n8n internal scratch)

## Fields stripped from `settings`

- `executionOrder` is kept (it can affect behavior)
- `saveDataErrorExecution`, `saveDataSuccessExecution`, `saveManualExecutions`, `saveExecutionProgress` are kept (operational)
- UI preferences (none currently identified — strip on a per-version basis if discovered)

## When the fingerprint changes

Any of the following will produce a new fingerprint:

- A node is added, removed, renamed, or has its `type` / `typeVersion` changed
- A node parameter changes (excluding the stripped UI fields)
- A credential reference is added, removed, or swapped
- Connections topology changes
- `active` flips
- The set of resources extracted from the workflow changes (this captures cases where parameter changes don't change the node but **do** change what resource it points at — e.g., editing an HTTP URL)

## When it doesn't change

- Moving nodes on the canvas
- Adding / removing canvas annotations
- Editing `notesInFlow`
- Renaming the workflow itself (workflow name lives in frontmatter, not the fingerprint — so `name` changes update the note but don't emit a "logic changed" changelog entry; they emit a "renamed" entry instead). **Because the name is not hashed, a rename is invisible to a fingerprint-only comparison — it must be caught by comparing `name` separately.** `scripts/detect-changes.sh` does this (`RENAMED`); the refresh procedure Step 3 requires it. The same applies to archived/active `status`, also unhashed (`STATUS_CHANGED`).

## First-time generation

When a workflow has no existing note, refresh:

1. Computes the fingerprint as above
2. Writes the full note (auto + empty manual stub)
3. Logs the workflow as **added** in the changelog

## On mismatch

When the computed fingerprint differs from the stored fingerprint (or `detect-changes.sh` reports `RENAMED` / `STATUS_CHANGED`), follow `sync/refresh-procedure.md` Step 4: capture the manual block, regenerate the note (the renderer is create-only, so delete + re-render by id), migrate the slug if the name changed (4f-slug), update `fingerprint` / `status` / `auto_generated_at` in frontmatter, and append the change to today's changelog per `sync/changelog-format.md`. Use `Edit` (never `Write`) on any surviving note; do **not** use the `mcp__obsidian__*` tools (they point at a different vault — see `CLAUDE.md`).

## Why this exact algorithm

- Sorting keys + nodes by ID makes the hash insensitive to JSON serialization order — two refreshes of the same logical state produce the same hash even if n8n's API returns fields in a different order between calls.
- Including extracted resources in the hash means "edited URL" or "swapped credential" both register as semantic change, even though they live in `parameters`.
- SHA-256 is cryptographic-strength overkill but cheap and produces clean 64-character hex strings for the frontmatter.
