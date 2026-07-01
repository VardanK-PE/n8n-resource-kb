---
n8n_id: "6mD2UQ8ZxX7y6iQP"
name: "PCI SAQ Webapp"
status: active
last_modified: 2026-03-11T19:54:59.861Z
tags: []
fingerprint: "880548cc17f7238698a9a7ea58e3b0eaf17a203fded0cf99d1df77441dc294d9"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PCI SAQ Webapp

## Summary

- **Status:** active
- **n8n ID:** `6mD2UQ8ZxX7y6iQP`
- **Nodes:** 89
- **Last modified:** 2026-03-11T19:54:59.861Z

## Triggers

- **webhook** — node "Webhook" (id `02ac9acf-f5d7-404e-b1c1-a10c1c915594`) — ["POST","GET","DELETE"] `791f7121-50cd-4d32-a530-97f4d82804e1`
- **error** — node "Error Trigger" (id `1a66bd32-82a2-4b16-9705-07fdb3bd1761`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `0767dca1-df82-4264-bc4e-5f87e2ffc520`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message8" (id `180b242f-80c5-4400-86a4-c668f28e242a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download a draft form" (id `31907fb2-f072-4e5a-9001-780ad86fd86c`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "JWT" (id `37bbfd67-6c77-4f73-9c35-e2bb172e354c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet1" (id `3a451c05-6d71-4e87-a9d9-580874c3b5ef`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file" (id `3e42a070-f11f-4119-af5a-93a1c990ba1a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `41877c1f-775f-4758-9086-f4a0b6c43248`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Success Key Request" (id `4dbdaea9-e798-42ff-8eda-0ffb2e693d41`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report the merchant did not respond to signature request1" (id `5844859a-c439-450e-a4ed-8bab5a1a337e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `5b50169e-c4e4-44cb-9b94-dabe54b7a041`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send a message" (id `5e20c763-ad6a-413e-9cde-4721d4edfcc8`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Execute a SQL query" (id `63324d96-333b-4136-9591-970d4bbf74bc`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Execute a SQL query2" (id `6556fb45-b326-42e4-adbe-0b1d410f6529`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Retrieve prefilled values" (id `718a8bac-4617-4134-947a-037861da20c9`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message9" (id `75aae8cf-a449-41ca-9e8b-4d9a04b591ed`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request10" (id `837b0364-91ee-4954-9be0-df6557928ba0`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "JWT1" (id `989168e3-2f9e-4ddd-95a1-d2433b92c4c9`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `a410307d-0ec6-46f6-a4d6-defc4f2dcd48`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant Detail" (id `ac927bb0-f8c4-4fd1-bbd4-e664d1cb5f3a`)
- [[../resources/credentials/qrznqthnoxn5a2vt|Docuseal Auth]] (`httpHeaderAuth`, id `QrznQthNoxN5a2vt`) — node "HTTP Request2" (id `b6e70ba1-02aa-4698-ac12-88a0b166573f`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Execute a SQL query1" (id `bded4661-8e82-4101-b3d5-c51c34348e45`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Invalid Key Request" (id `c3bc9632-2ea5-450b-b58c-92576e029c86`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Retrieve prefilled values2" (id `e1ffe007-a346-4e29-b1f5-d00b10fefb76`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Respond to Webhook3" (id `e258d385-a684-4798-8e0d-c72fb61eb7b6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "PCI SAQ Detail" (id `e52b8a74-9a01-4fab-a9b9-6bea08c47631`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Report the merchant did not respond to signature request2" (id `f75aebae-2262-4fad-93f2-c70d57f01e64`)
- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Decode JWT" (id `fc937e41-567d-4303-9f0a-592e00c45018`)

### HTTP URLs

- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions/pdf` — node "HTTP Request10" (id `837b0364-91ee-4954-9be0-df6557928ba0`)
- [[../resources/http-urls/api-docuseal-com|api.docuseal.com]] — `POST https://api.docuseal.com/submissions/pdf` — node "HTTP Request2" (id `b6e70ba1-02aa-4698-ac12-88a0b166573f`)

### Databases

- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Execute a SQL query" (id `63324d96-333b-4136-9591-970d4bbf74bc`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Execute a SQL query2" (id `6556fb45-b326-42e4-adbe-0b1d410f6529`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant Detail" (id `ac927bb0-f8c4-4fd1-bbd4-e664d1cb5f3a`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Execute a SQL query1" (id `bded4661-8e82-4101-b3d5-c51c34348e45`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update row in sheet1" (id `3a451c05-6d71-4e87-a9d9-580874c3b5ef`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update row in sheet" (id `5b50169e-c4e4-44cb-9b94-dabe54b7a041`)
- [[../resources/google-sheets/1nflgutfryodvz8gc7ihshxoeywuaoxe4a29goxqmr2w|PCI Form Fields]] (id `1NFlgutFRYOdvz8Gc7IhsHxOeYWUaoXe4a29goxqMR2w`) — op `?`, tab `PCI 4.0.1 R1 Form Fields` — node "Retrieve prefilled values" (id `718a8bac-4617-4134-947a-037861da20c9`)
- [[../resources/google-sheets/1nflgutfryodvz8gc7ihshxoeywuaoxe4a29goxqmr2w|PCI Form Fields]] (id `1NFlgutFRYOdvz8Gc7IhsHxOeYWUaoXe4a29goxqMR2w`) — op `?`, tab `PCI 4.0.1 R1 Form Fields` — node "Retrieve prefilled values2" (id `e1ffe007-a346-4e29-b1f5-d00b10fefb76`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "PCI SAQ Detail" (id `e52b8a74-9a01-4fab-a9b9-6bea08c47631`)

### Google Drive

- [[../resources/google-drive/1nmjzu7qayimyjwsdzklxibic1wmc5n5f|PCI-DSS-v4_0_1-SAQ-A-r1_16.pascal.v6.pdf]] (`file`, id `1nMjZu7qayIMyjWsdzKLxiBiC1WMC5n5F`) — op `download` — node "Download a draft form" (id `31907fb2-f072-4e5a-9001-780ad86fd86c`)
- [[../resources/google-drive/14usfjge7mhj-bz-rhqqnoecz2siuppyu|PCI Forms - Unsigned]] (`folder`, id `14usFjGe7mHj_Bz-rhQqnOECz2SiuPpyU`) — op `?` — node "Upload file" (id `3e42a070-f11f-4119-af5a-93a1c990ba1a`)
- *(dynamic)* — op `download` — node "Download file" (id `41877c1f-775f-4758-9086-f4a0b6c43248`)

### Data tables (n8n)

- [[../resources/data-tables/ap2swoa41lboeuma|PciSaqMerchantSaqSubmissions]] (id `AP2SwoA41lboeUma`) — op `upsert` — node "Upsert merchant-saq" (id `0143d8c0-dfd4-4694-95d0-1f659c1daf98`)
- [[../resources/data-tables/vh7zlzysfokqdtnc|PciSaqLogins]] (id `vh7zLzySfoKQDtnc`) — op `update` — node "Update row(s)" (id `070079aa-ef70-4528-96c3-ee055ae804fb`)
- [[../resources/data-tables/ap2swoa41lboeuma|PciSaqMerchantSaqSubmissions]] (id `AP2SwoA41lboeUma`) — op `get` — node "Get merchant-saq1" (id `1659d334-a01f-43eb-9606-89d238d2deac`)
- [[../resources/data-tables/ap2swoa41lboeuma|PciSaqMerchantSaqSubmissions]] (id `AP2SwoA41lboeUma`) — op `update` — node "Archive Merchant SAQ" (id `170b3221-b666-4ee5-84dd-3c7c08c459fe`)
- [[../resources/data-tables/vh7zlzysfokqdtnc|PciSaqLogins]] (id `vh7zLzySfoKQDtnc`) — op `rowExists` — node "If row exists" (id `452bdf71-7a39-45cc-9a0b-b18faa6ebfdb`)
- [[../resources/data-tables/ap2swoa41lboeuma|PciSaqMerchantSaqSubmissions]] (id `AP2SwoA41lboeUma`) — op `get` — node "Get merchant-saq" (id `51275d06-3924-4672-96c9-3be6cc6c8eeb`)
- [[../resources/data-tables/vh7zlzysfokqdtnc|PciSaqLogins]] (id `vh7zLzySfoKQDtnc`) — op `?` — node "Create Code" (id `5c525b33-57d1-45d7-8e21-09bc374bcc98`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Send a message4" (id `0767dca1-df82-4264-bc4e-5f87e2ffc520`)
- [[../resources/slack-channels/c09mqbcgm0a|pci-saq-scribe-webapp]] (id `C09MQBCGM0A`) — op `channel` — node "Send a message8" (id `180b242f-80c5-4400-86a4-c668f28e242a`)
- [[../resources/slack-channels/c09mqbcgm0a|pci-saq-scribe-webapp]] (id `C09MQBCGM0A`) — op `channel` — node "Success Key Request" (id `4dbdaea9-e798-42ff-8eda-0ffb2e693d41`)
- [[../resources/slack-channels/c09mqbcgm0a|pci-saq-scribe-webapp]] (id `C09MQBCGM0A`) — op `channel` — node "Report the merchant did not respond to signature request1" (id `5844859a-c439-450e-a4ed-8bab5a1a337e`)
- [[../resources/slack-channels/c09mqbcgm0a|pci-saq-scribe-webapp]] (id `C09MQBCGM0A`) — op `channel` — node "Send a message9" (id `75aae8cf-a449-41ca-9e8b-4d9a04b591ed`)
- [[../resources/slack-channels/c09mqbcgm0a|pci-saq-scribe-webapp]] (id `C09MQBCGM0A`) — op `channel` — node "Send a message6" (id `a410307d-0ec6-46f6-a4d6-defc4f2dcd48`)
- [[../resources/slack-channels/c09mqbcgm0a|pci-saq-scribe-webapp]] (id `C09MQBCGM0A`) — op `channel` — node "Invalid Key Request" (id `c3bc9632-2ea5-450b-b58c-92576e029c86`)
- [[../resources/slack-channels/c09mqbcgm0a|pci-saq-scribe-webapp]] (id `C09MQBCGM0A`) — op `channel` — node "Report the merchant did not respond to signature request2" (id `f75aebae-2262-4fad-93f2-c70d57f01e64`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
