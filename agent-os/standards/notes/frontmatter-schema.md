# Standard: Frontmatter Schema

Every note in the vault has YAML frontmatter. The schema differs by note type but obeys a common rule: **refresh-owned keys are off-limits to manual editing**.

Refresh-owned keys (any note type): `n8n_id`, `fingerprint`, `last_modified`, `status`, `auto_generated_at`, `type`.

## Workflow notes — `vault/workflows/<workflow-name>.md`

```yaml
---
n8n_id: "abc123def456"          # n8n workflow ID (string)
name: "Sync HubSpot to Sheets"  # human name from n8n
status: active                  # active | inactive | deleted
last_modified: 2026-06-01T14:32:11Z  # ISO 8601 UTC, from n8n
tags:                           # n8n tags + any optional user tags
  - production
  - hubspot
fingerprint: "f1a2b3c4..."      # SHA-256 hex; see sync/fingerprint.md
auto_generated_at: 2026-06-01T17:07:00Z  # when refresh last wrote auto block
---
```

Notes:
- `status: deleted` means the workflow disappeared from n8n. The note is preserved (so manual annotations survive); reverse-lookups should treat deleted workflows as historical.
- `tags` is the union of n8n's `tags` field and any tags the user has added manually. Refresh replaces only the n8n-sourced subset; do not remove tags the user added.

## Resource notes — `vault/resources/<type>/<name>.md`

Common shape:

```yaml
---
type: credential                # one of the resource categories below
name: "hubspot-prod"            # canonical resource identifier
auto_generated_at: 2026-06-01T17:07:00Z
---
```

Type-specific additional keys:

| Type | Path | Extra keys |
|---|---|---|
| `credential` | `resources/credentials/` | `credential_type` (e.g. `httpHeaderAuth`, `postgres`), `n8n_credential_id` |
| `service` | `resources/services/` | `host` (when extractable) |
| `database` | `resources/databases/` | `engine` (`postgres` / `mysql` / `mongodb` / …), `host`, `database` |
| `trigger` | `resources/triggers/` | `trigger_type` (`webhook` / `schedule` / `cron` / `event`), plus `path` (webhook) or `cron_expression` (schedule) |
| `llm-model` | `resources/llm-models/` | `provider` (`openai` / `anthropic` / `google` / …), `model` |
| `http-url` | `resources/http-urls/` | `host` (grouping key — the note represents a host, the body lists individual URLs / paths) |
| `env-var` | `resources/env-vars/` | none beyond common |
| `custom-node` | `resources/custom-nodes/` | `package` (npm package name), `version` (when known) |

## Changelog notes — `vault/changelogs/YYYY-MM-DD.md`

```yaml
---
date: 2026-06-01
workflows_added: 2
workflows_modified: 5
workflows_removed: 0
resources_added: 7
resources_removed: 1
taxonomy_gaps: 1
auto_generated_at: 2026-06-01T17:07:00Z
---
```

Changelogs have **no manual block**. They are immutable historical records — manual notes about a change belong on the workflow or resource note, not the changelog.

## Index note — `vault/index.md`

```yaml
---
type: index
auto_generated_at: 2026-06-02T00:03:00Z
---
```

The index is the vault's front door: a single orientation note that surfaces section counts and wikilinks down into `workflows/`, every `resources/<type>/`, and `changelogs/`. There is exactly one canonical path (`vault/index.md`), so no `name` or slug field is needed.

Unlike workflow and resource notes, the index has no `n8n_id`, `fingerprint`, `last_modified`, or `status` — it reflects **vault state**, not n8n state. The only refresh-owned keys are `type: index` (literal string) and `auto_generated_at`.

Unlike changelogs, the index **does** carry a manual block. The auto block holds machine-generated counts and links; the manual block is for hand-written orientation prose the maintainer wants visible on the front page (project context, runbook pointers, on-call notes, etc.). The standard auto / manual contract from `notes/auto-manual-blocks.md` applies.

## Filename conventions

- Slugify names: lowercase, replace runs of non-alphanumerics with `-`, trim leading/trailing `-`.
- Collisions are resolved by appending the n8n ID short prefix: `sync-hubspot-to-sheets.md` vs `sync-hubspot-to-sheets-abc123.md`.
- HTTP-url resources are keyed by **host**, not full URL. The note body enumerates the per-URL / per-path detail.

## Why this schema

- `fingerprint` lives in the workflow note (not a separate index) so a single read tells refresh everything it needs.
- `auto_generated_at` lets a future Phase 2 dashboard surface stale notes.
- Resource-type-specific keys are kept minimal to avoid drift; deeper detail belongs in the auto-block body, not frontmatter.
