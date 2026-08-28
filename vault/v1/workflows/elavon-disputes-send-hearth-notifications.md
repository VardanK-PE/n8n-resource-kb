---
n8n_id: "8YHh1wSkFjN6tExy"
instance: v1
name: "Elavon Disputes - Send Hearth Notifications"
status: inactive
last_modified: 2026-08-28T19:12:54.797Z
tags: []
fingerprint: "1c760c8a6af3c5008669babacd7b77c7ecc48c3684fb44f0a057cd829353f181"
auto_generated_at: 2026-08-28T21:13:05Z
---

<!-- auto:start -->

# Elavon Disputes - Send Hearth Notifications

## Summary

- **Status:** inactive
- **n8n ID:** `8YHh1wSkFjN6tExy`
- **Nodes:** 27
- **Last modified:** 2026-08-28T19:12:54.797Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `0143e5d9-abf0-4b32-95e1-4d3ab0db3277`)
- **error** — node "Error Trigger" (id `1cf49fa6-2a81-448f-a9ae-90d444e9ebf8`)
- **manual** — node "When clicking ‘Execute workflow’" (id `32335534-1d3c-4da7-adc7-4a015e103244`)

## Depends on

### Credentials

- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send a message6" (id `0629a3ac-21ff-460c-b209-44fce49e6544`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet8" (id `29002685-51de-438b-8152-c726bbc49bed`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `3e70ed71-a0d0-45a1-b13e-79c0626dab88`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet2" (id `4c66b741-e1e0-4baa-a69b-8269fe14cc0e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get new disputes" (id `71e4ef50-6c28-48d3-b83a-ddee62252d9c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file1" (id `8dc8dad9-90bb-45ed-b701-841a34d33df6`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Query merchant data" (id `d60b9e7b-2848-4916-88c9-ebd5ec7d050d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `decd8075-b490-4df8-bf5d-792063efe196`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `e8467ce3-fa0b-4b3e-b169-e3c4cf6d096f`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Query merchant data" (id `d60b9e7b-2848-4916-88c9-ebd5ec7d050d`)

### Google Sheets

- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Get row(s) in sheet8" (id `29002685-51de-438b-8152-c726bbc49bed`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `appendOrUpdate`, tab `Chargebacks Hearth` — node "Append or update row in sheet" (id `3e70ed71-a0d0-45a1-b13e-79c0626dab88`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `appendOrUpdate`, tab `Chargebacks Hearth` — node "Append or update row in sheet2" (id `4c66b741-e1e0-4baa-a69b-8269fe14cc0e`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Chargebacks Hearth` — node "Get new disputes" (id `71e4ef50-6c28-48d3-b83a-ddee62252d9c`)

### Google Drive

- *(dynamic)* — op `download` — node "Download file1" (id `8dc8dad9-90bb-45ed-b701-841a34d33df6`)

### Slack channels

- [[../resources/slack-channels/c09b9gx9rf1|hearth-dispute-alerts]] (id `C09B9GX9RF1`) — op `channel` — node "Send a message6" (id `0629a3ac-21ff-460c-b209-44fce49e6544`)
- [[../resources/slack-channels/n8n-sandbox-of-doom|n8n-sandbox-of-doom]] (id `n8n-sandbox-of-doom`) — op `channel` — node "Send a message4" (id `decd8075-b490-4df8-bf5d-792063efe196`)
- [[../resources/slack-channels/ops-alerts|ops_alerts]] (id `ops_alerts`) — op `channel` — node "Send a message" (id `e8467ce3-fa0b-4b3e-b169-e3c4cf6d096f`)

### Sub-workflows (Execute Workflow calls)

- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `1eb4b9dd-fad9-4323-9aeb-2bebb326a5bf`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Send base notification" (id `233c558e-d710-4389-9a3d-a4b109789ef2`)
- [[send-email-simple-text|Send Email: Simple Text]] (n8n_id `Zr3vF0LVpsPrzHVY`) — node "Call 'Send Email: Simple Text'" (id `8c59c088-2279-43b0-9c77-e4c8dcc51c34`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
