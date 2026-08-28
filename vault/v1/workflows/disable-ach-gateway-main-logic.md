---
n8n_id: "eF2KMTnYGmBJu9EA"
instance: v1
name: "Disable ACH Gateway - Main Logic"
status: active
last_modified: 2026-06-23T19:16:17.056Z
tags: []
fingerprint: "4c7f6076c0c2ed6a811b2c401ec93f12fd554f9352b138c3121cdfc60c45bc1b"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Disable ACH Gateway - Main Logic

## Summary

- **Status:** active
- **n8n ID:** `eF2KMTnYGmBJu9EA`
- **Nodes:** 40
- **Last modified:** 2026-06-23T19:16:17.056Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `37bd194d-f995-4b59-8335-a30ae8781092`) — `every 3 hour(s) at :35`
- **manual** — node "When clicking ‘Execute workflow’" (id `54262bd3-03d1-4e19-ae1b-5dc102d5fa70`)
- **schedule** — node "Schedule Trigger1" (id `8c334aad-cda3-4f3e-b0f6-50a55bd1ce41`) — `every 6 hour(s) at :45`
- **schedule** — node "Schedule Trigger2" (id `f0191bd9-80ea-4846-99f6-7106472c149b`) — `every 1 hour(s) at :55`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `4fa371ca-b27d-4597-8a82-4f17bc75117e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `613ef91c-d055-49b7-ba50-a8b1e4020c62`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `4fa371ca-b27d-4597-8a82-4f17bc75117e`)

### Google Sheets

- [[../resources/google-sheets/1iibhzez9yrtypccwdolvqkpk5fa392dubqsbehauxbw|PayEngineAI Bot - Email Logs]] (id `1IIBhzeZ9YRtYPccwDOlvqkpk5Fa392dUBqSbeHAuXbw`) — op `?`, tab `ElavonDeclinedACH` — node "Get row(s) in sheet" (id `613ef91c-d055-49b7-ba50-a8b1e4020c62`)

### Data tables (n8n)

- [[../resources/data-tables/s79t8iehgnurdtue|Elavon - Disable ACH Gateway Queue]] (id `s79T8iEHGNuRDtuE`) — op `update` — node "Update row(s)" (id `08a0325b-38b2-4004-8897-6cc1714be954`)
- [[../resources/data-tables/s79t8iehgnurdtue|Elavon - Disable ACH Gateway Queue]] (id `s79T8iEHGNuRDtuE`) — op `update` — node "Update row(s)2" (id `143e994d-d3ea-4e6f-8b64-965aa056441b`)
- [[../resources/data-tables/s79t8iehgnurdtue|Elavon - Disable ACH Gateway Queue]] (id `s79T8iEHGNuRDtuE`) — op `?` — node "Insert row" (id `3ec7a255-4d09-4bbe-b036-e7a1b1a57514`)
- [[../resources/data-tables/s79t8iehgnurdtue|Elavon - Disable ACH Gateway Queue]] (id `s79T8iEHGNuRDtuE`) — op `get` — node "Get row(s)2" (id `4e09f367-3cbc-40d7-ade2-5194f6866d18`)
- [[../resources/data-tables/s79t8iehgnurdtue|Elavon - Disable ACH Gateway Queue]] (id `s79T8iEHGNuRDtuE`) — op `update` — node "Update row(s)1" (id `60934baf-0b48-451a-b354-da04c1118443`)
- [[../resources/data-tables/s79t8iehgnurdtue|Elavon - Disable ACH Gateway Queue]] (id `s79T8iEHGNuRDtuE`) — op `get` — node "Get row(s)" (id `a7127d60-58c3-4e7e-918f-d3ac80b11176`)
- [[../resources/data-tables/s79t8iehgnurdtue|Elavon - Disable ACH Gateway Queue]] (id `s79T8iEHGNuRDtuE`) — op `rowNotExists` — node "If row does not exist" (id `b32627d2-0d66-4928-8481-43ddaae3baf8`)
- [[../resources/data-tables/s79t8iehgnurdtue|Elavon - Disable ACH Gateway Queue]] (id `s79T8iEHGNuRDtuE`) — op `get` — node "Get row(s)3" (id `d996461f-61ad-4990-aac4-0d27757dc43c`)
- [[../resources/data-tables/s79t8iehgnurdtue|Elavon - Disable ACH Gateway Queue]] (id `s79T8iEHGNuRDtuE`) — op `get` — node "Get row(s)1" (id `dd8180ae-6c25-42aa-be35-e78a97446e40`)

### Sub-workflows (Execute Workflow calls)

- [[check-elavon-ach-gateway-status-2|Check Elavon ACH gateway status 2]] (n8n_id `WaRNwwXwbHcPmYTk`) — node "Call 'Check Elavon ACH gateway status'1" (id `199b1e81-4a9d-45fd-9455-3c022c626389`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'6" (id `428c1c56-ebbe-42d8-b40b-600bc47cd4d3`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'3" (id `45449ddf-5999-4374-aae0-05fef0fb40c9`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `55c9c155-3e40-426a-ba0a-d6bd3d41257d`)
- [[disable-elavon-ach-gateway-for-a-given-merchant|Disable Elavon ACH gateway for a given merchant]] (n8n_id `E66SPMxJDH28QBxI`) — node "Call 'Disable Elavon ACH gateway for a given merchant'1" (id `63409834-d9a6-4168-a41d-f6abedf1831c`)
- [[check-elavon-ach-gateway-status|Check Elavon ACH gateway status]] (n8n_id `MgUymrWWSzLhoUxF`) — node "Call 'Check Elavon ACH gateway status'" (id `6dd09ced-1166-41c6-9df6-4a7ef83a01fd`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Create a base message1" (id `739cdbfb-a3a1-4230-b8db-510df342d7f8`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'1" (id `775881ec-519c-4594-af58-e04b0fd317a8`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'9" (id `86bc40d1-e31f-47ef-801d-b2f2d4a23957`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'4" (id `ae9b4e81-4021-479e-ac64-d788e5ec791f`)
- [[check-elavon-ach-gateway-status|Check Elavon ACH gateway status]] (n8n_id `MgUymrWWSzLhoUxF`) — node "Call 'Check Elavon ACH gateway status'2" (id `c843631c-55dd-436e-bcde-5d1d09117a66`)
- [[disable-elavon-ach-gateway-for-a-given-merchant|Disable Elavon ACH gateway for a given merchant]] (n8n_id `E66SPMxJDH28QBxI`) — node "Call 'Disable Elavon ACH gateway for a given merchant'" (id `cc07df45-e7fe-44c8-9ad5-7e1b123242a6`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Create a base message" (id `d14e6a9b-58cc-41ec-8227-e91a0eb3085c`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'2" (id `d81b9ea2-0644-4da3-836e-fb03d7b02efa`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
