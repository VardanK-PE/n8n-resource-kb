---
n8n_id: "oTAgUSqxBxQkuAjR"
name: "OpsInternalBot - Main"
status: active
last_modified: 2026-04-20T16:32:45.322Z
tags: []
fingerprint: "0ec0f87d176a766ae1403d593939c303c41037f3127844203b27206ccd578d43"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# OpsInternalBot - Main

## Summary

- **Status:** active
- **n8n ID:** `oTAgUSqxBxQkuAjR`
- **Nodes:** 11
- **Last modified:** 2026-04-20T16:32:45.322Z

## Triggers

- **webhook** — node "Webhook" (id `c11fa349-b775-4680-8f7c-95331e7f12a4`) — POST `ops-internal-bot`

## Depends on

### Credentials

- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message3" (id `827ea699-6096-44ec-8395-7515cfdd34e3`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Send a message3" (id `827ea699-6096-44ec-8395-7515cfdd34e3`)

### Sub-workflows (Execute Workflow calls)

- [[opsinternalbot-disputes-NSkdXVo1|OpsInternalBot - Disputes]] (n8n_id `NSkdXVo1cjKZO7SG`) — node "Call 'OpsInternalBot - Token Inport Job'1" (id `7a0b812c-df11-4c55-878d-f1d38e9ee578`)
- [[opsinternalbot-token-inport-job|OpsInternalBot - Token Inport Job]] (n8n_id `1jDrShgq2CNgU8z9`) — node "Call 'OpsInternalBot - Token Inport Job'" (id `eb762010-b582-42ac-a0ad-7fa6c69b6a57`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
