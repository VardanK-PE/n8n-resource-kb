---
n8n_id: "XHmdKvSqP7myaPIo"
name: "Ops - Expiry"
status: inactive
last_modified: 2026-04-17T20:39:45.819Z
tags: []
fingerprint: "2615d7e7968092271272002792062e8efba4d6681b1652bc1f03913affcb111b"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Ops - Expiry

## Summary

- **Status:** inactive
- **n8n ID:** `XHmdKvSqP7myaPIo`
- **Nodes:** 34
- **Last modified:** 2026-04-17T20:39:45.819Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `1521e47d-7a3a-4920-a181-e20fcd254272`)
- **schedule** — node "Schedule Trigger" (id `9528a0ee-d4e2-41c7-8a6a-815d26ca6043`) — `daily at 7:00`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Dispute Data" (id `27c66234-a1f6-462e-81e6-59d3d2de6f0e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Clear sheet" (id `2c819275-af59-4f28-8217-9590bb848613`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `3483a469-f00f-4b0b-a5b5-e654ac1e61ec`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Dispute Attachments" (id `a5ab03b3-14f6-403a-8b94-bc40f7d29616`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Dispute Data1" (id `c2937342-e9f2-4ca0-878d-8d0b9db32c99`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request refund transactions in ACD or AMR states" (id `e2859804-afdf-4ef0-bdb1-9f8ce1c7ccdb`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request refund transactions in ACD or AMR states" (id `e2859804-afdf-4ef0-bdb1-9f8ce1c7ccdb`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `chargebacks` — node "Dispute Data" (id `27c66234-a1f6-462e-81e6-59d3d2de6f0e`)
- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `clear`, tab `Case # about to expire` — node "Clear sheet" (id `2c819275-af59-4f28-8217-9590bb848613`)
- [[../resources/google-sheets/1cltxfeklqgzgu-f3jj3i3wvviwplozhfujuefjzubas|Elavon dispute reporting]] (id `1cltxFEklqGZgu-F3jJ3i3wvvIwPLOzHFUjUefJZuBas`) — op `append`, tab `Case # about to expire` — node "Append row in sheet" (id `3483a469-f00f-4b0b-a5b5-e654ac1e61ec`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Dispute Attachments" (id `a5ab03b3-14f6-403a-8b94-bc40f7d29616`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Disputes` — node "Dispute Data1" (id `c2937342-e9f2-4ca0-878d-8d0b9db32c99`)

### Sub-workflows (Execute Workflow calls)

- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Slack - Create a base message for today" (id `0fdfe2dd-1217-44bc-be75-9c86116ed7ec`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `57841ea3-1448-4c21-9887-20ce9711729a`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Slack - Create a base message for 7 days" (id `6da38350-22d9-4fac-aa91-33d8dd07557f`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'1" (id `ce553e31-23ed-4f9e-8a24-75057c987342`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
