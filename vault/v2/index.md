---
type: index
instance: v2
auto_generated_at: 2026-08-28T20:46:45Z
---

<!-- auto:start -->

# n8n Vault — v2 (New instance)

## About

This subtree mirrors the **New n8n instance** (alias `v2`). It is a Claude-driven, Obsidian-native knowledge base derived from that live instance: one note per workflow under `workflows/`, one note per unique resource under `resources/<type>/`, and dated changelogs under `changelogs/`.

See `../../CLAUDE.md` (repo root) for the intent → runbook map and the manual / auto block contract.

## Sections

- `workflows/` — 2 notes; one per n8n workflow
- **Resources** — `resources/<type>/` (categories surface as the taxonomy grows):
  - `resources/credentials/` — 1
  - `resources/http-urls/` — 1
- `changelogs/` — 1 notes; one per refresh-day that produced semantic change

## How to find things

- **Reverse lookup** ("what uses X?") — open the resource note; the auto block lists every `(workflow, node)` pair touching it.
- **Forward lookup** ("what does this workflow touch?") — open the workflow note.
- **Refresh the vault** — ask Claude to sync `v2`; the runbook at `../../agent-os/standards/sync/refresh-procedure.md` drives it.

## Last refreshed

2026-08-28T20:46:45Z

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add orientation prose for newcomers, project-specific notes, links to runbooks, on-call pointers, etc. -->

<!-- manual:end -->
