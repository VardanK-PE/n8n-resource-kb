#!/usr/bin/env bash
# Render workflow + resource notes into vault/ from cached workflow JSON.
#
# Usage:
#   scripts/render-vault.sh --instance <v1|v2> <workflow-id> [<workflow-id> ...]
#   scripts/render-vault.sh --instance <v1|v2> --all
#
# --instance selects which instance subtree to render into (vault/<instance>/).
# It is required — n8n IDs are only unique within an instance, so rendering into
# the wrong subtree would silently corrupt the other instance's notes.
#
# Bash 3.2-compatible (no associative arrays). All data wrangling goes through jq.
#
# Resource keying:
#   credential:  n8n credential id  (names drift over time; id is canonical)
#   database:    engine + credential id  (db host lives on the credential)
#   llm-model:   provider/model slug
#   http-url:    hostname
#   trigger:     trigger_type + path/schedule discriminator
#   env-var:     variable name
#   custom-node: npm package name
#   workflow-callee:  target n8n workflow id (bidirectional sub-workflow link)
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

# --- Required instance selector (validated allowlist) ---
if [ "${1:-}" != "--instance" ]; then
  echo "usage: $0 --instance <v1|v2> [<workflow-id> ... | --all]" >&2
  exit 2
fi
INSTANCE="${2:-}"
case "$INSTANCE" in
  v1|v2) ;;
  *) echo "ERROR: unknown instance '${INSTANCE:-}' (allowed: v1, v2)." >&2; exit 2 ;;
esac
shift 2

VAULT="vault/$INSTANCE"
CACHE="$VAULT/_cache"
NOW="$(date -u '+%Y-%m-%dT%H:%M:%SZ')"

mkdir -p \
  "$VAULT/workflows" \
  "$VAULT/resources/credentials" \
  "$VAULT/resources/databases" \
  "$VAULT/resources/triggers" \
  "$VAULT/resources/llm-models" \
  "$VAULT/resources/http-urls" \
  "$VAULT/resources/env-vars" \
  "$VAULT/resources/custom-nodes" \
  "$VAULT/resources/google-sheets" \
  "$VAULT/resources/google-drive" \
  "$VAULT/resources/data-tables" \
  "$VAULT/resources/slack-channels" \
  "$VAULT/resources/github-repos" \
  "$VAULT/resources/google-docs" \
  "$VAULT/resources/s3-buckets" \
  "$VAULT/resources/kafka-topics" \
  "$VAULT/resources/mcp-servers" \
  "$CACHE/render-tmp"

# Filter regex (same as the scope decisions: archived + name-based backups skipped at --all)
SKIP_NAME_REGEX='(^|[^a-z])(bk|backup|copy|archived?)([^a-z]|$)|backup[\s_-]*[0-9]'

# Determine targets
TARGETS_FILE="$CACHE/render-tmp/targets.txt"
: > "$TARGETS_FILE"
if [ "${1:-}" = "--all" ]; then
  jq -r --arg re "$SKIP_NAME_REGEX" '
    select((.isArchived | not) and ((.name | test($re; "i")) | not))
    | .id
  ' "$CACHE/list.jsonl" > "$TARGETS_FILE"
