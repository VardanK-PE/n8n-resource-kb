---
n8n_id: "A4CLCcD8gPm77Gus"
instance: v1
name: "Monthly ACH Reports - bk 2025-0924"
status: inactive
last_modified: 2025-09-25T04:30:56.104Z
tags:
  - "backups"
fingerprint: "b42dcb7ceae324286fea0b9390e17e9db7eb88977b019ddb8585c388504e7b72"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Monthly ACH Reports - bk 2025-0924

## Summary

- **Status:** inactive
- **n8n ID:** `A4CLCcD8gPm77Gus`
- **Nodes:** 105
- **Last modified:** 2025-09-25T04:30:56.104Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `a4e16c02-8519-4674-b220-44f552fc4899`) — `every 1 hour(s)`
- **execute-workflow** — node "When Executed by Another Workflow" (id `bed1296b-edce-4fb0-b548-b5d8b0e945ce`)
- **manual** — node "When clicking ‘Execute workflow’" (id `cd824575-e798-4002-a697-76be99218f27`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Created Invoice" (id `00c1ff98-2a1b-4b6d-9acc-a35fdbf7cdf7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create Log Entry" (id `0d2e5096-6e41-48a7-973b-c5e54bbf88e1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets3" (id `0e3e8a52-d44e-4a99-bbd7-3ba5bccd5c53`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `1182688b-acd2-4c6a-9de6-0a167a0bef18`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "DB Fee Schedules1" (id `18703f56-f6ab-4a4b-a4e1-89e14040bede`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get ACH Transactions1" (id `1a14c8f1-61a1-4b42-803d-d22b82d678cd`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get ACH Transactions" (id `1cd8a13c-8385-4171-899a-0e821a06b3bc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets12" (id `57cb1178-2311-4b6b-8c44-81236b717bab`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `658fe679-9c39-46ea-af42-8cd4b009178a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append to All Transactions" (id `699d8d50-21a9-4813-b62e-5fb69c5783d3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Created Customer1" (id `7001fccf-446c-4379-b1f3-aa9377a6c3da`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append row in sheet" (id `736ef2c2-3c4d-4438-ad39-913a26d63737`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `8904a3f1-92c0-45c9-8e50-b8bbc87a933c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Parsed Fee Schedules" (id `89803fec-d2a5-49d8-a203-f484dfdb89f9`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "GetOrganizationDetails1" (id `917661a6-cdbb-4e15-8462-13e632f9afbb`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `91cd9ffc-d17f-4a7d-b35f-1de635e124b4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append to Aggregate Data" (id `9d3290f2-9db7-46f9-a62c-7811ee7282de`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `9f4c0229-a8e2-4196-a37d-57382dd03b81`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "DB Fee Schedules" (id `a0270a23-3974-4bf6-a43e-95974bccbca7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets9" (id `a49dc478-d1eb-4545-a99f-53488194ef47`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "GetOrganizationDetails" (id `a5ff710a-aafd-4893-abd6-a117cc7d9816`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "GetFundingTransactionsFromForte" (id `a7174f02-5efe-4629-86a5-2a6cc5444973`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `ab13c0ac-8d8b-45fe-9239-f706d8889274`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update fee schedule table1" (id `ab53c41f-fa0c-4fff-971c-5e129cf0d324`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `aba6dec0-c3c9-4457-b147-6cc0028a797e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet2" (id `afbf59ff-bc22-42f4-9088-15b59bfe8e10`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Fee Schedules" (id `bf528797-2f7e-4ad6-b220-fda6b9d48849`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `bf5a31c2-caed-4270-93ea-a20b4eeba2f4`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres3" (id `c14498a0-9549-4958-925b-e9ac4694bae8`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres4" (id `c653363a-af49-458e-98ef-f4e3a5562a23`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `d5be021f-dd58-4497-9a39-c29fabcce1c9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update fee schedule table" (id `d822b137-8d74-424c-8e79-63bb00269d32`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `dd4e08f1-9821-469b-9d79-8835e48f58e8`)
- [[../resources/credentials/w2zoksnllwt306s9|Forte Production Account]] (`httpBasicAuth`, id `w2zokSnlLwt306s9`) — node "GetFundingsFromForte" (id `e5b80fb0-68ec-49d0-a8d6-699e014fcc26`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres2" (id `edff16cf-cf13-473b-90ec-24c7745064a4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Created Customer" (id `f370e058-fe3d-40e7-b98f-4073fcc4f2c2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `fc7e6e35-9dcd-43cf-94df-522b4d20ae49`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/payment/ach` — node "Perform the Charge" (id `0e0604a7-8d59-4b27-aab1-4f1c0c56f77d`)
- [[../resources/http-urls/quickbooks-api-intuit-com|quickbooks.api.intuit.com]] — `POST https://quickbooks.api.intuit.com/v3/company/9341452828840730/customer?minorversion=75` — node "Create Customer1" (id `84d6807c-a5c8-44ae-9a24-104c3baa1393`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/{{ $json.processor_merchant_id }}` — node "GetOrganizationDetails1" (id `917661a6-cdbb-4e15-8462-13e632f9afbb`)
- [[../resources/http-urls/gw-payengine-co|gw.payengine.co]] — `POST https://gw.payengine.co/api/bank-accounts` — node "HTTP Request" (id `94231009-6208-4e44-8276-c0f5ad79d114`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/{{ $('Loop Over Items').item.json.processor_merchant_id }}/transactions` — node "GetOrganizationDetails" (id `a5ff710a-aafd-4893-abd6-a117cc7d9816`)
- [[../resources/http-urls/quickbooks-api-intuit-com|quickbooks.api.intuit.com]] — `POST https://quickbooks.api.intuit.com/v3/company/9341452828840730/invoice?minorversion=75` — node "Create QB Invoice" (id `a7122589-5250-408d-9d60-65ea4ee1194e`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/org_444639/locations/loc_325348/fundings/{{ $json.funding_id }}/transactions` — node "GetFundingTransactionsFromForte" (id `a7174f02-5efe-4629-86a5-2a6cc5444973`)
- [[../resources/http-urls/api-forte-net|api.forte.net]] — `GET https://api.forte.net/v3/organizations/org_444639/locations/loc_325348/fundings` — node "GetFundingsFromForte" (id `e5b80fb0-68ec-49d0-a8d6-699e014fcc26`)
- [[../resources/http-urls/quickbooks-api-intuit-com|quickbooks.api.intuit.com]] — `POST https://quickbooks.api.intuit.com/v3/company/9341452828840730/customer?minorversion=75` — node "Create Customer2" (id `fb4c76a4-1614-455e-a442-9bc318a1708f`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "DB Fee Schedules1" (id `18703f56-f6ab-4a4b-a4e1-89e14040bede`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get ACH Transactions1" (id `1a14c8f1-61a1-4b42-803d-d22b82d678cd`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get ACH Transactions" (id `1cd8a13c-8385-4171-899a-0e821a06b3bc`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `8904a3f1-92c0-45c9-8e50-b8bbc87a933c`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "DB Fee Schedules" (id `a0270a23-3974-4bf6-a43e-95974bccbca7`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `aba6dec0-c3c9-4457-b147-6cc0028a797e`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres3" (id `c14498a0-9549-4958-925b-e9ac4694bae8`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres4" (id `c653363a-af49-458e-98ef-f4e3a5562a23`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres2" (id `edff16cf-cf13-473b-90ec-24c7745064a4`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model" (id `658fe679-9c39-46ea-af42-8cd4b009178a`)
- [[../resources/llm-models/anthropic-claude-sonnet-4-20250514|anthropic / claude-sonnet-4-20250514]] — node "Anthropic Chat Model1" (id `dd4e08f1-9821-469b-9d79-8835e48f58e8`)

### Google Sheets

- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `QB LOGS - INVOICES` — node "Log Created Invoice" (id `00c1ff98-2a1b-4b6d-9acc-a35fdbf7cdf7`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `BANK_ACCOUNT_TOKENS_LOG` — node "Create Log Entry" (id `0d2e5096-6e41-48a7-973b-c5e54bbf88e1`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $json.date }}-ALL-AGGREGATE` — node "Google Sheets3" (id `0e3e8a52-d44e-4a99-bbd7-3ba5bccd5c53`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $json['date'] }}-ALL-AGGREGATE` — node "Get row(s) in sheet1" (id `1182688b-acd2-4c6a-9de6-0a167a0bef18`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `update`, tab `={{ $('When clicking ‘Execute workflow’').item.json['start-date'] }}-ALL-AGGREGATE` — node "Google Sheets12" (id `57cb1178-2311-4b6b-8c44-81236b717bab`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `={{ $('InputFields').item.json["start-date"] }}-ALL` — node "Append to All Transactions" (id `699d8d50-21a9-4813-b62e-5fb69c5783d3`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `QB LOGS - CUSTOMERS CREATED` — node "Log Created Customer1" (id `7001fccf-446c-4379-b1f3-aa9377a6c3da`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `PE_FORTE_TRANSACTIONS_LOG` — node "Append row in sheet" (id `736ef2c2-3c4d-4438-ad39-913a26d63737`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `FEE_SCHEDULES` — node "Parsed Fee Schedules" (id `89803fec-d2a5-49d8-a203-f484dfdb89f9`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `create`, tab `null` — node "Google Sheets2" (id `91cd9ffc-d17f-4a7d-b35f-1de635e124b4`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `={{ $('InputFields').first().json["start-date"] }}-ALL-AGGREGATE` — node "Append to Aggregate Data" (id `9d3290f2-9db7-46f9-a62c-7811ee7282de`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $json['start-date'] }}-ALL-AGGREGATE` — node "Get row(s) in sheet" (id `9f4c0229-a8e2-4196-a37d-57382dd03b81`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `update`, tab `={{ $('When clicking ‘Execute workflow’').item.json['start-date'] }}-ALL-AGGREGATE` — node "Google Sheets9" (id `a49dc478-d1eb-4545-a99f-53488194ef47`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `update`, tab `={{ $json.date }}-ALL-AGGREGATE` — node "Google Sheets4" (id `ab13c0ac-8d8b-45fe-9239-f706d8889274`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `appendOrUpdate`, tab `FEE_SCHEDULES` — node "Append or update fee schedule table1" (id `ab53c41f-fa0c-4fff-971c-5e129cf0d324`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `update`, tab `={{ $('When clicking ‘Execute workflow’').item.json.date }}-ALL-AGGREGATE` — node "Get row(s) in sheet2" (id `afbf59ff-bc22-42f4-9088-15b59bfe8e10`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `FEE_SCHEDULES` — node "Get Fee Schedules" (id `bf528797-2f7e-4ad6-b220-fda6b9d48849`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `={{ $('InputFields').item.json["start-date"] }}-FORTE` — node "Google Sheets1" (id `bf5a31c2-caed-4270-93ea-a20b4eeba2f4`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `create`, tab `null` — node "Google Sheets5" (id `d5be021f-dd58-4497-9a39-c29fabcce1c9`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `appendOrUpdate`, tab `FEE_SCHEDULES` — node "Append or update fee schedule table" (id `d822b137-8d74-424c-8e79-63bb00269d32`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `append`, tab `QB LOGS - CUSTOMERS CREATED` — node "Log Created Customer" (id `f370e058-fe3d-40e7-b98f-4073fcc4f2c2`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|FORTE TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `create`, tab `null` — node "Google Sheets" (id `fc7e6e35-9dcd-43cf-94df-522b4d20ae49`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
