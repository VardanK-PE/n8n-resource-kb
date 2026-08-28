#!/usr/bin/env bash
# Categorize an instance's workflows for a refresh, comparing the live cache
# against the current vault notes. Emits one tab-separated line per workflow:
#
#   <CATEGORY>\t<id>\t<note-slug-or-->\t<detail>
#
# Categories:
#   ADDED      - live in n8n, no note yet, and eligible for one
#   SKIPPED    - live in n8n, no note, but intentionally noteless per the render
#                policy (archived, or a backup/bk/copy-named workflow)
#   MODIFIED   - fingerprint differs (semantic/logic change)
#   RENAMED    - fingerprint MATCHES but the workflow name changed. This is the
#                case a fingerprint-only check misses: per fingerprint.md the name
#                is deliberately NOT hashed, so renames must be caught here.
#   STATUS_CHANGED - active/archived state flipped without a logic change
#                (e.g. active -> inactive, or inactive -> archived)
#   REMOVED    - has a note (status != deleted) but is gone from n8n
#   UNCHANGED  - fingerprint, name and status all match
#
# A workflow can be both MODIFIED and RENAMED; MODIFIED takes precedence in the
# emitted category, with "renamed" noted in the detail column.
#
# Usage:  scripts/detect-changes.sh <v1|v2>
# Requires: Step 1 of the refresh has populated vault/<inst>/_cache/.
set -euo pipefail

INST="${1:-}"
case "$INST" in
  v1|v2) ;;
  *) echo "usage: $0 <v1|v2>" >&2; exit 2 ;;
esac

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"
CACHE="vault/$INST/_cache"
WFDIR="vault/$INST/workflows"

test -s "$CACHE/list.jsonl" || { echo "ERROR: $CACHE/list.jsonl missing — run refresh Step 1 first." >&2; exit 2; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
NOTES="$TMP/notes.tsv"   # id \t name \t status \t fingerprint \t slug
LIVE="$TMP/live.tsv"     # id \t name \t status \t fingerprint \t skip(0|1)

# Mirrors scripts/render-vault.sh's --all filter: archived or backup/bk/copy-named
# workflows are intentionally not given notes.
SKIP_NAME_REGEX='(^|[^a-z])(bk|backup|copy|archived?)([^a-z]|$)|backup[ _-]*[0-9]'
: > "$NOTES"; : > "$LIVE"

# --- Index existing notes (id -> name/status/fingerprint/slug) ---
for f in "$WFDIR"/*.md; do
  [ -e "$f" ] || continue
  awk -F': ' '
    /^n8n_id:/     { gsub(/"/,"",$2); id=$2 }
    /^name:/       { s=$0; sub(/^name: /,"",s); gsub(/^"|"$/,"",s); nm=s }
    /^status:/     { st=$2 }
    /^fingerprint:/{ gsub(/"/,"",$2); fp=$2 }
    /^---/         { if (seen++) { print id "\t" nm "\t" st "\t" fp; exit } }
  ' "$f" | while IFS=$'\t' read -r id nm st fp; do
    printf '%s\t%s\t%s\t%s\t%s\n' "$id" "$nm" "$st" "$fp" "$(basename "$f" .md)" >> "$NOTES"
  done
done

# --- Compute live state (id -> name/status/fingerprint) ---
while IFS= read -r id; do
  j="$CACHE/workflows/$id.json"
  [ -s "$j" ] || continue
  nm=$(jq -r '.name' "$j")
  # Match render-vault.sh's status precedence: archived > active > inactive.
  st=$(jq -r 'if .isArchived then "archived" elif .active then "active" else "inactive" end' "$j")
  fp=$(jq -cS -f scripts/jq/canonical.jq < "$j" | shasum -a 256 | cut -d' ' -f1)
  skip=$(jq -r --arg re "$SKIP_NAME_REGEX" 'if (.isArchived // false) or ((.name // "") | test($re;"i")) then 1 else 0 end' "$j")
  printf '%s\t%s\t%s\t%s\t%s\n' "$id" "$nm" "$st" "$fp" "$skip" >> "$LIVE"
done < <(jq -r '.id' "$CACHE/list.jsonl")

# --- Categorize (single awk over both tables) ---
awk -F'\t' '
  NR==FNR { n_name[$1]=$2; n_status[$1]=$3; n_fp[$1]=$4; n_slug[$1]=$5; have_note[$1]=1; next }
  {
    id=$1; L_name=$2; L_status=$3; L_fp=$4; L_skip=$5; live_seen[id]=1
    if (!(id in have_note)) {
      if (L_skip=="1") print "SKIPPED\t" id "\t-\t" L_status ": " L_name
      else             print "ADDED\t"   id "\t-\t" L_name
      next
    }
    slug=n_slug[id]
    if (n_fp[id] != L_fp) {
      extra = (n_name[id] != L_name) ? "logic+rename: \"" n_name[id] "\" -> \"" L_name "\"" : "logic change"
      print "MODIFIED\t" id "\t" slug "\t" extra; next
    }
    if (n_name[id] != L_name) { print "RENAMED\t" id "\t" slug "\t\"" n_name[id] "\" -> \"" L_name "\""; next }
    if (n_status[id] != L_status) {
      print "STATUS_CHANGED\t" id "\t" slug "\t" n_status[id] " -> " L_status; next
    }
    print "UNCHANGED\t" id "\t" slug "\t"
  }
  END {
    for (id in have_note) if (!(id in live_seen) && n_status[id] != "deleted")
      print "REMOVED\t" id "\t" n_slug[id] "\t was: " n_name[id]
  }
' "$NOTES" "$LIVE"
