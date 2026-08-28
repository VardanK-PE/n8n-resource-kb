---
n8n_id: "J24a0qIXslRvAe5m"
name: "Monthly ACH Reports"
status: active
last_modified: 2026-08-04T16:59:14.276Z
tags: []
fingerprint: "7796fd65b2b149cd1184f4ff03488352497c1a81a5a62bfa42e45ec69c326344"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Monthly ACH Reports

## Summary

- **Status:** active
- **n8n ID:** `J24a0qIXslRvAe5m`
- **Nodes:** 195
- **Last modified:** 2026-08-04T16:59:14.276Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `0c6e16ae-cc5b-442f-be77-f2c30d7f6ce4`)
- **schedule** — node "Schedule Trigger" (id `0dc0315b-2e1f-49bc-9480-2ceecc131ce8`) — `every 1 hour(s)`
- **execute-workflow** — node "When Executed by Another Workflow" (id `e323231f-aa70-4dc3-bd76-62b539c9b653`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `083a8209-bcdc-412a-8edc-118fcbcdc951`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Transaction Details1" (id `10f93267-286c-4070-9d2d-934de30650b4`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Send a message1" (id `1417d5aa-1b85-4eb9-8fa9-2de05421984a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet3" (id `16a474bd-02be-4a2e-bb8f-93630d79bbeb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `19d9f385-72d5-4b4a-9877-9ee5b4f5ba47`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `1efbcb93-222c-4a2e-aa0e-72fc66363f6d`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Delete an invoice" (id `22eb2764-ba52-42b1-8daa-08e3c85a720d`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `23c11ace-bd16-4bf5-81db-7bc5f2c15603`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres5" (id `2baef4e6-b3cb-40d1-902b-d6763ed11879`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `2c79ba76-58fa-4e7f-90d1-876bed1eb648`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet5" (id `2e780a86-6215-414a-994b-25201479e733`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets6" (id `2f2d6035-1434-4a51-bf28-384f38783e4f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Parsed Fee Schedules" (id `3e244988-f7a2-4bdf-bb08-6a0777ec56d7`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account (n8n api key)]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `4056ffcb-7978-42ec-867e-83bc09d7728b`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `42f4789c-7f0d-4ae7-a190-685342f8ac30`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail1" (id `42f58172-8cbd-4a09-9aad-39cbc7b319ad`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `452cbe75-97b4-4038-bc98-1889196ced18`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get a message" (id `46b4566d-0031-4c5f-8910-63a59c8ff844`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet2" (id `4d7f05a4-ad9a-4428-9c4f-77e8862f8cb8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file" (id `504f4a83-0dc9-4b2f-be7b-70974ffbbdb9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append to All Transactions" (id `597e6d97-33cc-4a36-bebe-bacd31d0ce16`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update fee schedule table" (id `5bf59762-943d-4909-9332-9ccada8efab5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create Start-Date ALL Sheet" (id `5ea9bb3c-15c8-4a1e-93a6-01d77c5d217f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Partner Residuals Terms" (id `5feb8e31-cd27-46bb-ad49-9e6e85695074`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `669fce6a-2c8a-4f33-91e7-8c8881e3d870`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "GetFundingsFromForte" (id `681ca8a6-53db-4eb5-94ec-3e370d84acc4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Created Customer" (id `6d7797bc-2793-41f5-9b1f-4a495a47b95c`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "DB Fee Schedules1" (id `6daab464-d5c7-4e48-9c41-204f65c6dd8a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Merchant Transactions" (id `7193b05c-c478-4753-8524-b64cad6b77a9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `71e74552-063f-43aa-922d-f24b8e1dccd6`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "GetFundingTransactionsFromForte" (id `73096e07-70b0-454a-98d1-d672a4343ece`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Created Invoice" (id `744375ca-85ff-4a6d-9dfb-79cbdc4997e6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets8" (id `7ee92533-d06a-4e30-bb7e-3b539734a9b3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append to Aggregate Data" (id `829996ca-d9c4-4019-bff4-b291519bb21f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet1" (id `8783ff70-91b1-4f15-8b10-63b76271a12a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet4" (id `8c1b04e6-837c-43ee-81db-5ac402d6d3aa`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "QuickBooks Online" (id `8de75d52-3ba3-42c7-9456-1e9f529c38d4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Created Customer1" (id `913bfac5-1d60-4069-8200-c69f5f2f877c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create Start-Date ALL-AGGREGATE Sheet" (id `92b832ae-1380-48da-aa3a-d357e78b4ef4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Bank Account Fields" (id `9a1c2530-e51e-4f5c-ae2a-b2fd8a155acc`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Get many invoices2" (id `9b143e7f-5ad9-445a-805c-4ee06910aec0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets10" (id `9f369faf-bc24-4838-967b-acf2751e1283`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `a8e0c9ec-d3c7-4087-91da-6f3b689a9b08`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get ACH Transactions1" (id `a90c751e-ff93-42e7-a06b-122d5529cb69`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Search files and folders" (id `ab84186d-c095-4569-b8c6-debec916cc70`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres3" (id `ae0f9ac6-77d4-40fa-a8f4-0363a664dcc2`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant Details" (id `af2a9a61-1de1-4920-9e5f-2073fba1495f`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Create QB Invoice" (id `ba39b763-14ae-4cad-84fd-9b08ef6f6d5a`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "DB Fee Schedules" (id `ba8d2784-e4d6-461d-8f57-77e83af9983e`)
- [[../resources/credentials/reyaj1uaergdkbhn|Hearth Gmail Account]] (`gmailOAuth2`, id `ReYAj1UAergdKBHN`) — node "Gmail" (id `bdb0851a-574f-4990-9b9a-50e66e6647e8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Tokens Logs" (id `be22ab14-2791-417a-be30-b34cc559f065`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get ACH Transactions" (id `ca99d96c-391b-4f50-8144-4fe08cdd8778`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `caf790b2-3f15-45a1-bff9-e157087eba7d`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "GetOrganizationDetails1" (id `cdb856f5-12a4-4498-a9e0-e50ef535fabb`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant Details1" (id `d10db473-2284-46aa-a7a3-0103bd4734bc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Fee Schedules" (id `d16181b9-ce7a-46c2-976d-afc35d2c0bdc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update Transaction Details" (id `d5e0c0cc-398f-45b8-995f-b984dffeed03`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet2" (id `d60cd683-4732-464f-9a8c-c169e04b20aa`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Create Customer1" (id `db143d0b-1451-4e08-a94b-20884b1670ff`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "GetOrganizationDetails" (id `de92493d-7c46-4c7a-8bc4-27c44af94a6d`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Create Customer2" (id `e0d3826d-d016-4d04-a32f-ff503d5e8260`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Get many invoices3" (id `e40fe037-6287-4b29-8807-7232237792c8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create folder" (id `e81b46fe-e842-4d23-a262-a065010151d4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update fee schedule table1" (id `eb3fd5f8-6738-416d-8cd1-1f417ca21959`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "FindCustomer1" (id `ed0ba244-c94f-4d15-90c5-6e182465cc40`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get DB Merchant Details" (id `edb0a383-1139-46a5-8fe1-830efbf07ecf`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `eede0d28-edd5-4b10-ac55-e707b0d21456`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres4" (id `f29b33be-972f-4d34-9f12-0cef20f0d539`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "FindCustomer" (id `f2db1a41-01f4-4c1c-8603-e0327e1e2fc7`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Get many invoices1" (id `f6a978a6-22fd-4050-b5fc-5b884233d5bf`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Get many invoices" (id `f79ae4ef-dc65-429a-b4f4-d38153e30765`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `fed6c61c-cbf7-4b0b-bb99-6f15e243535d`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/payment/ach` — node "Perform the Charge" (id `15d8a51a-bede-4ee2-a406-7e23295b1476`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/org_444639/locations/loc_325348/fundings` — node "GetFundingsFromForte" (id `681ca8a6-53db-4eb5-94ec-3e370d84acc4`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/org_444639/locations/loc_325348/fundings/{{ $json.funding_id }}/transactions` — node "GetFundingTransactionsFromForte" (id `73096e07-70b0-454a-98d1-d672a4343ece`)
- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/bank-accounts` — node "Create Bank Account Token - US" (id `7437f078-5514-438a-bf09-c087ec8d718b`)
- [[../resources/http-urls/pf-prod-ecs-task-container-gotenberg-3000|pf-prod-ecs-task-container-gotenberg:3000]] — `POST http://pf-prod-ecs-task-container-gotenberg:3000/forms/chromium/convert/html` — node "Convert To PDF [GOTENBERG]" (id `8c47f30f-768c-4570-b566-2dc23ddfefcb`)
- [[../resources/http-urls/quickbooks-api-intuit-com|quickbooks.api.intuit.com]] — `POST https://quickbooks.api.intuit.com/v3/company/9341452828840730/invoice?minorversion=75` — node "Create QB Invoice" (id `ba39b763-14ae-4cad-84fd-9b08ef6f6d5a`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/{{ $json.processor_merchant_id }}` — node "GetOrganizationDetails1" (id `cdb856f5-12a4-4498-a9e0-e50ef535fabb`)
- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/bank-accounts` — node "Create Bank Account Token - CA" (id `d9e75194-cd11-491e-93db-3163aacbcd96`)
- [[../resources/http-urls/quickbooks-api-intuit-com|quickbooks.api.intuit.com]] — `POST https://quickbooks.api.intuit.com/v3/company/9341452828840730/customer?minorversion=75` — node "Create Customer1" (id `db143d0b-1451-4e08-a94b-20884b1670ff`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/{{ $('Loop Over Items').item.json.processor_merchant_id }}/transactions` — node "GetOrganizationDetails" (id `de92493d-7c46-4c7a-8bc4-27c44af94a6d`)
- [[../resources/http-urls/quickbooks-api-intuit-com|quickbooks.api.intuit.com]] — `POST https://quickbooks.api.intuit.com/v3/company/9341452828840730/customer?minorversion=75` — node "Create Customer2" (id `e0d3826d-d016-4d04-a32f-ff503d5e8260`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `23c11ace-bd16-4bf5-81db-7bc5f2c15603`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres5" (id `2baef4e6-b3cb-40d1-902b-d6763ed11879`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `42f4789c-7f0d-4ae7-a190-685342f8ac30`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `452cbe75-97b4-4038-bc98-1889196ced18`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "DB Fee Schedules1" (id `6daab464-d5c7-4e48-9c41-204f65c6dd8a`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get ACH Transactions1" (id `a90c751e-ff93-42e7-a06b-122d5529cb69`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres3" (id `ae0f9ac6-77d4-40fa-a8f4-0363a664dcc2`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant Details" (id `af2a9a61-1de1-4920-9e5f-2073fba1495f`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "DB Fee Schedules" (id `ba8d2784-e4d6-461d-8f57-77e83af9983e`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get ACH Transactions" (id `ca99d96c-391b-4f50-8144-4fe08cdd8778`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Merchant Details1" (id `d10db473-2284-46aa-a7a3-0103bd4734bc`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get DB Merchant Details" (id `edb0a383-1139-46a5-8fe1-830efbf07ecf`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres4" (id `f29b33be-972f-4d34-9f12-0cef20f0d539`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model1" (id `2c79ba76-58fa-4e7f-90d1-876bed1eb648`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-6|anthropic / claude-sonnet-4-6]] — node "Anthropic Chat Model" (id `4056ffcb-7978-42ec-867e-83bc09d7728b`)

### Google Sheets

- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $json['month'] }}-ALL-AGGREGATE` — node "Get row(s) in sheet1" (id `083a8209-bcdc-412a-8edc-118fcbcdc951`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `update`, tab `={{ $('When clicking ‘Execute workflow’').item.json['start-date'] }}-ALL-AGGREGATE` — node "Update Transaction Details1" (id `10f93267-286c-4070-9d2d-934de30650b4`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `2025-09-ALL-AGGREGATE` — node "Get row(s) in sheet3" (id `16a474bd-02be-4a2e-bb8f-93630d79bbeb`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `update`, tab `={{ $('Entry 4').first().json.month }}-ALL-AGGREGATE` — node "Google Sheets4" (id `19d9f385-72d5-4b4a-9877-9ee5b4f5ba47`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `create`, tab `null` — node "Google Sheets" (id `1efbcb93-222c-4a2e-aa0e-72fc66363f6d`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `2025-07-ALL-AGGREGATE` — node "Get row(s) in sheet5" (id `2e780a86-6215-414a-994b-25201479e733`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `QB LOGS - INVOICES` — node "Google Sheets6" (id `2f2d6035-1434-4a51-bf28-384f38783e4f`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `FEE_SCHEDULES` — node "Parsed Fee Schedules" (id `3e244988-f7a2-4bdf-bb08-6a0777ec56d7`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `append`, tab `ach_backbill_email_notices` — node "Append row in sheet2" (id `4d7f05a4-ad9a-4428-9c4f-77e8862f8cb8`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `={{ $('InputFields').item.json["start-date"] }}-ALL` — node "Append to All Transactions" (id `597e6d97-33cc-4a36-bebe-bacd31d0ce16`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `appendOrUpdate`, tab `FEE_SCHEDULES` — node "Append or update fee schedule table" (id `5bf59762-943d-4909-9332-9ccada8efab5`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `create`, tab `null` — node "Create Start-Date ALL Sheet" (id `5ea9bb3c-15c8-4a1e-93a6-01d77c5d217f`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "Partner Residuals Terms" (id `5feb8e31-cd27-46bb-ad49-9e6e85695074`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `={{ $('InputFields').item.json["start-date"] }}-FORTE` — node "Google Sheets1" (id `669fce6a-2c8a-4f33-91e7-8c8881e3d870`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `QB LOGS - CUSTOMERS CREATED` — node "Log Created Customer" (id `6d7797bc-2793-41f5-9b1f-4a495a47b95c`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $('Entry').item.json.month }}-ALL` — node "Get Merchant Transactions" (id `7193b05c-c478-4753-8524-b64cad6b77a9`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $json['start-date'] }}-ALL-AGGREGATE` — node "Get row(s) in sheet" (id `71e74552-063f-43aa-922d-f24b8e1dccd6`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `QB LOGS - INVOICES` — node "Log Created Invoice" (id `744375ca-85ff-4a6d-9dfb-79cbdc4997e6`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $('Entry').item.json.month }}-ALL-AGGREGATE` — node "Google Sheets8" (id `7ee92533-d06a-4e30-bb7e-3b539734a9b3`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `={{ $('InputFields').first().json["start-date"] }}-ALL-AGGREGATE` — node "Append to Aggregate Data" (id `829996ca-d9c4-4019-bff4-b291519bb21f`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `append`, tab `ach_backbill_email_notices` — node "Append row in sheet1" (id `8783ff70-91b1-4f15-8b10-63b76271a12a`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `2025-08-ALL-AGGREGATE` — node "Get row(s) in sheet4" (id `8c1b04e6-837c-43ee-81db-5ac402d6d3aa`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `QB LOGS - CUSTOMERS CREATED` — node "Log Created Customer1" (id `913bfac5-1d60-4069-8200-c69f5f2f877c`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `create`, tab `null` — node "Create Start-Date ALL-AGGREGATE Sheet" (id `92b832ae-1380-48da-aa3a-d357e78b4ef4`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `update`, tab `={{ $('When clicking ‘Execute workflow’').item.json['start-date'] }}-ALL-AGGREGATE` — node "Update Bank Account Fields" (id `9a1c2530-e51e-4f5c-ae2a-b2fd8a155acc`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `update`, tab `={{ $('Entry').first().json.month }}-ALL-AGGREGATE` — node "Google Sheets10" (id `9f369faf-bc24-4838-967b-acf2751e1283`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `BANK_ACCOUNT_TOKENS_LOG` — node "Tokens Logs" (id `be22ab14-2791-417a-be30-b34cc559f065`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `FEE_SCHEDULES` — node "Get Fee Schedules" (id `d16181b9-ce7a-46c2-976d-afc35d2c0bdc`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `update`, tab `={{ $('When clicking ‘Execute workflow’').item.json['start-date'] }}-ALL-AGGREGATE` — node "Update Transaction Details" (id `d5e0c0cc-398f-45b8-995f-b984dffeed03`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `update`, tab `={{ $('Workflow Settings').item.json.month }}-ALL-AGGREGATE` — node "Get row(s) in sheet2" (id `d60cd683-4732-464f-9a8c-c169e04b20aa`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `appendOrUpdate`, tab `FEE_SCHEDULES` — node "Append or update fee schedule table1" (id `eb3fd5f8-6738-416d-8cd1-1f417ca21959`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `PE_FORTE_TRANSACTIONS_LOG` — node "Append row in sheet" (id `eede0d28-edd5-4b10-ac55-e707b0d21456`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $json.month }}-ALL-AGGREGATE` — node "Google Sheets3" (id `fed6c61c-cbf7-4b0b-bb99-6f15e243535d`)

### Google Drive

- *(dynamic)* — op `?` — node "Upload file" (id `504f4a83-0dc9-4b2f-be7b-70974ffbbdb9`)
- *(dynamic)* — op `download` — node "Download file" (id `a8e0c9ec-d3c7-4087-91da-6f3b689a9b08`)
- [[../resources/google-drive/1gqr78vvr-bot-qjk1r4x9ub0w7g7myjb|Merchant Processing Statements]] (`folder`, id `1gQr78vvR-bot-qJk1R4X9Ub0W7g7MyJb`) — op `?` — node "Create folder" (id `e81b46fe-e842-4d23-a262-a065010151d4`)

## Used by (workflows)

- [[pe-reports-request-form|PE Reports Request Form]] — node "Execute Workflow" (id `ac9d7695-f6e7-43f0-90e6-a697c1ca0dab`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
