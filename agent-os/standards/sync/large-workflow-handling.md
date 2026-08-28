# Standard: Large-Workflow Handling

n8n workflow JSON can run hundreds of KB per workflow (deep `parameters` with code blocks, prompts, queries, schemas, etc.). Reading raw JSON into Claude's context blows through the window on the first complex workflow.

This standard defines the working pattern that keeps the refresh procedure tractable regardless of workflow size.

## Core principle

**Claude orchestrates. `jq` extracts. Disk holds the bulk.**

The full workflow JSON is fetched once, written to disk, and then processed exclusively by `Bash` + `jq` pipelines that produce small, structured outputs. Claude reads only the extracted summaries — never the raw JSON file, never the curl response stdout in bulk.

## Disk layout

The cache is **per instance** — one under each instance subtree, where `<INST>` is the instance alias (`v1` | `v2`):

```
vault/<INST>/_cache/                 # gitignored (matched by vault/*/_cache/)
├── list.jsonl                       # most recent /api/v1/workflows result (paginated, concatenated)
└── workflows/
    └── <n8n_id>.json               # one file per workflow, full JSON from /api/v1/workflows/<id>
```

The cache is the single source of in-memory data during a refresh. Subsequent steps (resource extraction, fingerprint, note construction) read from the cache, not from re-fetched API responses. Because n8n IDs are only unique within an instance, each instance keeps its own cache — never share one across instances.

`vault/<INST>/_cache/` is gitignored. It's a working scratch area — purgeable at any time without losing real state.

## Tool discipline (hard rules)

1. **Never `cat` a workflow JSON file into the conversation.** Use `jq` to extract specific fields.
2. **Never `Read` a file under `vault/<INST>/_cache/workflows/`.** It exists for `jq`, not for Claude's context.
3. **Don't pipe raw API responses through `echo` / print.** Always redirect to disk: `scripts/n8n-api.sh "$INST" "/api/v1/workflows/$ID" > vault/$INST/_cache/workflows/$ID.json` then drive from there.
4. **Print only small summaries via `jq`.** When checking a workflow's shape, write a `jq` query that returns counts, names, or specific values — not the whole node.

If you need to inspect a workflow during debugging, name the question first ("how many HTTP nodes?", "what credential does node X use?") and write the `jq` for that question. Never "open the file to look around."

## Reusable `jq` programs

Reusable extraction logic lives under `scripts/jq/` in this repo. Each program reads a workflow JSON from stdin and emits compact, sorted JSON to stdout. Compose them; don't inline complex `jq` in shell heredocs.

Initial set (seeded with the spec; extended as taxonomy grows):

| Script | Purpose | Output shape |
|---|---|---|
| `scripts/jq/nodes-summary.jq` | Compact per-node summary | `[{id, name, type, typeVersion, disabled}]` |
| `scripts/jq/canonical.jq` | Fingerprint canonical projection (sorted, UI fields stripped) | canonical JSON for hashing |
| `scripts/jq/extract-http-urls.jq` | HTTP Request nodes → host + path + method | `[{node_id, node_name, host, method, path}]` |
| `scripts/jq/extract-credentials.jq` | All credential references across all nodes | `[{node_id, node_name, credential_type, credential_name}]` |
| `scripts/jq/extract-subworkflows.jq` | Execute-Workflow node references | `[{node_id, node_name, target_workflow_id}]` |
| `scripts/jq/extract-triggers.jq` | Webhook / schedule / cron / event triggers | `[{node_id, node_name, trigger_type, path|cron}]` |
| `scripts/jq/extract-databases.jq` | Postgres / MySQL / MongoDB / etc. nodes → engine + host + db + tables | `[{node_id, node_name, engine, host, database, tables, query_snippet}]` |
| `scripts/jq/extract-llm-models.jq` | LangChain LLM / chat-model / embedding nodes → provider + model | `[{node_id, node_name, provider, model}]` |
| `scripts/jq/extract-env-vars.jq` | Regex `$env\.[A-Z_][A-Z0-9_]*` over all string parameters | `[{node_id, node_name, var_name}]` |
| `scripts/jq/extract-custom-nodes.jq` | Nodes whose type isn't `n8n-nodes-base.*` or `@n8n/*` | `[{node_id, node_name, type, package}]` |

