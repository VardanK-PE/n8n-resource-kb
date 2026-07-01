# Product Mission

## Problem

Operating a non-trivial n8n instance becomes opaque fast. Today there is no reliable way to answer day-to-day questions about workflows and the resources they depend on:

- **Reverse lookup is missing.** "Which workflows use this credential / service / database table / LLM model / HTTP endpoint?" — required for rotating secrets, deprecating services, planning migrations, and incident response. Today this is answered by manually clicking through workflows in the n8n UI.
- **Forward lookup is unstructured.** "What does this workflow actually touch?" — opening the workflow in the n8n editor shows the canvas, but extracting a clean inventory of every external dependency (credentials, services, DB tables, sub-workflows, triggers, LLM models, HTTP URLs, env vars, custom nodes) is manual and error-prone.
- **Node-level granularity is lost.** Even when you know "workflow X uses Postgres," you still have to hunt for which specific node uses it. Impact analysis needs node name + node ID, not just workflow name.
- **Change history is shallow.** n8n records an `updatedAt` timestamp but does not produce a human-readable record of *what* changed between revisions. There is no structured changelog to audit, review, or roll back from.
- **There is no shared knowledge layer.** Manual context — owner, criticality, runbook links, business purpose — has nowhere to live alongside the workflow definition.

## Target Users

The maintainer(s) of this n8n instance — operators, automation engineers, and the platform/ops function responsible for keeping production workflows healthy. Primary use cases:

- **Impact analysis** before rotating a credential, deprecating a service, or refactoring a shared sub-workflow.
- **Incident response** when a workflow breaks and the responder needs a fast inventory of what it touches.
- **Audits & onboarding** for new team members or compliance reviews.
- **Change review** to understand what shifted between two points in time.

## Solution

A Claude-driven, Obsidian-native knowledge base, **synced on-demand from n8n**, that turns the n8n instance into a browsable, queryable structured graph.

What makes the approach different:

- **Resources are first-class citizens — and workflows are resources too.** Every credential, service, database, table, LLM model, HTTP URL, env var, and custom node has its own note with a reverse-lookup list of every `(workflow, node)` pair that uses it. **Workflows themselves are also resources**, because other workflows call them via Execute-Workflow nodes — so each workflow note carries both "resources I depend on" and "workflows that depend on me".
- **Node-level granularity.** Every resource usage records the specific node name *and* node ID inside the workflow — so impact analysis points you straight at the lines to change.
- **Discovery-driven taxonomy.** Start with the known resource categories; expand the taxonomy as new resource types surface during real workflow exploration.
- **Structured human-readable changelogs.** Each refresh diffs a per-workflow fingerprint against the prior sync and writes a dated changelog note describing what changed in business terms ("added HTTP node X targeting api.example.com", "schedule changed from hourly to daily", "removed HubSpot credential").
- **Manual annotations are preserved.** Notes have guarded sections so human-authored context (owner, criticality, runbook, business purpose) is never clobbered by a refresh.
- **No new service to run.** Sync is conversational — triggered through Claude Code using the existing `n8n-mcp` and `obsidian` MCP tools. The vault is the UI; Obsidian is the browser; git (optional) is the durability layer.
