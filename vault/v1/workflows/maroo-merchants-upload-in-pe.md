---
n8n_id: "0K9vDmRCbRs21Elr"
instance: v1
name: "Maroo - Merchants Upload In PE"
status: inactive
last_modified: 2025-01-23T23:29:57.943Z
tags: []
fingerprint: "44f66a41ea0ad4de89e77ef8456682bc966f2db76f1fc0e8d3522f2d3dc2c092"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Maroo - Merchants Upload In PE

## Summary

- **Status:** inactive
- **n8n ID:** `0K9vDmRCbRs21Elr`
- **Nodes:** 24
- **Last modified:** 2025-01-23T23:29:57.943Z

## Triggers

- **manual** — node "When clicking ‘Test workflow’" (id `6cb4892f-514c-4bb9-af52-9b3bb4f24418`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Group IDs" (id `043217f8-ccf1-4807-9f6c-f4d06a197f98`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Read From Sheet" (id `12253e31-9d81-4991-8b70-c7cf7e90fd45`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `2cd46d4d-d9b6-4c26-b4df-ba0e73d52171`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Merchant" (id `82423a96-0d75-4dc6-9a3a-8b0fb5fd775f`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Group IDs1" (id `8ee17d4f-1e4b-46e6-9728-f3b684347d18`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Output Sheet1" (id `9ca176c2-22d0-4dd4-87a2-29627ee59b1c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Output Sheet" (id `c661c1cc-92f6-4547-96bf-720233beb3d1`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Output" (id `ee3576ac-3404-41b4-b668-77775f4dba3d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Read From Sheet1" (id `f93dc289-1380-4937-93af-300d34cce265`)

### HTTP URLs

- *(dynamic URL)* — `PUT {{ $input.first().json.url }}` — node "Update Group" (id `a1aec6a8-10f0-4f07-8299-7a1bbf3754fe`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/merchant` — node "Create PE Merchant" (id `fbb588ef-8e59-49de-9e67-30d145bad946`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `select`, table `{"__rl":true,"value":"account_groups","mode":"list","cachedResultName":"account_groups"}` — node "Group IDs" (id `043217f8-ccf1-4807-9f6c-f4d06a197f98`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `select`, table `{"__rl":true,"value":"merchant","mode":"list","cachedResultName":"merchant"}` — node "Merchant" (id `82423a96-0d75-4dc6-9a3a-8b0fb5fd775f`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `select`, table `{"__rl":true,"value":"lexis_nexis_api_logs","mode":"list","cachedResultName":"lexis_nexis_api_logs"}` — node "Group IDs1" (id `8ee17d4f-1e4b-46e6-9728-f3b684347d18`)

### Google Sheets

- [[../resources/google-sheets/1kyciagn3jbwpyz6-n8gar4-ysjkielebwxmpqxnsos4|PayEngine_data_maroo_filled_v2]] (id `1KycIaGn3jBWPYz6-N8gAr4-ysJKIelEbWxMpqXNSos4`) — op `?`, tab `Maroo pe req` — node "Read From Sheet" (id `12253e31-9d81-4991-8b70-c7cf7e90fd45`)
- [[../resources/google-sheets/1iz3f2newxfygqqduspyn7ozb7w3bib65eloihwkovr4|decrypted-data_maroo]] (id `1Iz3f2nEWXFYGqqdusPYN7OZB7W3biB65elOiHwkovR4`) — op `?`, tab `decrypted-data_maroo` — node "Google Sheets" (id `2cd46d4d-d9b6-4c26-b4df-ba0e73d52171`)
- [[../resources/google-sheets/1rcqa041y7xb7zdffttknrz7vtwvtujpt3jaten-f1qa|Maroo Test Sheet]] (id `1rcQa041Y7xB7ZDfftTKnrZ7VTwvTUJPT3JaTen-F1qA`) — op `appendOrUpdate`, tab `Lexis Nexis Txn IDs` — node "Output Sheet1" (id `9ca176c2-22d0-4dd4-87a2-29627ee59b1c`)
- [[../resources/google-sheets/1kyciagn3jbwpyz6-n8gar4-ysjkielebwxmpqxnsos4|PayEngine_data_maroo_filled_v2]] (id `1KycIaGn3jBWPYz6-N8gAr4-ysJKIelEbWxMpqXNSos4`) — op `appendOrUpdate`, tab `Output` — node "Output Sheet" (id `c661c1cc-92f6-4547-96bf-720233beb3d1`)
- [[../resources/google-sheets/1kyciagn3jbwpyz6-n8gar4-ysjkielebwxmpqxnsos4|PayEngine_data_maroo_filled_v2]] (id `1KycIaGn3jBWPYz6-N8gAr4-ysJKIelEbWxMpqXNSos4`) — op `append`, tab `Maroo pe req` — node "Output" (id `ee3576ac-3404-41b4-b668-77775f4dba3d`)
- [[../resources/google-sheets/1kyciagn3jbwpyz6-n8gar4-ysjkielebwxmpqxnsos4|PayEngine_data_maroo_filled_v2]] (id `1KycIaGn3jBWPYz6-N8gAr4-ysJKIelEbWxMpqXNSos4`) — op `?`, tab `Output` — node "Read From Sheet1" (id `f93dc289-1380-4937-93af-300d34cce265`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
