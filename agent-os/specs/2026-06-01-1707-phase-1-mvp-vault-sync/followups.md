# Phase 1 MVP — Open follow-ups

These items remain after the Task 1–4 scaffolding pass. Phase 1 is **not** considered done until they're resolved.

## 1. Bootstrap `.env` (manual step — owner: maintainer)

The n8n REST API key needs to live in `./.env` (gitignored). To enable:

```sh
cp .env.example .env
```

Then open `.env` and set:

- `N8N_API_URL` — your n8n instance URL
- `N8N_API_KEY` — the API token

Working values exist at `../n8n_claude/.mcp.json` (sibling project, same instance). The refresh runbook also documents a fallback that reads from that sibling file directly via `jq` — useful for a one-off smoke test before `.env` exists.

**Why this is a manual step:** the auto-mode classifier blocks the agent from writing files that contain hardcoded credentials. The maintainer should do this once, manually.

## 2. End-to-end smoke run (the original Task 5)

Once `.env` exists (or using the sibling-project fallback), run the refresh per `agent-os/standards/sync/refresh-procedure.md`. **This no longer requires a session restart** — the REST API is reachable via `curl` directly. The smoke run can happen in any session.

Acceptance criteria:

- `vault/_cache/workflows/*.json` populated, one file per active workflow (gitignored)
- `vault/workflows/*.md` populated, one note per active workflow
- `vault/resources/<type>/*.md` populated, with reverse-lookup auto blocks listing `(workflow, node-name, node-id)` triples
- `vault/changelogs/YYYY-MM-DD.md` written
- A sub-workflow note shows bidirectional dependency (`Depends on (workflows)` on the caller, `Used by (workflows)` on the callee)
- Add a manual annotation inside a `<!-- manual:* -->` block, run refresh a second time, confirm the annotation survives
- Re-running refresh with no n8n-side change produces zero file modifications and no changelog (fingerprint stability)
- Any taxonomy gaps from this first run get captured here, then resolved by extending `agent-os/standards/sync/resource-taxonomy.md` + the matching `scripts/jq/extract-*.jq`

## 3. `jq` script validation against real workflows

The starter scripts under `scripts/jq/` are best-effort against my mental model of n8n's JSON shape. The first real refresh will reveal:

- **HTTP URL parsing** — the regex assumes `scheme://host/...`. Edge cases: relative URLs, expression-templated URLs (`{{ $node.X.json.url }}`), URLs built from string concatenation.
- **Credentials** — the assumption is `node.credentials` is `{ <credType>: { id, name } }`. Confirm against current n8n versions.
- **Triggers** — schedule trigger has multiple shapes across n8n versions (`cronExpression` vs `rule.interval`). The extractor may miss the cron in newer formats.
- **Sub-workflows** — `parameters.workflowId` may be `{ value, mode, cachedResultName }` or a plain string. Both branches are handled but should be verified.
- **LLM models** — type-string matching for `lmChat*`, `embeddings*` etc. relies on regex. May miss provider-specific naming.
- **Env vars** — the regex `$env\.[A-Z_][A-Z0-9_]*` may not match all valid n8n env-var names (lowercase, digits-first edge cases).

Expect one round of script tuning after the first run.

## 4. Standards drift to watch on the first real run

- **Resource taxonomy coverage** — the v1 mapping in `sync/resource-taxonomy.md` is a best guess. Expect to extend it (and add matching `scripts/jq/extract-*.jq`) on first contact.
- **Fingerprint stability** — confirm that two back-to-back refreshes on an unchanged workflow produce identical hashes. If not, more fields need stripping from `canonical.jq`.
- **Filename collisions** — the slugify rules may need a tiebreaker.
- **HTTP URL grouping** — currently group by host. If the instance heavily uses one host with many endpoints, the host note may grow unwieldy and per-path notes might be warranted.

## 5. Scope decisions explicitly deferred to Phase 2

These appear in `agent-os/product/roadmap.md` Phase 2 and are **not** in this spec's scope:

- Scheduled (cron) sync
- Full workflow JSON snapshots
- Dashboards / generated index notes
- Multi-environment support
- Ownership / criticality classification
- Webhook-based push refresh
- Cross-instance dedup

If user requests touch any of these, defer with a pointer to the roadmap.
