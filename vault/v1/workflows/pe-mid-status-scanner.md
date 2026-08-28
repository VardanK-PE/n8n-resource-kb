---
n8n_id: "Mkm7iWi7eAmwGCTn"
name: "PE Mid Status Scanner"
status: inactive
last_modified: 2025-08-27T15:12:58.317Z
tags: []
fingerprint: "d0a51d4e3e9a83a36372357caba2daacc8b663dfc4449f78f358697642f98e03"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PE Mid Status Scanner

## Summary

- **Status:** inactive
- **n8n ID:** `Mkm7iWi7eAmwGCTn`
- **Nodes:** 116
- **Last modified:** 2025-08-27T15:12:58.317Z

## Triggers

- **error** — node "Error Trigger" (id `34dfdbd9-c000-4323-8b1d-f822594594a9`)
- **manual** — node "When clicking ‘Execute workflow’" (id `556355bd-ac63-495f-877b-b7e7fde71da6`)
- **schedule** — node "Schedule Trigger" (id `5cf82fa1-5be5-4434-864b-06b7dd33f092`) — `every 1 minute(s)`
- **execute-workflow** — node "When Executed by Another Workflow" (id `de10c0ae-7a0d-4a19-b2fd-ebd33c70716b`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Records5" (id `0533ca9c-5048-4af2-9fe9-c15480eabfb5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Records" (id `0698100d-6660-43d2-a202-689e76c5dd1b`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PE_Merchants" (id `08f40eab-3019-4100-8831-e98fd963b60e`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Details" (id `0ce43ab1-bc32-4c88-a022-5d2ec57e71d1`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Update Status2" (id `119dae85-f74c-488c-af9c-0d8b565a1cba`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `13ff0b72-d74e-4558-a19c-c670dca150bf`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Account Merchants1" (id `19ffb938-3eca-4a12-89af-ed8797e57434`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Records8" (id `202a502f-8fe8-4783-bfaa-300ecef678d8`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model2" (id `27b693b9-63ec-40da-8dba-9207a44fb4ef`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message3" (id `2b922b57-daeb-4566-8bae-8caf517b6efe`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `2dbde462-566c-4078-b29a-cd32ee73e75d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Records3" (id `30949e61-c879-4dbf-9b08-a64d2cea7b86`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Partner Account Lookup1" (id `33e3835b-5840-4e68-a598-b75890372993`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Set status to not executing" (id `3e6dc9f2-03be-45fe-9c0e-490b0133d4f6`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `461daca5-c0b0-4077-8354-fe84600c15cb`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Update Status" (id `46cc84e1-0b0a-41f2-9e4c-eb39b86fcc66`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Hearth" (id `4ce78b3c-ae54-4f2a-8771-d624bd5b9994`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Records11" (id `4e7b1123-f2b3-4925-bfbb-4e9321a32385`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Search Hearth Merchants Inbox" (id `52b790c9-d241-4d17-848b-5a005074ca36`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Records4" (id `5937a6a3-acb2-4b26-a522-36d42edbab73`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Set status to not executing1" (id `5ae76176-a7d3-4968-9bc9-449e58ebb30d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `62391c32-aadb-4844-8d80-42360160da6e`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Update Merchant Status" (id `6be3ca71-e1f1-47ea-a3a4-2e3cc45dc695`)
- [[../resources/credentials/rlxlkmcb9jzcnyyk|Postgres ST production read replica]] (`postgres`, id `rlXLkMcb9jzcnYYK`) — node "Execute a SQL query1" (id `6d7176ff-1f88-43e6-92c7-66b4cc0f2677`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Set status to executing" (id `7069bd3e-0bd9-412b-b8e7-0130d576d0e0`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `75291b4b-cc56-4282-8aa1-559473ff21c6`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Account Merchants" (id `77aaa210-5009-4169-aac0-5985fb300aab`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Records9" (id `79c079e2-99a9-4c55-b613-ae3c80e4eed2`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Update Merchant Status3" (id `86cbe687-a06a-4133-99f1-1d53690f53e9`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `9eeab53e-82ac-43f9-9766-db9f4aa1cbcb`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Get Email Details From PE Hearth Inbox" (id `a018b42d-db5b-4b40-8e84-7d058f0b8be9`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant/Partner Details Lookup" (id `a646617a-8ee6-4507-83ca-78c1187bc79f`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Update Merchant Status1" (id `b333b9ba-c8be-4db4-b275-77fa2895a6a2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Records1" (id `b62df4fe-9a23-4ae1-8237-933643411498`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Details1" (id `b6d41baf-fbbb-4ba2-aa60-a1c6c679e1c3`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `b8860d1a-3622-40fd-9a19-550c6e0d56b4`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Update Merchant Status2" (id `ba6ad241-b92d-44bc-8569-0eff7c2df7f7`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `bea62e0e-9a40-4db1-97bb-7398e882413c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Records10" (id `c04b2f02-9fdc-413b-99db-38cfc2be4c06`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Records6" (id `c2b4a563-ba35-4e5a-bf92-a834f4e7a690`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Records2" (id `cb6cf047-fc83-457d-a6bc-14bce5842d0e`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get Email Details From PE Merchants Inbox" (id `d132bf60-8ab1-4947-948c-696409c29502`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Merchant Logs" (id `e875be05-13a6-4de6-81ef-d1c7f267e595`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Records7" (id `e8e632fd-7fe3-43e4-b3b9-a03a48bbfa05`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message2" (id `eaab1175-9896-458c-b37f-c00af1d0fe5f`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Search PE Merchants Inbox" (id `ec8ba7a4-0c03-4163-a3f9-c38ac2b60583`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `f0eab54a-71eb-4bda-8497-5b73bb08afac`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Get Accounts" (id `f836f6ae-1d27-47f0-a07f-4e6275f47c9b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `ff63ac0c-f69b-4381-aa07-2d4a2b54f3cd`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/merchant/{{ $json.pe_merchant_id }}` — node "Get Merchant Details" (id `0ce43ab1-bc32-4c88-a022-5d2ec57e71d1`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_merchant_id }}/status` — node "Update Status2" (id `119dae85-f74c-488c-af9c-0d8b565a1cba`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Account Merchants1" (id `19ffb938-3eca-4a12-89af-ed8797e57434`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/2e5bd48a-bce3-4398-af6b-e4bb33a733df/status` — node "Update Status" (id `46cc84e1-0b0a-41f2-9e4c-eb39b86fcc66`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_merchant_id }}/status` — node "Update Merchant Status" (id `6be3ca71-e1f1-47ea-a3a4-2e3cc45dc695`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Account Merchants" (id `77aaa210-5009-4169-aac0-5985fb300aab`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_merchant_id }}/status` — node "Update Merchant Status3" (id `86cbe687-a06a-4133-99f1-1d53690f53e9`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_merchant_id }}/status` — node "Update Merchant Status1" (id `b333b9ba-c8be-4db4-b275-77fa2895a6a2`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/merchant/{{ $json.pe_merchant_id }}` — node "Get Merchant Details1" (id `b6d41baf-fbbb-4ba2-aa60-a1c6c679e1c3`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_merchant_id }}/status` — node "Update Merchant Status2" (id `ba6ad241-b92d-44bc-8569-0eff7c2df7f7`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/accounts` — node "HTTP Request2" (id `d94597f5-db03-4970-99b2-d429da277ca4`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/user/auth` — node "HTTP Request" (id `db697696-569b-483d-9d27-8bf2b807b7e0`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/magic?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hc3RlckBwbGF0Zm9ybWZhY3RvcnkuaW8iLCJsb2dpbklkIjoiZkJ0WnVqYm5OQiIsImlhdCI6MTc1NTM1NTI1OCwiZXhwIjoxNzU1MzU1NTU4fQ.aL3alR2hOgF3kYFDRwc8wOcWpgMp2V7Z6O6YlfK7uVM` — node "HTTP Request1" (id `e69a5d85-e147-442a-8d50-828685248795`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/merchant/617e0d27-d114-488e-b24e-285f88ffe9dc/logs` — node "Get Merchant Logs" (id `e875be05-13a6-4de6-81ef-d1c7f267e595`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/master/accounts` — node "Get Accounts" (id `f836f6ae-1d27-47f0-a07f-4e6275f47c9b`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Partner Account Lookup1" (id `33e3835b-5840-4e68-a598-b75890372993`)
- [[../resources/databases/postgres-rlxlkmcb9jzcnyyk|postgres (via Postgres ST production read replica)]] — op `executeQuery` — node "Execute a SQL query1" (id `6d7176ff-1f88-43e6-92c7-66b4cc0f2677`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant/Partner Details Lookup" (id `a646617a-8ee6-4507-83ca-78c1187bc79f`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `bea62e0e-9a40-4db1-97bb-7398e882413c`)

### LLM models

- [[../resources/llm-models/anthropic-claude-3-5-sonnet-20241022|anthropic / claude-3-5-sonnet-20241022]] — node "Anthropic Chat Model2" (id `27b693b9-63ec-40da-8dba-9207a44fb4ef`)
- [[../resources/llm-models/anthropic-claude-opus-4-20250514|anthropic / claude-opus-4-20250514]] — node "Anthropic Chat Model" (id `9eeab53e-82ac-43f9-9766-db9f4aa1cbcb`)
- [[../resources/llm-models/anthropic-claude-opus-4-20250514|anthropic / claude-opus-4-20250514]] — node "Anthropic Chat Model1" (id `b8860d1a-3622-40fd-9a19-550c6e0d56b4`)

### Google Sheets

- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `MIDStatusScanner` — node "Existing Records5" (id `0533ca9c-5048-4af2-9fe9-c15480eabfb5`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `MIDStatusScanner` — node "Existing Records" (id `0698100d-6660-43d2-a202-689e76c5dd1b`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `MIDStatusScannerExecuting` — node "Get row(s) in sheet" (id `13ff0b72-d74e-4558-a19c-c670dca150bf`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `MIDStatusScanner` — node "Existing Records8" (id `202a502f-8fe8-4783-bfaa-300ecef678d8`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `MIDStatusScanner` — node "Existing Records3" (id `30949e61-c879-4dbf-9b08-a64d2cea7b86`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `MIDStatusScannerExecuting` — node "Set status to not executing" (id `3e6dc9f2-03be-45fe-9c0e-490b0133d4f6`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `AIExecutionHistory` — node "Existing Records11" (id `4e7b1123-f2b3-4925-bfbb-4e9321a32385`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `MIDStatusScanner` — node "Existing Records4" (id `5937a6a3-acb2-4b26-a522-36d42edbab73`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `MIDStatusScannerExecuting` — node "Set status to not executing1" (id `5ae76176-a7d3-4968-9bc9-449e58ebb30d`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `MIDStatusScannerExecuting` — node "Set status to executing" (id `7069bd3e-0bd9-412b-b8e7-0130d576d0e0`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `MIDStatusScanner` — node "Existing Records9" (id `79c079e2-99a9-4c55-b613-ae3c80e4eed2`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `MIDStatusScanner` — node "Existing Records1" (id `b62df4fe-9a23-4ae1-8237-933643411498`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `MIDStatusScanner` — node "Existing Records10" (id `c04b2f02-9fdc-413b-99db-38cfc2be4c06`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `MIDStatusScanner` — node "Existing Records6" (id `c2b4a563-ba35-4e5a-bf92-a834f4e7a690`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `update`, tab `MIDStatusScanner` — node "Existing Records2" (id `cb6cf047-fc83-457d-a6bc-14bce5842d0e`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `MIDStatusScanner` — node "Existing Records7" (id `e8e632fd-7fe3-43e4-b3b9-a03a48bbfa05`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `append`, tab `MIDStatusScanner` — node "Append row in sheet" (id `f0eab54a-71eb-4bda-8497-5b73bb08afac`)
- [[../resources/google-sheets/1zgtznbhecvtp-hfhbrlt62huww4z7fzpsnzjyyq8vjc|PE Merchant Email AI Assistant]] (id `1ZgTZnBheCvtp-hfhBrlt62HuWW4Z7fzpSnZjYyq8Vjc`) — op `?`, tab `AIExecutionHistory` — node "Get row(s) in sheet1" (id `ff63ac0c-f69b-4381-aa07-2d4a2b54f3cd`)

### Slack channels

- [[../resources/slack-channels/c09ajn9le67|merchant-status-scanner-ai]] (id `C09AJN9LE67`) — op `channel` — node "Send a message3" (id `2b922b57-daeb-4566-8bae-8caf517b6efe`)
- [[../resources/slack-channels/c09ajn9le67|merchant-status-scanner-ai]] (id `C09AJN9LE67`) — op `channel` — node "Send a message4" (id `2dbde462-566c-4078-b29a-cd32ee73e75d`)
- [[../resources/slack-channels/c09ajn9le67|merchant-status-scanner-ai]] (id `C09AJN9LE67`) — op `channel` — node "Send a message" (id `461daca5-c0b0-4077-8354-fe84600c15cb`)
- [[../resources/slack-channels/c09ajn9le67|merchant-status-scanner-ai]] (id `C09AJN9LE67`) — op `channel` — node "Send a message5" (id `62391c32-aadb-4844-8d80-42360160da6e`)
- [[../resources/slack-channels/c09ajn9le67|merchant-status-scanner-ai]] (id `C09AJN9LE67`) — op `channel` — node "Send a message1" (id `75291b4b-cc56-4282-8aa1-559473ff21c6`)
- [[../resources/slack-channels/c09ajn9le67|merchant-status-scanner-ai]] (id `C09AJN9LE67`) — op `channel` — node "Send a message2" (id `eaab1175-9896-458c-b37f-c00af1d0fe5f`)

### Sub-workflows (Execute Workflow calls)

- [[pe-mid-status-scanner|PE Mid Status Scanner]] (n8n_id `Mkm7iWi7eAmwGCTn`) — node "Search Emails" (id `2e4d2d17-6801-404d-94c6-736f8e66ce26`)
- [[pe-mid-status-scanner|PE Mid Status Scanner]] (n8n_id `Mkm7iWi7eAmwGCTn`) — node "Execute Workflow1" (id `47b5db69-fddc-426a-89b3-7b4c959962ff`)
- [[pe-mid-status-scanner|PE Mid Status Scanner]] (n8n_id `Mkm7iWi7eAmwGCTn`) — node "Search Emails (arch)" (id `a85e8646-588a-43e1-b701-f2ee1899bcf0`)

## Used by (workflows)

- [[pe-mid-status-scanner|PE Mid Status Scanner]] — node "Execute Workflow1" (id `47b5db69-fddc-426a-89b3-7b4c959962ff`)
- [[pe-mid-status-scanner|PE Mid Status Scanner]] — node "Search Emails" (id `2e4d2d17-6801-404d-94c6-736f8e66ce26`)
- [[pe-mid-status-scanner|PE Mid Status Scanner]] — node "Search Emails (arch)" (id `a85e8646-588a-43e1-b701-f2ee1899bcf0`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
