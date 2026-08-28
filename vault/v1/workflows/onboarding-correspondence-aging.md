---
n8n_id: "DjgdzbbtR7fJ4oWX"
instance: v1
name: "Onboarding Correspondence Aging"
status: active
last_modified: 2026-04-21T18:51:53.023Z
tags: []
fingerprint: "f401dab0f4681179ccfce972371118ac502e47a3ead4dfd76562d5dfe37fcce8"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Onboarding Correspondence Aging

## Summary

- **Status:** active
- **n8n ID:** `DjgdzbbtR7fJ4oWX`
- **Nodes:** 79
- **Last modified:** 2026-04-21T18:51:53.023Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `8a5f0df2-da9f-4c1d-9adb-38f66f8fe5d7`)
- **error** — node "Error Trigger" (id `b28c0509-2b5d-4cae-9dbf-c48dedd4d6e4`)
- **schedule** — node "Schedule Trigger1" (id `ba10afc2-047f-4fac-a6fa-6897e40e78dc`) — `every 1 week(s), every 1 week(s)`
- **execute-workflow** — node "When Executed by Another Workflow" (id `c90f5064-4528-4433-b597-a6daa180ac9f`)
- **schedule** — node "Schedule Trigger" (id `e51bdbd7-67b5-4b01-b64e-d5f3691de33b`) — `daily at 4:00, daily at 13:00, daily at 14:36`
- **schedule** — node "Schedule Trigger2" (id `ebb42198-a00b-4e43-8215-88f6dba11ad1`) — `every 1 week(s), every 1 week(s)`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Latest Correspondence Record" (id `0032c38a-9d42-455c-9581-6b855020e450`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `0eff225c-f513-4c13-900b-0a6cc8aa6c55`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message13" (id `16a4803a-509e-4c91-b39a-69144ac8bc34`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `1db91d91-119c-4d80-b59d-75ede75de0ac`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet3" (id `25aa0377-9451-4bef-b0f7-afec942038d1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet4" (id `28d56ca0-314a-4e7c-a0aa-ca44e8923d45`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "From Forte" (id `29fd4f19-ff75-49c7-a58b-056d8f34a7dc`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send a message3" (id `2bd7ba3f-bede-43a0-87b2-b6f249749e11`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message16" (id `2e96b837-d096-48f7-b834-e4b697c5c1a1`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message12" (id `53db1a6b-a98b-47bc-990e-61944bfa53b2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `547c8e9e-b4e9-4a7f-ba9a-fe4b293c0d1e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet2" (id `56f9cc0d-41a2-4c79-a7c2-64153e6e342a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Remapped AWBs" (id `5ccde573-ffab-42c3-a457-928712bd494d`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send a message10" (id `6a49a215-ff90-4b50-8dde-cc4f20c6e4b2`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message14" (id `750330d4-a78d-4a6b-8607-18a4b474cd97`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query1" (id `7defc07f-9a36-4f7f-baae-6bc84137098d`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send a message2" (id `7e9adf44-486c-41a0-866e-b4c8f5f37c08`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send a message9" (id `7eb36f98-7c26-4d4f-8429-7c466681e8f3`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message15" (id `993e7b01-12a3-48fc-9cd2-fac028e5ea18`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "From Merchant" (id `a18aa6cb-383c-4b90-a879-3ede091c6191`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "To Forte" (id `a7f2fe8e-b633-4236-b24a-6d65a15d4efb`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "To Elavon" (id `a92ce36e-6739-4ab0-880d-b471dac9300e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `ab82766d-113a-42c7-b3f5-08ad001749c4`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message8" (id `bd51a776-2b0e-41c8-9028-c409591aa94b`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send a message7" (id `c61e5e5e-35f4-4de2-b746-637a5a992b81`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `ccd3addc-ceae-49e7-b35a-4f68179c7cba`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `d59c2571-d089-461d-b6aa-8f842ead6a18`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send a message11" (id `da0d8219-d3e2-4da4-88a6-9185d3aa61f2`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `dc82c0e2-2db9-4189-ae3b-d01d9a578926`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `dd12c1f7-c144-479e-99be-0259e900856b`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "To Merchant" (id `de53dcd2-9112-42ac-ab5b-165c79447e0c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `e06c823d-ed93-4192-a168-88c2d41c4d3d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `e19ae970-51f9-4f03-9a03-f321dd3de3e2`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message17" (id `e36c2def-ffbe-40b3-b8dc-50c61e5e7d17`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "From Elavon" (id `fe5f47d0-9a33-4d71-8519-34ba8b396b66`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query1" (id `7defc07f-9a36-4f7f-baae-6bc84137098d`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `dc82c0e2-2db9-4189-ae3b-d01d9a578926`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator6" (id `0446f3e6-e6f9-4525-9ff3-1bc5ec6314aa`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator7" (id `13b6b635-90d0-45c3-8930-03604240cefe`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator5" (id `32e5b8cc-4ff0-4ad5-92a4-702db96cb1f8`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator2" (id `4ba97268-1846-4f07-aebb-e975deeb6867`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator3" (id `ae4c2028-eb41-4434-a6cf-e4ed328297e8`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator1" (id `d0a1bd83-d4bc-4f77-bfa4-56f748a43d73`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator4" (id `df91f345-38e7-451a-84af-42356299485e`)
- [[../resources/custom-nodes/n8n-nodes-document-generator|n8n-nodes-document-generator]] — type `n8n-nodes-document-generator.documentGenerator` — node "DocumentGenerator" (id `e77d44df-21fd-455d-9e77-0729bbd05004`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `correspondanceDelays` — node "Latest Correspondence Record" (id `0032c38a-9d42-455c-9581-6b855020e450`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `correspondanceDelays` — node "Append or update row in sheet" (id `1db91d91-119c-4d80-b59d-75ede75de0ac`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `correspondanceDelays` — node "Get row(s) in sheet3" (id `25aa0377-9451-4bef-b0f7-afec942038d1`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `correspondanceDelays` — node "Get row(s) in sheet4" (id `28d56ca0-314a-4e7c-a0aa-ca44e8923d45`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `correspondanceDelays` — node "Get row(s) in sheet1" (id `547c8e9e-b4e9-4a7f-ba9a-fe4b293c0d1e`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `correspondanceDelays` — node "Get row(s) in sheet2" (id `56f9cc0d-41a2-4c79-a7c2-64153e6e342a`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `awb-remaps` — node "Get Remapped AWBs" (id `5ccde573-ffab-42c3-a457-928712bd494d`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `correspondanceDelays` — node "Get row(s) in sheet" (id `ccd3addc-ceae-49e7-b35a-4f68179c7cba`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `correspondanceDelays` — node "Update row in sheet" (id `d59c2571-d089-461d-b6aa-8f842ead6a18`)

### Slack channels

- [[../resources/slack-channels/c09sg9l3zgw|C09SG9L3ZGW]] (id `C09SG9L3ZGW`) — op `channel` — node "Send a message" (id `0eff225c-f513-4c13-900b-0a6cc8aa6c55`)
- *(dynamic channel)* — op `channel` — node "Send a message13" (id `16a4803a-509e-4c91-b39a-69144ac8bc34`)
- *(dynamic channel)* — op `channel` — node "Send a message3" (id `2bd7ba3f-bede-43a0-87b2-b6f249749e11`)
- [[../resources/slack-channels/c0aqn1d03fs|flex-payengine-ai-alerts]] (id `C0AQN1D03FS`) — op `channel` — node "Send a message16" (id `2e96b837-d096-48f7-b834-e4b697c5c1a1`)
- [[../resources/slack-channels/c0aqn1d03fs|flex-payengine-ai-alerts]] (id `C0AQN1D03FS`) — op `channel` — node "Send a message12" (id `53db1a6b-a98b-47bc-990e-61944bfa53b2`)
- [[../resources/slack-channels/c09kj1ydx4k|hearth-onboarding-aging-report]] (id `C09KJ1YDX4K`) — op `channel` — node "Send a message10" (id `6a49a215-ff90-4b50-8dde-cc4f20c6e4b2`)
- [[../resources/slack-channels/c0aqn1d03fs|flex-payengine-ai-alerts]] (id `C0AQN1D03FS`) — op `channel` — node "Send a message14" (id `750330d4-a78d-4a6b-8607-18a4b474cd97`)
- [[../resources/slack-channels/c09kj1ydx4k|hearth-onboarding-aging-report]] (id `C09KJ1YDX4K`) — op `channel` — node "Send a message2" (id `7e9adf44-486c-41a0-866e-b4c8f5f37c08`)
- *(dynamic channel)* — op `channel` — node "Send a message9" (id `7eb36f98-7c26-4d4f-8429-7c466681e8f3`)
- *(dynamic channel)* — op `channel` — node "Send a message15" (id `993e7b01-12a3-48fc-9cd2-fac028e5ea18`)
- *(dynamic channel)* — op `channel` — node "Send a message6" (id `ab82766d-113a-42c7-b3f5-08ad001749c4`)
- *(dynamic channel)* — op `channel` — node "Send a message8" (id `bd51a776-2b0e-41c8-9028-c409591aa94b`)
- [[../resources/slack-channels/c09kj1ydx4k|hearth-onboarding-aging-report]] (id `C09KJ1YDX4K`) — op `channel` — node "Send a message7" (id `c61e5e5e-35f4-4de2-b746-637a5a992b81`)
- *(dynamic channel)* — op `channel` — node "Send a message11" (id `da0d8219-d3e2-4da4-88a6-9185d3aa61f2`)
- [[../resources/slack-channels/c09c901een4|hearth-alerts-internal]] (id `C09C901EEN4`) — op `channel` — node "Send a message4" (id `dd12c1f7-c144-479e-99be-0259e900856b`)
- *(dynamic channel)* — op `channel` — node "Send a message5" (id `e06c823d-ed93-4192-a168-88c2d41c4d3d`)
- *(dynamic channel)* — op `channel` — node "Send a message1" (id `e19ae970-51f9-4f03-9a03-f321dd3de3e2`)
- *(dynamic channel)* — op `channel` — node "Send a message17" (id `e36c2def-ffbe-40b3-b8dc-50c61e5e7d17`)

## Used by (workflows)

- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] — node "Run Correspondence Aging Report" (id `564bd1d8-8eee-4518-b2e5-9c867fa0ac33`)
- [[payengineai-bot-v1-1-feb-26-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] — node "Run Correspondence Aging Report" (id `25568675-6936-4e80-bb49-e1b3c65db470`)
- [[payengineai-bot-v1-1-feb-26-2026-saot95eapiyc8s56|PayEngineAI Bot (v1.1) - Feb 26 2026]] — node "Run Correspondence Aging Report" (id `5143dd76-b493-494f-8294-6705adab3692`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
