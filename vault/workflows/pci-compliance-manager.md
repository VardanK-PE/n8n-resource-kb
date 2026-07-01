---
n8n_id: "qe7aK1jVPOC81wIg"
name: "PCI Compliance Manager"
status: inactive
last_modified: 2025-09-16T19:20:03.613Z
tags: []
fingerprint: "9425d5628813f898e25e0766b9ceef269481ae8f5d9f9d92ca1eaaca117f2fa2"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PCI Compliance Manager

## Summary

- **Status:** inactive
- **n8n ID:** `qe7aK1jVPOC81wIg`
- **Nodes:** 162
- **Last modified:** 2025-09-16T19:20:03.613Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `f5716844-29f4-42b1-8090-0d3a97d03dd0`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `03b0d0d1-f704-4f3d-82a5-74c3d0039f51`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing1" (id `09715676-601c-4ae9-8909-9886ba7cd1b0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Check processing status" (id `0ab25826-a74f-44b4-b1a5-fd04ce69c8b7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get pending merchants1" (id `10680970-e41f-49fe-a774-78ecc22f4017`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing" (id `1708e7e3-5f6e-489a-9f5e-1f18562e1a30`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request7" (id `1b8e6bad-4619-487e-b87f-d30a13a3ebca`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get Merchant Data1" (id `21d044b9-0c15-4005-a2b5-764c0927a567`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets10" (id `21ee0886-4431-440f-9a73-486404d00388`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets11" (id `29afe109-299c-473c-87fa-7beb325124f1`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report docs are waiting for approval" (id `2a4c3b91-7fa2-458a-908c-53f36330938e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `2c36e734-1038-41ed-bcd3-c51d68dcbe31`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing2" (id `2d12101c-3ce2-4ea5-affa-2b4fca13cab0`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Error - Error downloading signed document2" (id `2dc88f4e-c6bf-4d25-ba6f-6afe3343b0fd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Reset processing field" (id `2f758afe-a882-4e2a-8dbd-f2790ec5281c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `312b46dc-c13f-4c11-a817-501d65043ab3`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Create a draft1" (id `34f8265d-f6b8-4b28-b666-3494cc4f7677`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Save signed PDF" (id `3d6295c1-2342-4a7a-98b3-ccbd0b50d746`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request9" (id `416d703f-5be5-4877-95a2-475b34826b21`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Error - Error downloading signed document" (id `4507870a-fd1e-4a16-a044-a3b4633c3935`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report the merchant did not respond to signature request2" (id `4a75f643-0136-4090-a48f-c34c27d3b466`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `5265c506-e9fe-4b27-b723-47134fe2b208`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report the merchant did not respond to signature request1" (id `5292b7bb-eba3-477c-be03-71f226a4dbaa`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report the merchant did not respond to signature request" (id `53afcf79-ce5c-40b5-bd7f-082c89dbdcf2`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `56c41534-7d5a-4237-9905-c105ff51b7eb`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request10" (id `61db0c76-3c92-46bb-98f3-4dfb61a489cb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets13" (id `6409c7b8-2487-4216-999f-2fe4aad81a8d`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Fill the form and send to sign" (id `66bfa32a-8ac0-488d-b1bf-2b4ea663914f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets7" (id `67c4740b-97f0-4b77-9874-8e7548b1b0e1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Retrieve prefilled values" (id `6b2dbc64-e9cf-4ee7-88a7-d7cf1e214ca9`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request3" (id `71c61ed2-c423-4815-a47e-6b39e8f795c7`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing4" (id `7294d314-47c5-4fe6-b183-ab308c1bf30a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `73974ffb-9862-4d5b-96db-e5f960e43685`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request6" (id `7c16b6cc-d0b8-4f29-ad74-128a86cdd4ee`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Approved merchants" (id `7ca87f6d-31de-4472-a5c0-a8c0b968a8d0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `7e1f60b0-26a5-480b-803d-22bcf8bb5fb7`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request2" (id `8648b790-cf8e-4786-a888-83d317369fa0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Set entry processing completed" (id `8ea04870-40e1-4aaa-8a8f-f441dd8258fb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets8" (id `8ec4d417-7957-4bd9-a168-97d5288329c5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Save signed PDF to GDrive" (id `8f54fa4b-4beb-4cf2-9319-d295c79eb1af`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Fill the form and send to sign2" (id `90bac208-cd1b-4353-a2a1-6b59f702fe6f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Save audit log" (id `92ee9bb2-91bb-43fc-9a4f-77cdb1acf9f7`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request" (id `9354354d-2fe5-4847-88b4-3e15a3c501f2`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get Merchant Data" (id `9927eaa0-c119-4f21-8ae9-b97c9e9e5b36`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message2" (id `9c07e4c2-7d1a-4a9d-9d1b-9bbecebcb996`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive" (id `9d9b1c7d-2f52-4bb4-9e60-55f304f94580`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Download Documents" (id `a21feb4a-4f26-43fb-9c88-c21eaf781a63`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Download Documents" (id `a21feb4a-4f26-43fb-9c88-c21eaf781a63`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet1" (id `ad87be4e-6356-491e-b16e-3eec9f54fd84`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request1" (id `ae55a66e-c9b6-45ed-978b-73f823d95e15`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Get Submission Status1" (id `b707db07-e3b9-4967-b0a9-80853324ffa9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets9" (id `b93b4991-28fd-40c7-ae29-c7d1c0e74a0d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Unsigned Merchants" (id `c291183f-f63e-4c66-b068-4f5f82c11543`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message3" (id `c31473a1-e2fb-41ac-b169-2d81630f0000`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request8" (id `cbb0a7e8-28aa-4514-843f-3c7ba5048a15`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `cd617a42-7d2c-4284-a0e4-933338d66a74`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report signed documents received" (id `cde1bdc1-097e-4fa7-89c6-23d89bcf419d`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Fill the form and send to sign1" (id `ce658ce8-9608-49be-bdc1-0fc2efca35e4`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Download Signed File" (id `d0a9ff79-33ab-4a04-aa8c-444f70273ddc`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Download Signed File" (id `d0a9ff79-33ab-4a04-aa8c-444f70273ddc`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request4" (id `dba5094b-f328-4479-a6c2-3705bd061b70`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get pending merchants" (id `dd876af8-a7c4-4343-b31f-d60312c5d710`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report error happened when checking for signature" (id `de283841-dadf-4dfc-a833-ebcb6ab549b0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Check on sent items" (id `dfc05721-c6ef-45cb-b4db-6799a8afc353`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create a draft" (id `e0c5bdb9-de28-4bf3-99a1-0346a74c06ce`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file" (id `e4717611-873e-49ff-8fee-a69855ec728e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Retrieve prefilled values2" (id `e70f3fb5-f474-453a-806b-96939f05476e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Error - Error downloading signed document1" (id `e7e673ee-bf44-4738-b6c9-9c3acb23948f`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Download AuditLog" (id `ed59f97f-deab-4688-96d6-a6fd40dae100`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Download AuditLog" (id `ed59f97f-deab-4688-96d6-a6fd40dae100`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request5" (id `f0a03a4b-2647-44a9-9529-4270a7c5cf16`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `f2ff7ba5-6fde-418c-b669-afaa7fec1a7b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download a draft form" (id `f40c6a83-48e5-4b36-9c31-211a10edc8df`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Retrieve prefilled values1" (id `f5ecee7f-a812-461c-a166-c922c71fde3d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets12" (id `fc5216fb-66cf-420e-8334-ea1cae4e0367`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Get Submission Status" (id `ff4f8b59-f32e-4006-85e0-9c0343379b35`)

### HTTP URLs

- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submitters` — node "HTTP Request7" (id `1b8e6bad-4619-487e-b87f-d30a13a3ebca`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submitters` — node "HTTP Request9" (id `416d703f-5be5-4877-95a2-475b34826b21`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions/pdf` — node "HTTP Request10" (id `61db0c76-3c92-46bb-98f3-4dfb61a489cb`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions` — node "Fill the form and send to sign" (id `66bfa32a-8ac0-488d-b1bf-2b4ea663914f`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submissions/3097513` — node "HTTP Request3" (id `71c61ed2-c423-4815-a47e-6b39e8f795c7`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submitters` — node "HTTP Request6" (id `7c16b6cc-d0b8-4f29-ad74-128a86cdd4ee`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions/pdf` — node "HTTP Request2" (id `8648b790-cf8e-4786-a888-83d317369fa0`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions` — node "Fill the form and send to sign2" (id `90bac208-cd1b-4353-a2a1-6b59f702fe6f`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/templates` — node "HTTP Request" (id `9354354d-2fe5-4847-88b4-3e15a3c501f2`)
- *(dynamic URL)* — `GET {{ $json.document_url }}` — node "Download Documents" (id `a21feb4a-4f26-43fb-9c88-c21eaf781a63`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions` — node "HTTP Request1" (id `ae55a66e-c9b6-45ed-978b-73f823d95e15`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submissions/{{ $json['Submission ID'] }}` — node "Get Submission Status1" (id `b707db07-e3b9-4967-b0a9-80853324ffa9`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submitters` — node "HTTP Request8" (id `cbb0a7e8-28aa-4514-843f-3c7ba5048a15`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions` — node "Fill the form and send to sign1" (id `ce658ce8-9608-49be-bdc1-0fc2efca35e4`)
- *(dynamic URL)* — `GET {{ $json.document_url }}` — node "Download Signed File" (id `d0a9ff79-33ab-4a04-aa8c-444f70273ddc`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions` — node "HTTP Request4" (id `dba5094b-f328-4479-a6c2-3705bd061b70`)
- *(dynamic URL)* — `GET {{ $json.audit_log_url }}` — node "Download AuditLog" (id `ed59f97f-deab-4688-96d6-a6fd40dae100`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions` — node "HTTP Request5" (id `f0a03a4b-2647-44a9-9529-4270a7c5cf16`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submissions/{{ $json['Submission ID'] }}` — node "Get Submission Status" (id `ff4f8b59-f32e-4006-85e0-9c0343379b35`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get Merchant Data1" (id `21d044b9-0c15-4005-a2b5-764c0927a567`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get Merchant Data" (id `9927eaa0-c119-4f21-8ae9-b97c9e9e5b36`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `f2ff7ba5-6fde-418c-b669-afaa7fec1a7b`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-doc-fill|n8n-nodes-doc-fill]] — type `n8n-nodes-doc-fill.docFill` — node "Doc Fill1" (id `72b5154f-fd82-4cb2-a264-57a22452deec`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Check processing status" (id `0ab25826-a74f-44b4-b1a5-fd04ce69c8b7`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get pending merchants1" (id `10680970-e41f-49fe-a774-78ecc22f4017`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Google Sheets10" (id `21ee0886-4431-440f-9a73-486404d00388`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Google Sheets11" (id `29afe109-299c-473c-87fa-7beb325124f1`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Reset processing field" (id `2f758afe-a882-4e2a-8dbd-f2790ec5281c`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Google Sheets" (id `312b46dc-c13f-4c11-a817-501d65043ab3`)
- [[../resources/google-sheets/1nflgutfryodvz8gc7ihshxoeywuaoxe4a29goxqmr2w|PCI Form Fields]] (id `1NFlgutFRYOdvz8Gc7IhsHxOeYWUaoXe4a29goxqMR2w`) — op `?`, tab `PCI 4.0.1 R1 Form Fields` — node "Get row(s) in sheet" (id `5265c506-e9fe-4b27-b723-47134fe2b208`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Google Sheets13" (id `6409c7b8-2487-4216-999f-2fe4aad81a8d`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Google Sheets7" (id `67c4740b-97f0-4b77-9874-8e7548b1b0e1`)
- [[../resources/google-sheets/1nflgutfryodvz8gc7ihshxoeywuaoxe4a29goxqmr2w|PCI Form Fields]] (id `1NFlgutFRYOdvz8Gc7IhsHxOeYWUaoXe4a29goxqMR2w`) — op `?`, tab `PCI 4.0.1 R1 Form Fields` — node "Retrieve prefilled values" (id `6b2dbc64-e9cf-4ee7-88a7-d7cf1e214ca9`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Google Sheets5" (id `73974ffb-9862-4d5b-96db-e5f960e43685`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get Approved merchants" (id `7ca87f6d-31de-4472-a5c0-a8c0b968a8d0`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Google Sheets4" (id `7e1f60b0-26a5-480b-803d-22bcf8bb5fb7`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `update`, tab `Sheet1` — node "Set entry processing completed" (id `8ea04870-40e1-4aaa-8a8f-f441dd8258fb`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Google Sheets8" (id `8ec4d417-7957-4bd9-a168-97d5288329c5`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update row in sheet1" (id `ad87be4e-6356-491e-b16e-3eec9f54fd84`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Google Sheets9" (id `b93b4991-28fd-40c7-ae29-c7d1c0e74a0d`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get Unsigned Merchants" (id `c291183f-f63e-4c66-b068-4f5f82c11543`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update row in sheet" (id `cd617a42-7d2c-4284-a0e4-933338d66a74`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get pending merchants" (id `dd876af8-a7c4-4343-b31f-d60312c5d710`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Check on sent items" (id `dfc05721-c6ef-45cb-b4db-6799a8afc353`)
- [[../resources/google-sheets/1nflgutfryodvz8gc7ihshxoeywuaoxe4a29goxqmr2w|PCI Form Fields]] (id `1NFlgutFRYOdvz8Gc7IhsHxOeYWUaoXe4a29goxqMR2w`) — op `?`, tab `PCI 4.0.1 R1 Form Fields` — node "Retrieve prefilled values2" (id `e70f3fb5-f474-453a-806b-96939f05476e`)
- [[../resources/google-sheets/1nflgutfryodvz8gc7ihshxoeywuaoxe4a29goxqmr2w|PCI Form Fields]] (id `1NFlgutFRYOdvz8Gc7IhsHxOeYWUaoXe4a29goxqMR2w`) — op `?`, tab `PCI 4.0.1 R1 Form Fields` — node "Retrieve prefilled values1" (id `f5ecee7f-a812-461c-a166-c922c71fde3d`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Google Sheets12" (id `fc5216fb-66cf-420e-8334-ea1cae4e0367`)

### Google Drive

- *(dynamic)* — op `download` — node "Download file" (id `2c36e734-1038-41ed-bcd3-c51d68dcbe31`)
- [[../resources/google-drive/1m8lvv7nytyc3pkzcppk2olblyvjwxd12|Signed]] (`folder`, id `1M8LVV7NYTyc3PKzCPpk2OlBLYVJwXd12`) — op `?` — node "Save signed PDF" (id `3d6295c1-2342-4a7a-98b3-ccbd0b50d746`)
- [[../resources/google-drive/root|/ (Root folder)]] (`folder`, id `root`) — op `?` — node "Save signed PDF to GDrive" (id `8f54fa4b-4beb-4cf2-9319-d295c79eb1af`)
- [[../resources/google-drive/1m8lvv7nytyc3pkzcppk2olblyvjwxd12|Signed]] (`folder`, id `1M8LVV7NYTyc3PKzCPpk2OlBLYVJwXd12`) — op `?` — node "Save audit log" (id `92ee9bb2-91bb-43fc-9a4f-77cdb1acf9f7`)
- [[../resources/google-drive/1bcpcqsqjqnojk8puzxme8unzrt5nty6o|PCI_SAQ_A_ECOM_TEMPLATE.pdf]] (`file`, id `1BCPCQsqJqnOJK8PUZxMe8uNzrT5NTy6o`) — op `download` — node "Google Drive" (id `9d9b1c7d-2f52-4bb4-9e60-55f304f94580`)
- [[../resources/google-drive/14usfjge7mhj-bz-rhqqnoecz2siuppyu|PCI Forms - Unsigned]] (`folder`, id `14usFjGe7mHj_Bz-rhQqnOECz2SiuPpyU`) — op `?` — node "Upload file" (id `e4717611-873e-49ff-8fee-a69855ec728e`)
- [[../resources/google-drive/1nmjzu7qayimyjwsdzklxibic1wmc5n5f|PCI-DSS-v4_0_1-SAQ-A-r1_16.pascal.v6.pdf]] (`file`, id `1nMjZu7qayIMyjWsdzKLxiBiC1WMC5n5F`) — op `download` — node "Download a draft form" (id `f40c6a83-48e5-4b36-9c31-211a10edc8df`)

### Slack channels

- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Send a message1" (id `03b0d0d1-f704-4f3d-82a5-74c3d0039f51`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Report Items sent for singing1" (id `09715676-601c-4ae9-8909-9886ba7cd1b0`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Report Items sent for singing" (id `1708e7e3-5f6e-489a-9f5e-1f18562e1a30`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Report docs are waiting for approval" (id `2a4c3b91-7fa2-458a-908c-53f36330938e`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Items sent for singing2" (id `2d12101c-3ce2-4ea5-affa-2b4fca13cab0`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Error - Error downloading signed document2" (id `2dc88f4e-c6bf-4d25-ba6f-6afe3343b0fd`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Report Error - Error downloading signed document" (id `4507870a-fd1e-4a16-a044-a3b4633c3935`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Report the merchant did not respond to signature request2" (id `4a75f643-0136-4090-a48f-c34c27d3b466`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Report the merchant did not respond to signature request1" (id `5292b7bb-eba3-477c-be03-71f226a4dbaa`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report the merchant did not respond to signature request" (id `53afcf79-ce5c-40b5-bd7f-082c89dbdcf2`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Send a message" (id `56c41534-7d5a-4237-9905-c105ff51b7eb`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Items sent for singing4" (id `7294d314-47c5-4fe6-b183-ab308c1bf30a`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Send a message2" (id `9c07e4c2-7d1a-4a9d-9d1b-9bbecebcb996`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Send a message3" (id `c31473a1-e2fb-41ac-b169-2d81630f0000`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report signed documents received" (id `cde1bdc1-097e-4fa7-89c6-23d89bcf419d`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Report error happened when checking for signature" (id `de283841-dadf-4dfc-a833-ebcb6ab549b0`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Report Error - Error downloading signed document1" (id `e7e673ee-bf44-4738-b6c9-9c3acb23948f`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
