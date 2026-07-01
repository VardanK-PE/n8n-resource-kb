---
type: http-url
resource_id: "api.forte.net"
current_name: "api.forte.net"
aliases: ["api.forte.net"]
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# api.forte.net

- **Resource id (canonical):** `api.forte.net`
- **Current name:** api.forte.net
- **Host:** `api.forte.net`

## Used by

- [[../../workflows/hearth-applications-autosubmitter|Hearth Applications Autosubmitter]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/{{ $json.application_id }}` — node "Forte Get Merchant Status" (id `c8c84f95-376e-4770-822e-0c27691e10af`)
- [[../../workflows/hearth-applications-autosubmitter|Hearth Applications Autosubmitter]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/{{ $json.data.find(d => d.processor_id === 'forte')?.application_id }}` — node "GetFundingTransactionsFromForte" (id `274e62f0-265d-4c0c-bb2c-7f9d816b84be`)
- [[../../workflows/hearth-applications-autosubmitter|Hearth Applications Autosubmitter]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/{{ $json.forte_processor_application_id }}` — node "Forte Get Merchant Details" (id `0005bb7d-e37e-4169-80c3-fc42754e5f07`)
- [[../../workflows/hearth-applications-autosubmitter|Hearth Applications Autosubmitter]] — `GET https://api.forte.net/v3/organizations/org_444639/locations` — node "GetFundingTransactionsFromForte1" (id `9ac60bf0-f56a-4013-9aae-64ac49ecf755`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — `GET https://api.forte.net/v3/organizations/org_444639/locations/loc_325348/fundings` — node "GetFundingsFromForte" (id `681ca8a6-53db-4eb5-94ec-3e370d84acc4`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — `GET https://api.forte.net/v3/organizations/org_444639/locations/loc_325348/fundings/{{ $json.funding_id }}/transactions` — node "GetFundingTransactionsFromForte" (id `73096e07-70b0-454a-98d1-d672a4343ece`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — `GET https://api.forte.net/v3/organizations/{{ $('Loop Over Items').item.json.processor_merchant_id }}/transactions` — node "GetOrganizationDetails" (id `de92493d-7c46-4c7a-8bc4-27c44af94a6d`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — `GET https://api.forte.net/v3/organizations/{{ $json.processor_merchant_id }}` — node "GetOrganizationDetails1" (id `cdb856f5-12a4-4498-a9e0-e50ef535fabb`)
- [[../../workflows/payengineai-bot-v1|PayEngineAI Bot (v1)]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/app_{{ $fromAI('ForteApplicationID', ``, 'string') }}` — node "Forte Rejected Reason Lookup" (id `9e20f883-3058-4988-a985-5ca3f6de0c25`)
- [[../../workflows/payengineai-bot-v1-1-feb-26-2026|PayEngineAI Bot (v1.1) - Feb 26 2026]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/app_{{ $fromAI('ForteApplicationID', ``, 'string') }}` — node "Forte Rejected Reason Lookup" (id `cc83a563-1ae6-4ef4-821d-aea24e55853d`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
