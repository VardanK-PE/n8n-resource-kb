---
n8n_id: "LdXwJbJlLzW635Qq"
instance: v1
name: "PCI Monitoring"
status: active
last_modified: 2026-06-26T17:58:21.739Z
tags: []
fingerprint: "6eee9428c1b1a43ba89af7075479f7e297906ea02ef8219851efd588e62fcfce"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PCI Monitoring

## Summary

- **Status:** active
- **n8n ID:** `LdXwJbJlLzW635Qq`
- **Nodes:** 88
- **Last modified:** 2026-06-26T17:58:21.739Z

## Triggers

- **schedule** — node "Schedule Trigger: Daily check PCI SAQ Status" (id `4584584e-c965-49e9-8841-e7b091b06d20`) — `daily at 10:00`
- **schedule** — node "Schedule Trigger: Hourly check PCI SAQ Status" (id `9de085b8-1787-4a0a-9fe7-1280853b6491`) — `every 1 hour(s) at :30`
- **schedule** — node "Schedule Trigger: Generate partner reports" (id `d29d5654-98f5-487a-ba8d-632e6825bf8b`) — `daily at 4:00`
- **manual** — node "When clicking ‘Execute workflow’" (id `d2a1cbd5-8a46-4534-b2d7-9ba62bcb527e`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "partners" (id `119db46f-4e04-440d-9ad1-4d18912520fa`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `18bee46a-cce3-4f09-9f50-dbc2094b82d1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet1" (id `1b55509b-a8b8-4386-9310-26f24d36a087`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Download Signed File1" (id `36f41e15-5c5a-4172-90ab-3c66e19a1e3e`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Download Signed File1" (id `36f41e15-5c5a-4172-90ab-3c66e19a1e3e`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query3" (id `3c55c356-7e5e-4dbb-b3b5-4c1ef2fa7e21`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Clear sheet" (id `498cc049-6d07-4922-8c36-5ed51b77cf40`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `498f88fe-d383-486f-85dc-d20196b71e92`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet2" (id `517a55ac-f93a-4d31-b4fd-75a5f44915fc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update PCI SAQ Signed Date" (id `58059a7e-9090-4efe-ba9e-1fed386ddcd9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet5" (id `58978abc-e16b-493f-8404-5670688a04a1`)
- [[../resources/credentials/zdgu54lbylgkgro9|VAPI Bearer Auth]] (`httpBearerAuth`, id `Zdgu54LbylGKGRO9`) — node "Download Signed File" (id `5b641278-1a48-4dcd-8791-3de8db24c4bb`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Download Signed File" (id `5b641278-1a48-4dcd-8791-3de8db24c4bb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "partners1" (id `67e8b2c0-b9e5-4746-b7b7-29329c94a1d6`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query4" (id `6fbec902-da84-4b99-b439-46c3fd610d7d`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send a message" (id `75dbe12c-4056-424f-8cf3-40ad9d7ad8ea`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet4" (id `99eff530-e019-4932-981b-5e50ab8d643a`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query5" (id `a37c0b0f-cf5e-4104-b01c-074000ef7cc8`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Get Submission Status3" (id `a439b6d3-826e-46d9-a0c8-9bd3930df71f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `a914da14-0ac0-470d-959c-3a0ab3c116dd`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Get Submission Status2" (id `ac16f2bb-b23c-4dad-a4be-34f0dcc985d4`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message2" (id `ac4eacd9-e880-4e50-a8d4-2d2df4c561c4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Active Merchants4" (id `b09cbeb1-c846-4578-bc17-162bf469fda1`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send a message1" (id `b850441a-bf8d-46d6-bf65-70f1a875310c`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Delete a message" (id `b9a77479-c0f1-47f7-acb6-37e555257b85`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "Get Submission Status" (id `bfdd5bb6-c483-4dff-b7d5-af06cf913429`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `faeb035b-0705-4afb-8c12-304e01b6a88c`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ $json.documents[0].url }}` — node "Download Signed File1" (id `36f41e15-5c5a-4172-90ab-3c66e19a1e3e`)
- *(dynamic URL)* — `GET {{ $json.document_url }}` — node "Download Signed File" (id `5b641278-1a48-4dcd-8791-3de8db24c4bb`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submissions/5253077` — node "Get Submission Status3" (id `a439b6d3-826e-46d9-a0c8-9bd3930df71f`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submissions/{{ $json['Submission ID'] }}` — node "Get Submission Status2" (id `ac16f2bb-b23c-4dad-a4be-34f0dcc985d4`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `GET https://api.docuseal.com/submissions/{{ $json['Submission ID'] }}` — node "Get Submission Status" (id `bfdd5bb6-c483-4dff-b7d5-af06cf913429`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query3" (id `3c55c356-7e5e-4dbb-b3b5-4c1ef2fa7e21`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query4" (id `6fbec902-da84-4b99-b439-46c3fd610d7d`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query5" (id `a37c0b0f-cf5e-4104-b01c-074000ef7cc8`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partner_alerts_pci` — node "partners" (id `119db46f-4e04-440d-9ad1-4d18912520fa`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get row(s) in sheet" (id `18bee46a-cce3-4f09-9f50-dbc2094b82d1`)
- *(dynamic spreadsheet)* — op `appendOrUpdate`, tab `={{ $('Partner Mids').first().json.partner_reports_gsheet_sheeet_id }}` — node "Append or update row in sheet1" (id `1b55509b-a8b8-4386-9310-26f24d36a087`)
- *(dynamic spreadsheet)* — op `clear`, tab `={{ $('Partner Mids').first().json.partner_reports_gsheet_sheeet_id }}` — node "Clear sheet" (id `498cc049-6d07-4922-8c36-5ed51b77cf40`)
- [[../resources/google-sheets/14ovfq9vwfvvlwtigzwoi9amplwudiqguyg7r4g1k9ho|PE LocalExpress Reports (shared)]] (id `14OVfQ9VWFVVlWTIGzwoI9aMPLwuDIqGUyg7R4g1K9Ho`) — op `?`, tab `Merchant PCI SAQ Status` — node "Get row(s) in sheet2" (id `517a55ac-f93a-4d31-b4fd-75a5f44915fc`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update PCI SAQ Signed Date" (id `58059a7e-9090-4efe-ba9e-1fed386ddcd9`)
- [[../resources/google-sheets/14ovfq9vwfvvlwtigzwoi9amplwudiqguyg7r4g1k9ho|PE LocalExpress Reports (shared)]] (id `14OVfQ9VWFVVlWTIGzwoI9aMPLwuDIqGUyg7R4g1K9Ho`) — op `update`, tab `Merchant PCI SAQ Status` — node "Update row in sheet5" (id `58978abc-e16b-493f-8404-5670688a04a1`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partner_alerts_pci` — node "partners1" (id `67e8b2c0-b9e5-4746-b7b7-29329c94a1d6`)
- [[../resources/google-sheets/1swpg9e6oppao-bvxztiuwp3swnuvz-ox0ljaqbvuues|PE Hearth Reports (shared)]] (id `1SwPG9E6OPPAO_BvXZTIuWp3SwnUvZ-OX0LJAQbvUues`) — op `update`, tab `Merchant PCI SAQ Status` — node "Update row in sheet4" (id `99eff530-e019-4932-981b-5e50ab8d643a`)
- [[../resources/google-sheets/1swpg9e6oppao-bvxztiuwp3swnuvz-ox0ljaqbvuues|PE Hearth Reports (shared)]] (id `1SwPG9E6OPPAO_BvXZTIuWp3SwnUvZ-OX0LJAQbvUues`) — op `appendOrUpdate`, tab `Merchant PCI SAQ Status` — node "Append or update row in sheet" (id `a914da14-0ac0-470d-959c-3a0ab3c116dd`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get Active Merchants4" (id `b09cbeb1-c846-4578-bc17-162bf469fda1`)
- [[../resources/google-sheets/12anwcwda3lehvie6u9qxu2lr-vzsk1hq3bbbgngotyy|PE Supermove Reports (shared)]] (id `12anWCwdA3lEHVIe6u9qxu2lr_vZsK1hQ3BBBGNgOTyY`) — op `?`, tab `Sheet1` — node "Get row(s) in sheet1" (id `faeb035b-0705-4afb-8c12-304e01b6a88c`)

### Slack channels

- [[../resources/slack-channels/c09pc6hkhpy|payengine-ai-alerts]] (id `C09PC6HKHPY`) — op `channel` — node "Send a message5" (id `498f88fe-d383-486f-85dc-d20196b71e92`)
- *(dynamic channel)* — op `channel` — node "Send a message" (id `75dbe12c-4056-424f-8cf3-40ad9d7ad8ea`)
- *(dynamic channel)* — op `channel` — node "Send a message2" (id `ac4eacd9-e880-4e50-a8d4-2d2df4c561c4`)
- [[../resources/slack-channels/c0953te3t8r|hearth-payengine-support]] (id `C0953TE3T8R`) — op `channel` — node "Send a message1" (id `b850441a-bf8d-46d6-bf65-70f1a875310c`)
- *(dynamic channel)* — op `delete` — node "Delete a message" (id `b9a77479-c0f1-47f7-acb6-37e555257b85`)

### Sub-workflows (Execute Workflow calls)

- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'" (id `07ba278c-57c1-4196-9295-b98e793ba75b`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'" (id `3c67f410-4e17-437c-ae87-a252a96461ba`)
- [[send-email-html|Send Email: HTML]] (n8n_id `H9qPciXCz00KxAyF`) — node "Call 'Send Email: HTML'" (id `4ac9adb7-1ddb-461e-8cf7-1cef81f8c292`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Call 'Slack - Create a base message'1" (id `c4600e65-5ceb-46fc-8ca0-b678d993f204`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
