---
type: index-router
auto_generated_at: 2026-08-29T00:00:00Z
---

<!-- auto:start -->

# n8n Vault

This vault tracks **two n8n instances**, each in its own isolated subtree. n8n
workflow IDs are only unique within an instance, so the subtrees never share
notes or cache.

| Instance | Alias | Subtree | Front door |
|---|---|---|---|
| Old n8n instance | `v1` | `v1/` | `[[v1/index]]` |
| New n8n instance | `v2` | `v2/` | `[[v2/index]]` |

- Reading/refreshing/looking-up is always **scoped to one instance**. Pass the
  alias to the API wrapper (`scripts/n8n-api.sh v1 …` / `… v2 …`) and to the
  renderer (`scripts/render-vault.sh --instance v1 …`).
- Shared reference templates live at `_templates/` (not instance-specific).
- See `../CLAUDE.md` for the intent → runbook map and the manual / auto block
  contract that protects hand-written annotations across refreshes.

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Cross-instance orientation, migration notes (v1 → v2), on-call pointers, etc. -->

<!-- manual:end -->
