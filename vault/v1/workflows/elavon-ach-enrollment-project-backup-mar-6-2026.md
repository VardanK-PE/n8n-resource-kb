---
n8n_id: "3S9GieeEX931NTyh"
name: "Elavon ACH Enrollment Project - Backup Mar 6, 2026"
status: inactive
last_modified: 2026-03-09T18:41:51.376Z
tags: []
fingerprint: "a62c6e45e5309aa4a166cdc7cc85a8370872d344904da5eecf12585de882b099"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Elavon ACH Enrollment Project - Backup Mar 6, 2026

## Summary

- **Status:** inactive
- **n8n ID:** `3S9GieeEX931NTyh`
- **Nodes:** 136
- **Last modified:** 2026-03-09T18:41:51.376Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `24ff3d97-498e-4496-ab01-2f31700ef8f3`) — `every 4 hour(s)`
- **error** — node "Error Trigger" (id `3d35f6ae-39e5-4f24-b337-1d6a9c4695fa`)
- **manual** — node "When clicking ‘Execute workflow’" (id `923262ab-02ed-4adb-97f2-9258f70db20d`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Error - Error downloading signed document" (id `014886a2-d5b3-47ff-bc1c-a731a9f8c807`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet2" (id `03fb04be-ed50-4c47-a5f0-f517acea7f74`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report error happened when checking for signature" (id `06b0370c-70ca-449a-bad6-ee445c5fcddd`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Download AuditLog" (id `07ef7f5d-478b-4e06-a63e-604a68440631`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Download AuditLog" (id `07ef7f5d-478b-4e06-a63e-604a68440631`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `0a7f33fa-c7be-4fc8-b4d6-15e5da9467cb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `14f12846-0f92-46a1-8aaa-371e1c8a05ea`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file1" (id `1871f663-ec3d-4396-9b2e-598f661343d9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download a draft form" (id `1cc539e4-5fc2-4c38-9611-97e5c2d17a45`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing4" (id `24302a50-51c5-445f-ad87-b0c24698a504`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Download Signed File" (id `2655d80f-0f05-430f-86ff-33b188ef29a6`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Download Signed File" (id `2655d80f-0f05-430f-86ff-33b188ef29a6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Sent Docs1" (id `2761e2f5-3af3-4df2-ab05-b3f5c77509df`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file5" (id `28d95d83-a8ce-4a61-9ecd-2b36182419c3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file4" (id `2c5b3e58-32aa-45bb-8293-5edc82fe08d4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet1" (id `2c8c66ac-b9e2-4232-bc44-99fadc8f7ad0`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get merchant data1" (id `34cdcf30-f899-403e-99ca-61eaaac6400b`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request" (id `36bcadc1-2a4f-4432-94d1-41ea5402fab1`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing" (id `3bb13915-1469-4726-8915-48cae559a398`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing5" (id `3ff403bd-8741-441b-a8d6-375fcd681bb2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `4034f33b-87f2-4af6-ac13-fb8568f39643`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file3" (id `445e08a6-92c5-44a2-90cd-97b7faab0bb4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet2" (id `4ca1f084-902f-467e-a158-51ec51456ac4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Save signed PDF" (id `4ff3d388-e87c-4a7c-ad52-8aa5d6be44c6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Save audit log" (id `5c729628-e061-49d2-ac2a-f0f54b528b4a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `5f3e9146-d4ff-4978-87f9-b5a72df8d5de`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Set entry processing completed1" (id `64e6b2e9-5767-409d-aad3-9a5f988ddd41`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report signed documents received" (id `66c25b6c-f96f-47c7-a52a-7104015e393d`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request1" (id `6cc9c033-32e0-4bd3-bc5f-7ef0c99ceebf`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query2" (id `74d43165-2c9b-47f4-9f1e-f6c5347a5a3e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report problem retrieving data for merchants" (id `7c1a65ca-5783-4e29-9170-378a10e62029`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report the merchant did not respond to signature request1" (id `7c9aefa7-c541-4320-a7cf-7df75f6492d7`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request2" (id `7ed5b203-0842-4eb7-8cf7-4b369ecc0091`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send a message" (id `85ce7140-788e-4bbe-8914-b7a5d9c6ebc2`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report docs are waiting for approval" (id `8a990138-c922-411b-84de-ef030ff30793`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Error - Error downloading signed document4" (id `8f3a4f25-688d-4ab4-a8ff-09e0a86771da`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `92b9a66e-c670-43c7-a69e-0f96e20cd767`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `94eb2e16-d1b3-4e6f-8273-3efebc8f8f6c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Sent Docs" (id `9959fb95-934b-463a-b932-c2855c4b6fc3`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report error happened when checking for signature1" (id `a3b53112-8842-464e-8320-69d9d7e9a187`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Set entry processing completed" (id `a4bf24ea-289b-4255-b6e0-f03d45029223`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Approved Docs" (id `a728fff0-b84a-408f-bc9d-875fd4c2067f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report the merchant did not respond to signature request" (id `aac91169-db29-4d3a-905d-577d5b3fe9e4`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing1" (id `ae7f949e-4866-4014-b54f-9e32d0d96a8a`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Remove old submission" (id `af762880-dc85-424e-8bd4-7dc2e31a825b`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Get Submission Status" (id `b352c0e6-db75-4e6a-9a80-eb412f34f606`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create a draft" (id `bc1fbb3c-9a67-453f-acd7-128ed30462e7`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send a message2" (id `c8526aa9-7661-458b-8c77-5fb25bdd5646`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query1" (id `c882eaba-0b1a-48f6-9818-908d423684be`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Get Submission Status1" (id `d9bbfb5f-d933-4d43-ad90-cae04d66d3c0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet1" (id `e5fcc730-f879-4268-b683-f2b6002e0a57`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file" (id `e62d46b1-8b47-4e8a-b2a2-af17583f3121`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get merchant data" (id `e6751ef1-387a-407c-ac49-6294ee602ff0`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report docs are waiting for approval1" (id `e74d91f3-05e7-430e-9b66-846013761c9b`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing6" (id `e95fe02b-dfdf-4623-bf45-47ce5d2ad125`)
- [[../resources/credentials/qoe8xwrjuiohobns|EasyPost Prod Account]] (`httpBasicAuth`, id `qoE8xwrJUiOHObns`) — node "Create and verify address" (id `ed6720d1-4f68-436d-9ff9-00930b2ba862`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create a draft2" (id `eec6b608-7d0b-4043-a3a0-ef4c2f397082`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet3" (id `f652a418-b04e-4f41-b29f-a42dad8046e2`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Error - Error downloading signed document3" (id `fd2a18f5-7cea-4d83-9a48-9a7378b79cca`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report the merchant did not respond to signature request2" (id `fd9f8032-e5e0-4c0e-b78f-2f25634685ba`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ $json.audit_log_url }}` — node "Download AuditLog" (id `07ef7f5d-478b-4e06-a63e-604a68440631`)
- *(dynamic URL)* — `GET {{ $json.document_url }}` — node "Download Signed File" (id `2655d80f-0f05-430f-86ff-33b188ef29a6`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions/pdf` — node "HTTP Request" (id `36bcadc1-2a4f-4432-94d1-41ea5402fab1`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions/pdf` — node "HTTP Request1" (id `6cc9c033-32e0-4bd3-bc5f-7ef0c99ceebf`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions/pdf` — node "HTTP Request2" (id `7ed5b203-0842-4eb7-8cf7-4b369ecc0091`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `DELETE https://api.docuseal.com/submissions/{{ $json.id }}` — node "Remove old submission" (id `af762880-dc85-424e-8bd4-7dc2e31a825b`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submissions/{{ $json['Submission ID'] }}` — node "Get Submission Status" (id `b352c0e6-db75-4e6a-9a80-eb412f34f606`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submissions?status=pending&q={{ $json['Email Signature'] }}&limit=100` — node "Get Submission Status1" (id `d9bbfb5f-d933-4d43-ad90-cae04d66d3c0`)
- [[../resources/http-urls/api-easypost-com|api.easypost.com]] — `POST https://api.easypost.com/v2/addresses/create_and_verify` — node "Create and verify address" (id `ed6720d1-4f68-436d-9ff9-00930b2ba862`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get merchant data1" (id `34cdcf30-f899-403e-99ca-61eaaac6400b`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query2" (id `74d43165-2c9b-47f4-9f1e-f6c5347a5a3e`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `94eb2e16-d1b3-4e6f-8273-3efebc8f8f6c`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query1" (id `c882eaba-0b1a-48f6-9818-908d423684be`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get merchant data" (id `e6751ef1-387a-407c-ac49-6294ee602ff0`)

### Google Sheets

- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `update`, tab `Sheet1` — node "Update row in sheet2" (id `03fb04be-ed50-4c47-a5f0-f517acea7f74`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `?`, tab `Sheet1` — node "Get row(s) in sheet" (id `0a7f33fa-c7be-4fc8-b4d6-15e5da9467cb`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `appendOrUpdate`, tab `Sheet1` — node "Append or update row in sheet" (id `14f12846-0f92-46a1-8aaa-371e1c8a05ea`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `?`, tab `Sheet1` — node "Get Sent Docs1" (id `2761e2f5-3af3-4df2-ab05-b3f5c77509df`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `update`, tab `Sheet1` — node "Update row in sheet1" (id `2c8c66ac-b9e2-4232-bc44-99fadc8f7ad0`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `?`, tab `Sheet1` — node "Get row(s) in sheet1" (id `4034f33b-87f2-4af6-ac13-fb8568f39643`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `appendOrUpdate`, tab `Sheet1` — node "Append or update row in sheet2" (id `4ca1f084-902f-467e-a158-51ec51456ac4`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `update`, tab `Sheet1` — node "Update row in sheet" (id `5f3e9146-d4ff-4978-87f9-b5a72df8d5de`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `update`, tab `Sheet1` — node "Set entry processing completed1" (id `64e6b2e9-5767-409d-aad3-9a5f988ddd41`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `?`, tab `Sheet1` — node "Get Sent Docs" (id `9959fb95-934b-463a-b932-c2855c4b6fc3`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `update`, tab `Sheet1` — node "Set entry processing completed" (id `a4bf24ea-289b-4255-b6e0-f03d45029223`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `?`, tab `Sheet1` — node "Get Approved Docs" (id `a728fff0-b84a-408f-bc9d-875fd4c2067f`)
- [[../resources/google-sheets/1kmyrbqfyux3a8407nqtqlisjtcwa-ies6vb0qaproa8|Active Hearth merchants]] (id `1kMYRBqFYUx3a8407NqtQLiSJtCwA-Ies6Vb0QaPROA8`) — op `appendOrUpdate`, tab `Sheet1` — node "Append or update row in sheet1" (id `e5fcc730-f879-4268-b683-f2b6002e0a57`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `appendOrUpdate`, tab `Sheet1` — node "Append or update row in sheet3" (id `f652a418-b04e-4f41-b29f-a42dad8046e2`)

### Google Drive

- *(dynamic)* — op `download` — node "Download file1" (id `1871f663-ec3d-4396-9b2e-598f661343d9`)
- [[../resources/google-drive/1dzfcvjdodte8rczqfb0xbp28ijkefbav|ACH_Electronic_Check_Service_Enrollment_Form_Indirect_JULY_2025_3.pdf]] (`file`, id `1dZFCVJDodTe8rCZqFB0XbP28iJKEfbaV`) — op `download` — node "Download a draft form" (id `1cc539e4-5fc2-4c38-9611-97e5c2d17a45`)
- *(dynamic)* — op `download` — node "Download file5" (id `28d95d83-a8ce-4a61-9ecd-2b36182419c3`)
- *(dynamic)* — op `download` — node "Download file4" (id `2c5b3e58-32aa-45bb-8293-5edc82fe08d4`)
- *(dynamic)* — op `download` — node "Download file3" (id `445e08a6-92c5-44a2-90cd-97b7faab0bb4`)
- [[../resources/google-drive/1m8lvv7nytyc3pkzcppk2olblyvjwxd12|Signed]] (`folder`, id `1M8LVV7NYTyc3PKzCPpk2OlBLYVJwXd12`) — op `?` — node "Save signed PDF" (id `4ff3d388-e87c-4a7c-ad52-8aa5d6be44c6`)
- [[../resources/google-drive/1m8lvv7nytyc3pkzcppk2olblyvjwxd12|Signed]] (`folder`, id `1M8LVV7NYTyc3PKzCPpk2OlBLYVJwXd12`) — op `?` — node "Save audit log" (id `5c729628-e061-49d2-ac2a-f0f54b528b4a`)
- *(dynamic)* — op `download` — node "Download file" (id `92b9a66e-c670-43c7-a69e-0f96e20cd767`)
- [[../resources/google-drive/1u9mgwcdwzxtfvm73-qxxuv7dcpep3s1c|Unsigned]] (`folder`, id `1U9MGwcdwZXTfVm73-qxXuv7DcPep3S1c`) — op `?` — node "Upload file" (id `e62d46b1-8b47-4e8a-b2a2-af17583f3121`)

### Slack channels

- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Error - Error downloading signed document" (id `014886a2-d5b3-47ff-bc1c-a731a9f8c807`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report error happened when checking for signature" (id `06b0370c-70ca-449a-bad6-ee445c5fcddd`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Items sent for singing4" (id `24302a50-51c5-445f-ad87-b0c24698a504`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Items sent for singing" (id `3bb13915-1469-4726-8915-48cae559a398`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Items sent for singing5" (id `3ff403bd-8741-441b-a8d6-375fcd681bb2`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report signed documents received" (id `66c25b6c-f96f-47c7-a52a-7104015e393d`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report problem retrieving data for merchants" (id `7c1a65ca-5783-4e29-9170-378a10e62029`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report the merchant did not respond to signature request1" (id `7c9aefa7-c541-4320-a7cf-7df75f6492d7`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report docs are waiting for approval" (id `8a990138-c922-411b-84de-ef030ff30793`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Error - Error downloading signed document4" (id `8f3a4f25-688d-4ab4-a8ff-09e0a86771da`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report error happened when checking for signature1" (id `a3b53112-8842-464e-8320-69d9d7e9a187`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report the merchant did not respond to signature request" (id `aac91169-db29-4d3a-905d-577d5b3fe9e4`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Items sent for singing1" (id `ae7f949e-4866-4014-b54f-9e32d0d96a8a`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report docs are waiting for approval1" (id `e74d91f3-05e7-430e-9b66-846013761c9b`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Items sent for singing6" (id `e95fe02b-dfdf-4623-bf45-47ce5d2ad125`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Error - Error downloading signed document3" (id `fd2a18f5-7cea-4d83-9a48-9a7378b79cca`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report the merchant did not respond to signature request2" (id `fd9f8032-e5e0-4c0e-b78f-2f25634685ba`)

### Sub-workflows (Execute Workflow calls)

- [[elavon-ach-exemption-form-generator|Elavon ACH Exemption Form Generator]] (n8n_id `c4rexPHrWGfGDBUP`) — node "Execute Workflow1" (id `26551902-0cd9-44df-a6ea-12383115cc13`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `662f71ef-cec5-4f0c-8982-bb483eaba7d4`)
- [[send-email-simple-text|Send Email: Simple Text]] (n8n_id `Zr3vF0LVpsPrzHVY`) — node "Call 'Send Email: Simple Text'" (id `66b2b56f-9587-49e2-affd-a8b41fbddda2`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
