# Standards for Phase 1 MVP — n8n → Obsidian Vault Sync

The following standards govern this work. Each is a separate file under `agent-os/standards/` so it can be referenced from `CLAUDE.md`, templates, and future specs without duplication.

---

## notes/auto-manual-blocks

**File:** `agent-os/standards/notes/auto-manual-blocks.md`

**Why it applies:** every note in the vault is partially auto-generated and partially human-authored. Without a guarded-block contract, refresh would clobber manual annotations and the vault loses its "shared knowledge layer" value. This is the load-bearing contract of capability 5.

---

## notes/frontmatter-schema

**File:** `agent-os/standards/notes/frontmatter-schema.md`

**Why it applies:** the refresh procedure reads `fingerprint` to detect change, reads `n8n_id` / `status` to identify workflows, and writes back updated values. Reverse-lookup reads `type` / `name`. A uniform schema is required for these operations to be reliable across every note in the vault.

---

## sync/resource-taxonomy

**File:** `agent-os/standards/sync/resource-taxonomy.md`

**Why it applies:** capability 1 (resource extraction) and capability 2 (resource pages) both depend on a canonical mapping from n8n node types and parameters to resource categories. The open-taxonomy rule (flag unknowns in changelog) is what lets the vault grow with real usage.

---

## sync/fingerprint

**File:** `agent-os/standards/sync/fingerprint.md`

**Why it applies:** capability 4 (refresh + changelog) depends on a stable, content-aware hash to detect "did this workflow actually change?" — `last_modified` alone is too coarse and produces false positives from UI-only edits.

---

## sync/refresh-procedure

**File:** `agent-os/standards/sync/refresh-procedure.md`

**Why it applies:** this is the runbook `CLAUDE.md` routes to when the user says "refresh the vault". It binds every other standard together into an end-to-end procedure (list workflows → fingerprint → diff → write notes → preserve manual blocks → emit changelog).

---

## sync/reverse-lookup

**File:** `agent-os/standards/sync/reverse-lookup.md`

**Why it applies:** the second core user intent ("what uses X?"). Specifies how to resolve a resource name to its note and extract the `(workflow, node-name, node-id)` triples from the auto block.

---

## sync/changelog-format

**File:** `agent-os/standards/sync/changelog-format.md`

**Why it applies:** capability 4 requires "human-readable" changelog entries. Without a defined format, entries drift and become unreviewable. Also defines where taxonomy gaps and deleted workflows surface.
