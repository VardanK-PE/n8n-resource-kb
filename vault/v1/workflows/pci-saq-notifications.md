---
n8n_id: "vGETi2yfirGyOg4o"
instance: v1
name: "PCI SAQ Notifications"
status: active
last_modified: 2026-08-14T18:23:27.297Z
tags: []
fingerprint: "23a72163cfaf15aca8652123a8ab376e2206b5cca3b085b320dd8e5b22d8159a"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PCI SAQ Notifications

## Summary

- **Status:** active
- **n8n ID:** `vGETi2yfirGyOg4o`
- **Nodes:** 106
- **Last modified:** 2026-08-14T18:23:27.297Z

## Triggers

- **schedule** — node "Non-Supermove trigger1" (id `024b40fd-cbea-46d6-a2e7-7f7a6a7ffbc5`) — `every 1 month(s) on day 5`
- **schedule** — node "Supermove new merchants daily" (id `04240bf1-7155-4e62-8398-b946d078bfc8`) — `daily at 10:50`
- **schedule** — node "Non-Supermove trigger4" (id `34294ce0-65de-476b-9b63-6744559dc239`) — `every 1 month(s) on day 20`
- **schedule** — node "Non-Supermove new merchants daily" (id `3bad9b1b-18ed-4fb8-b0a6-3efea02ae3e3`) — `daily at 10:55`
- **schedule** — node "Schedule Trigger1" (id `5c75f5af-66f1-4f36-8903-0a85f88281bb`) — `every 10 minute(s)`
- **schedule** — node "Non-Supermove trigger5" (id `640ef3c5-2fbe-472c-af10-dd307c904be1`) — `every 1 month(s) on day 20`
- **schedule** — node "Non-Supermove trigger" (id `6565e7a6-a532-4896-91ba-667bc673f1df`) — `every 1 month(s) on day 5`
- **schedule** — node "Non-Supermove trigger7" (id `75fa542e-3140-4d9d-a9d3-0d827f5c7fec`) — `every 1 month(s) on day 20`
- **error** — node "Error Trigger" (id `7fa95bd6-5a6a-479a-a68f-ea38df193444`)
- **schedule** — node "Non-Supermove trigger2" (id `91ba8ea8-a523-4019-b344-161561ac7f00`) — `every 1 month(s) on day 5`
- **schedule** — node "Non-Supermove trigger6" (id `9347e18f-c859-41f0-84fd-598437509ab9`) — `every 1 month(s) on day 20`
- **schedule** — node "Non-Supermove trigger3" (id `d70d8ed2-7a74-49a3-805d-b714a643d6f7`) — `every 1 month(s) on day 5`
- **manual** — node "When clicking ‘Execute workflow’" (id `f02ad5de-6ef3-4574-a7a0-7fe9ea77f796`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `12eb491e-1af6-40f9-80db-9917c068687d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get PCI email resends" (id `202c0668-f1a8-4dff-97fe-c7b78eefe8b8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file2" (id `309a27af-330f-438b-9657-be727bccf2a8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Due Date" (id `45714127-7c05-4471-8fbe-514e4fbfe0f3`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get PE Merchant Details2" (id `4c41970f-b467-481a-991b-5b7e2ce9a2bf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get PCI email resends1" (id `5c4f191f-26c3-4c2e-a9e1-ff1ef665dc95`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Due Date1" (id `695e3247-1794-4237-99eb-bee899c9dff1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get All active merchants" (id `6ac89e18-ecd2-4f58-a70a-a2e57e3dd774`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file1" (id `6f9b9692-f6cc-474b-85c8-a02972ab9155`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Supermove Merchants" (id `93f2f98d-956c-41f6-a8da-850f43caa59d`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get PE Merchant Details" (id `996365fd-4d84-4fd1-897a-3a10f6ed0321`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `a82ae22c-0ebb-4ebf-afdc-c4fc58b7baec`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `a873aab8-aeb9-41b4-a8dd-6cea87f51fa7`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `ae746090-ff9c-49ce-8945-015cab71a876`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet3" (id `dd4e84ae-94da-455d-ac93-89702cf306d2`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get PE Merchant Details2" (id `4c41970f-b467-481a-991b-5b7e2ce9a2bf`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get PE Merchant Details" (id `996365fd-4d84-4fd1-897a-3a10f6ed0321`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get PCI email resends" (id `202c0668-f1a8-4dff-97fe-c7b78eefe8b8`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update Due Date" (id `45714127-7c05-4471-8fbe-514e4fbfe0f3`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get PCI email resends1" (id `5c4f191f-26c3-4c2e-a9e1-ff1ef665dc95`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update Due Date1" (id `695e3247-1794-4237-99eb-bee899c9dff1`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get All active merchants" (id `6ac89e18-ecd2-4f58-a70a-a2e57e3dd774`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get Supermove Merchants" (id `93f2f98d-956c-41f6-a8da-850f43caa59d`)
- [[../resources/google-sheets/1tzj6c2myzcgheeedev2jmtxenkb4oqpy6vfobfudqye|PCI non compliant merchants report]] (id `1TZJ6C2mYZCgHEEEDEv2jmtxENKB4OQpy6VFoBfudqyE`) — op `append`, tab `SM` — node "Append row in sheet" (id `a873aab8-aeb9-41b4-a8dd-6cea87f51fa7`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update row in sheet3" (id `dd4e84ae-94da-455d-ac93-89702cf306d2`)

### Google Drive

- [[../resources/google-drive/1h57cwff-z9t6ptw-gf5xkuv-wx2qf7jj|PCI SAQ Sign Document.jpg]] (`file`, id `1h57cwFF_z9T6pTw-gF5XKUV_Wx2Qf7Jj`) — op `download` — node "Download file2" (id `309a27af-330f-438b-9657-be727bccf2a8`)
- [[../resources/google-drive/1h57cwff-z9t6ptw-gf5xkuv-wx2qf7jj|PCI SAQ Sign Document.jpg]] (`file`, id `1h57cwFF_z9T6pTw-gF5XKUV_Wx2Qf7Jj`) — op `download` — node "Download file1" (id `6f9b9692-f6cc-474b-85c8-a02972ab9155`)
- [[../resources/google-drive/1h57cwff-z9t6ptw-gf5xkuv-wx2qf7jj|PCI SAQ Sign Document.jpg]] (`file`, id `1h57cwFF_z9T6pTw-gF5XKUV_Wx2Qf7Jj`) — op `download` — node "Download file" (id `a82ae22c-0ebb-4ebf-afdc-c4fc58b7baec`)

### Slack channels

- [[../resources/slack-channels/c09mqbcgm0a|pci-saq-scribe-webapp]] (id `C09MQBCGM0A`) — op `channel` — node "Send a message6" (id `12eb491e-1af6-40f9-80db-9917c068687d`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `ae746090-ff9c-49ce-8945-015cab71a876`)

### Sub-workflows (Execute Workflow calls)

- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Report failed PCI SAQ notification" (id `92e8c1eb-db0d-403d-b5a1-87c65fbeb3b7`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Create error base" (id `ab55cbe7-dcf6-4676-b863-9e9f5fed573e`)
- [[send-email-simple-text|Send Email: Simple Text]] (n8n_id `Zr3vF0LVpsPrzHVY`) — node "Send PCI SAQ email" (id `ccf6b1f2-3084-44c3-bf3c-9ee1dbff3632`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Create a base message" (id `fadc41a0-abbf-413c-9989-ee81b271da4a`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
