---
n8n_id: "rWsv8W7dqcspvcaz"
instance: v1
name: "Hearth - Merchant Max Transaction Limit Email Alerts"
status: active
last_modified: 2026-01-12T20:00:24.324Z
tags: []
fingerprint: "e9b6eb025e74e230ddb59f8e267422c5a0796e5b8958d9e43ff07f3f8f9e6073"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Hearth - Merchant Max Transaction Limit Email Alerts

## Summary

- **Status:** active
- **n8n ID:** `rWsv8W7dqcspvcaz`
- **Nodes:** 20
- **Last modified:** 2026-01-12T20:00:24.324Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `43b85100-f9c8-4e11-a976-ee81dfe9767b`)
- **error** — node "Error Trigger" (id `5f6654dc-a098-46bb-8649-4694064f1141`)
- **schedule** — node "Schedule Trigger" (id `e8bbb9da-d29e-4d43-a2c5-8fb9869d8892`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send a message" (id `0efaed28-17ba-4c04-b8c9-67d95b5382a6`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query1" (id `36cde4fc-66f9-4238-84f0-a98ce5247c33`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get transactions since last execution" (id `52ec18cd-40f8-462a-a4de-887c5021374c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `74c49746-7a1b-425d-a5fd-94c16ac96371`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `7c8de103-83d5-4a2a-919a-3745cd08f2fb`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send Message to partner" (id `873d783b-b98c-4e98-b55f-54032469ba71`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `9b7f4ec5-90ba-454d-9e3f-ca98009369e0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `adc95bd5-3617-4694-a835-e529f9b75a36`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "No Stop Funds List" (id `b4706316-0235-4219-8f54-67915ce8e994`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send email to merchant" (id `b75a0aa2-9032-4400-a367-63d43e608700`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query1" (id `36cde4fc-66f9-4238-84f0-a98ce5247c33`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get transactions since last execution" (id `52ec18cd-40f8-462a-a4de-887c5021374c`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `no_stop_funds_list` — node "Get row(s) in sheet" (id `7c8de103-83d5-4a2a-919a-3745cd08f2fb`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `no_stop_funds_list` — node "Update row in sheet" (id `adc95bd5-3617-4694-a835-e529f9b75a36`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `no_stop_funds_list` — node "No Stop Funds List" (id `b4706316-0235-4219-8f54-67915ce8e994`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Send a message4" (id `74c49746-7a1b-425d-a5fd-94c16ac96371`)
- [[../resources/slack-channels/c08tfuk2ndq|hearth-transaction-alerts]] (id `C08TFUK2NDQ`) — op `channel` — node "Send Message to partner" (id `873d783b-b98c-4e98-b55f-54032469ba71`)
- [[../resources/slack-channels/c09c901een4|hearth-alerts-internal]] (id `C09C901EEN4`) — op `channel` — node "Send a message6" (id `9b7f4ec5-90ba-454d-9e3f-ca98009369e0`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
