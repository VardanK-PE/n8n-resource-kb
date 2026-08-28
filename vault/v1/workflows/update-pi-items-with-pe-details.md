---
n8n_id: "GXtdNPhHxKiailuk"
name: "Update PI items with PE Details"
status: inactive
last_modified: 2025-11-25T17:48:45.602Z
tags: []
fingerprint: "05b3ddd24d74129267097f85ab91bf6956b1aaad4c711a5b56a2b26ea8830891"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Update PI items with PE Details

## Summary

- **Status:** inactive
- **n8n ID:** `GXtdNPhHxKiailuk`
- **Nodes:** 32
- **Last modified:** 2025-11-25T17:48:45.602Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `9b058235-10dd-4dcb-8909-bc59d8101cd0`)
- **error** — node "Error Trigger" (id `de388ae6-4ba9-49c9-a22e-2da4aab6662e`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `010b3532-0930-4739-836d-4731db666572`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks7" (id `0ece33fd-4741-4f5d-9044-a6c7dc259cae`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet2" (id `19dc97ab-840c-4930-974a-df59623e5334`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `1b571d8b-3f7c-4219-bc7e-131311307845`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet5" (id `4aa92672-2e4b-46a6-ad04-c5772de3f5ad`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get new items" (id `6c4ebd6c-0c89-43f8-9dcb-f0f7ac130cc9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `71747373-44ba-4b11-9a2f-436f3bc422cd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get MIDs1" (id `8100434b-c27a-40ed-9a65-69e854e7ddc3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get MIDs" (id `9e8beee3-1ab7-42ac-a9ba-a14163d10fdc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Chargebacks3" (id `d1302aa0-fe59-471f-894e-245ee7913f29`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet7" (id `f6ee1fb1-57c5-4efc-8e48-2d0b09fe62aa`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks7" (id `0ece33fd-4741-4f5d-9044-a6c7dc259cae`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `1b571d8b-3f7c-4219-bc7e-131311307845`)

### Env vars

- [[../resources/env-vars/n8n-editor-base-url|N8N_EDITOR_BASE_URL]] — node "Stop and Error" (id `505e7eee-4ade-4e17-8287-9704d9315b00`)

### Google Sheets

- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `appendOrUpdate`, tab `Chargebacks Hearth` — node "Append or update row in sheet2" (id `19dc97ab-840c-4930-974a-df59623e5334`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `chargebacks` — node "Get row(s) in sheet5" (id `4aa92672-2e4b-46a6-ad04-c5772de3f5ad`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `chargebacks` — node "Get new items" (id `6c4ebd6c-0c89-43f8-9dcb-f0f7ac130cc9`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `chargebacks` — node "Update row in sheet" (id `71747373-44ba-4b11-9a2f-436f3bc422cd`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Get MIDs1" (id `8100434b-c27a-40ed-9a65-69e854e7ddc3`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get MIDs" (id `9e8beee3-1ab7-42ac-a9ba-a14163d10fdc`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `chargebacks` — node "Update Chargebacks3" (id `d1302aa0-fe59-471f-894e-245ee7913f29`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `chargebacks` — node "Get row(s) in sheet7" (id `f6ee1fb1-57c5-4efc-8e48-2d0b09fe62aa`)

### Slack channels

- [[../resources/slack-channels/c09pc6hkhpy|payengine-ai-alerts]] (id `C09PC6HKHPY`) — op `channel` — node "Send a message5" (id `010b3532-0930-4739-836d-4731db666572`)

## Used by (workflows)

- [[elavon-on-pi-daily-monitor-completion|Elavon: On PI Daily Monitor Completion]] — node "Add MID partner info" (id `1eda6a8e-35a2-4892-aacd-030c93a9f2cb`)
- [[elavon-on-pi-daily-monitor-completion|Elavon: On PI Daily Monitor Completion]] — node "Add chargeback partner info" (id `3beb36da-32bb-4875-af49-eded8c810f91`)
- [[elavon-on-pi-daily-monitor-completion|Elavon: On PI Daily Monitor Completion]] — node "Set newly added entries date created" (id `8d256e60-6da9-423e-9c2e-cdefad43a130`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
