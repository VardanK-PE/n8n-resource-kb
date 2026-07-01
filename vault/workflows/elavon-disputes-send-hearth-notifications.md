---
n8n_id: "8YHh1wSkFjN6tExy"
name: "Elavon Disputes - Send Hearth Notifications"
status: inactive
last_modified: 2026-01-08T15:30:07.826Z
tags: []
fingerprint: "ebf5c2e9a2454c00f7d363eb220b7a060da08ab6fa125259459afb1f008f9f02"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Elavon Disputes - Send Hearth Notifications

## Summary

- **Status:** inactive
- **n8n ID:** `8YHh1wSkFjN6tExy`
- **Nodes:** 19
- **Last modified:** 2026-01-08T15:30:07.826Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `0143e5d9-abf0-4b32-95e1-4d3ab0db3277`)
- **error** — node "Error Trigger" (id `1cf49fa6-2a81-448f-a9ae-90d444e9ebf8`)
- **manual** — node "When clicking ‘Execute workflow’" (id `32335534-1d3c-4da7-adc7-4a015e103244`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet8" (id `29002685-51de-438b-8152-c726bbc49bed`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet1" (id `2cfc78a0-cc08-43b9-898d-68a993cd1ff1`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create a draft1" (id `4fa0955f-b809-49d8-b86c-1b5dec333c56`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get new disputes" (id `71e4ef50-6c28-48d3-b83a-ddee62252d9c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file1" (id `8dc8dad9-90bb-45ed-b701-841a34d33df6`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send a message5" (id `a285481a-f8e5-486f-96e0-a42e557560d9`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send a message4" (id `decd8075-b490-4df8-bf5d-792063efe196`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `e8467ce3-fa0b-4b3e-b169-e3c4cf6d096f`)

### Google Sheets

- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Get row(s) in sheet8" (id `29002685-51de-438b-8152-c726bbc49bed`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `appendOrUpdate`, tab `Chargebacks Hearth` — node "Append or update row in sheet1" (id `2cfc78a0-cc08-43b9-898d-68a993cd1ff1`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Chargebacks Hearth` — node "Get new disputes" (id `71e4ef50-6c28-48d3-b83a-ddee62252d9c`)

### Google Drive

- *(dynamic)* — op `download` — node "Download file1" (id `8dc8dad9-90bb-45ed-b701-841a34d33df6`)

### Slack channels

- [[../resources/slack-channels/c09jmte0m18|pe-alert-tests-internal]] (id `C09JMTE0M18`) — op `channel` — node "Send a message5" (id `a285481a-f8e5-486f-96e0-a42e557560d9`)
- [[../resources/slack-channels/c09b9gx9rf1|hearth-dispute-alerts]] (id `C09B9GX9RF1`) — op `channel` — node "Send a message4" (id `decd8075-b490-4df8-bf5d-792063efe196`)
- [[../resources/slack-channels/c09jr6ph8tx|n8n-sandbox-of-doom]] (id `C09JR6PH8TX`) — op `channel` — node "Send a message" (id `e8467ce3-fa0b-4b3e-b169-e3c4cf6d096f`)

## Used by (workflows)

- [[elavon-on-pi-daily-monitor-completion|Elavon: On PI Daily Monitor Completion]] — node "Send Hearth notifications" (id `e63f6782-154c-4a9c-9d47-ecdf014a2fd2`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
