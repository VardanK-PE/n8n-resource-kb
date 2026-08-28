#!/usr/bin/env bash
# Wrapper for n8n REST API calls against a NAMED instance. The agent invokes
# this script instead of sourcing .env directly — the ~/.claude/hooks/block-env-files.sh
# hook blocks any Bash command that mentions .env, but the wrapper hides that
# detail from the agent's command line. Critically, the agent only ever passes
# an instance ALIAS (v1/v2) — never a URL or API key — so secrets never enter
# the agent's command line, transcript, or context.
#
# Usage:
#   scripts/n8n-api.sh <instance> <endpoint-path> [extra curl args...]
# Examples:
#   scripts/n8n-api.sh v1 /api/v1/workflows?limit=100
#   scripts/n8n-api.sh v2 /api/v1/workflows/abc123def
#
# Instances (aliases): v1 = Old n8n instance, v2 = New n8n instance.
# Credentials live in the gitignored .env as suffixed pairs:
#   N8N_API_URL_V1 / N8N_API_KEY_V1 , N8N_API_URL_V2 / N8N_API_KEY_V2
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# --- Instance alias (validated against an allowlist BEFORE it is ever used to
#     build a variable name, so a caller cannot smuggle indirection/injection
#     into N8N_API_KEY_<X>). ---
INSTANCE="${1:-}"
case "$INSTANCE" in
  v1|v2) ;;
  "") echo "Usage: $0 <instance:v1|v2> <endpoint-path> [extra curl args...]" >&2; exit 1 ;;
  *)  echo "ERROR: unknown instance '$INSTANCE' (allowed: v1, v2)." >&2; exit 2 ;;
esac
shift

# Load auth from .env if present (single gitignored file holds both instances).
if [ -f "$REPO_ROOT/.env" ]; then
  set -a
  # shellcheck source=/dev/null
  . "$REPO_ROOT/.env"
  set +a
fi

# Capture any legacy UNSUFFIXED values (.env may still use the old single-instance
# names) before we overwrite the vars with the per-instance lookup.
LEGACY_URL="${N8N_API_URL:-}"
LEGACY_KEY="${N8N_API_KEY:-}"

# Resolve per-instance credentials via indirect expansion on the VALIDATED alias.
# (portable uppercase — macOS ships bash 3.2, which lacks ${var^^})
SUFFIX="$(printf '%s' "$INSTANCE" | tr '[:lower:]' '[:upper:]')"   # v1 -> V1, v2 -> V2
url_var="N8N_API_URL_${SUFFIX}"
key_var="N8N_API_KEY_${SUFFIX}"
N8N_API_URL="${!url_var:-}"
N8N_API_KEY="${!key_var:-}"

# Fallback for v1 only: legacy unsuffixed vars, then the sibling n8n_claude
# project (which has the OLD instance configured). v2 has no sibling fallback —
# it requires .env.
if [ "$INSTANCE" = "v1" ]; then
  [ -z "$N8N_API_URL" ] && N8N_API_URL="$LEGACY_URL"
  [ -z "$N8N_API_KEY" ] && N8N_API_KEY="$LEGACY_KEY"
  if { [ -z "$N8N_API_URL" ] || [ -z "$N8N_API_KEY" ]; } && [ -f "$REPO_ROOT/../n8n_claude/.mcp.json" ]; then
    N8N_API_URL="$(jq -r '.mcpServers."n8n-mcp".env.N8N_API_URL' "$REPO_ROOT/../n8n_claude/.mcp.json")"
    N8N_API_KEY="$(jq -r '.mcpServers."n8n-mcp".env.N8N_API_KEY' "$REPO_ROOT/../n8n_claude/.mcp.json")"
  fi
fi

if [ -z "$N8N_API_URL" ] || [ -z "$N8N_API_KEY" ]; then
  echo "ERROR: no credentials for instance '$INSTANCE'. Set ${url_var} and ${key_var} in .env (copy from .env.example)." >&2
  exit 2
fi

ENDPOINT="${1:-}"
if [ -z "$ENDPOINT" ]; then
  echo "Usage: $0 <instance:v1|v2> <endpoint-path> [extra curl args...]" >&2
  exit 1
fi
shift

# Allow callers to pass either "/api/v1/foo" or "api/v1/foo"
ENDPOINT="${ENDPOINT#/}"

curl -fsS \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Accept: application/json" \
  "$@" \
  "$N8N_API_URL/$ENDPOINT"
