---
n8n_id: "ynZxXnClUUPirig4"
instance: v1
name: "Hearth Merchant Capabilities Status"
status: active
last_modified: 2026-05-08T16:10:26.194Z
tags: []
fingerprint: "0be695bc28f51494b4c8c8186e200138f311ee36e72df93390fe47431be43715"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Hearth Merchant Capabilities Status

## Summary

- **Status:** active
- **n8n ID:** `ynZxXnClUUPirig4`
- **Nodes:** 35
- **Last modified:** 2026-05-08T16:10:26.194Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `1a38e410-16bb-47d8-bf6f-d357a3611317`) — `every 1 hour(s) at :10`
- **schedule** — node "Schedule Trigger1" (id `7d00b445-1680-4482-b3c5-5fcd19a47db4`) — `every 1 hour(s) at :20`
- **schedule** — node "Schedule Trigger2" (id `cffbf7a7-b9e1-42ac-b00a-21a2d045a724`) — `every 1 hour(s) at :10`
- **manual** — node "When clicking ‘Execute workflow’" (id `fc465777-82e0-48e0-a41a-ce8bb9bdadb4`)

## Depends on

### Credentials

- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages" (id `0eea5b27-67fe-423d-a536-09219761260c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `4a4e3404-980b-49f0-abcb-a9a0560e52b7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Clear sheet1" (id `5c24d28f-f6ba-4495-a30d-cf4ad062fe89`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query2" (id `6313a7ba-a12c-4068-a7cf-9c1d6e02840f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet1" (id `72ceafbf-f5cb-4971-8f32-5dcca39e2996`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Clear sheet" (id `83109397-9dc2-4c84-ace1-48b9236eace9`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages1" (id `8610d2bf-806c-4e25-ae5f-fbcc1ce8c2d8`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `8aa4bfbf-7236-4f67-b38c-676f995d7ee8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `aecb2147-4c09-4c24-b84e-e67b82729482`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query3" (id `b8599979-afb8-4857-8233-715fba7bfa09`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `e8e92a5f-3a2b-4376-8c5c-814b324988c1`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "PE Merchant merchant-onboarding-api-logs1" (id `ee40a867-4868-4742-a639-a453fc1317e5`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchant-onboarding-api-logs/{{ $json.pe_merchant_id }}` — node "PE Merchant merchant-onboarding-api-logs1" (id `ee40a867-4868-4742-a639-a453fc1317e5`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query2" (id `6313a7ba-a12c-4068-a7cf-9c1d6e02840f`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `8aa4bfbf-7236-4f67-b38c-676f995d7ee8`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query3" (id `b8599979-afb8-4857-8233-715fba7bfa09`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `hearthMIDCapabilites` — node "Get row(s) in sheet" (id `4a4e3404-980b-49f0-abcb-a9a0560e52b7`)
- [[../resources/google-sheets/1swpg9e6oppao-bvxztiuwp3swnuvz-ox0ljaqbvuues|PE Hearth Reports (shared)]] (id `1SwPG9E6OPPAO_BvXZTIuWp3SwnUvZ-OX0LJAQbvUues`) — op `clear`, tab `Active MID Capabilities` — node "Clear sheet1" (id `5c24d28f-f6ba-4495-a30d-cf4ad062fe89`)
- [[../resources/google-sheets/1swpg9e6oppao-bvxztiuwp3swnuvz-ox0ljaqbvuues|PE Hearth Reports (shared)]] (id `1SwPG9E6OPPAO_BvXZTIuWp3SwnUvZ-OX0LJAQbvUues`) — op `appendOrUpdate`, tab `Active MID Capabilities` — node "Append or update row in sheet1" (id `72ceafbf-f5cb-4971-8f32-5dcca39e2996`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `clear`, tab `hearthMIDCapabilites` — node "Clear sheet" (id `83109397-9dc2-4c84-ace1-48b9236eace9`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `hearthMIDCapabilites` — node "Append or update row in sheet" (id `aecb2147-4c09-4c24-b84e-e67b82729482`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `hearthMIDCapabilites` — node "Get row(s) in sheet1" (id `e8e92a5f-3a2b-4376-8c5c-814b324988c1`)

### Sub-workflows (Execute Workflow calls)

- [[check-elavon-ach-gateway-status|Check Elavon ACH gateway status]] (n8n_id `MgUymrWWSzLhoUxF`) — node "Call 'Check ACH gateway status'" (id `07260b91-2fbb-4ef6-9960-d27f183e2816`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
