---
type: index
auto_generated_at: 2026-06-02T00:08:53Z
---

<!-- auto:start -->

# n8n Vault

## About

This vault is a Claude-driven, Obsidian-native knowledge base derived from a live n8n instance. Every workflow has a note under `workflows/`; every credential, service, database, trigger, LLM model, HTTP host, env var, custom node — and any other discovered category — has a note under `resources/<type>/` with reverse-lookup links to the workflows that use it. Dated changelog notes record what changed on each refresh.

See `../CLAUDE.md` (repo root) for the intent → runbook map and the manual / auto block contract that protects hand-written annotations across refreshes.

## Sections

Browse these folders via the file-explorer sidebar — Obsidian has no built-in way to link to a folder (both `[[wiki]]` and `[md](folder/)` links auto-create blank notes on click), so paths here are shown as code only.

- `workflows/` — 202 notes; one per n8n workflow
- **Resources** — `vault/resources/<type>/`, alphabetical (new categories surface automatically as the taxonomy grows):
  - `resources/credentials/` — 62
  - `resources/custom-nodes/` — 11
  - `resources/data-tables/` — 21
  - `resources/databases/` — 8
  - `resources/env-vars/` — 1
  - `resources/github-repos/` — 2
  - `resources/google-docs/` — 3
  - `resources/google-drive/` — 26
  - `resources/google-sheets/` — 68
  - `resources/http-urls/` — 43
  - `resources/kafka-topics/` — 4
  - `resources/llm-models/` — 16
  - `resources/mcp-servers/` — 2
  - `resources/s3-buckets/` — 1
  - `resources/services/` — 0
  - `resources/slack-channels/` — 51
  - `resources/triggers/` — 103
- `changelogs/` — 0 notes; one per refresh-day that produced semantic change

## How to find things

- **Reverse lookup** ("what uses X?") — open the resource note; the auto block lists every `(workflow, node)` pair touching it.
- **Forward lookup** ("what does this workflow touch?") — open the workflow note; the auto block lists every resource it depends on.
- **What changed today?** — open the most recent file under `changelogs/`.
- **Refresh the vault** — ask Claude; the runbook at `../agent-os/standards/sync/refresh-procedure.md` drives the sync.

## Last refreshed

2026-06-02T00:08:53Z

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add orientation prose for newcomers, project-specific notes, links to runbooks, on-call pointers, etc. -->

<!-- manual:end -->