elif [ $# -gt 0 ]; then
  for id in "$@"; do echo "$id" >> "$TARGETS_FILE"; done
else
  echo "usage: $0 <workflow-id> [...] | --all" >&2
  exit 2
fi

TARGET_COUNT=$(wc -l < "$TARGETS_FILE" | tr -d ' ')
echo "rendering $TARGET_COUNT workflow(s)" >&2

# Build the id → {name, slug} map across the WHOLE list, so sub-workflow refs
# can resolve even if the callee isn't in this run's target set.
# Slugs are disambiguated: if two workflows share the same base slug, all but
# the first get an "-<id-prefix>" suffix appended.
jq -r '"\(.id)\t\(.name)\t\(.createdAt // "")"' "$CACHE/list.jsonl" > "$CACHE/render-tmp/id-name-raw.tsv"

# slugify takes a string on stdin and writes the slug on stdout
slugify() {
  tr '[:upper:]' '[:lower:]' \
    | LC_ALL=C sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//' \
    | cut -c1-80
}

# Build id-slug.tsv (id<tab>slug<tab>name) with collision disambiguation.
# Sort by createdAt so the disambiguation is stable across runs (older workflows
# get the unsuffixed slug; newer ones get the -<prefix> suffix).
awk -F'\t' '{ print $3 "\t" $1 "\t" $2 }' "$CACHE/render-tmp/id-name-raw.tsv" \
  | sort \
  | awk -F'\t' '
    {
      id   = $2
      name = $3
      # slug = lowercase, non-alnum -> "-", trim
      slug = tolower(name)
      gsub(/[^a-z0-9]+/, "-", slug)
      sub(/^-+/, "", slug)
      sub(/-+$/, "", slug)
      slug = substr(slug, 1, 80)
      if (slug in seen) {
        # Disambiguate with the first 8 chars of the id
        slug = slug "-" substr(id, 1, 8)
      }
      seen[slug] = 1
      print id "\t" slug "\t" name
    }
  ' > "$CACHE/render-tmp/id-slug.tsv"

# Resolve a workflow id → "slug|name" (best-effort)
id_to_slug_name() {
  local id="$1"
  awk -F'\t' -v id="$id" '$1==id { print $2 "|" $3; exit }' "$CACHE/render-tmp/id-slug.tsv"
}

# Resolve a workflow id → slug only
id_to_slug() {
  local id="$1"
  awk -F'\t' -v id="$id" '$1==id { print $2; exit }' "$CACHE/render-tmp/id-slug.tsv"
}

# Usage record file — one line per resource usage, JSON
USAGES_JSONL="$CACHE/render-tmp/usages.jsonl"
: > "$USAGES_JSONL"

# Per-workflow processing
while IFS= read -r ID; do
  [ -z "$ID" ] && continue
  WF="$CACHE/workflows/$ID.json"
  if [ ! -s "$WF" ]; then
    echo "WARN: no cache for $ID" >&2
    continue
  fi

  NAME=$(jq -r '.name' < "$WF")
  # Use the canonical id-slug map so colliding names get disambiguated identically
  # across the workflow note + every wiki link that points at it.
  SLUG=$(id_to_slug "$ID")
  if [ -z "$SLUG" ]; then
    # Fallback: workflow not in list (shouldn't happen, but be defensive)
    SLUG=$(printf '%s' "$NAME" | slugify)
  fi
  NOTE="$VAULT/workflows/$SLUG.md"

  ACTIVE=$(jq -r '.active' < "$WF")
  IS_ARCHIVED=$(jq -r '.isArchived' < "$WF")
  if   [ "$IS_ARCHIVED" = "true" ]; then STATUS="archived"
  elif [ "$ACTIVE" = "true" ];      then STATUS="active"
  else                                   STATUS="inactive"
  fi
  LAST_MOD=$(jq -r '.updatedAt' < "$WF")
  FP=$(jq -cS -f scripts/jq/canonical.jq < "$WF" | shasum -a 256 | cut -d' ' -f1)
  NODE_COUNT=$(jq '.nodes | length' < "$WF")

  TMPDIR="$CACHE/render-tmp/$ID"
  mkdir -p "$TMPDIR"

  jq -c -f scripts/jq/extract-triggers.jq     < "$WF" > "$TMPDIR/triggers.json"
  jq -c -f scripts/jq/extract-credentials.jq  < "$WF" > "$TMPDIR/credentials.json"
  jq -c -f scripts/jq/extract-http-urls.jq    < "$WF" > "$TMPDIR/http-urls.json"
  jq -c -f scripts/jq/extract-databases.jq    < "$WF" > "$TMPDIR/databases.json"
  jq -c -f scripts/jq/extract-llm-models.jq   < "$WF" > "$TMPDIR/llm-models.json"
  jq -c -f scripts/jq/extract-env-vars.jq     < "$WF" > "$TMPDIR/env-vars.json"
  jq -c -f scripts/jq/extract-subworkflows.jq < "$WF" > "$TMPDIR/subworkflows.json"
  jq -c -f scripts/jq/extract-custom-nodes.jq < "$WF" > "$TMPDIR/custom-nodes.json"
  jq -c -f scripts/jq/extract-google-sheets.jq < "$WF" > "$TMPDIR/google-sheets.json"
  jq -c -f scripts/jq/extract-google-drive.jq < "$WF" > "$TMPDIR/google-drive.json"
  jq -c -f scripts/jq/extract-data-tables.jq < "$WF" > "$TMPDIR/data-tables.json"
  jq -c -f scripts/jq/extract-slack-channels.jq < "$WF" > "$TMPDIR/slack-channels.json"
  jq -c -f scripts/jq/extract-github-repos.jq    < "$WF" > "$TMPDIR/github-repos.json"
  jq -c -f scripts/jq/extract-google-docs.jq     < "$WF" > "$TMPDIR/google-docs.json"
  jq -c -f scripts/jq/extract-s3-buckets.jq      < "$WF" > "$TMPDIR/s3-buckets.json"
  jq -c -f scripts/jq/extract-kafka-topics.jq    < "$WF" > "$TMPDIR/kafka-topics.json"
  jq -c -f scripts/jq/extract-mcp-clients.jq     < "$WF" > "$TMPDIR/mcp-clients.json"

  WF_SLUG="$SLUG"

  # Emit one usage record per resource reference. Resource id is canonical (n8n id when available).
  jq -c \
    --arg wf_slug "$WF_SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "credential",
      resource_id: (.credential_id // (.credential_type + ":" + (.credential_name // "unknown"))),
      resource_name: (.credential_name // "unknown"),
      detail: { credential_type: .credential_type, credential_id: .credential_id, credential_name: .credential_name },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/credentials.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "http-url",
      resource_id: (.host // "dynamic-host"),
      resource_name: (.host // "dynamic-host"),
      detail: { url: .url, method: .method, host: .host },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/http-urls.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "database",
      resource_id: (.engine + "/" + (.credential.id // "no-cred")),
      resource_name: (.engine + " (via " + (.credential.name // "no-credential") + ")"),
      detail: { engine: .engine, credential: .credential, operation: .operation, table: .table, schema: .schema, query_snippet: .query_snippet },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/databases.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "llm-model",
      resource_id: ((.provider // "unknown") + "/" + (.model // "unspecified")),
      resource_name: ((.provider // "?") + " / " + (.model // "unspecified")),
      detail: { provider: .provider, model: .model, node_type: .node_type },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/llm-models.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "env-var",
      resource_id: .var_name,
      resource_name: .var_name,
      detail: { var_name: .var_name },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/env-vars.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "custom-node",
      resource_id: (.package // .type),
      resource_name: (.package // .type),
      detail: { package: .package, type: .type },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/custom-nodes.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "trigger",
      resource_id: (.trigger_type + ":" + (.path // .schedule // .node_id)),
      resource_name: (.trigger_type + " — " + (.path // .schedule // .node_name)),
      detail: { trigger_type: .trigger_type, node_type: .node_type, path: .path, method: .method, schedule: .schedule },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/triggers.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "workflow-callee",
      resource_id: .target_workflow_id,
      resource_name: .target_workflow_id,
      detail: { target_workflow_id: .target_workflow_id },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/subworkflows.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "google-sheets",
      resource_id: .spreadsheet_id,
      resource_name: (.spreadsheet_name // .spreadsheet_id),
      detail: {
        spreadsheet_id: .spreadsheet_id,
        spreadsheet_name: .spreadsheet_name,
        spreadsheet_url: .spreadsheet_url,
        sheet_tab_name: .sheet_tab_name,
        operation: .operation
      },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/google-sheets.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "google-drive",
      resource_id: .drive_id,
      resource_name: (.drive_name // .drive_id),
      detail: { kind: .kind, drive_id: .drive_id, drive_name: .drive_name, drive_url: .drive_url, operation: .operation },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/google-drive.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "data-table",
      resource_id: .table_id,
      resource_name: (.table_name // .table_id),
      detail: { table_id: .table_id, table_name: .table_name, table_url: .table_url, operation: .operation },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/data-tables.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "slack-channel",
      resource_id: .channel_id,
      resource_name: (.channel_name // .channel_id),
      detail: { channel_id: .channel_id, channel_name: .channel_name, operation: .operation },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/slack-channels.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "github-repo",
      resource_id: .repo_full,
      resource_name: .repo_full,
      detail: { owner: .owner, repository: .repository, repo_url: .repo_url, operation: .operation, resource: .resource },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/github-repos.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "google-doc",
      resource_id: .document_id,
      resource_name: (.document_name // .document_id),
      detail: { document_id: .document_id, document_name: .document_name, operation: .operation },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/google-docs.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "s3-bucket",
      resource_id: .bucket,
      resource_name: .bucket,
      detail: { bucket: .bucket, operation: .operation, file_name: .file_name },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/s3-buckets.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "kafka-topic",
      resource_id: .topic,
      resource_name: .topic,
      detail: { topic: .topic, role: .role, group_id: .group_id },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/kafka-topics.json" >> "$USAGES_JSONL"

  jq -c \
    --arg wf_slug "$SLUG" --arg wf_id "$ID" --arg wf_name "$NAME" \
    '.[] | {
      type: "mcp-server",
      resource_id: .endpoint_url,
      resource_name: (.host // .endpoint_url),
      detail: { endpoint_url: .endpoint_url, host: .host },
      workflow: { id: $wf_id, slug: $wf_slug, name: $wf_name },
      node: { name: .node_name, id: .node_id }
    }' "$TMPDIR/mcp-clients.json" >> "$USAGES_JSONL"

  # ---- Render the workflow note (only if it doesn't already exist) ----
  if [ -e "$NOTE" ]; then
    echo "exists, skipping write: $NOTE" >&2
    continue
  fi

  # Pre-compute the sub-workflow rendered lines (need name resolution)
  SUB_LINES_FILE="$TMPDIR/sub-lines.txt"
  : > "$SUB_LINES_FILE"
  while IFS= read -r line; do
    tid=$(printf '%s' "$line" | jq -r '.target_workflow_id // ""')
    nname=$(printf '%s' "$line" | jq -r '.node_name')
    nid=$(printf '%s' "$line" | jq -r '.node_id')
    if [ -n "$tid" ]; then
      resolved=$(id_to_slug_name "$tid")
      tslug="${resolved%%|*}"; tname="${resolved##*|}"
      if [ -n "$tslug" ]; then
        echo "- [[$tslug|$tname]] (n8n_id \`$tid\`) — node \"$nname\" (id \`$nid\`)" >> "$SUB_LINES_FILE"
      else
        echo "- *unresolved* n8n_id \`$tid\` — node \"$nname\" (id \`$nid\`)" >> "$SUB_LINES_FILE"
      fi
    fi
  done < <(jq -c '.[]?' "$TMPDIR/subworkflows.json")

  # Tags as YAML — always a space after the key
  TAGS_YAML=$(jq -r '.tags // [] | map(.name) | if length == 0 then " []" else "\n" + (map("  - \"" + . + "\"") | join("\n")) end' < "$WF")

  {
    cat <<EOF
---
n8n_id: "$ID"
instance: $INSTANCE
name: "$NAME"
status: $STATUS
last_modified: $LAST_MOD
tags:$TAGS_YAML
fingerprint: "$FP"
auto_generated_at: $NOW
---

<!-- auto:start -->

# $NAME

## Summary

- **Status:** $STATUS
- **n8n ID:** \`$ID\`
- **Nodes:** $NODE_COUNT
- **Last modified:** $LAST_MOD

EOF

    if [ "$(jq 'length' "$TMPDIR/triggers.json")" -gt 0 ]; then
      echo "## Triggers"; echo
      jq -r '.[] | "- **\(.trigger_type)** — node \"\(.node_name)\" (id `\(.node_id)`)" + (
        if .path then " — \(.method // "GET") `\(.path)`"
        elif .schedule then " — `\(.schedule)`"
        else "" end
      )' "$TMPDIR/triggers.json"
      echo
    fi

    HAS_DEPS=0
    for f in credentials http-urls databases llm-models env-vars subworkflows custom-nodes google-sheets google-drive data-tables slack-channels github-repos google-docs s3-buckets kafka-topics mcp-clients; do
      [ "$(jq 'length' "$TMPDIR/$f.json")" -gt 0 ] && HAS_DEPS=1
    done

    if [ $HAS_DEPS -eq 1 ]; then
      echo "## Depends on"; echo

      if [ "$(jq 'length' "$TMPDIR/credentials.json")" -gt 0 ]; then
        echo "### Credentials"; echo
        jq -r '.[] | "- [[../resources/credentials/" + ((.credential_id // (.credential_type + "-" + (.credential_name // "unknown"))) | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase) + "|" + (.credential_name // "unknown") + "]] (`\(.credential_type)`, id `\(.credential_id // "—")`) — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/credentials.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/http-urls.json")" -gt 0 ]; then
        echo "### HTTP URLs"; echo
        jq -r '.[] | "- " + (if .host then "[[../resources/http-urls/\(.host | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase)|\(.host)]]" else "*(dynamic URL)*" end) + " — `\(.method) \(.url)` — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/http-urls.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/databases.json")" -gt 0 ]; then
        echo "### Databases"; echo
        jq -r '.[] | "- [[../resources/databases/" + ((.engine + "-" + (.credential.id // "no-cred")) | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase) + "|" + .engine + " (via " + (.credential.name // "no-credential") + ")]] — op `\(.operation // "?")`" + (if .table then ", table `\(.table)`" else "" end) + " — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/databases.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/llm-models.json")" -gt 0 ]; then
        echo "### LLM models"; echo
        jq -r '.[] | "- [[../resources/llm-models/" + ((.provider // "unknown") + "-" + (.model // "unspecified") | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase) + "|\(.provider // "?") / \(.model // "?")]] — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/llm-models.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/env-vars.json")" -gt 0 ]; then
        echo "### Env vars"; echo
        jq -r '.[] | "- [[../resources/env-vars/\(.var_name | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase)|\(.var_name)]] — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/env-vars.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/custom-nodes.json")" -gt 0 ]; then
        echo "### Custom / community nodes"; echo
        jq -r '.[] | "- [[../resources/custom-nodes/\((.package // .type) | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase)|\(.package // .type)]] — type `\(.type)` — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/custom-nodes.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/google-sheets.json")" -gt 0 ]; then
        echo "### Google Sheets"; echo
        jq -r '.[] | "- " + (if (.spreadsheet_id | startswith("=")) then "*(dynamic spreadsheet)*" else "[[../resources/google-sheets/\(.spreadsheet_id | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase)|\(.spreadsheet_name // .spreadsheet_id)]] (id `\(.spreadsheet_id)`)" end) + " — op `\(.operation // "?")`, tab `\(.sheet_tab_name // "?")` — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/google-sheets.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/google-drive.json")" -gt 0 ]; then
        echo "### Google Drive"; echo
        jq -r '.[] | "- " + (if (.drive_id | startswith("=")) then "*(dynamic)*" else "[[../resources/google-drive/\(.drive_id | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase)|\(.drive_name // .drive_id)]] (`\(.kind)`, id `\(.drive_id)`)" end) + " — op `\(.operation // "?")` — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/google-drive.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/data-tables.json")" -gt 0 ]; then
        echo "### Data tables (n8n)"; echo
        jq -r '.[] | "- [[../resources/data-tables/\(.table_id | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase)|\(.table_name // .table_id)]] (id `\(.table_id)`) — op `\(.operation // "?")` — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/data-tables.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/slack-channels.json")" -gt 0 ]; then
        echo "### Slack channels"; echo
        jq -r '.[] | "- " + (if (.channel_id | startswith("=")) then "*(dynamic channel)*" else "[[../resources/slack-channels/\(.channel_id | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase)|\(.channel_name // .channel_id)]] (id `\(.channel_id)`)" end) + " — op `\(.operation // "?")` — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/slack-channels.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/github-repos.json")" -gt 0 ]; then
        echo "### GitHub repos"; echo
        jq -r '.[] | "- [[../resources/github-repos/\(.repo_full | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase)|\(.repo_full)]] — op `\(.operation // "?")` on `\(.resource // "—")` — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/github-repos.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/google-docs.json")" -gt 0 ]; then
        echo "### Google Docs"; echo
        jq -r '.[] | "- " + (if (.document_id | startswith("=")) then "*(dynamic doc)*" else "[[../resources/google-docs/\(.document_id | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase)|\(.document_name // .document_id)]] (id `\(.document_id)`)" end) + " — op `\(.operation // "?")` — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/google-docs.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/s3-buckets.json")" -gt 0 ]; then
        echo "### AWS S3 buckets"; echo
        jq -r '.[] | "- " + (if (.bucket | startswith("=")) then "*(dynamic bucket)*" else "[[../resources/s3-buckets/\(.bucket | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase)|\(.bucket)]]" end) + " — op `\(.operation // "?")` — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/s3-buckets.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/kafka-topics.json")" -gt 0 ]; then
        echo "### Kafka topics"; echo
        jq -r '.[] | "- [[../resources/kafka-topics/\(.topic | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase)|\(.topic)]] (`\(.role)`) — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/kafka-topics.json"
        echo
      fi

      if [ "$(jq 'length' "$TMPDIR/mcp-clients.json")" -gt 0 ]; then
        echo "### MCP servers (external)"; echo
        jq -r '.[] | "- [[../resources/mcp-servers/\(.endpoint_url | gsub("[^A-Za-z0-9]+"; "-") | ascii_downcase)|\(.host // .endpoint_url)]] — `\(.endpoint_url)` — node \"\(.node_name)\" (id `\(.node_id)`)"' "$TMPDIR/mcp-clients.json"
        echo
      fi

      if [ -s "$SUB_LINES_FILE" ]; then
        echo "### Sub-workflows (Execute Workflow calls)"; echo
        cat "$SUB_LINES_FILE"
        echo
      fi
    fi

    echo "## Used by (workflows)"; echo
    echo "*(populated in the resource-aggregation pass after all workflows are rendered)*"
    echo

    cat <<'EOF'
<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
EOF

  } > "$NOTE"

  echo "wrote $NOTE" >&2
done < "$TARGETS_FILE"

# ============================================================
# Resource note pass — aggregate usages.jsonl into per-resource notes.
# ============================================================

if [ ! -s "$USAGES_JSONL" ]; then
  echo "no usage records — nothing to aggregate" >&2
  exit 0
fi

# Group by (type, resource_id) into resource records with aliases + usages
RESOURCES_JSONL="$CACHE/render-tmp/resources.jsonl"
jq -cs '
  # Drop usages where resource_id is a dynamic expression (={{ ... }}) — they
  # are not stable identifiers and would create useless "dynamic" resource notes.
  map(select(.resource_id | tostring | startswith("=") | not))
  | group_by([.type, .resource_id])
  | map({
      type: .[0].type,
      resource_id: .[0].resource_id,
      aliases: (map(.resource_name) | unique),
      current_name: (.[0].resource_name),
      detail: (.[0].detail),
      usages: (map({workflow, node, detail}) | sort_by(.workflow.slug, .node.name))
    })
  | .[]
' "$USAGES_JSONL" > "$RESOURCES_JSONL"

echo "$(wc -l < "$RESOURCES_JSONL" | tr -d ' ') unique resources to render" >&2

# Render each resource
while IFS= read -r resource; do
  rtype=$(printf '%s' "$resource" | jq -r '.type')
  rid=$(printf '%s'   "$resource" | jq -r '.resource_id')
  rname=$(printf '%s' "$resource" | jq -r '.current_name')

  # slugify the resource_id for the filename (avoid weird chars in paths)
  rid_slug=$(printf '%s' "$rid" | slugify)

  case "$rtype" in
    credential)         dir="$VAULT/resources/credentials" ;;
    http-url)           dir="$VAULT/resources/http-urls" ;;
    database)           dir="$VAULT/resources/databases" ;;
    llm-model)          dir="$VAULT/resources/llm-models" ;;
    env-var)            dir="$VAULT/resources/env-vars" ;;
    custom-node)        dir="$VAULT/resources/custom-nodes" ;;
    google-sheets)      dir="$VAULT/resources/google-sheets" ;;
    google-drive)       dir="$VAULT/resources/google-drive" ;;
    data-table)         dir="$VAULT/resources/data-tables" ;;
    slack-channel)      dir="$VAULT/resources/slack-channels" ;;
    github-repo)        dir="$VAULT/resources/github-repos" ;;
    google-doc)         dir="$VAULT/resources/google-docs" ;;
    s3-bucket)          dir="$VAULT/resources/s3-buckets" ;;
    kafka-topic)        dir="$VAULT/resources/kafka-topics" ;;
    mcp-server)         dir="$VAULT/resources/mcp-servers" ;;
    trigger)            dir="$VAULT/resources/triggers" ;;
    workflow-callee)
      # Don't write a separate resource note for sub-workflow callees;
      # instead, patch the callee's workflow note in the "Used by" pass below.
      continue ;;
    *) echo "WARN: unknown resource type $rtype" >&2; continue ;;
  esac

  # Trigger resource notes: only webhook, schedule, cron. The rest
  # (error / manual / execute-workflow / other) are control flow primitives,
  # not impact-analysis resources.
  if [ "$rtype" = "trigger" ]; then
    ttype=$(printf '%s' "$resource" | jq -r '.detail.trigger_type')
    case "$ttype" in
      webhook|schedule|cron) ;;
      *) continue ;;
    esac
  fi

  note="$dir/$rid_slug.md"
  if [ -e "$note" ]; then
    echo "exists, skipping: $note" >&2
    continue
  fi

  {
    cat <<EOF
---
type: $rtype
instance: $INSTANCE
resource_id: "$rid"
current_name: $(printf '%s' "$rname" | jq -Rs .)
aliases: $(printf '%s' "$resource" | jq -c '.aliases')
auto_generated_at: $NOW
---

<!-- auto:start -->

# $rname

- **Resource id (canonical):** \`$rid\`
- **Current name:** $rname
EOF

    aliases_count=$(printf '%s' "$resource" | jq '.aliases | length')
    if [ "$aliases_count" -gt 1 ]; then
      echo "- **Historical aliases:**"
      printf '%s' "$resource" | jq -r '.aliases[] | "  - " + .'
    fi

    # Type-specific detail block
    case "$rtype" in
      credential)
        ctype=$(printf '%s' "$resource" | jq -r '.detail.credential_type // "—"')
        echo "- **n8n credential type:** \`$ctype\`"
        ;;
      http-url)
        host=$(printf '%s' "$resource" | jq -r '.detail.host // "—"')
        echo "- **Host:** \`$host\`"
        ;;
      database)
        engine=$(printf '%s' "$resource" | jq -r '.detail.engine')
        cname=$(printf '%s' "$resource" | jq -r '.detail.credential.name // "—"')
        echo "- **Engine:** \`$engine\`"
        echo "- **Credential:** $cname"
        ;;
      llm-model)
        prov=$(printf '%s' "$resource" | jq -r '.detail.provider // "—"')
        model=$(printf '%s' "$resource" | jq -r '.detail.model // "—"')
        echo "- **Provider:** \`$prov\`"
        echo "- **Model:** \`$model\`"
        ;;
      env-var)
        echo "- **Variable name:** \`$rid\`"
        ;;
      custom-node)
        echo "- **Package:** \`$rid\`"
        ;;
      google-sheets)
        url=$(printf '%s' "$resource" | jq -r '.detail.spreadsheet_url // empty')
        [ -n "$url" ] && echo "- **URL:** $url"
        echo "- **Spreadsheet ID:** \`$rid\`"
        ;;
      google-drive)
        url=$(printf '%s' "$resource" | jq -r '.detail.drive_url // empty')
        kind=$(printf '%s' "$resource" | jq -r '.detail.kind // "—"')
        echo "- **Kind:** $kind"
        [ -n "$url" ] && echo "- **URL:** $url"
        echo "- **Drive resource ID:** \`$rid\`"
        ;;
      data-table)
        url=$(printf '%s' "$resource" | jq -r '.detail.table_url // empty')
        [ -n "$url" ] && echo "- **Path:** \`$url\`"
        echo "- **Table ID:** \`$rid\`"
        ;;
      slack-channel)
        echo "- **Channel ID:** \`$rid\`"
        ;;
      github-repo)
        owner=$(printf '%s' "$resource" | jq -r '.detail.owner')
        repo=$(printf '%s' "$resource" | jq -r '.detail.repository')
        url=$(printf '%s' "$resource" | jq -r '.detail.repo_url // empty')
        echo "- **Owner:** \`$owner\`"
        echo "- **Repository:** \`$repo\`"
        [ -n "$url" ] && echo "- **URL:** $url"
        ;;
      google-doc)
        echo "- **Document ID:** \`$rid\`"
        ;;
      s3-bucket)
        echo "- **Bucket:** \`$rid\`"
        ;;
      kafka-topic)
        echo "- **Topic:** \`$rid\`"
        ;;
      mcp-server)
        host=$(printf '%s' "$resource" | jq -r '.detail.host // "—"')
        echo "- **Host:** \`$host\`"
        echo "- **Endpoint URL:** \`$rid\`"
        ;;
      trigger)
        ttype=$(printf '%s' "$resource" | jq -r '.detail.trigger_type')
        echo "- **Trigger type:** \`$ttype\`"
        path=$(printf '%s' "$resource" | jq -r '.detail.path // empty')
        sched=$(printf '%s' "$resource" | jq -r '.detail.schedule // empty')
        [ -n "$path" ]  && echo "- **Path:** \`$path\` (\`$(printf '%s' "$resource" | jq -r '.detail.method // "GET"')\`)"
        [ -n "$sched" ] && echo "- **Schedule:** \`$sched\`"
        ;;
    esac

    echo
    echo "## Used by"
    echo

    # Usage list, sorted by workflow slug
    if [ "$rtype" = "http-url" ]; then
      # Group URLs by path for HTTP — useful to see distinct endpoints
      printf '%s' "$resource" | jq -r '
        .usages
        | sort_by(.workflow.slug, .detail.url)
        | .[]
        | "- [[../../workflows/\(.workflow.slug)|\(.workflow.name)]] — `\(.detail.method // "GET") \(.detail.url)` — node \"\(.node.name)\" (id `\(.node.id)`)"'
    elif [ "$rtype" = "google-sheets" ]; then
      printf '%s' "$resource" | jq -r '
        .usages
        | sort_by(.workflow.slug, .detail.sheet_tab_name)
        | .[]
        | "- [[../../workflows/\(.workflow.slug)|\(.workflow.name)]] — op `\(.detail.operation // "?")`, tab `\(.detail.sheet_tab_name // "?")` — node \"\(.node.name)\" (id `\(.node.id)`)"'
    elif [ "$rtype" = "database" ]; then
      printf '%s' "$resource" | jq -r '
        .usages
        | sort_by(.workflow.slug, .node.name)
        | .[]
        | "- [[../../workflows/\(.workflow.slug)|\(.workflow.name)]] — op `\(.detail.operation // "?")`" + (if .detail.table then ", table `\(.detail.table)`" else "" end) + " — node \"\(.node.name)\" (id `\(.node.id)`)"'
    else
      printf '%s' "$resource" | jq -r '
        .usages
        | sort_by(.workflow.slug, .node.name)
        | .[]
        | "- [[../../workflows/\(.workflow.slug)|\(.workflow.name)]] — node \"\(.node.name)\" (id `\(.node.id)`)"'
    fi

    echo

    cat <<'EOF'
<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
EOF

  } > "$note"

  echo "wrote $note" >&2
done < "$RESOURCES_JSONL"

# ============================================================
# Patch "Used by (workflows)" section on workflow notes — bidirectional sub-workflow links.
# ============================================================

# For each unique target workflow id that received a callee usage, gather callers
# and append them to the callee's workflow note (if one exists in $VAULT/workflows/).

jq -cs '
  map(select(.type == "workflow-callee"))
  | group_by(.resource_id)
  | map({
      target_id: .[0].resource_id,
      callers: (map({workflow, node}) | sort_by(.workflow.slug, .node.name))
    })
  | .[]
' "$USAGES_JSONL" > "$CACHE/render-tmp/callees.jsonl"

while IFS= read -r callee; do
  target_id=$(printf '%s' "$callee" | jq -r '.target_id')
  resolved=$(id_to_slug_name "$target_id")
  target_slug="${resolved%%|*}"
  [ -z "$target_slug" ] && continue
  target_note="$VAULT/workflows/$target_slug.md"
  [ ! -e "$target_note" ] && continue

  # Build the "Used by" section content to a file (avoids awk -v newline issues).
  block_file="$CACHE/render-tmp/used-by-$target_id.txt"
  printf '%s' "$callee" | jq -r '
    .callers[]
    | "- [[" + .workflow.slug + "|" + .workflow.name + "]] — node \"\(.node.name)\" (id `\(.node.id)`)"
  ' > "$block_file"

  placeholder='*(populated in the resource-aggregation pass after all workflows are rendered)*'
  if grep -qF "$placeholder" "$target_note"; then
    tmp="$target_note.tmp"
    awk -v ph="$placeholder" -v bf="$block_file" '
      BEGIN {
        block = ""
        while ((getline line < bf) > 0) {
          block = (block == "" ? line : block "\n" line)
        }
        close(bf)
      }
      index($0, ph) > 0 { print block; next }
      { print }
    ' "$target_note" > "$tmp" && mv "$tmp" "$target_note"
    echo "patched Used-by on $target_note" >&2
  fi
done < "$CACHE/render-tmp/callees.jsonl"

# Final report
echo "--- render done ---" >&2
echo "workflow notes:      $(ls "$VAULT/workflows" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "credential notes:    $(ls "$VAULT/resources/credentials" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "http-url notes:      $(ls "$VAULT/resources/http-urls" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "database notes:      $(ls "$VAULT/resources/databases" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "trigger notes:       $(ls "$VAULT/resources/triggers" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "llm-model notes:     $(ls "$VAULT/resources/llm-models" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "env-var notes:       $(ls "$VAULT/resources/env-vars" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "custom-node notes:   $(ls "$VAULT/resources/custom-nodes" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "google-sheets notes: $(ls "$VAULT/resources/google-sheets" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "google-drive notes:  $(ls "$VAULT/resources/google-drive" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "data-table notes:    $(ls "$VAULT/resources/data-tables" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "slack-channel notes: $(ls "$VAULT/resources/slack-channels" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "github-repo notes:   $(ls "$VAULT/resources/github-repos" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "google-doc notes:    $(ls "$VAULT/resources/google-docs" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "s3-bucket notes:     $(ls "$VAULT/resources/s3-buckets" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "kafka-topic notes:   $(ls "$VAULT/resources/kafka-topics" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
echo "mcp-server notes:    $(ls "$VAULT/resources/mcp-servers" 2>/dev/null | grep -v '^\.gitkeep$' | wc -l | tr -d ' ')" >&2
