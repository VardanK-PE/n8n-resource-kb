# n8n-resources

A **Claude-driven, Obsidian-native knowledge base** for an n8n instance. The vault under `vault/` is fully derived from the live n8n instance (plus hand-written annotations), and kept in sync conversationally through Claude Code.

It turns an opaque n8n instance into a browsable, queryable graph so you can answer questions like:

- **Reverse lookup** — "Which workflows use this credential / database table / LLM model / HTTP endpoint?" (needed before rotating a secret or deprecating a service)
- **Forward lookup** — "What does this workflow actually touch?" — a clean inventory of every dependency, down to the specific node name and ID.
- **Change history** — "What changed since the last sync?" — human-readable, dated changelogs.

There is **no service to deploy, no build step, and no test suite**. The "runtime" is Claude Code talking to the n8n REST API and writing markdown.

## How it works

- The **n8n instance** (REST API) is the source of truth.
- **Claude Code** is the sync engine — it fetches workflows, extracts their dependencies via `jq`, and writes one markdown note per workflow and per resource.
- **Obsidian** is the browsing UI — open the `vault/` folder as a vault and navigate via `[[wikilinks]]`.
- **git** (this repo) is the durability layer — history of both auto-generated content and manual annotations.

Each note has an **auto-generated block** (rewritten on every refresh) and a **manual-annotation block** (never touched by refresh) separated by explicit markers, so hand-written context — owner, criticality, runbook links — survives syncs.

## Repo layout

```
vault/                    The knowledge base (open this in Obsidian)
  index.md                Router across instances → links to each v<N>/index.md
  v1/  v2/                One isolated subtree per n8n instance (Old / New):
    index.md              Entry point: section overview, counts, navigation
    workflows/            One note per n8n workflow in this instance
    resources/<type>/     One note per unique resource, 17 types
                          (credentials, services, databases, triggers,
                           llm-models, http-urls, env-vars, custom-nodes, …)
    changelogs/YYYY-MM-DD.md  What changed on each refresh day
    _cache/               Fetched workflow JSON — gitignored, regenerable
  _templates/             Shared reference templates Claude follows (not live notes)

agent-os/                 Product docs, standards (the runbooks), current spec
scripts/
  n8n-api.sh              n8n REST API helper — first arg is the instance alias (v1|v2)
  render-vault.sh         Vault rendering helper — takes --instance v1|v2
  jq/*.jq                 Extraction programs that drive every workflow read

CLAUDE.md                 Project router: maps user intent → the right runbook
```

## Setup

1. **Clone** and open the folder in Claude Code.
2. **Credentials** — copy the example env file and fill in both instances' n8n details:
   ```bash
   cp .env.example .env
   # edit .env: set N8N_API_URL_V1/N8N_API_KEY_V1 (Old) and N8N_API_URL_V2/N8N_API_KEY_V2 (New)
   ```
   The credentials file is gitignored and never committed. Claude reaches the API only through `scripts/n8n-api.sh <v1|v2> …`, which keeps keys out of the command line.
3. **Browse the vault** — open the `vault/` directory as an Obsidian vault, or just read the markdown directly. Start at `vault/index.md` (the cross-instance router), then dive into `vault/v1/` or `vault/v2/`.

## Usage

Everything is conversational — talk to Claude Code in this repo. Common intents:

| You say | What happens |
|---|---|
| "refresh the vault" / "sync n8n" | Re-fetches workflows, diffs against last sync, updates notes + writes a changelog |
| "what uses X?" / "what depends on X?" | Reverse lookup — lists every `(workflow, node)` pair touching that resource |
| "what changed today?" | Reads the most recent changelog |
| "note that X is owned by …" | Adds a manual annotation (only in the guarded manual block) |

Claude routes each intent to the corresponding runbook in `agent-os/standards/`. See `CLAUDE.md` for the full map and the hard invariants that keep the vault from getting corrupted.

## What's tracked vs. ignored

**Tracked:** the vault (notes, changelogs, templates, shared `.obsidian/` config), `agent-os/` docs and standards, `scripts/`, and `CLAUDE.md`.

**Ignored** (see `.gitignore`): the credentials file, `.mcp.json`, each instance's `vault/*/_cache/` (regenerable workflow JSON), Obsidian per-user workspace state, per-machine Claude settings, and `.DS_Store`.
