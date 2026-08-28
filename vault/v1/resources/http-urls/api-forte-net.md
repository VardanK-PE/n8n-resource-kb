---
type: http-url
instance: v1
resource_id: "api.forte.net"
current_name: "api.forte.net"
aliases: ["api.forte.net"]
auto_generated_at: 2026-08-19T19:25:44Z
---

<!-- auto:start -->

# api.forte.net

- **Resource id (canonical):** `api.forte.net`
- **Current name:** api.forte.net
- **Host:** `api.forte.net`

## Used by

- [[../../workflows/forte-gateway-auto-submitter-v2|Forte Gateway Auto-submitter V2]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/{{ $json.application_id }}` — node "Forte Get Merchant Status" (id `8768fb3e-fb1f-4fb6-8b32-da5b73ce7a3f`)
- [[../../workflows/forte-gateway-auto-submitter-v2|Forte Gateway Auto-submitter V2]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/{{ $json.forte_processor_application_id }}` — node "Forte Get Merchant Details" (id `53968add-7d21-4a6c-a811-eea2be8ba12d`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/{{ $json.application_id }}` — node "Forte Get Merchant Status" (id `c8c84f95-376e-4770-822e-0c27691e10af`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/{{ $json.data.find(d => d.processor_id === 'forte')?.application_id }}` — node "GetFundingTransactionsFromForte" (id `274e62f0-265d-4c0c-bb2c-7f9d816b84be`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/{{ $json.forte_processor_application_id }}` — node "Forte Get Merchant Details" (id `0005bb7d-e37e-4169-80c3-fc42754e5f07`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://api.forte.net/v3/organizations/org_444639/locations` — node "GetFundingTransactionsFromForte1" (id `9ac60bf0-f56a-4013-9aae-64ac49ecf755`)
- [[../../workflows/monthly-ach-reports-bk-2025-0924|Monthly ACH Reports - bk 2025-0924]] — `GET https://api.forte.net/v3/organizations/org_444639/locations/loc_325348/fundings/{{ $json.funding_id }}/transactions` — node "GetFundingTransactionsFromForte" (id `a7174f02-5efe-4629-86a5-2a6cc5444973`)
- [[../../workflows/monthly-ach-reports-bk-2025-0924|Monthly ACH Reports - bk 2025-0924]] — `GET https://api.forte.net/v3/organizations/org_444639/locations/loc_325348/fundings` — node "GetFundingsFromForte" (id `e5b80fb0-68ec-49d0-a8d6-699e014fcc26`)
- [[../../workflows/monthly-ach-reports-bk-2025-0924|Monthly ACH Reports - bk 2025-0924]] — `GET https://api.forte.net/v3/organizations/{{ $('Loop Over Items').item.json.processor_merchant_id }}/transactions` — node "GetOrganizationDetails" (id `a5ff710a-aafd-4893-abd6-a117cc7d9816`)
- [[../../workflows/monthly-ach-reports-bk-2025-0924|Monthly ACH Reports - bk 2025-0924]] — `GET https://api.forte.net/v3/organizations/{{ $json.processor_merchant_id }}` — node "GetOrganizationDetails1" (id `917661a6-cdbb-4e15-8462-13e632f9afbb`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — `GET https://api.forte.net/v3/organizations/org_444639/locations/loc_325348/fundings/{{ $json.funding_id }}/transactions` — node "GetFundingTransactionsFromForte" (id `73096e07-70b0-454a-98d1-d672a4343ece`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — `GET https://api.forte.net/v3/organizations/org_444639/locations/loc_325348/fundings` — node "GetFundingsFromForte" (id `681ca8a6-53db-4eb5-94ec-3e370d84acc4`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — `GET https://api.forte.net/v3/organizations/{{ $('Loop Over Items').item.json.processor_merchant_id }}/transactions` — node "GetOrganizationDetails" (id `de92493d-7c46-4c7a-8bc4-27c44af94a6d`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — `GET https://api.forte.net/v3/organizations/{{ $json.processor_merchant_id }}` — node "GetOrganizationDetails1" (id `cdb856f5-12a4-4498-a9e0-e50ef535fabb`)
- [[../../workflows/payengineai-bot-v1-1-feb-26-2026-saot95eapiyc8s56|PayEngineAI Bot (v1.1) - Feb 26 2026]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/app_{{ $fromAI('ForteApplicationID', ``, 'string') }}` — node "Forte Rejected Reason Lookup" (id `24d9d4d0-95fc-443c-ae5c-7d4228d54bb0`)
- [[../../workflows/payengineai-bot-v1-1-feb-26-2026|PayEngineAI Bot (v1.2) - Jun 12 2026]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/app_{{ $fromAI('ForteApplicationID', ``, 'string') }}` — node "Forte Rejected Reason Lookup" (id `cc83a563-1ae6-4ef4-821d-aea24e55853d`)
- [[../../workflows/payengineai-bot-v1|PayEngineAI Bot (v1)]] — `GET https://api.forte.net/v3/organizations/org_426264/applications/app_{{ $fromAI('ForteApplicationID', ``, 'string') }}` — node "Forte Rejected Reason Lookup" (id `9e20f883-3058-4988-a985-5ca3f6de0c25`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
