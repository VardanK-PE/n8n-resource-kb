---
n8n_id: "AHut96GVGmZfIXWw"
name: "Elavon CISCO CRES Message Extractor"
status: active
last_modified: 2026-01-28T16:42:46.326Z
tags: []
fingerprint: "93eebb6878b6cbec58eb701ff5b0ec7314b0a0c5dbea51ce7377ee1f2661f50b"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Elavon CISCO CRES Message Extractor

## Summary

- **Status:** active
- **n8n ID:** `AHut96GVGmZfIXWw`
- **Nodes:** 60
- **Last modified:** 2026-01-28T16:42:46.326Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `627a4304-7ab5-412a-be30-51872fa816f0`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `8d9bbd1a-a862-4700-bd36-da4dab40f71e`)
- **error** — node "Error Trigger" (id `b5989b25-c012-45e1-9180-7f5df1e796e3`)
- **schedule** — node "Schedule Trigger" (id `d31f730a-de72-4dea-be29-79068029d327`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages1" (id `10fa0109-ce80-4975-896a-ea3463e6646c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message2" (id `1ae85e4e-f8e7-4e45-9f37-356eb2e154bc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet3" (id `1f7926d5-9f97-4355-8693-f59c7751bc06`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail7" (id `232520d3-927b-48d1-b57c-8d7a01e36943`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `274ec3e3-0886-4da6-8acc-5e30e94d2888`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get a document" (id `287f5e73-d162-4637-b4fa-d91e56ffc876`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet2" (id `2917c4a1-5eb3-4bbe-b41f-cfe8340e6121`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `33a1ae0a-5816-4fc9-9e8f-c4b6eb0274c4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `43767dc0-7299-402a-9669-5265b25c37ae`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `5c3d3c6d-225e-45d3-aae4-83f8407b208e`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send a message1" (id `6d4e3a91-d52b-4ad7-9143-939e11469bb7`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail5" (id `77d90a5d-d90d-48b9-8fa7-c136333f3493`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages3" (id `8a7f0fff-145b-4972-8470-b2a4a9ace2cb`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message7" (id `8a85afe6-1613-40a1-a2d1-299f944b204c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `900b0b0f-303c-4271-b816-3a0b2cb43b44`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send a message" (id `acec660c-92e1-45b6-8e9f-e1765c94fc7b`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages2" (id `b4f86442-f966-43d4-ae2c-fb766b5dc8f8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet2" (id `b5e4c2f4-50b1-40cf-addc-c179dc6d81e4`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages" (id `c0040cde-7c37-4b1d-82c5-c2a65328a179`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail6" (id `c3d16882-813e-445b-a3a1-b84b7dea632c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `c7594d5c-4b86-43aa-a10d-39456f6cf645`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail3" (id `d0299485-b377-4601-8ba0-5877385eee1f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Upload a file" (id `d47b3d22-ff7a-46f2-99ef-2d172179b1f5`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Add label to message" (id `d6836b85-11a3-4742-86d0-7cea955f4645`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `e38f1c3e-1a55-41fd-93ea-c7360bf6275c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `ebd4e562-7738-47a0-83dd-4f018596dac5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `ec7a594c-1234-4047-9ee6-891da08ffee9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet1" (id `f1b0e233-8bee-4e77-ba9c-ae74c717c91e`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail8" (id `f98867d5-20d0-422c-9bc8-dd86ffa08b63`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `elavon_cisco_cres_messages` — node "Append or update row in sheet3" (id `1f7926d5-9f97-4355-8693-f59c7751bc06`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `update`, tab `emails` — node "Google Sheets5" (id `274ec3e3-0886-4da6-8acc-5e30e94d2888`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `elavon_cisco_cres_messages` — node "Append or update row in sheet2" (id `2917c4a1-5eb3-4bbe-b41f-cfe8340e6121`)
- [[../resources/google-sheets/10yahywgavwbz5ln0aehguzxwp-hieevu7ii7ovj55gg|CISCO_MERCHANT_CREDENTIALS]] (id `10yAHYWgAvWBz5ln0aEhGuzxwP_HIeeVu7iI7ovJ55gg`) — op `?`, tab `Sheet1` — node "Google Sheets" (id `33a1ae0a-5816-4fc9-9e8f-c4b6eb0274c4`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `elavon_cisco_cres_messages` — node "Get row(s) in sheet1" (id `43767dc0-7299-402a-9669-5265b25c37ae`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `elavon_cisco_cres_messages` — node "Get row(s) in sheet" (id `5c3d3c6d-225e-45d3-aae4-83f8407b208e`)
- [[../resources/google-sheets/1h2fats1alewxdviez9ekr-l82ys3dtvuhm83vrs70ea|ELAVON_DISPUTES_TRACKER]] (id `1h2fAts1AlEwXdVIEZ9EkR-L82Ys3DTVUhM83vrs70eA`) — op `?`, tab `emails` — node "Get row(s) in sheet2" (id `b5e4c2f4-50b1-40cf-addc-c179dc6d81e4`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `elavon_cisco_cres_messages` — node "Append or update row in sheet" (id `e38f1c3e-1a55-41fd-93ea-c7360bf6275c`)
- [[../resources/google-sheets/10yahywgavwbz5ln0aehguzxwp-hieevu7ii7ovj55gg|CISCO_MERCHANT_CREDENTIALS]] (id `10yAHYWgAvWBz5ln0aEhGuzxwP_HIeeVu7iI7ovJ55gg`) — op `?`, tab `Sheet1` — node "Google Sheets3" (id `ec7a594c-1234-4047-9ee6-891da08ffee9`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `elavon_cisco_cres_messages` — node "Append or update row in sheet1" (id `f1b0e233-8bee-4e77-ba9c-ae74c717c91e`)

### Slack channels

- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send a message2" (id `1ae85e4e-f8e7-4e45-9f37-356eb2e154bc`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send a message7" (id `8a85afe6-1613-40a1-a2d1-299f944b204c`)
- [[../resources/slack-channels/c092ruaq86q|disputes-automation]] (id `C092RUAQ86Q`) — op `channel` — node "Slack" (id `900b0b0f-303c-4271-b816-3a0b2cb43b44`)
- [[../resources/slack-channels/c0997kku3tr|merchant-emails-assistant-ai]] (id `C0997KKU3TR`) — op `channel` — node "Send a message6" (id `c7594d5c-4b86-43aa-a10d-39456f6cf645`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `ebd4e562-7738-47a0-83dd-4f018596dac5`)

### Google Docs

- [[../resources/google-docs/1ldhpwwwk3udlr-axscnjrib3jyv5kmr6sgelrsx4tys|1ldHPwWwk3udlr-axscNjRIb3jYV5KMr6sGELRSX4tys]] (id `1ldHPwWwk3udlr-axscNjRIb3jYV5KMr6sGELRSX4tys`) — op `get` — node "Get a document" (id `287f5e73-d162-4637-b4fa-d91e56ffc876`)

### Sub-workflows (Execute Workflow calls)

- [[elavon-cisco-cres-message-extractor|Elavon CISCO CRES Message Extractor]] (n8n_id `AHut96GVGmZfIXWw`) — node "Execute Workflow" (id `67076c63-b833-423c-bd1f-468ff0e648dd`)

## Used by (workflows)

- [[elavon-cisco-cres-message-extractor|Elavon CISCO CRES Message Extractor]] — node "Execute Workflow" (id `67076c63-b833-423c-bd1f-468ff0e648dd`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
