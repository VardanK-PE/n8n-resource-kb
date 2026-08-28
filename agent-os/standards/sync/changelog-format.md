# Standard: Changelog Format

Each refresh that produces meaningful change writes one file **in the refreshed instance's subtree**: `vault/<instance>/changelogs/YYYY-MM-DD.md` (UTC date), where `<instance>` is `v1` or `v2`. Multiple refreshes of the same instance on the same day append to the same file. The two instances keep independent changelog series.

## File structure

```markdown
---
date: 2026-06-01
instance: v1
workflows_added: 2
workflows_modified: 5
workflows_removed: 0
resources_added: 7
resources_removed: 1
taxonomy_gaps: 1
auto_generated_at: 2026-06-01T17:07:00Z
---

# Changelog — 2026-06-01 (v1)

## Run at 17:07 UTC

### Workflows added

- [[../workflows/sync-hubspot-to-sheets]] (n8n_id `abc123`)
- [[../workflows/nightly-report]] (n8n_id `def456`)

### Workflows modified

#### [[../workflows/customer-onboarding]]

- Added HTTP node "Get Customer Profile" targeting `api.example.com/v2/customers/{id}`
- Schedule changed from `0 * * * *` (hourly) to `0 9 * * *` (daily at 09:00)
- Removed credential reference: `hubspot-staging` (was on node "Push to HubSpot", id `4f2a`)

#### [[../workflows/...]]

…

### Workflows removed

(empty section omitted if none)

### Resource diffs

- Added: [[../resources/http-urls/api-example-com]], [[../resources/credentials/stripe-prod]], …
- Removed (now zero usages): [[../resources/credentials/hubspot-staging]]

### Taxonomy gaps

- Node type `@acme/n8n-nodes-custom.thing` (in workflow [[../workflows/customer-onboarding]], node "Do Acme Thing", id `7a3b`) — yields a resource that does not match any rule in `sync/resource-taxonomy.md`. Recommend extending the taxonomy.
```

## Required sections per run

A run section appears for every refresh that produced change. Order within the run section:

1. Workflows added
2. Workflows modified (with per-workflow sub-section listing the specific changes)
3. Workflows removed
4. Resource diffs (added / removed-now-zero-usages)
5. Taxonomy gaps

Empty sections are omitted.

## Per-workflow modification entries

Each bullet in a "Workflows modified" sub-section describes one semantic change in human terms. Aim for the form `<verb> <thing> <qualifier>`. Examples:

- "Added HTTP node 'Get Customer' targeting `api.example.com`"
- "Schedule changed from `0 * * * *` to `0 9 * * *`"
- "Removed credential `hubspot-prod` from node 'Push to HubSpot' (id 4f2a)"
- "Renamed node 'Old Name' → 'New Name'"
- "Swapped postgres credential: `db-staging` → `db-prod` on node 'Read Customers'"
- "Workflow deactivated"
- "Workflow renamed: 'Old Name' → 'New Name'"

Avoid raw JSON diffs — those are forensic data for Phase 2's full-snapshot feature, not for the human-readable changelog.

## Multiple runs same day

If `vault/<instance>/changelogs/<today>.md` already exists, append a new `## Run at HH:MM UTC` section. Update the frontmatter counts (`workflows_added`, etc.) to reflect the **cumulative** totals across all runs that day. Do not overwrite the prior run's section.

## No-change runs

Do not create a file if a run had zero changes. The changelog is a record of meaningful change, not a per-run heartbeat.

## Immutability

Changelogs have **no manual block**. Once written, they are append-only by future runs of the same day and otherwise immutable. If the user wants to annotate a specific change, they annotate the relevant workflow or resource note, not the changelog.

## Taxonomy gap entries

A taxonomy gap is the changelog's signal that `sync/resource-taxonomy.md` should grow. Each entry must include:

- The exact node `type` string
- The workflow + node name + node ID where it was found
- A brief note on what was unmapped (e.g., "yields URL but extraction rule missing", "appears to reference an unknown credential type")

Resolving a gap is a manual step: the maintainer extends `sync/resource-taxonomy.md`, then re-runs refresh.
