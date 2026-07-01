---
type: index
auto_generated_at: 2026-01-01T00:00:00Z
---

<!-- auto:start -->

# n8n Vault

## About

This vault is a Claude-driven, Obsidian-native knowledge base derived from a live n8n instance. Every workflow has a note under `workflows/`; every credential, service, database, trigger, LLM model, HTTP host, env var, custom node (and any other discovered category) has a note under `resources/<type>/` with reverse-lookup links to the workflows that use it. Dated `changelogs/` notes record what changed on each refresh.

See `CLAUDE.md` (repo root) for the intent → runbook map and the manual / auto block contract.

## Sections

Browse these folders via the file-explorer sidebar — Obsidian has no built-in way to link to a folder (both `[[wiki]]` and `[md](folder/)` links auto-create blank notes on click), so paths here are shown as code only.

- `workflows/` — N notes; one per n8n workflow
- **Resources** — `vault/resources/<type>/`, alphabetical (new categories surface automatically as the taxonomy grows):
  - `resources/credentials/` — N
  - `resources/databases/` — N
  - …
- `changelogs/` — N notes; one per refresh-day that produced semantic change

## Last refreshed

2026-01-01T00:00:00Z

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add orientation prose for newcomers, project-specific notes, links to runbooks, etc. -->

<!-- manual:end -->
