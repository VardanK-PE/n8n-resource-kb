# Standard: Refresh Procedure (runbook)

This is the runbook Claude follows when the user says any of:

- "refresh the vault"
- "sync n8n"
- "update the vault"
- "rebuild the n8n knowledge base"

It composes every other standard in `agent-os/standards/{notes,sync}/` into an end-to-end operation. Follow it strictly — manual annotations depend on the integrity of step 4.

## Inputs

- `vault/` (current state — workflow + resource + changelog notes)
- The live n8n instance, reached via its **REST API** (no MCP server required)
- This run's date in UTC (used to name the changelog file)

## Working pattern for large workflows

n8n workflow JSON can be hundreds of KB per workflow. **Never read raw workflow JSON into Claude's context.** Use the cache + `jq` pipeline pattern defined in `sync/large-workflow-handling.md`:

- Every fetched workflow lands in `vault/_cache/workflows/<n8n_id>.json` (gitignored)
- Resource extraction, fingerprint computation, and node inspection all happen via `jq` programs under `scripts/jq/`
- Claude reads only the small structured outputs of those programs — never `cat` / `Read` against `vault/_cache/workflows/*`

Every step below assumes this pattern. If a step appears to want a workflow's full contents in context, that's a bug — write a `jq` query that returns just the fields you need.

## Outputs

