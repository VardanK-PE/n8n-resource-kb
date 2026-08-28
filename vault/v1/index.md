---
type: index
instance: v1
auto_generated_at: 2026-08-28T21:35:46Z
---

<!-- auto:start -->

# n8n Vault — v1 (Old instance)

## About

This subtree is a Claude-driven, Obsidian-native knowledge base derived from the **v1 (Old)** n8n instance. Every workflow has a note under `workflows/`; every credential, service, database, trigger, LLM model, HTTP host, env var, custom node — and any other discovered category — has a note under `resources/<type>/` with reverse-lookup links to the workflows that use it. Dated changelog notes record what changed on each refresh.

See `../../CLAUDE.md` (repo root) for the intent → runbook map and the manual / auto block contract that protects hand-written annotations across refreshes. `../index.md` is the cross-instance router.

## Sections

Browse these folders via the file-explorer sidebar — Obsidian has no built-in way to link to a folder (both `[[wiki]]` and `[md](folder/)` links auto-create blank notes on click), so paths here are shown as code only.

- `workflows/` — 243 notes; one per n8n workflow
- **Resources** — `resources/<type>/`, alphabetical (new categories surface automatically as the taxonomy grows):
  - `resources/credentials/` — 64
  - `resources/custom-nodes/` — 11
  - `resources/data-tables/` — 23
  - `resources/databases/` — 8
  - `resources/env-vars/` — 1
  - `resources/github-repos/` — 2
  - `resources/google-docs/` — 3
  - `resources/google-drive/` — 28
  - `resources/google-sheets/` — 75
  - `resources/http-urls/` — 46
  - `resources/kafka-topics/` — 4
  - `resources/llm-models/` — 18
  - `resources/mcp-servers/` — 2
  - `resources/s3-buckets/` — 1
  - `resources/slack-channels/` — 54
  - `resources/triggers/` — 153
- `changelogs/` — 2 notes; one per refresh-day that produced semantic change

## How to find things

- **Reverse lookup** ("what uses X?") — open the resource note; the auto block lists every `(workflow, node)` pair touching it.
- **Forward lookup** ("what does this workflow touch?") — open the workflow note; the auto block lists every resource it depends on.
- **What changed today?** — open the most recent file under `changelogs/`.
- **Refresh the vault** — ask Claude to sync `v1`; the runbook at `../../agent-os/standards/sync/refresh-procedure.md` drives the sync.

## Last refreshed

2026-08-28T21:35:46Z

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add orientation prose for newcomers, project-specific notes, links to runbooks, on-call pointers, etc. -->

<!-- manual:end -->
