---
n8n_id: "lqbiGZX3Bc3f5AaW"
name: "Elavon Dispute"
status: inactive
last_modified: 2026-02-10T17:06:57.232Z
tags: []
fingerprint: "1a131a9b63272c0162a11b86cb2710d73e41874b73061ab2a27a7d17c8021206"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Elavon Dispute

## Summary

- **Status:** inactive
- **n8n ID:** `lqbiGZX3Bc3f5AaW`
- **Nodes:** 338
- **Last modified:** 2026-02-10T17:06:57.232Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `5704fe49-5a84-416b-b465-ebda1d68ff10`)
- **manual** — node "When clicking ‘Execute workflow’" (id `b23493a0-cd77-400d-9427-bf808ded3da4`)
- **schedule** — node "Schedule Trigger" (id `d04bab75-d347-4dfb-9860-2c85aa38a257`) — `every 1 hour(s)`
- **error** — node "Error Trigger" (id `d406832b-9dfc-4b3b-95b8-6a2254ed755f`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message7" (id `0045de85-57dc-42f8-b756-e8a24ed2ca2c`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send a message3" (id `0067faba-2ff2-4792-bcaa-b3a8594815e0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet5" (id `0374ee40-0629-4af2-8b1f-9f5d0017985c`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create a draft9" (id `05b8ae10-9396-4b7a-87ad-e8a2b2734e56`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update transaction details2" (id `05c0f2af-d5b1-4ca3-8949-935641db897f`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send email from Hearth inbox (with Attachments)" (id `07dc1577-1a07-46cf-b883-769806e640de`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message8" (id `0af66e16-229c-4418-8400-3ea87219ae23`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `0b795939-9898-48f9-9822-986af2a61b37`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks10" (id `0d0e6aee-3069-43ae-9653-18dcc1f561d3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update transaction details6" (id `0edc800d-f000-4360-8a33-6ad3f1f432b8`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message10" (id `12dd6881-827a-4089-83c0-a4351421bc18`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update transaction details3" (id `1497fe9b-05a2-4d91-85ba-b4fb58175938`)
- [[../resources/credentials/mla6ntr86w0mqqdf|PE AWS Account (Prod)]] (`aws`, id `mLa6NtR86w0mqQDF`) — node "Download a file2" (id `1537891f-0a9c-4e22-9413-3aacb86c49f3`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Fuzzy match on original transaction2" (id `188c3549-c7e8-486d-af92-3986ef124861`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks11" (id `1a73457e-3b80-4a39-907f-4a272b914520`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send email from Hearth inbox (with Attachments)1" (id `206481cb-ee48-4642-88b5-9d1df70f1a48`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks3" (id `216c6f54-c91c-43db-b5a0-b420512075be`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message9" (id `24f1be6b-df44-4c65-bdc5-774c3b61c20f`)
- [[../resources/credentials/mla6ntr86w0mqqdf|PE AWS Account (Prod)]] (`aws`, id `mLa6NtR86w0mqQDF`) — node "Download a file1" (id `2d7dfb87-372e-4c3a-aa44-11bb018659dd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update transaction details4" (id `2d833def-46e6-46ba-b9fc-82a57b71159c`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks1" (id `2fbeabfb-8310-4c3a-a3a0-2cb79fb6ee51`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send email from PE inbox (with Attachments)1" (id `34091468-c5f6-4511-a355-7a40c6ae59f7`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send email from PE inbox" (id `3b938cd6-3ba4-48c9-b653-c781048ec665`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks14" (id `3ba17d8e-fe95-4a30-be5d-9ab6baeb213d`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks13" (id `3c76360b-ca46-4a8f-83d5-17612d085028`)
- [[../resources/credentials/mla6ntr86w0mqqdf|PE AWS Account (Prod)]] (`aws`, id `mLa6NtR86w0mqQDF`) — node "Download a file" (id `3dabce63-752a-4ffd-9cef-1213f237ba84`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file2" (id `3e2e540d-287d-46d1-ac59-fdb4bfe1192d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update processed file entries" (id `435de80d-7d14-4c42-a6d4-89b4b5f1bf1d`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Fuzzy match on original transaction" (id `44ee5d9b-74e0-416e-9a0c-0641fd4133ec`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "PROD Update Transaction" (id `459be85d-ddc5-4bc9-ab41-2c654f1c275e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get PI Chargebacks" (id `48cc9aa5-70e5-4e97-a822-85c1f57599e4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update transaction details" (id `49f67577-77e2-47f3-9f73-3cd819b96e5d`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create a draft8" (id `4ae8ee0a-1492-40cd-b4a3-3388b213b8f7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update chargeback processing status" (id `4c6d96b8-d85e-4082-aa4d-fb28c05d340d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `4ea49d91-821a-4edb-a7e6-a34c05c5c2c0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get pending disputes3" (id `4f4a20c6-0aea-4f5a-b532-462cfbeebfb5`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send email from Hearth inbox" (id `505366e8-89d7-4764-a3fe-006de5e5b8df`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `51540b2b-e160-4e15-976e-5afebf2771ef`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send message to dispute-alerts" (id `5f4b3480-6bf5-4990-99f7-8669d9f0c6bd`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Fuzzy match on original transaction3" (id `64d8cd23-6eaa-40f2-9995-7a287238d39c`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send email from PE inbox1" (id `6566d1a4-7461-4817-a996-8503adec6b42`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message11" (id `67f00cdc-8975-4eea-96d6-08112bc96f7f`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks2" (id `7009ef23-d1db-427d-82a3-7ee24b953a42`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update transaction details5" (id `73278609-1861-4e0d-bebb-fc82262ffc02`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks9" (id `743c0e0f-24ab-412b-a955-c46ddf35fad3`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `788e1642-393e-4ac7-a870-8f60f1f1a520`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update transaction details1" (id `7c910e11-03db-490a-9cf2-2ef2670dd03b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `7dd476fd-4814-4ef2-a6de-30dd4e2dc544`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Dispute Emails1" (id `82845838-d383-429e-bba0-19242b04b481`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet2" (id `8620843c-e715-46bb-a66d-f0b44e9b239f`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request transaction data" (id `87cba235-0d11-46d6-9964-4f3b215dcebd`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks" (id `8d8704a3-17c4-44b7-a4df-08c3620f0df4`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks8" (id `961a8b7a-b242-4e32-96f0-86a51e159387`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `962a1d91-09b2-4784-a0cc-bae6bdbb6b47`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks12" (id `98e4b96f-252c-4af6-9ba8-a04e73d2f5ec`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send message to nowhere" (id `9ddc40a0-d507-456e-a720-9820aa8f5aa8`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `a0298029-47c9-4644-ac40-2e6ba445797a`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create a draft11" (id `a2fec789-2870-4e50-85ff-26dcb3940d58`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message2" (id `a545c74f-c707-4eac-9598-05f87a9aaa0a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download orphaned email file" (id `b5d761f2-2eda-494f-82d2-f314557dd53a`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks6" (id `b7fd7b7f-8a19-4153-8e22-e4f0ba800ac2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `b9b8045a-aa89-43fd-ae58-061e12feaab9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Elavon dispute emails" (id `c002a685-8e24-4383-8744-7f0edfced735`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `c0ee5e88-7947-4aa2-b916-09e0f5890abf`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks4" (id `c30fae62-67dc-4cec-9e03-e8ee074b3357`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get pending disputes1" (id `c7272f60-44a9-48f8-b1d5-af001a822067`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send email from Hearth inbox1" (id `ca58f7e5-5d13-4972-be55-d6d3bd19d35a`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create a draft10" (id `d0b6faa3-e4bc-456e-be98-c56c3fef8665`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet7" (id `d1910675-b223-4614-8a1f-4f8b896123da`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update transaction details7" (id `db8095f2-3f1b-49bf-a2c9-317797e7a2aa`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get pending disputes" (id `ddf2fbb5-9aca-4d5c-9be0-5b3683c02fa4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get C Transactions" (id `e1a217f8-0080-4ebb-91f9-16a2bb6c2954`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet3" (id `e28aacef-5b65-4459-ade6-afe6e92b9c91`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create a draft" (id `e63ffb33-8cd7-49c3-8cda-26fefcf75636`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet6" (id `e6932cf3-1dfe-414b-9352-0bc1d63a836a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message12" (id `e75d31e2-b619-464f-8b64-bbf754f87c3b`)
- [[../resources/credentials/l1fdqv2gyxyjgim6|PE Staging Sandbox]] (`httpBearerAuth`, id `l1fDQv2GYxYjgim6`) — node "HTTP Request1" (id `e8dce8b2-6f0d-4609-9630-567a8941a79f`)
- [[../resources/credentials/l1fdqv2gyxyjgim6|PE Staging Sandbox]] (`httpBearerAuth`, id `l1fDQv2GYxYjgim6`) — node "Sandbox Staging Update Transaction" (id `ea336132-ee9b-4135-ba51-66e7fe8484ca`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file1" (id `ed016fd7-a21a-442e-bd05-ab51582c688e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Dispute Emails" (id `ed91d387-ff43-4e56-979e-22729f0636bd`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks5" (id `f04c384e-61bd-4bbd-9523-595ae13dd216`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request all chargebacks7" (id `fc22eb58-d65c-41a9-839c-fdd7c6c49ed8`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send email from PE inbox (with Attachments)" (id `fe4ee6a5-fe15-495e-bd03-eac9c75c3cf7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet4" (id `ff787c53-f0be-4f5d-8d0b-ec76e5d90bf4`)

### HTTP URLs

- *(dynamic URL)* — `PATCH {{ $json.parameters.pe_console_base_url }}/api/transaction/{{ $json.parameters.transaction_id }}/dispute` — node "PROD Update Transaction" (id `459be85d-ddc5-4bc9-ab41-2c654f1c275e`)
- [[../resources/http-urls/staging-sandbox-payengine-dev|staging-sandbox.payengine.dev]] — `GET https://staging-sandbox.payengine.dev/api/transaction/{{$json.dispute_id}}/dispute` — node "HTTP Request1" (id `e8dce8b2-6f0d-4609-9630-567a8941a79f`)
- *(dynamic URL)* — `PATCH {{ $json.parameters.pe_console_base_url }}/api/transaction/{{ $json.parameters.transaction_id }}/dispute` — node "Sandbox Staging Update Transaction" (id `ea336132-ee9b-4135-ba51-66e7fe8484ca`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks10" (id `0d0e6aee-3069-43ae-9653-18dcc1f561d3`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Fuzzy match on original transaction2" (id `188c3549-c7e8-486d-af92-3986ef124861`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks11" (id `1a73457e-3b80-4a39-907f-4a272b914520`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks3" (id `216c6f54-c91c-43db-b5a0-b420512075be`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks1" (id `2fbeabfb-8310-4c3a-a3a0-2cb79fb6ee51`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks14" (id `3ba17d8e-fe95-4a30-be5d-9ab6baeb213d`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks13" (id `3c76360b-ca46-4a8f-83d5-17612d085028`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Fuzzy match on original transaction" (id `44ee5d9b-74e0-416e-9a0c-0641fd4133ec`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Fuzzy match on original transaction3" (id `64d8cd23-6eaa-40f2-9995-7a287238d39c`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks2" (id `7009ef23-d1db-427d-82a3-7ee24b953a42`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks9" (id `743c0e0f-24ab-412b-a955-c46ddf35fad3`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request transaction data" (id `87cba235-0d11-46d6-9964-4f3b215dcebd`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks" (id `8d8704a3-17c4-44b7-a4df-08c3620f0df4`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks8" (id `961a8b7a-b242-4e32-96f0-86a51e159387`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks12" (id `98e4b96f-252c-4af6-9ba8-a04e73d2f5ec`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks6" (id `b7fd7b7f-8a19-4153-8e22-e4f0ba800ac2`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks4" (id `c30fae62-67dc-4cec-9e03-e8ee074b3357`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks5" (id `f04c384e-61bd-4bbd-9523-595ae13dd216`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request all chargebacks7" (id `fc22eb58-d65c-41a9-839c-fdd7c6c49ed8`)

### Google Sheets

- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Disputes` — node "Get row(s) in sheet5" (id `0374ee40-0629-4af2-8b1f-9f5d0017985c`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `appendOrUpdate`, tab `Disputes` — node "Update transaction details2" (id `05c0f2af-d5b1-4ca3-8949-935641db897f`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `appendOrUpdate`, tab `Disputes` — node "Update transaction details6" (id `0edc800d-f000-4360-8a33-6ad3f1f432b8`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `appendOrUpdate`, tab `Disputes` — node "Update transaction details3" (id `1497fe9b-05a2-4d91-85ba-b4fb58175938`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `appendOrUpdate`, tab `Disputes` — node "Update transaction details4" (id `2d833def-46e6-46ba-b9fc-82a57b71159c`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `update`, tab `emails` — node "Update processed file entries" (id `435de80d-7d14-4c42-a6d4-89b4b5f1bf1d`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `chargebacks` — node "Get PI Chargebacks" (id `48cc9aa5-70e5-4e97-a822-85c1f57599e4`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `appendOrUpdate`, tab `Disputes` — node "Update transaction details" (id `49f67577-77e2-47f3-9f73-3cd819b96e5d`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `appendOrUpdate`, tab `Chargebacks PI` — node "Update chargeback processing status" (id `4c6d96b8-d85e-4082-aa4d-fb28c05d340d`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Chargebacks PI` — node "Get pending disputes3" (id `4f4a20c6-0aea-4f5a-b532-462cfbeebfb5`)
- [[../resources/google-sheets/1mnr-pxywecmy8vkf3yu8tj7n7p-ymf3aw-ptwwtvwtq|Test Spreadsheet]] (id `1mnR_pxYweCmY8Vkf3Yu8tJ7N7p-yMf3aw-pTWWTVwTQ`) — op `appendOrUpdate`, tab `Sheet1` — node "Append or update row in sheet" (id `51540b2b-e160-4e15-976e-5afebf2771ef`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `appendOrUpdate`, tab `Chargebacks PI` — node "Update transaction details5" (id `73278609-1861-4e0d-bebb-fc82262ffc02`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `appendOrUpdate`, tab `Disputes` — node "Update transaction details1" (id `7c910e11-03db-490a-9cf2-2ef2670dd03b`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Get Dispute Emails1" (id `82845838-d383-429e-bba0-19242b04b481`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Disputes` — node "Get row(s) in sheet2" (id `8620843c-e715-46bb-a66d-f0b44e9b239f`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `chargebacks` — node "Get row(s) in sheet1" (id `962a1d91-09b2-4784-a0cc-bae6bdbb6b47`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `update`, tab `emails` — node "Update row in sheet" (id `b9b8045a-aa89-43fd-ae58-061e12feaab9`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Get Elavon dispute emails" (id `c002a685-8e24-4383-8744-7f0edfced735`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Disputes` — node "Get row(s) in sheet" (id `c0ee5e88-7947-4aa2-b916-09e0f5890abf`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Chargebacks PI` — node "Get pending disputes1" (id `c7272f60-44a9-48f8-b1d5-af001a822067`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Disputes` — node "Get row(s) in sheet7" (id `d1910675-b223-4614-8a1f-4f8b896123da`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `appendOrUpdate`, tab `Chargebacks PI` — node "Update transaction details7" (id `db8095f2-3f1b-49bf-a2c9-317797e7a2aa`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Chargebacks PI` — node "Get pending disputes" (id `ddf2fbb5-9aca-4d5c-9be0-5b3683c02fa4`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Disputes` — node "Get C Transactions" (id `e1a217f8-0080-4ebb-91f9-16a2bb6c2954`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Disputes` — node "Get row(s) in sheet3" (id `e28aacef-5b65-4459-ade6-afe6e92b9c91`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Get row(s) in sheet6" (id `e6932cf3-1dfe-414b-9352-0bc1d63a836a`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Get Dispute Emails" (id `ed91d387-ff43-4e56-979e-22729f0636bd`)
- [[../resources/google-sheets/1yjaxptblalfg3vl85hcqqfx-mbzstwor3olkqbky19a|Elavon Disputes - Datastore]] (id `1YJaXpTBLALFg3Vl85hcQqfx-mBZStwor3oLKqBKy19A`) — op `?`, tab `Disputes` — node "Get row(s) in sheet4" (id `ff787c53-f0be-4f5d-8d0b-ec76e5d90bf4`)

### Google Drive

- *(dynamic)* — op `download` — node "Download file2" (id `3e2e540d-287d-46d1-ac59-fdb4bfe1192d`)
- *(dynamic)* — op `download` — node "Download file" (id `7dd476fd-4814-4ef2-a6de-30dd4e2dc544`)
- *(dynamic)* — op `download` — node "Download orphaned email file" (id `b5d761f2-2eda-494f-82d2-f314557dd53a`)
- *(dynamic)* — op `download` — node "Download file1" (id `ed016fd7-a21a-442e-bd05-ab51582c688e`)

### Slack channels

- [[../resources/slack-channels/c09jr6ph8tx|n8n-sandbox-of-doom]] (id `C09JR6PH8TX`) — op `channel` — node "Send a message7" (id `0045de85-57dc-42f8-b756-e8a24ed2ca2c`)
- [[../resources/slack-channels/c09jr6ph8tx|n8n-sandbox-of-doom]] (id `C09JR6PH8TX`) — op `channel` — node "Send a message8" (id `0af66e16-229c-4418-8400-3ea87219ae23`)
- [[../resources/slack-channels/c0998514tkp|elavon-loss-prevention-alerts]] (id `C0998514TKP`) — op `channel` — node "Send a message" (id `0b795939-9898-48f9-9822-986af2a61b37`)
- [[../resources/slack-channels/c09jr6ph8tx|n8n-sandbox-of-doom]] (id `C09JR6PH8TX`) — op `channel` — node "Send a message10" (id `12dd6881-827a-4089-83c0-a4351421bc18`)
- [[../resources/slack-channels/c09jr6ph8tx|n8n-sandbox-of-doom]] (id `C09JR6PH8TX`) — op `channel` — node "Send a message9" (id `24f1be6b-df44-4c65-bdc5-774c3b61c20f`)
- [[../resources/slack-channels/c09pc6hkhpy|payengine-ai-alerts]] (id `C09PC6HKHPY`) — op `channel` — node "Send a message5" (id `4ea49d91-821a-4edb-a7e6-a34c05c5c2c0`)
- [[../resources/slack-channels/c08r8h75n15|dispute-alerts]] (id `C08R8H75N15`) — op `channel` — node "Send message to dispute-alerts" (id `5f4b3480-6bf5-4990-99f7-8669d9f0c6bd`)
- [[../resources/slack-channels/c08r8h75n15|dispute-alerts]] (id `C08R8H75N15`) — op `channel` — node "Send a message11" (id `67f00cdc-8975-4eea-96d6-08112bc96f7f`)
- [[../resources/slack-channels/c09jr6ph8tx|n8n-sandbox-of-doom]] (id `C09JR6PH8TX`) — op `channel` — node "Send a message6" (id `788e1642-393e-4ac7-a870-8f60f1f1a520`)
- [[../resources/slack-channels/c09jr6ph8tx|n8n-sandbox-of-doom]] (id `C09JR6PH8TX`) — op `channel` — node "Send message to nowhere" (id `9ddc40a0-d507-456e-a720-9820aa8f5aa8`)
- [[../resources/slack-channels/c0998514tkp|elavon-loss-prevention-alerts]] (id `C0998514TKP`) — op `channel` — node "Send a message4" (id `a0298029-47c9-4644-ac40-2e6ba445797a`)
- [[../resources/slack-channels/c0998514tkp|elavon-loss-prevention-alerts]] (id `C0998514TKP`) — op `channel` — node "Send a message2" (id `a545c74f-c707-4eac-9598-05f87a9aaa0a`)
- [[../resources/slack-channels/c09jr6ph8tx|n8n-sandbox-of-doom]] (id `C09JR6PH8TX`) — op `channel` — node "Send a message12" (id `e75d31e2-b619-464f-8b64-bbf754f87c3b`)

### AWS S3 buckets

- *(dynamic bucket)* — op `?` — node "Download a file2" (id `1537891f-0a9c-4e22-9413-3aacb86c49f3`)
- *(dynamic bucket)* — op `?` — node "Download a file1" (id `2d7dfb87-372e-4c3a-aa44-11bb018659dd`)
- *(dynamic bucket)* — op `?` — node "Download a file" (id `3dabce63-752a-4ffd-9cef-1213f237ba84`)

### Sub-workflows (Execute Workflow calls)

- [[send-email-html|Send Email: HTML]] (n8n_id `H9qPciXCz00KxAyF`) — node "Call 'Send Email'" (id `058b9d38-d986-4039-95a4-51db8cf9c3a6`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Create a base message" (id `0bccb684-4934-4a1c-a05d-79304bd2a8fc`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Call 'Elavon Dispute'" (id `2a14fca5-fc1b-45af-aeb8-8848a5bbada4`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Update Transaction State1" (id `2d451884-efe7-4146-9e5e-5b9e7f0f6467`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send email failed notification1" (id `2d669e85-aace-4f60-9e0a-975f5de0e5e5`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send notification4" (id `3a7bae3b-a34c-4169-9e45-b68e3a3b9db6`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send email succeed notification1" (id `3d6cbc6b-cd49-4100-991c-e16331523ca1`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Email not sent notification" (id `4a672851-5f43-4730-adbb-bd211f17791f`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Create Base Message" (id `55b70dff-0754-4885-bba5-1d86a66648a8`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send notification" (id `5fbd2dcc-0550-42c8-ad73-808492f9c8c5`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send notification2" (id `6a6f809b-51b6-475d-bc5c-00e1dfa9dea3`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Send" (id `7217d6da-615d-4ff7-b923-fb665de95505`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send notification13" (id `74e97538-fb97-4074-9ef9-60256d0d0234`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send email not found message" (id `8106e70b-9e0e-4356-ae95-aec4af75e9df`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'1" (id `82045f43-f769-4a71-8b90-ca3c6451ec35`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send actual email1" (id `88aaf008-6ebe-4b89-8933-de20084a595b`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send notification12" (id `95b41b06-a7ab-4aed-b981-59f36f70f817`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send notification1" (id `9b4708e0-feb2-4e3c-8948-555d72655d9d`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send email failed notification" (id `9b5f5093-9562-4651-9a62-0d33b9fe254b`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Create Base Message1" (id `9d2ae75c-efd1-4b5e-afce-1fba4310168d`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Update Transaction State" (id `9f88e1a3-6b68-44c5-be4f-d5a638d0c92b`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send email succeed notification" (id `aa0ddb47-78da-4a1e-bfd0-c96e84dcac57`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send notification3" (id `c16ef3ad-c694-43e9-a557-1ebce76e67da`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Send email not found message1" (id `d1d36b37-394a-4dc9-b8a9-07679c8e97c3`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `d9cb0b33-45f7-40e4-bd2a-a2a9c9a4e30b`)
- [[elavon-dispute|Elavon Dispute]] (n8n_id `lqbiGZX3Bc3f5AaW`) — node "Resolve Transaction Info" (id `e4cc29d9-bfd6-49b6-a01a-e73c96cfc5e5`)

## Used by (workflows)

- [[dispute-process-elavon-attachments|Dispute - Process Elavon attachments]] — node "Create Base Message1" (id `82acd8fd-6cdc-4f19-a954-9acb35273502`)
- [[dispute-process-elavon-attachments|Dispute - Process Elavon attachments]] — node "Email not sent notification" (id `8d78a625-b495-4603-a9cd-81690d9d02e9`)
- [[elavon-dispute|Elavon Dispute]] — node "Call 'Elavon Dispute'" (id `2a14fca5-fc1b-45af-aeb8-8848a5bbada4`)
- [[elavon-dispute|Elavon Dispute]] — node "Create Base Message" (id `55b70dff-0754-4885-bba5-1d86a66648a8`)
- [[elavon-dispute|Elavon Dispute]] — node "Create Base Message1" (id `9d2ae75c-efd1-4b5e-afce-1fba4310168d`)
- [[elavon-dispute|Elavon Dispute]] — node "Email not sent notification" (id `4a672851-5f43-4730-adbb-bd211f17791f`)
- [[elavon-dispute|Elavon Dispute]] — node "Resolve Transaction Info" (id `e4cc29d9-bfd6-49b6-a01a-e73c96cfc5e5`)
- [[elavon-dispute|Elavon Dispute]] — node "Send actual email1" (id `88aaf008-6ebe-4b89-8933-de20084a595b`)
- [[elavon-dispute|Elavon Dispute]] — node "Send email failed notification" (id `9b5f5093-9562-4651-9a62-0d33b9fe254b`)
- [[elavon-dispute|Elavon Dispute]] — node "Send email failed notification1" (id `2d669e85-aace-4f60-9e0a-975f5de0e5e5`)
- [[elavon-dispute|Elavon Dispute]] — node "Send email not found message" (id `8106e70b-9e0e-4356-ae95-aec4af75e9df`)
- [[elavon-dispute|Elavon Dispute]] — node "Send email not found message1" (id `d1d36b37-394a-4dc9-b8a9-07679c8e97c3`)
- [[elavon-dispute|Elavon Dispute]] — node "Send email succeed notification" (id `aa0ddb47-78da-4a1e-bfd0-c96e84dcac57`)
- [[elavon-dispute|Elavon Dispute]] — node "Send email succeed notification1" (id `3d6cbc6b-cd49-4100-991c-e16331523ca1`)
- [[elavon-dispute|Elavon Dispute]] — node "Send notification" (id `5fbd2dcc-0550-42c8-ad73-808492f9c8c5`)
- [[elavon-dispute|Elavon Dispute]] — node "Send notification1" (id `9b4708e0-feb2-4e3c-8948-555d72655d9d`)
- [[elavon-dispute|Elavon Dispute]] — node "Send notification12" (id `95b41b06-a7ab-4aed-b981-59f36f70f817`)
- [[elavon-dispute|Elavon Dispute]] — node "Send notification13" (id `74e97538-fb97-4074-9ef9-60256d0d0234`)
- [[elavon-dispute|Elavon Dispute]] — node "Send notification2" (id `6a6f809b-51b6-475d-bc5c-00e1dfa9dea3`)
- [[elavon-dispute|Elavon Dispute]] — node "Send notification3" (id `c16ef3ad-c694-43e9-a557-1ebce76e67da`)
- [[elavon-dispute|Elavon Dispute]] — node "Send notification4" (id `3a7bae3b-a34c-4169-9e45-b68e3a3b9db6`)
- [[elavon-dispute|Elavon Dispute]] — node "Update Transaction State" (id `9f88e1a3-6b68-44c5-be4f-d5a638d0c92b`)
- [[elavon-dispute|Elavon Dispute]] — node "Update Transaction State1" (id `2d451884-efe7-4146-9e5e-5b9e7f0f6467`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