Programs MUST:

- Read from stdin (so they compose with `curl ... | jq -f ...` or `jq -f ... < cached.json`)
- Always sort by node `id` then any secondary key
- Emit valid JSON (use `jq -c` for compact, `jq -S` if downstream needs key sort)
- Be small and single-purpose — extend with new scripts instead of bloating existing ones

## End-to-end pattern in the refresh procedure

```sh
# All API calls go through the wrapper, which resolves this instance's auth from
# .env (never `source .env` — the .env hook blocks it). First arg = alias.
INST=v1    # or v2

mkdir -p vault/$INST/_cache/workflows

# Step 1: get the list (small response, OK to read into context if needed)
scripts/n8n-api.sh "$INST" "/api/v1/workflows?limit=100" \
  | jq -c '.data[] | {id, name, active, updatedAt, tags}' \
  > vault/$INST/_cache/list.jsonl

# For each workflow ID, fetch to disk
while read -r row; do
  id=$(echo "$row" | jq -r .id)
  scripts/n8n-api.sh "$INST" "/api/v1/workflows/$id" \
    > vault/$INST/_cache/workflows/"$id".json
done < vault/$INST/_cache/list.jsonl

# Per-workflow extraction (raw JSON never leaves disk)
jq -c -f scripts/jq/extract-http-urls.jq    < vault/$INST/_cache/workflows/$id.json
jq -c -f scripts/jq/extract-credentials.jq  < vault/$INST/_cache/workflows/$id.json
jq -c -f scripts/jq/extract-subworkflows.jq < vault/$INST/_cache/workflows/$id.json
# ...etc per resource category

# Fingerprint
jq -cS -f scripts/jq/canonical.jq < vault/$INST/_cache/workflows/$id.json \
  | shasum -a 256 \
  | cut -d' ' -f1
```

Each pipeline above emits at most a few hundred bytes to Claude's context. The MB-scale raw JSON stays on disk.

## When `jq` isn't enough

If a node type appears that the existing scripts don't handle (taxonomy gap), the procedure for investigating it:

1. Use `jq` to extract just that one node's record from the cached JSON:

   ```sh
   jq '.nodes[] | select(.id=="<id>")' < vault/$INST/_cache/workflows/$wf_id.json
   ```

2. Look at the node in isolation — it's small. Decide what to extract.
3. Add a new `scripts/jq/extract-*.jq` (or extend an existing one).
4. Update `agent-os/standards/sync/resource-taxonomy.md` to document the new mapping.
5. Re-run refresh.

Never pull the whole workflow into context to "look around." Always slice to the node in question.

## Idempotent caching

Re-running refresh against an unchanged instance should:

- Re-fetch the list (cheap)
- Skip re-fetching each workflow whose `updatedAt` hasn't changed since the cached copy's `mtime` **AND** whose fingerprint matches the vault note. (Use `find vault/$INST/_cache/workflows/$id.json -newer …` or just compare `updatedAt` to the cached file's recorded value.)

This avoids re-hitting the API for every refresh; it also avoids re-running every `jq` extraction. Fingerprint stability is what actually decides whether to write notes, but cached JSON skipping is what keeps the API + CPU footprint small.

## Memory budget

A rough budget per refresh, to know when to stop and design differently:

- List response: 1–2 KB per workflow → maybe 200 KB for 100 workflows. OK to handle in context.
- Per-workflow extracted summary (all `jq` outputs concatenated): ~2–10 KB. Multiplied by 100 workflows → 200 KB–1 MB. Still OK in **disk**; keep in `vault/$INST/_cache/extracted/<id>.json` if needed and merge incrementally.
- Notes written to `vault/$INST/workflows/<slug>.md`: bounded by workflow content, not raw JSON. Typical 2–5 KB.
- Raw JSON (NEVER in context): hundreds of KB per workflow × N workflows. Stays in `vault/$INST/_cache/workflows/`.

If a single workflow's extracted summary itself approaches 50 KB, that's a sign the extraction is too verbose — tighten the `jq` to drop redundant fields.
