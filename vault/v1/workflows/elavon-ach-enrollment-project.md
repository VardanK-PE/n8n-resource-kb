---
n8n_id: "KmnebcPbbtKfdaYY"
instance: v1
name: "Elavon ACH Enrollment Project"
status: active
last_modified: 2026-04-28T16:17:11.986Z
tags: []
fingerprint: "6612ed90d3de4fe595ae098b430adcbeee4ecab9027bf45c6ce593277418117d"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Elavon ACH Enrollment Project

## Summary

- **Status:** active
- **n8n ID:** `KmnebcPbbtKfdaYY`
- **Nodes:** 122
- **Last modified:** 2026-04-28T16:17:11.986Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `c02e695e-0f03-4c87-b0e9-995f31ba2d75`) — `every 4 hour(s)`
- **manual** — node "When clicking ‘Execute workflow’" (id `c3a8f970-5384-42d6-a755-920fd758ae79`)
- **error** — node "Error Trigger" (id `dfe73c71-bdc3-4960-b0ff-03337392e5f8`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `0531aa18-a4e0-444e-8dfc-b7a4f4292631`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file1" (id `114ed2bb-7a65-409d-ac64-5b78aee79143`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get merchant data" (id `17481b93-3548-416d-aded-69bf847965b5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Sent Docs" (id `1b3c3311-df9c-4475-860e-e0fa2cd584a1`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request2" (id `1bf2aefd-0c3c-4501-8d7b-370d2a60656c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Error - Error downloading signed document3" (id `242cd76c-edd0-4cea-a5e4-c1b26fd05747`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing5" (id `2c8ee33f-cfd1-4426-989c-48f8425104c0`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing6" (id `375acf03-fe0a-4fb1-91c0-f8bb4bbac8b9`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Download AuditLog" (id `3f8a4156-44dd-4412-aade-6ea90aa02935`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Download AuditLog" (id `3f8a4156-44dd-4412-aade-6ea90aa02935`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing1" (id `4161af22-5338-4814-ad6d-529384cc87fc`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send a message2" (id `471bd478-efd7-4353-839b-1bc321d20ef8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Set entry processing completed1" (id `487fec81-c65e-49e7-8d95-4c11daa5c62d`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing" (id `4ec6271a-c120-4daf-aee4-2fecdaa6fb4c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file3" (id `57df477a-70a0-42b5-8c70-6bb81e9e0287`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet2" (id `589f9083-5831-41d5-a780-c4b7c73648f6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Sent Docs1" (id `5d93bcc6-0eb0-43df-b0ea-1da2e816836e`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Items sent for singing4" (id `627c048e-e363-455f-bb5c-70b72124d5f3`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Download Signed File" (id `642d994a-be62-448a-bb2a-06eefcad682f`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Download Signed File" (id `642d994a-be62-448a-bb2a-06eefcad682f`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request1" (id `6f73dd6e-5a91-4584-8690-0dee8667fbf4`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Create a draft2" (id `7553067c-ebd4-4327-bc73-b5d43bb74d25`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Save signed PDF" (id `830873e9-6db6-4c46-b0aa-0bc167fdf9ac`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file" (id `853893d3-311f-4d58-98eb-29b3d827c595`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report the merchant did not respond to signature request2" (id `8f9b9d04-9cc2-47e0-96cf-fda30acc7ce8`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report problem retrieving data for merchants" (id `9656efd9-448c-4cea-a33c-fb5641829d51`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `9e97a9c7-af08-42ba-a74e-a8d1bf45a3a9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Approved Docs" (id `ab8fa525-bb51-4aae-9946-fa2cbc97eaf3`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report the merchant did not respond to signature request1" (id `afe5f6bb-0d83-4328-b4f9-4abc1fbf44c6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `b14c53e8-98e6-40af-9ae6-5ecfd39f36e1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet1" (id `b3d4a7aa-37fc-45b6-b730-d7a62de284f1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `bc5b5df6-b7a2-443b-87b1-e81c3571b894`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report error happened when checking for signature" (id `c0659938-1b55-4a50-ac95-f80ee1cc8548`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report docs are waiting for approval" (id `c0ef805c-f0af-47af-839e-dddde18b68dc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `c6d05758-84eb-415a-9715-a67fd0200d06`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Error - Error downloading signed document4" (id `c7694fa8-cfa8-4689-818e-f2ec98b83874`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file5" (id `c8dbb3c9-2c83-4c15-ba2b-95454757f714`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Set entry processing completed" (id `d0054095-fda6-4aaa-ae1e-cf0db697155a`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Send a message" (id `d16e364e-b7f6-4d35-97e1-f2a92dd650bb`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Remove old submission" (id `d39993dd-018f-4de0-9838-e4d2267c2cb5`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report Error - Error downloading signed document" (id `d4184944-e7ba-41ff-8b98-94cd3a7d4264`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Get Submission Status" (id `d52d2eef-38ac-4122-91d4-8ac02632aaad`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Save audit log" (id `d5a8c2a3-a7ce-4cbb-9761-d43473bef8b9`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report docs are waiting for approval1" (id `db983987-ca8c-49de-8660-8243679f2f55`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file4" (id `ddc7a3e6-92bc-4d3b-b748-b14a79f0fc70`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Get Submission Status1" (id `e4062312-231e-496d-a356-3f7eeeaa11dc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download a draft form" (id `f587cccd-5e7c-4da0-bac5-d5df70e89e78`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report error happened when checking for signature1" (id `fe0f1477-2df3-469f-a3ca-e406d89e2894`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report signed documents received" (id `fe116248-ae5c-47ef-a08f-f4cd7c8b669c`)

### HTTP URLs

- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions/pdf` — node "HTTP Request2" (id `1bf2aefd-0c3c-4501-8d7b-370d2a60656c`)
- *(dynamic URL)* — `GET {{ $json.audit_log_url }}` — node "Download AuditLog" (id `3f8a4156-44dd-4412-aade-6ea90aa02935`)
- *(dynamic URL)* — `GET {{ $json.document_url }}` — node "Download Signed File" (id `642d994a-be62-448a-bb2a-06eefcad682f`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions/pdf` — node "HTTP Request1" (id `6f73dd6e-5a91-4584-8690-0dee8667fbf4`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `DELETE https://api.docuseal.com/submissions/{{ $json.id }}` — node "Remove old submission" (id `d39993dd-018f-4de0-9838-e4d2267c2cb5`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submissions/{{ $json['Submission ID'] }}` — node "Get Submission Status" (id `d52d2eef-38ac-4122-91d4-8ac02632aaad`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submissions?status=pending&q={{ $json['Email Signature'] }}&limit=100` — node "Get Submission Status1" (id `e4062312-231e-496d-a356-3f7eeeaa11dc`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `0531aa18-a4e0-444e-8dfc-b7a4f4292631`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get merchant data" (id `17481b93-3548-416d-aded-69bf847965b5`)

### Google Sheets

- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `?`, tab `Sheet1` — node "Get Sent Docs" (id `1b3c3311-df9c-4475-860e-e0fa2cd584a1`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `update`, tab `Sheet1` — node "Set entry processing completed1" (id `487fec81-c65e-49e7-8d95-4c11daa5c62d`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `update`, tab `Sheet1` — node "Update row in sheet2" (id `589f9083-5831-41d5-a780-c4b7c73648f6`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `?`, tab `Sheet1` — node "Get Sent Docs1" (id `5d93bcc6-0eb0-43df-b0ea-1da2e816836e`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `update`, tab `Sheet1` — node "Update row in sheet" (id `9e97a9c7-af08-42ba-a74e-a8d1bf45a3a9`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `?`, tab `Sheet1` — node "Get Approved Docs" (id `ab8fa525-bb51-4aae-9946-fa2cbc97eaf3`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `?`, tab `Sheet1` — node "Get row(s) in sheet1" (id `b14c53e8-98e6-40af-9ae6-5ecfd39f36e1`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `update`, tab `Sheet1` — node "Update row in sheet1" (id `b3d4a7aa-37fc-45b6-b730-d7a62de284f1`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `appendOrUpdate`, tab `Sheet1` — node "Append or update row in sheet" (id `bc5b5df6-b7a2-443b-87b1-e81c3571b894`)
- [[../resources/google-sheets/1otox-drrtqbytbb2yscl2o8hilgqwgxyvsplxvhhbno|Hearth ACH Enrollment Merchant]] (id `1otox_DRRtQBYTBb2YsCl2O8hilGqWGxYVSPLxVHHbno`) — op `update`, tab `Sheet1` — node "Set entry processing completed" (id `d0054095-fda6-4aaa-ae1e-cf0db697155a`)

### Google Drive

- *(dynamic)* — op `download` — node "Download file1" (id `114ed2bb-7a65-409d-ac64-5b78aee79143`)
- *(dynamic)* — op `download` — node "Download file3" (id `57df477a-70a0-42b5-8c70-6bb81e9e0287`)
- [[../resources/google-drive/1m8lvv7nytyc3pkzcppk2olblyvjwxd12|Signed]] (`folder`, id `1M8LVV7NYTyc3PKzCPpk2OlBLYVJwXd12`) — op `?` — node "Save signed PDF" (id `830873e9-6db6-4c46-b0aa-0bc167fdf9ac`)
- [[../resources/google-drive/1u9mgwcdwzxtfvm73-qxxuv7dcpep3s1c|Unsigned]] (`folder`, id `1U9MGwcdwZXTfVm73-qxXuv7DcPep3S1c`) — op `?` — node "Upload file" (id `853893d3-311f-4d58-98eb-29b3d827c595`)
- *(dynamic)* — op `download` — node "Download file" (id `c6d05758-84eb-415a-9715-a67fd0200d06`)
- *(dynamic)* — op `download` — node "Download file5" (id `c8dbb3c9-2c83-4c15-ba2b-95454757f714`)
- [[../resources/google-drive/1m8lvv7nytyc3pkzcppk2olblyvjwxd12|Signed]] (`folder`, id `1M8LVV7NYTyc3PKzCPpk2OlBLYVJwXd12`) — op `?` — node "Save audit log" (id `d5a8c2a3-a7ce-4cbb-9761-d43473bef8b9`)
- *(dynamic)* — op `download` — node "Download file4" (id `ddc7a3e6-92bc-4d3b-b748-b14a79f0fc70`)
- [[../resources/google-drive/1dzfcvjdodte8rczqfb0xbp28ijkefbav|ACH_Electronic_Check_Service_Enrollment_Form_Indirect_JULY_2025_3.pdf]] (`file`, id `1dZFCVJDodTe8rCZqFB0XbP28iJKEfbaV`) — op `download` — node "Download a draft form" (id `f587cccd-5e7c-4da0-bac5-d5df70e89e78`)

### Slack channels

- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Error - Error downloading signed document3" (id `242cd76c-edd0-4cea-a5e4-c1b26fd05747`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Items sent for singing5" (id `2c8ee33f-cfd1-4426-989c-48f8425104c0`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Items sent for singing6" (id `375acf03-fe0a-4fb1-91c0-f8bb4bbac8b9`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Items sent for singing1" (id `4161af22-5338-4814-ad6d-529384cc87fc`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Items sent for singing" (id `4ec6271a-c120-4daf-aee4-2fecdaa6fb4c`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Items sent for singing4" (id `627c048e-e363-455f-bb5c-70b72124d5f3`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report the merchant did not respond to signature request2" (id `8f9b9d04-9cc2-47e0-96cf-fda30acc7ce8`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report problem retrieving data for merchants" (id `9656efd9-448c-4cea-a33c-fb5641829d51`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report the merchant did not respond to signature request1" (id `afe5f6bb-0d83-4328-b4f9-4abc1fbf44c6`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report error happened when checking for signature" (id `c0659938-1b55-4a50-ac95-f80ee1cc8548`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report docs are waiting for approval" (id `c0ef805c-f0af-47af-839e-dddde18b68dc`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Error - Error downloading signed document4" (id `c7694fa8-cfa8-4689-818e-f2ec98b83874`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report Error - Error downloading signed document" (id `d4184944-e7ba-41ff-8b98-94cd3a7d4264`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report docs are waiting for approval1" (id `db983987-ca8c-49de-8660-8243679f2f55`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report error happened when checking for signature1" (id `fe0f1477-2df3-469f-a3ca-e406d89e2894`)
- [[../resources/slack-channels/c09e2246xt8|elavon-ach-enrollment]] (id `C09E2246XT8`) — op `channel` — node "Report signed documents received" (id `fe116248-ae5c-47ef-a08f-f4cd7c8b669c`)

### Sub-workflows (Execute Workflow calls)

- [[elavon-ach-exemption-form-generator|Elavon ACH Exemption Form Generator]] (n8n_id `c4rexPHrWGfGDBUP`) — node "Execute Workflow1" (id `40919da8-cbc9-4653-9743-9aa1e218bb45`)
- [[send-email-simple-text|Send Email: Simple Text]] (n8n_id `Zr3vF0LVpsPrzHVY`) — node "Call 'Send Email: Simple Text'" (id `442e49e4-e51f-49b0-a732-913812f0e92c`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `797c42aa-6a1e-489a-ba59-d46a3e27b8e8`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Create Base Messages (approved forms)" (id `ac6f692e-a122-49e4-b352-8553d99fd34c`)
- [[send-email-simple-text|Send Email: Simple Text]] (n8n_id `Zr3vF0LVpsPrzHVY`) — node "Call 'Send Email: Simple Text'1" (id `f6b8f1dc-fb9b-44ef-95a1-ca3ff4599046`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
