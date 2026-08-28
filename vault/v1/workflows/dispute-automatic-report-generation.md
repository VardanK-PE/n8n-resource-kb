---
n8n_id: "omlYEtChOOFF02N0"
instance: v1
name: "Dispute - Automatic report generation"
status: active
last_modified: 2026-08-27T18:44:37.196Z
tags: []
fingerprint: "be2ac23e645fcbc9be657824292e951c76282fdeafe42016aed7fb90469302b7"
auto_generated_at: 2026-08-28T21:13:05Z
---

<!-- auto:start -->

# Dispute - Automatic report generation

## Summary

- **Status:** active
- **n8n ID:** `omlYEtChOOFF02N0`
- **Nodes:** 18
- **Last modified:** 2026-08-27T18:44:37.196Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `75888e07-4982-422e-9e13-4fabe2201858`) — `daily at 12:00`
- **manual** — node "When clicking ‘Execute workflow’" (id `9f57a6e1-1c24-4889-961b-e5bee54e92a0`)

## Depends on

### Credentials

- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `00324bca-ce99-4787-81c1-e505edb079d0`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message1" (id `22a6ea85-4f3e-4979-88ba-805203d50045`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message3" (id `24e67cda-045d-4748-bdc9-929377160316`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message2" (id `25620f88-7a69-47d8-87cf-f1ea500559af`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `3c25ee90-a980-4c24-bdd6-36f708330587`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message" (id `53f8d656-b2ed-4e7e-a23f-ff19ed5964ac`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-5|anthropic / claude-sonnet-5]] — node "Anthropic Chat Model" (id `00324bca-ce99-4787-81c1-e505edb079d0`)

### Google Sheets

- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `append`, tab `Summary V3` — node "Append row in sheet" (id `3c25ee90-a980-4c24-bdd6-36f708330587`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Send a message1" (id `22a6ea85-4f3e-4979-88ba-805203d50045`)
- *(dynamic channel)* — op `channel` — node "Send a message3" (id `24e67cda-045d-4748-bdc9-929377160316`)
- *(dynamic channel)* — op `channel` — node "Send a message2" (id `25620f88-7a69-47d8-87cf-f1ea500559af`)
- [[../resources/slack-channels/c08r8h75n15|C08R8H75N15]] (id `C08R8H75N15`) — op `channel` — node "Send a message" (id `53f8d656-b2ed-4e7e-a23f-ff19ed5964ac`)

### Sub-workflows (Execute Workflow calls)

- [[dispute-compose-report|Dispute - Compose report]] (n8n_id `NWv022t59k7EtTFo`) — node "Call 'Dispute - Compose report'" (id `10bd26ae-4b13-4117-8a82-58a1ed6eee84`)
- [[dispute-create-report|Dispute - Create Report]] (n8n_id `IM3wk08pLLTXawd2`) — node "Call 'Dispute - Create Report'" (id `40fc8949-ca53-4ea8-a3f4-a91f7435b009`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
