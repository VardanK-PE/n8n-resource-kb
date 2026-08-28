---
n8n_id: "MWVMCbgzsdPIr6Rg"
instance: v1
name: "Elavon Loss Prevention Emails AI"
status: inactive
last_modified: 2025-08-30T23:19:51.174Z
tags: []
fingerprint: "3481c11c8d30777e3e4dcc824ffcb7cf6954bbd6686e3aa838c11ce1461f53ae"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Elavon Loss Prevention Emails AI

## Summary

- **Status:** inactive
- **n8n ID:** `MWVMCbgzsdPIr6Rg`
- **Nodes:** 56
- **Last modified:** 2025-08-30T23:19:51.174Z

## Triggers

- **error** — node "Error Trigger" (id `48437580-7ede-426b-8f8d-c018f7ebb788`)
- **manual** — node "Manual Execution" (id `59787472-7a77-4a55-b16b-c409e8c804e8`)
- **schedule** — node "Email Processing AI Trigger" (id `5fd31c6f-8d6d-4ed1-930e-2d01b0e079d0`) — `every 2 minute(s)`
- **schedule** — node "Email Logs Entries Trigger" (id `96fabfd8-14d5-4483-91c4-a5cf591adf78`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Partner Specific Instructions" (id `01205d7e-1418-42f2-9f06-ffd2b571df6a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Skipping trigger due to active processing state1" (id `01a715f4-3ff8-48f6-92bf-43b30e035e98`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create a draft for Merchant in Hearth Inbox" (id `1c5619b4-6ce1-456b-ae3f-cdd9140d13fd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Mark as processing" (id `1ec2e9f2-5bf0-4b6c-824b-f863abcf307d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `296da21b-e568-4767-9a97-2195825da5b3`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create a draft for Elavon Rep in PE Merchants Inbox" (id `2c64eab1-f7ba-4e06-a354-94955cc60b70`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet3" (id `2f6923aa-7d11-4c43-91fc-1581ad80324f`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox (Merchant Responses)" (id `30ce9fb2-a794-4443-ab8a-17346efc9d59`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message2" (id `5331834a-1d4f-42bf-8ffd-2417f689787d`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox (Loss Prevention)" (id `5f21568f-1668-4a52-987c-298f32bd3d0e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `66c36241-7360-4906-a0e4-367dfc7f4957`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Add label to message" (id `7bed4455-033a-4290-8eee-d13ad77b0ae5`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox1" (id `8c771444-c8e8-411d-946d-de2047fa767b`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages From PE Merchants Inbox Gmail" (id `8e6bbf8c-1222-4a2c-8ee9-8c5d74ecb971`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Records to process" (id `a3e2dfd9-8587-437f-8cc3-9537f6d0b3c9`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Add label to message2" (id `b13f67af-25f4-41e6-9bfd-b420bec150b2`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE Merchants Inbox (TAX INFO)" (id `b287b1ed-dd39-43fd-b5c6-0d6fc529f265`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `b8d2b68a-0a9f-49f2-bcc0-8a45b52292b5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `bac0f4ce-a163-4509-9bdf-bd58375bc3d7`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Partner Account Lookup1" (id `bc39177a-ade8-44a0-b60d-77e734264edf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Records in processing state" (id `c3894629-ee53-4e20-866a-14da3021f4c1`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages From Hearth Merchants Inbox Gmail1" (id `c3c41927-82a5-4e88-b90c-423e769eaec7`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create a draft for Merchants in PE Merchants Inbox" (id `c3f9bb6f-8dc8-4759-b3b7-0cb1ddc50338`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `cccff778-f9df-42bd-a0a8-008f8e15486b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet1" (id `cd27dc8d-d0b8-4b51-80ae-09f17038182a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message3" (id `d52bb76f-5b03-4927-8a0d-a0b02c75d056`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `dbdbc08c-acf0-45f7-af72-cdc04af654c9`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get message Details from PE Merchant Inbox" (id `efc0b75e-fd50-4333-be97-3c6d95efffbb`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth Inbox1" (id `f5a6e841-3ba4-4dcb-9a99-96d3ad3cef6b`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `f5cd89f9-7af9-4e54-9864-bd34b7f577ab`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get message Details from Hearth Merchant Inbox1" (id `f66d14d7-4388-41c5-8fdf-bd9d24e1ff8c`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Add label to message1" (id `f906d2b7-d2c3-4be2-b4aa-f691edb41f19`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Partner Account Lookup1" (id `bc39177a-ade8-44a0-b60d-77e734264edf`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model" (id `b8d2b68a-0a9f-49f2-bcc0-8a45b52292b5`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partnerSpceficInstructions` — node "Get Partner Specific Instructions" (id `01205d7e-1418-42f2-9f06-ffd2b571df6a`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `lossPreventionEmailLogs` — node "Mark as processing" (id `1ec2e9f2-5bf0-4b6c-824b-f863abcf307d`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `lossPreventionEmailLogs` — node "Update row in sheet3" (id `2f6923aa-7d11-4c43-91fc-1581ad80324f`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `lossPreventionEmailLogs` — node "Records to process" (id `a3e2dfd9-8587-437f-8cc3-9537f6d0b3c9`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `lossPrevenstionEmailLogs` — node "Append or update row in sheet" (id `bac0f4ce-a163-4509-9bdf-bd58375bc3d7`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `lossPreventionEmailLogs` — node "Records in processing state" (id `c3894629-ee53-4e20-866a-14da3021f4c1`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `lossPreventionEmailLogs` — node "Update row in sheet1" (id `cd27dc8d-d0b8-4b51-80ae-09f17038182a`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `lossPreventionEmailLogs` — node "Update row in sheet" (id `dbdbc08c-acf0-45f7-af72-cdc04af654c9`)

### Slack channels

- [[../resources/slack-channels/c0998514tkp|elavon-loss-prevention-alerts]] (id `C0998514TKP`) — op `channel` — node "Skipping trigger due to active processing state1" (id `01a715f4-3ff8-48f6-92bf-43b30e035e98`)
- [[../resources/slack-channels/c0998514tkp|elavon-loss-prevention-alerts]] (id `C0998514TKP`) — op `channel` — node "Send a message6" (id `296da21b-e568-4767-9a97-2195825da5b3`)
- *(dynamic channel)* — op `channel` — node "Send a message2" (id `5331834a-1d4f-42bf-8ffd-2417f689787d`)
- [[../resources/slack-channels/c0998514tkp|elavon-loss-prevention-alerts]] (id `C0998514TKP`) — op `channel` — node "Send a message" (id `66c36241-7360-4906-a0e4-367dfc7f4957`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `cccff778-f9df-42bd-a0a8-008f8e15486b`)
- [[../resources/slack-channels/c0998514tkp|elavon-loss-prevention-alerts]] (id `C0998514TKP`) — op `channel` — node "Send a message3" (id `d52bb76f-5b03-4927-8a0d-a0b02c75d056`)
- *(dynamic channel)* — op `channel` — node "Send a message1" (id `f5cd89f9-7af9-4e54-9864-bd34b7f577ab`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
