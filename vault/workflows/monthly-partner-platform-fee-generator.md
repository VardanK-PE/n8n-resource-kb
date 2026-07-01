---
n8n_id: "6kyZcLGdSZF0T7Lz"
name: "Monthly Partner Platform Fee Generator"
status: active
last_modified: 2026-05-27T18:36:07.634Z
tags: []
fingerprint: "fdf102ce07d3efb9629e2cfe3af702e4e7929acd99b347899f5ee748f3c7d801"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Monthly Partner Platform Fee Generator

## Summary

- **Status:** active
- **n8n ID:** `6kyZcLGdSZF0T7Lz`
- **Nodes:** 49
- **Last modified:** 2026-05-27T18:36:07.634Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `8700a11b-26b0-43d7-b5bb-0c3abbef1eb8`) — `every 1 month(s)`
- **manual** — node "When clicking ‘Execute workflow’" (id `a1936fa0-791b-471b-a276-d66278014df8`)

## Depends on

### Credentials

- [[../resources/credentials/jc4f45um3ujq28gc|PF Prod Device Management Replica]] (`postgres`, id `JC4f45um3UjQ28Gc`) — node "Get EMV Device Count" (id `06212a96-31b1-4ffb-a70f-cc260cac9f0b`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count2" (id `1952b656-32ad-4f32-b97c-660acefc8022`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `2c438e02-7489-4de5-be46-86471fb6666b`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens4" (id `2d539c4a-2f23-4683-ae83-6b80f78c3f30`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count iOS Softpos" (id `30191c7a-a592-4291-9026-b5b1d8ba1843`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Gateway Count1" (id `31156e22-e992-4ea2-9b83-d4e2cfa3146d`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count" (id `33ca3096-e7de-4de3-a70e-8aea3eb5922f`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Merchant Applications Count" (id `3ba8df70-0597-4913-b287-1c92bce52c18`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Create QB Invoice" (id `3d9e3099-217a-4708-8c05-7f863c1201bc`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens1" (id `58232c34-1242-46dc-8f58-6bf1716c8c6b`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count Android Softpos" (id `6b8a61ff-2770-450d-95b3-8dbf89cc3d89`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet1" (id `7930c714-2a3b-4bfb-b5ce-d9b9274280c0`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get Transaction Count1" (id `97d838c3-866e-4f20-bdba-898cfa52ba85`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get NT Count1" (id `a06f5db7-9de6-43f8-82ca-ce0f900071ab`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Merchant Applications Count1" (id `b15d8fd8-9281-47e1-ae65-d016370cddb3`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get TokenExchange Count" (id `be916685-d2bb-4858-80db-e70141762eb4`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Create an invoice" (id `c4437d44-f6fe-448b-a7ca-fb7568f9d5f6`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Gateway Count" (id `c5f3d99d-bb6b-4232-8738-576d4953cf0f`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens2" (id `cff8db08-8cbb-4403-a13a-da4588a166ef`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens3" (id `d945d63d-91d8-4aa0-936e-2e70c4121222`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get partner billing terms" (id `da9675ce-348b-457a-ad59-6db7e3cbef36`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens" (id `db72d062-6011-4cc7-9172-ff5d940135e7`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens5" (id `dd917649-c6d2-467c-bc8f-0c54c4e74db9`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get NT Count" (id `fac68ab7-dfd4-40e0-a098-f6d7e5461227`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `fdb6d940-a627-4710-8b46-0b9b7eb64e8b`)
- [[../resources/credentials/jc4f45um3ujq28gc|PF Prod Device Management Replica]] (`postgres`, id `JC4f45um3UjQ28Gc`) — node "Get EMV Device Count1" (id `fdc2911c-11fc-4231-8d7e-b0bb2c512baa`)

### HTTP URLs

- [[../resources/http-urls/ipinfo-io|ipinfo.io]] — `GET https://ipinfo.io/ip` — node "HTTP Request" (id `0dc87e64-6f7b-47cd-9335-ef1109314f13`)
- [[../resources/http-urls/quickbooks-api-intuit-com|quickbooks.api.intuit.com]] — `POST https://quickbooks.api.intuit.com/v3/company/9341452828840730/invoice?minorversion=75` — node "Create QB Invoice" (id `3d9e3099-217a-4708-8c05-7f863c1201bc`)

### Databases

- [[../resources/databases/postgres-jc4f45um3ujq28gc|postgres (via PF Prod Device Management Replica)]] — op `executeQuery` — node "Get EMV Device Count" (id `06212a96-31b1-4ffb-a70f-cc260cac9f0b`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count2" (id `1952b656-32ad-4f32-b97c-660acefc8022`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens4" (id `2d539c4a-2f23-4683-ae83-6b80f78c3f30`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count iOS Softpos" (id `30191c7a-a592-4291-9026-b5b1d8ba1843`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Gateway Count1" (id `31156e22-e992-4ea2-9b83-d4e2cfa3146d`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count" (id `33ca3096-e7de-4de3-a70e-8aea3eb5922f`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Merchant Applications Count" (id `3ba8df70-0597-4913-b287-1c92bce52c18`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens1" (id `58232c34-1242-46dc-8f58-6bf1716c8c6b`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count Android Softpos" (id `6b8a61ff-2770-450d-95b3-8dbf89cc3d89`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get Transaction Count1" (id `97d838c3-866e-4f20-bdba-898cfa52ba85`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get NT Count1" (id `a06f5db7-9de6-43f8-82ca-ce0f900071ab`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Merchant Applications Count1" (id `b15d8fd8-9281-47e1-ae65-d016370cddb3`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get TokenExchange Count" (id `be916685-d2bb-4858-80db-e70141762eb4`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Gateway Count" (id `c5f3d99d-bb6b-4232-8738-576d4953cf0f`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens2" (id `cff8db08-8cbb-4403-a13a-da4588a166ef`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens3" (id `d945d63d-91d8-4aa0-936e-2e70c4121222`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens" (id `db72d062-6011-4cc7-9172-ff5d940135e7`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens5" (id `dd917649-c6d2-467c-bc8f-0c54c4e74db9`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get NT Count" (id `fac68ab7-dfd4-40e0-a098-f6d7e5461227`)
- [[../resources/databases/postgres-jc4f45um3ujq28gc|postgres (via PF Prod Device Management Replica)]] — op `executeQuery` — node "Get EMV Device Count1" (id `fdc2911c-11fc-4231-8d7e-b0bb2c512baa`)

### Google Sheets

- [[../resources/google-sheets/1isfvqkczczl2ougziu5ljczc6bh4sw9tygvoeiq-nsm|Partner Platform Monthly Invoicing]] (id `1iSfvqkczczL2OuGziu5LjcZC6bH4sw9TyGvoeiq-nsM`) — op `append`, tab `Monthly Invoices` — node "Append row in sheet" (id `2c438e02-7489-4de5-be46-86471fb6666b`)
- [[../resources/google-sheets/1isfvqkczczl2ougziu5ljczc6bh4sw9tygvoeiq-nsm|Partner Platform Monthly Invoicing]] (id `1iSfvqkczczL2OuGziu5LjcZC6bH4sw9TyGvoeiq-nsM`) — op `append`, tab `ARM TIMEZONE` — node "Append row in sheet1" (id `7930c714-2a3b-4bfb-b5ce-d9b9274280c0`)
- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "Get partner billing terms" (id `da9675ce-348b-457a-ad59-6db7e3cbef36`)

### Slack channels

- [[../resources/slack-channels/c05db6zerj5|accounts-receivable]] (id `C05DB6ZERJ5`) — op `channel` — node "Send a message" (id `fdb6d940-a627-4710-8b46-0b9b7eb64e8b`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