- Updated / created notes under `vault/workflows/` and `vault/resources/<type>/`
- Optionally: `vault/changelogs/YYYY-MM-DD.md` (only if at least one workflow's fingerprint changed, was new, or went away)

## n8n REST API contract (used throughout)

**All API calls go through the wrapper script `scripts/n8n-api.sh`.** Do not source `.env` directly — the user-level hook at `~/.claude/hooks/block-env-files.sh` blocks any Bash command that contains `.env`. The wrapper hides credential access from the agent's command line.

Usage:

```sh
# Always quote endpoint paths — ? and & trigger zsh globbing if unquoted
scripts/n8n-api.sh '/api/v1/workflows?limit=100'
scripts/n8n-api.sh "/api/v1/workflows/$ID"
```

The wrapper:

1. Resolves auth from `./.env` (preferred) or `../n8n_claude/.mcp.json` (sibling fallback)
2. Calls curl with `X-N8N-API-KEY` + `Accept: application/json`
3. Uses `-fsS` so 4xx/5xx exits non-zero (no silent partial data)

Endpoints used:

| Purpose | Method | Path |
|---|---|---|
| List workflows (paginated, cursor-based) | GET | `/api/v1/workflows?limit=100&cursor=<nextCursor>` |
| Fetch one workflow | GET | `/api/v1/workflows/{id}` |

**Important:** the list endpoint **already returns full workflow JSON** (nodes, connections, settings, staticData, pinData — everything). For Phase 1 there is **no need to do a per-workflow fetch** unless you need just-fetched data for a specific ID. Paginate the list once → split per-workflow to disk → done.

Response shape for list: `{ "data": [ <FullWorkflowJson>… ], "nextCursor": string | null }`.

Observed full workflow fields (n8n 1.x on this instance):

- `id`, `name`, `active`, `isArchived`, `versionId`, `activeVersionId`, `activeVersion`
- `nodes[]` — `id`, `name`, `type`, `typeVersion`, `parameters`, `credentials`, `position`, `disabled`, `notesInFlow`
- `connections`, `settings`, `staticData`, `pinData`
- `tags[]` — `{ id, name, createdAt, updatedAt }`
- `meta`, `shared`, `triggerCount`, `createdAt`, `updatedAt`

Tags come back as objects, not strings — extract `.tags[].name` when normalizing into vault frontmatter.

Never echo `$N8N_API_KEY` to stdout. Never include it in changelog entries, vault notes, or conversation output.

## Procedure

### Step 1 — Enumerate workflows in n8n (also caches them, since the list returns full JSON)

The list endpoint returns full workflow JSON, so we cache everything in this single step. The agent never reads the per-page response into context — it goes straight to disk.

```sh
mkdir -p vault/_cache/workflows /tmp/n8n-pages
rm -f /tmp/n8n-pages/*.json /tmp/n8n-pages/*.jsonl 2>/dev/null
: > vault/_cache/list.jsonl

cursor=""
page=0
total=0
while :; do
  page=$((page+1))
  if [ -z "$cursor" ]; then
    url='/api/v1/workflows?limit=100'
  else
    url="/api/v1/workflows?limit=100&cursor=$cursor"
  fi

  scripts/n8n-api.sh "$url" > /tmp/n8n-pages/page-$page.json

  # Split each workflow into vault/_cache/workflows/<id>.json
  jq -c '.data[]' /tmp/n8n-pages/page-$page.json > /tmp/n8n-pages/page-$page.jsonl
  while IFS= read -r wf; do
    id=$(printf '%s' "$wf" | jq -r '.id')
    printf '%s' "$wf" > "vault/_cache/workflows/$id.json"
  done < /tmp/n8n-pages/page-$page.jsonl

  # Compact metadata index for refresh categorization
  jq -c '.data[] | {
    id, name, active, isArchived, triggerCount,
    nodeCount: (.nodes | length),
    createdAt, updatedAt,
    tags: (.tags // [] | map(.name))
  }' /tmp/n8n-pages/page-$page.json >> vault/_cache/list.jsonl

  count=$(jq '.data | length' /tmp/n8n-pages/page-$page.json)
  total=$((total+count))
  cursor=$(jq -r '.nextCursor // empty' /tmp/n8n-pages/page-$page.json)
  echo "page $page: +$count (total $total)" >&2

  [ -z "$cursor" ] && break
  [ "$page" -ge 50 ] && { echo "SAFETY: stopping at 50 pages" >&2; break; }
done

wc -l vault/_cache/list.jsonl
```

Build `N = {n8n_id → metadata}` by reading `vault/_cache/list.jsonl` (small — one compact JSON per line).

### Step 2 — Enumerate workflow notes in the vault

Use `Bash` (`ls vault/workflows/*.md` or `find vault/workflows -name '*.md' -not -name '.gitkeep'`) and `Read` each note. Parse the YAML frontmatter from the top.

Build `V = {n8n_id → frontmatter}`.

### Step 3 — Categorize each workflow

For every `id` in `N ∪ V`:

| In n8n? | In vault? | Category |
|---|---|---|
| yes | no | **Added** — generate new note |
| yes | yes, fingerprint matches | **Unchanged** — skip |
| yes | yes, fingerprint differs | **Modified** — diff + edit auto block |
| no | yes, status ≠ deleted | **Removed** — flip status, preserve note |
| no | yes, status = deleted | (no-op) |

### Step 4 — Process each workflow

For each non-skipped workflow:

#### 4a. Ensure the cached workflow JSON is present

Step 1 already cached every workflow (the list endpoint returns full JSON). Just verify:

```sh
test -s vault/_cache/workflows/"$ID".json || \
  scripts/n8n-api.sh "/api/v1/workflows/$ID" > vault/_cache/workflows/"$ID".json

jq '{id, name, nodes: (.nodes | length), updatedAt}' < vault/_cache/workflows/"$ID".json
```

A per-workflow fetch is only needed if Step 1 was skipped or a specific workflow's cached copy was purged.

#### 4b. Extract resources via `jq` programs

Apply each extractor under `scripts/jq/` to the cached JSON. Each returns a compact, sorted list:

```sh
jq -c -f scripts/jq/extract-http-urls.jq    < vault/_cache/workflows/"$ID".json
jq -c -f scripts/jq/extract-credentials.jq  < vault/_cache/workflows/"$ID".json
jq -c -f scripts/jq/extract-subworkflows.jq < vault/_cache/workflows/"$ID".json
jq -c -f scripts/jq/extract-triggers.jq     < vault/_cache/workflows/"$ID".json
jq -c -f scripts/jq/extract-databases.jq    < vault/_cache/workflows/"$ID".json
jq -c -f scripts/jq/extract-llm-models.jq   < vault/_cache/workflows/"$ID".json
jq -c -f scripts/jq/extract-env-vars.jq     < vault/_cache/workflows/"$ID".json
jq -c -f scripts/jq/extract-custom-nodes.jq < vault/_cache/workflows/"$ID".json
```

Concatenate the results into a per-workflow `extracted` record. Any node whose `type` matched no extractor — find via `scripts/jq/nodes-summary.jq` set-diff against the union of all extractor outputs — becomes an "Unmapped node reference" and produces a `taxonomy_gap` per `sync/resource-taxonomy.md`.

#### 4c. Compute fingerprint

```sh
jq -cS -f scripts/jq/canonical.jq < vault/_cache/workflows/"$ID".json \
  | shasum -a 256 \
  | cut -d' ' -f1
```

The canonical projection includes the extracted resources from 4b so fingerprint reflects them per `sync/fingerprint.md`.

#### 4d. Build the auto block

Per the workflow template (`vault/_templates/workflow.md`). Sections:

- **Summary** — node count, active/inactive, last_modified
- **Triggers** — extracted trigger resources (with links to their notes)
- **Depends on** — grouped by resource type:
  - Credentials → `[[../resources/credentials/<slug>]]` + node name + node ID per usage
  - Services / databases / http-urls / llm-models / env-vars / custom-nodes — same shape
  - Sub-workflows → `[[<workflow-slug>]]` + the calling Execute-Workflow node's name + ID
- **Used by (workflows)** — bidirectional: every other workflow whose Execute-Workflow references this one, with the calling node's name + ID
- **Unmapped node references** (only if any)

#### 4e. Read the existing note (if any) and capture its manual block

Use the `Read` tool. Extract the `<!-- manual:start -->` … `<!-- manual:end -->` region verbatim — this is the contract from `notes/auto-manual-blocks.md`.

If the manual block is missing or malformed, substitute the empty stub.

#### 4f. Write or patch the note

- **New note:** use the `Write` tool with the full file content (frontmatter + auto block + empty manual stub).
- **Existing note:** use the `Edit` tool. `old_string` is the current auto-block region (including the `<!-- auto:start -->` and `<!-- auto:end -->` markers) verbatim; `new_string` is the regenerated auto-block region with the same markers. Then issue a second `Edit` against the frontmatter block to update `fingerprint`, `last_modified`, `status`, `auto_generated_at`, and the n8n-sourced subset of `tags`.

**Never use `Write` on an existing note** — it overwrites the whole file and would clobber the manual block.

#### 4g. For "Removed" workflows

Edit the frontmatter to set `status: deleted` and edit the auto block to append a "Removed from n8n" line. Do not delete the file.

### Step 5 — Reconcile resource notes

After processing all workflows in memory, build the reverse-lookup index: for each `(resource_type, resource_name)`, collect every `(workflow_id, workflow_slug, node_name, node_id, …)` that references it.

For each resource note:

- If the note exists, capture its manual block and `Edit` the auto block with the new reverse-lookup list (sorted by workflow slug, then node name)
- If the note does not exist, create it from the appropriate `_templates/resource-<type>.md`
- If a previously-known resource has zero usages this run, do not delete the note: edit its auto block to record "0 current usages" and append a "resource no longer used" entry to today's changelog

### Step 6 — Workflow-as-resource bidirectionality

After Step 5, walk every workflow's "Used by (workflows)" section and ensure the back-references are consistent. For each `Execute Workflow` reference found in workflow A pointing at workflow B:

- A's "Depends on → Workflows" lists B
- B's "Used by (workflows)" lists A with the Execute-Workflow node's name + ID

Mismatches indicate a bug in extraction — surface them as a `taxonomy_gap` entry rather than silently fixing on one side only.

### Step 6.5 — Update `vault/index.md`

`vault/index.md` is the vault's orientation note (see `notes/frontmatter-schema.md` → "Index note"). Its auto block surfaces live section counts and wikilinks; refresh keeps it current.

#### Idempotency guard

**Skip this step entirely** when the run was a pure no-op — no workflow added/modified/removed and no resource note created/removed. This preserves the run-twice-zero-changes invariant in the Idempotency section below. The index updates only when vault structure actually shifted.

#### Computation

Counts come from disk (the vault), not from `vault/_cache/list.jsonl` (which mirrors n8n state). The index is a view of the vault.

```sh
workflows=$(ls vault/workflows/*.md 2>/dev/null | wc -l | tr -d ' ')
changelogs=$(ls vault/changelogs/*.md 2>/dev/null | wc -l | tr -d ' ')

# One bullet per resource category, alphabetical, so new categories surface automatically.
# Render paths as inline code only — do NOT use `[[wiki]]` or `[md](folder/)` link syntax.
# Obsidian creates a blank note on click for both forms when the target is a folder
# (verified — `[[workflows]]` and `[workflows/](workflows/)` both spawn `workflows.md`).
# Folder navigation happens via the file-explorer sidebar; the index is orientation only.
for d in vault/resources/*/; do
  cat=$(basename "$d")
  cnt=$(ls "$d"*.md 2>/dev/null | wc -l | tr -d ' ')
  printf -- '- `resources/%s/` — %s\n' "$cat" "$cnt"
done
```

#### Write rule (mirrors Step 4f)

- **If `vault/index.md` does not exist** → use `Write` with the full file content (frontmatter + auto block + empty manual stub) per `vault/_templates/index.md`.
- **If it exists** → `Read` it first to capture the manual block. Then `Edit` the auto-block region (exact-match `old_string` from `<!-- auto:start -->` through `<!-- auto:end -->`), and a second `Edit` to update `auto_generated_at` in the frontmatter.

**Never use `Write` on an existing `vault/index.md`** — it would clobber the manual block, same as any other vault note.

#### Frontmatter

Only two refresh-owned keys:

```yaml
---
type: index
auto_generated_at: <ISO 8601 UTC>
---
```

No `n8n_id`, `fingerprint`, `last_modified`, or `status` — those are workflow/resource concepts. The index reflects vault state, not n8n state.

### Step 7 — Write the changelog

If any workflow was added, modified, removed, or any taxonomy gap fired, write `vault/changelogs/<today>.md` per `sync/changelog-format.md`.

If no change occurred this run, do **not** create an empty changelog file. (The user asked for a changelog of meaningful change, not a per-run log.)

### Step 8 — Final report to the user

In the conversation, summarize:

- Counts: added / modified / removed / unchanged
- New resource categories that triggered taxonomy gaps (if any)
- Link to today's changelog note (if one was written)

## Tool selection

- `Bash` + `curl` + `jq` — n8n REST API calls and all workflow-JSON manipulation. The only source of truth for n8n state.
- `Bash` (`ls`, `find`, `grep`) — enumerating notes under `vault/`
- `Read` — loading **existing notes** (so the manual block can be captured before any write). **Never** to read `vault/_cache/workflows/*.json`.
- `Write` — creating brand-new notes (never on an existing path)
- `Edit` — every update to an existing note. `old_string` always matches the current auto block (or frontmatter line) verbatim; `new_string` carries the replacement
- The n8n-mcp skill bundle (`n8n-mcp-tools-expert`, `n8n-node-configuration`, `n8n-expression-syntax`, `n8n-workflow-patterns`, `n8n-validation-expert`) — useful as **reference docs** for node-shape questions during taxonomy extension, but no runtime dependency on the n8n-mcp MCP server.

**Do not use the `mcp__obsidian__*` tools for this project's vault.** The obsidian MCP server in this environment is configured against a different vault — see CLAUDE.md.

**Do not use the n8n-mcp MCP server even if available.** It's reported as unstable on this instance, and the REST API covers every Phase 1 need.

**Do not read raw workflow JSON into context.** See `sync/large-workflow-handling.md` — Claude should never `Read` or `cat` files under `vault/_cache/workflows/`. Use `jq` programs under `scripts/jq/` exclusively.

## Failure modes & recovery

- **n8n API call fails (non-2xx, auth error, network):** stop the run. Do not write a partial changelog. Surface the HTTP status + workflow ID where the run halted. The next refresh resumes by re-comparing fingerprints, so partial work doesn't corrupt state.
- **`scripts/n8n-api.sh` exits 2 ("no credentials"):** the user hasn't created `.env`. Tell them to `cp .env.example .env` and fill in `N8N_API_URL` + `N8N_API_KEY` (sibling fallback paths are documented in the wrapper script comments). Do not attempt to read `.env` directly — it's blocked by the user-level hook.
- **File write fails on a single note:** continue with other workflows. Collect the failures and surface them in the conversation summary at Step 8.
- **A manual block was lost** by a prior buggy run: refresh re-inserts the empty stub but does **not** fabricate content. Surface a warning in the conversation summary.
- **`Edit` rejects a replacement** because the prior auto block didn't match what was on disk: do NOT fall back to `Write` (would clobber the manual block). Re-read the note, recompute the diff against the actually-on-disk content, retry. If still failing, surface the file and stop processing that workflow.

## Idempotency

Running refresh twice in a row, with no n8n-side change between runs, must produce:

- Zero file modifications (every fingerprint matches)
- No changelog file
- A summary reporting "0 added, 0 modified, 0 removed"

If this property breaks, the fingerprint algorithm is unstable — investigate before continuing.
