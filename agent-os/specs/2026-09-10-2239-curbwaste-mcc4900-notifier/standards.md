# Standards for Curbwaste MCC 4900 Notifier

Most of this spec's work happens **on the n8n instance**, not in the vault, so only the
vault-facing tail of it (Task 5) is standards-governed. Rather than copy ~1,100 lines of
standards in here, this file names the standards that bind and quotes the specific clauses
that will actually be checked. Read the source files for anything beyond that.

---

## `sync/refresh-procedure` — governs Task 5

**Applies because** this spec creates a new workflow and a new data table on v1. Neither may
be hand-written into the vault; both must arrive through a refresh so the fingerprints,
frontmatter, and cross-links are generated consistently with everything else.

Binding points:

- Refresh is scoped to **one instance alias** at a time. This is a `v1` refresh only. `v1` and
  `v2` never share notes or cache — n8n workflow ids are unique only within an instance, and
  in fact `ajjvV2MZyEtuMj49` exists on v1 and 404s on v2.
- Read n8n through `scripts/n8n-api.sh v1 <endpoint>`. Never source `.env`; never pass a URL
  or key on the command line.
- The new workflow's note is created by the renderer, and the resource-aggregation pass is
  what populates "Used by (workflows)" on the three sub-workflow notes and the new
  data-table note. Do not hand-edit those back-references.

## `notes/auto-manual-blocks` — governs Task 5

**Applies because** the design rationale for this workflow is exactly the kind of content the
manual block exists to protect, and it must survive every future refresh.

Binding points, quoted:

- > The auto block always comes **before** the manual block in the file body.
- > **Use `Edit`** to replace only the auto-block region … Never use `Write` on an existing
  > note — it overwrites the whole file and would destroy the manual block.
- > Edit **only** between `<!-- manual:start -->` and `<!-- manual:end -->`.
- > refresh-owned frontmatter keys (`n8n_id`, `fingerprint`, `last_modified`, `status`,
  > `auto_generated_at`) are off-limits to manual editing.
- > **If the manual block is missing** … insert an empty manual block stub. Do not infer or
  > fabricate manual content.

Exact markers: `<!-- auto:start -->` / `<!-- auto:end -->` / `<!-- manual:start -->` /
`<!-- manual:end -->`.

## `sync/resource-taxonomy` — governs Task 5

**Applies because** the new workflow introduces resource references that refresh must map: a
Postgres database + credential, a schedule trigger, three `executeWorkflow` sub-workflow
references, and a data table.

Binding points:

- Sub-workflow references are **bidirectional**: the caller's "Depends on → Workflows" lists
  the callee, and the callee's "Used by → Workflows" lists the caller with the calling node's
  name and id. So `Send Email: Simple Text`, `Slack - Create a base message`, and
  `Slack - Send notification` all gain a new "Used by" entry.
- `n8n-nodes-base.scheduleTrigger` → `trigger` (type `schedule`), recording the cron
  expression. This workflow's is a 4-hour interval.
- `n8n-nodes-base.postgres` → `database` keyed by `(engine, host, database)`, body listing
  distinct tables parsed from the query, plus a `credential`. The new query touches
  `merchant`, `merchant_status`, and `merchant_processor_detail`.
- Open-taxonomy rule: anything unmappable is still recorded under "Unmapped node references"
  **and** logged as a `taxonomy_gap` in the changelog. Never silently dropped.

**Pre-existing gap worth noting, not fixing here:** the standard's "v1 categories" table lists
nine categories and does **not** include `data-tables` or `slack-channels`, yet both directory
trees exist and are populated in the vault. The taxonomy file is behind the renderer. No new
category is introduced by this spec, so no `taxonomy_gap` is expected from it — but if refresh
emits one for the data table, that is the stale standard talking, and extending
`resource-taxonomy.md` is the maintainer's explicit call, not a silent edit.

## `sync/changelog-format` — governs Task 5

**Applies because** the refresh that picks up this workflow produces semantic change (a new
workflow, a new data table, new back-references on three existing notes). Per hard invariant 4
in `CLAUDE.md`, skipping the changelog is not an option — the changelog *is* the audit trail.

## `sync/large-workflow-handling` — governs Tasks 3 and 5

**Applies because** verification involves reading the built workflow back from n8n, and
`Send Email: Simple Text` alone is 44 nodes.

Binding points:

- Cache fetched workflow JSON under `vault/v1/_cache/workflows/<id>.json` (gitignored).
- **Never** `Read` or `cat` a file under `_cache/workflows/` — always go through a `jq`
  program that returns only the small projection needed.
- Extractions go through pre-written programs in `scripts/jq/`, not inline `jq` in shell
  heredocs. Relevant here: `nodes-summary.jq`, `extract-subworkflows.jq`,
  `extract-data-tables.jq`, `extract-triggers.jq`, `extract-credentials.jq`.

## `notes/frontmatter-schema` — read before Task 5

Governs the keys the renderer writes on the new workflow and data-table notes. Nothing in
this spec deviates from it; listed so the schema is consulted rather than guessed if a
frontmatter question comes up.

---

## Not applicable

- `sync/reverse-lookup` — this spec answers no "what uses X?" question.
- `sync/fingerprint` — relevant to the renderer's change detection, which runs unmodified.
- `agent-os/product/*` — this is workflow authoring on the n8n instance, not a change to the
  vault-sync product.
