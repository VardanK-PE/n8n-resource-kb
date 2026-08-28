---
n8n_id: "TiGC9ck3kPX1tek4"
instance: v1
name: "Monthly Merchant Direct Billing"
status: inactive
last_modified: 2026-05-05T18:05:14.768Z
tags: []
fingerprint: "b804244eba5035783de113d95d6aa77bf41c67681b03ab2a19c9a4be424c6478"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Monthly Merchant Direct Billing

## Summary

- **Status:** inactive
- **n8n ID:** `TiGC9ck3kPX1tek4`
- **Nodes:** 48
- **Last modified:** 2026-05-05T18:05:14.768Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `a6a9c5af-aefb-476b-a749-10eb77c77d0d`)
- **schedule** — node "Schedule Trigger" (id `d370b4d3-9d9b-4161-826e-7198743c3b61`) — `every 1 month(s)`

## Depends on

### Credentials

- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens" (id `0d04f43c-aea1-4728-b8f1-e6c8e7bbdc82`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens1" (id `0fb99723-ce25-4691-8a7a-b0086b58442c`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens4" (id `1d064a74-4554-4cca-bab1-4d157583ce9f`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Gateway Count" (id `1e503f43-e8db-46a0-9597-80aa9d028e77`)
- [[../resources/credentials/jc4f45um3ujq28gc|PF Prod Device Management Replica]] (`postgres`, id `JC4f45um3UjQ28Gc`) — node "Get EMV Device Count1" (id `284606ba-24dd-4ca8-95f2-7b5a086a8462`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Create an invoice" (id `35de3889-0d9b-496c-aced-bc387c953490`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count" (id `4097587a-c503-44b0-94a9-eba1ec95f843`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens3" (id `42ba9b75-510f-4917-b7bc-e3400377c422`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get NT Count" (id `46e6acc4-649e-486f-a174-636a72a70dd4`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Merchant Applications Count" (id `4b6174f3-76f8-4a89-9273-fef91de840fc`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Gateway Count1" (id `4bd59766-c36f-4187-96f1-9f566fbb2bb7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get partner billing terms" (id `4f3ead33-c324-4c38-a1cb-3ecb9aef16f9`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens2" (id `50a59d4e-6ac3-4d2d-9fc3-953f01c0b432`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `607dd8ed-4020-4d60-b606-fdc08e7a51f2`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Create QB Invoice" (id `65f6a808-ee2c-4394-9e70-e088b5f474cd`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Merchant Applications Count1" (id `693648b5-fa6e-45c1-9c16-04468095427a`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get NT Count1" (id `7a7f74a8-0850-4c34-b95a-f839f933f950`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get Transaction Count1" (id `7ff52f75-8d20-44cf-a4ac-e81a6ba91789`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count Android Softpos" (id `8b02c6b1-a2cd-43e6-ba59-730e33341070`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet1" (id `a2dda3db-ee53-4ac1-8295-b70888ee7217`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count2" (id `c1f4894c-3f38-458e-8abe-e111f9e51c1e`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get TokenExchange Count" (id `d2b59940-7dbf-44ac-9a9a-cf9d3c226f95`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count iOS Softpos" (id `d6610ddc-8cd4-4917-afc3-e5ef6aa4b61b`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `e7754a6a-510e-4021-a0b3-566d23fe4cb8`)
- [[../resources/credentials/jc4f45um3ujq28gc|PF Prod Device Management Replica]] (`postgres`, id `JC4f45um3UjQ28Gc`) — node "Get EMV Device Count" (id `e8db3347-6771-4a58-800a-ba8fbcfcb45c`)

### HTTP URLs

- [[../resources/http-urls/quickbooks-api-intuit-com|quickbooks.api.intuit.com]] — `POST https://quickbooks.api.intuit.com/v3/company/9341452828840730/invoice?minorversion=75` — node "Create QB Invoice" (id `65f6a808-ee2c-4394-9e70-e088b5f474cd`)
- [[../resources/http-urls/ipinfo-io|ipinfo.io]] — `GET https://ipinfo.io/ip` — node "HTTP Request" (id `ec737e62-aff8-43fd-9a0c-0f19077523f6`)

### Databases

- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens" (id `0d04f43c-aea1-4728-b8f1-e6c8e7bbdc82`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens1" (id `0fb99723-ce25-4691-8a7a-b0086b58442c`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens4" (id `1d064a74-4554-4cca-bab1-4d157583ce9f`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Gateway Count" (id `1e503f43-e8db-46a0-9597-80aa9d028e77`)
- [[../resources/databases/postgres-jc4f45um3ujq28gc|postgres (via PF Prod Device Management Replica)]] — op `executeQuery` — node "Get EMV Device Count1" (id `284606ba-24dd-4ca8-95f2-7b5a086a8462`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count" (id `4097587a-c503-44b0-94a9-eba1ec95f843`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens3" (id `42ba9b75-510f-4917-b7bc-e3400377c422`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get NT Count" (id `46e6acc4-649e-486f-a174-636a72a70dd4`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Merchant Applications Count" (id `4b6174f3-76f8-4a89-9273-fef91de840fc`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Gateway Count1" (id `4bd59766-c36f-4187-96f1-9f566fbb2bb7`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens2" (id `50a59d4e-6ac3-4d2d-9fc3-953f01c0b432`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Merchant Applications Count1" (id `693648b5-fa6e-45c1-9c16-04468095427a`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get NT Count1" (id `7a7f74a8-0850-4c34-b95a-f839f933f950`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get Transaction Count1" (id `7ff52f75-8d20-44cf-a4ac-e81a6ba91789`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count Android Softpos" (id `8b02c6b1-a2cd-43e6-ba59-730e33341070`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count2" (id `c1f4894c-3f38-458e-8abe-e111f9e51c1e`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get TokenExchange Count" (id `d2b59940-7dbf-44ac-9a9a-cf9d3c226f95`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count iOS Softpos" (id `d6610ddc-8cd4-4917-afc3-e5ef6aa4b61b`)
- [[../resources/databases/postgres-jc4f45um3ujq28gc|postgres (via PF Prod Device Management Replica)]] — op `executeQuery` — node "Get EMV Device Count" (id `e8db3347-6771-4a58-800a-ba8fbcfcb45c`)

### Google Sheets

- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "Get partner billing terms" (id `4f3ead33-c324-4c38-a1cb-3ecb9aef16f9`)
- [[../resources/google-sheets/1isfvqkczczl2ougziu5ljczc6bh4sw9tygvoeiq-nsm|Partner Platform Monthly Invoicing]] (id `1iSfvqkczczL2OuGziu5LjcZC6bH4sw9TyGvoeiq-nsM`) — op `append`, tab `Monthly Invoices` — node "Append row in sheet" (id `607dd8ed-4020-4d60-b606-fdc08e7a51f2`)
- [[../resources/google-sheets/1isfvqkczczl2ougziu5ljczc6bh4sw9tygvoeiq-nsm|Partner Platform Monthly Invoicing]] (id `1iSfvqkczczL2OuGziu5LjcZC6bH4sw9TyGvoeiq-nsM`) — op `append`, tab `ARM TIMEZONE` — node "Append row in sheet1" (id `a2dda3db-ee53-4ac1-8295-b70888ee7217`)

### Slack channels

- [[../resources/slack-channels/c05db6zerj5|accounts-receivable]] (id `C05DB6ZERJ5`) — op `channel` — node "Send a message" (id `e7754a6a-510e-4021-a0b3-566d23fe4cb8`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
