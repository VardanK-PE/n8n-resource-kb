---
n8n_id: "9UH9sK3CWbFRtVGg"
name: "Elavon BI Automation (Daily Monitor)"
status: active
last_modified: 2026-06-15T16:54:51.298Z
tags: []
fingerprint: "8723115f002feebcd8ba670eab1dc65ab2c1e2fea88448f430b386ad15b60aae"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Elavon BI Automation (Daily Monitor)

## Summary

- **Status:** active
- **n8n ID:** `9UH9sK3CWbFRtVGg`
- **Nodes:** 101
- **Last modified:** 2026-06-15T16:54:51.298Z

## Triggers

- **error** — node "Error Trigger" (id `099eb7b4-ce94-4d0e-a3db-dbdd76311170`)
- **webhook** — node "Webhook" (id `9fb8593a-26ce-48f5-8b18-ac75afb2531b`) — GET `cb2a7e1e-9d9b-4485-9626-260b8c46e7c4`
- **schedule** — node "Schedule Trigger" (id `b56bcd8d-5d1d-4bd7-b473-de6eb13a9271`) — `daily at 7:15`

## Depends on

### Credentials

- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `0c8eadda-d4c6-4c27-8af6-55b76c8f0e66`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `0e0467d9-b13b-4aa4-a6e7-ba6f01bb9fa3`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail1" (id `0f7a4420-0dcf-40b8-8381-f2561dd75454`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `11efca59-4e37-451f-b4c4-f32115334fb7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets8" (id `37e9aa14-13b6-45a1-a3f3-76c22815156f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Chargebacks" (id `4ea36374-7687-4ac4-a361-a4c2d40cb3b6`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `51c61bf8-5f48-4557-afd7-399536819eea`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model2" (id `5276bf07-71e7-4e94-aefc-f009efff09ef`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `5a42d1e7-2ec8-46ff-9cbf-4240d47d2695`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail" (id `635fa646-c23c-44a2-ba42-dfa9702ecd9f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets7" (id `66a1d012-1afb-4a33-aa60-ef16aba827ca`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `6c712e16-a07c-43f1-a2d8-300b2f9e74f1`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file" (id `6d65f46f-a24e-4345-8483-aac2f79f9fc7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets10" (id `715c4ec0-38a9-4386-8d7b-00f97f1bc346`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Retrievals" (id `7ed0ad1f-c53f-4b20-a3e5-d0a7760ab332`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update IBV Monetary" (id `86e543cf-f9b0-4bae-9d54-48d31ddb3ebe`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `9a13494d-5fae-4cfb-97c8-9190447d7d59`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail3" (id `9eee70b8-09e1-4e53-81da-e243834b0404`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail2" (id `a0288b52-f5e1-480f-b48c-c3839d2a2cad`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update MID" (id `a6e4023b-375e-444c-bb06-cf118836d4c2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets6" (id `a8b2fcd7-a0d1-481c-ab36-dcc9ff9413a9`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model3" (id `ba96437e-4b99-4c12-91db-42b96bf69b91`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `bb07eb71-870d-4b49-9e78-4c7a8b3754cf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Partner App Reports" (id `f5b5f35b-516c-417d-8d61-2392d8a0b783`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets9" (id `f65b1bd7-cc50-4121-a4cd-5046cace6330`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres2" (id `fd1a3498-d6fc-4904-815b-0c44092ada9e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update IBV" (id `fd6ac07a-bb7f-4812-ad96-e87f3de41ac2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `fe5f91af-f6f5-4587-985d-f4ba8d611937`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `6c712e16-a07c-43f1-a2d8-300b2f9e74f1`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `bb07eb71-870d-4b49-9e78-4c7a8b3754cf`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres2" (id `fd1a3498-d6fc-4904-815b-0c44092ada9e`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model1" (id `0c8eadda-d4c6-4c27-8af6-55b76c8f0e66`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model" (id `11efca59-4e37-451f-b4c4-f32115334fb7`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model2" (id `5276bf07-71e7-4e94-aefc-f009efff09ef`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model3" (id `ba96437e-4b99-4c12-91db-42b96bf69b91`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator" (id `443a7c00-895c-41c7-b955-936741478498`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator1" (id `f65513a1-28c2-45bb-b2e6-fa7593999417`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partnerApplicationsReport` — node "Google Sheets8" (id `37e9aa14-13b6-45a1-a3f3-76c22815156f`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `chargebacks` — node "Update Chargebacks" (id `4ea36374-7687-4ac4-a361-a4c2d40cb3b6`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `partnerApplicationsReport` — node "Google Sheets7" (id `66a1d012-1afb-4a33-aa60-ef16aba827ca`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `partnerApplicationsReport` — node "Google Sheets10" (id `715c4ec0-38a9-4386-8d7b-00f97f1bc346`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `retrievals` — node "Update Retrievals" (id `7ed0ad1f-c53f-4b20-a3e5-d0a7760ab332`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `ibvMonetary` — node "Update IBV Monetary" (id `86e543cf-f9b0-4bae-9d54-48d31ddb3ebe`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partnerApplicationsReport` — node "Google Sheets5" (id `9a13494d-5fae-4cfb-97c8-9190447d7d59`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `mid` — node "Update MID" (id `a6e4023b-375e-444c-bb06-cf118836d4c2`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partnerApplicationsReport` — node "Google Sheets6" (id `a8b2fcd7-a0d1-481c-ab36-dcc9ff9413a9`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `partnerApplicationsReport` — node "Update Partner App Reports" (id `f5b5f35b-516c-417d-8d61-2392d8a0b783`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `partnerApplicationsReport` — node "Google Sheets9" (id `f65b1bd7-cc50-4121-a4cd-5046cace6330`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `ibv` — node "Update IBV" (id `fd6ac07a-bb7f-4812-ad96-e87f3de41ac2`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Google Sheets1" (id `fe5f91af-f6f5-4587-985d-f4ba8d611937`)

### Slack channels

- [[../resources/slack-channels/c09sg9l3zgw|ops-automation-alert]] (id `C09SG9L3ZGW`) — op `channel` — node "Send a message4" (id `0e0467d9-b13b-4aa4-a6e7-ba6f01bb9fa3`)
- *(dynamic channel)* — op `channel` — node "Send a message5" (id `51c61bf8-5f48-4557-afd7-399536819eea`)

### Sub-workflows (Execute Workflow calls)

- [[calculate-chargeback-composite-key|Calculate Chargeback Composite Key]] (n8n_id `YhBEB2syTygYFXO8`) — node "Execute Workflow1" (id `29e2fb4a-52f8-46c8-9df6-93e36bcfc1c9`)
- [[elavon-on-pi-daily-monitor-completion|Elavon: On PI Daily Monitor Completion]] (n8n_id `yPLpPO9vvfhOXV7W`) — node "Notify on daily monitor completion" (id `382a37f4-5785-4d08-8b8b-a10c5bd76403`)
- [[hearth-daily-application-aging-reports|Hearth - Daily Application Aging Reports]] (n8n_id `hSN8aYP7o7OYfGPY`) — node "Execute Workflow" (id `7578b694-f52b-4649-a522-f96dec1c6966`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
