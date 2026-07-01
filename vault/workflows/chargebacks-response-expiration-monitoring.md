---
n8n_id: "JcKp0Ehz4s4QirJd"
name: "Chargebacks: Response expiration monitoring"
status: active
last_modified: 2026-02-23T15:10:43.571Z
tags: []
fingerprint: "8bc0a52040d9772d1358c81cc57ec49c5fb99dfa1cf123d125d27395d316d92a"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Chargebacks: Response expiration monitoring

## Summary

- **Status:** active
- **n8n ID:** `JcKp0Ehz4s4QirJd`
- **Nodes:** 37
- **Last modified:** 2026-02-23T15:10:43.571Z

## Triggers

- **error** — node "Error Trigger" (id `087fc2f2-915d-4e43-a938-70f915f6acc9`)
- **manual** — node "When clicking ‘Execute workflow’" (id `7f8ee9dd-8eba-46a0-a302-df7c34472f4f`)
- **schedule** — node "Schedule Trigger" (id `db72c9bd-3a18-4ffe-b5dd-8d5a3a09ba07`) — `daily at 7:00`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `515726d2-54fe-4879-bcca-183bc72a0268`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `5b42dc05-9b54-4691-9af5-860338f2b8bf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Clear sheet" (id `63337e46-494c-4cc0-81b4-4b9238c2aec4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Dispute Data" (id `7d080499-29bd-4820-963f-a0ad62c28fe6`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request refund transactions in ACD or AMR states" (id `9b5dde13-3c17-425e-8259-3d31dde7bbb1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Dispute Attachments" (id `bfff3743-c809-4b7b-a775-4c03232320cf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Dispute Data1" (id `f23f1193-c929-4069-befd-141b4f99af6b`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request refund transactions in ACD or AMR states" (id `9b5dde13-3c17-425e-8259-3d31dde7bbb1`)

### Google Sheets

- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `append`, tab `Case # about to expire` — node "Append row in sheet" (id `515726d2-54fe-4879-bcca-183bc72a0268`)
- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `clear`, tab `Case # about to expire` — node "Clear sheet" (id `63337e46-494c-4cc0-81b4-4b9238c2aec4`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `chargebacks` — node "Dispute Data" (id `7d080499-29bd-4820-963f-a0ad62c28fe6`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Dispute Attachments" (id `bfff3743-c809-4b7b-a775-4c03232320cf`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Disputes` — node "Dispute Data1" (id `f23f1193-c929-4069-befd-141b4f99af6b`)

### Slack channels

- [[../resources/slack-channels/c08r8h75n15|dispute-alerts]] (id `C08R8H75N15`) — op `channel` — node "Send a message5" (id `5b42dc05-9b54-4691-9af5-860338f2b8bf`)

### Sub-workflows (Execute Workflow calls)

- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'1" (id `2555d8cf-ace6-4992-ac0b-80c25de6e8fd`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Slack - Create a base message for 7 days" (id `4de705b8-b6d3-4be0-a52e-a810a8cd1e70`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Slack - Create a base message for today" (id `79bdf65e-a2bf-4818-bc3e-8127c6cee2a9`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `9c16336d-fcdc-43ed-8d83-99d370462938`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
