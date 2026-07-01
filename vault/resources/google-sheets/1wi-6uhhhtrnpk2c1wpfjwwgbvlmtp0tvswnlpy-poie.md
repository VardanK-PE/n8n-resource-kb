---
type: google-sheets
resource_id: "1Wi_6UHhhtrnpk2c1WpfjwwGbvLmTp0TvSwnLPY_POIE"
current_name: "Combined ACH Transactions Data"
aliases: ["Combined ACH Transactions Data"]
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Combined ACH Transactions Data

- **Resource id (canonical):** `1Wi_6UHhhtrnpk2c1WpfjwwGbvLmTp0TvSwnLPY_POIE`
- **Current name:** Combined ACH Transactions Data
- **URL:** https://docs.google.com/spreadsheets/d/1Wi_6UHhhtrnpk2c1WpfjwwGbvLmTp0TvSwnLPY_POIE/edit?usp=drivesdk
- **Spreadsheet ID:** `1Wi_6UHhhtrnpk2c1WpfjwwGbvLmTp0TvSwnLPY_POIE`

## Used by

- [[../../workflows/billing-system-charge-merchant|Billing System - Charge Merchant]] — op `append`, tab `Error Log` — node "Update Transaction Details1" (id `ad71d68f-dac3-4457-a424-6de2b693daf3`)
- [[../../workflows/billing-system-charge-merchant|Billing System - Charge Merchant]] — op `append`, tab `Token Log` — node "Update Transaction Details3" (id `659780f4-5dc7-4e5a-8b5d-d37083a34bc5`)
- [[../../workflows/billing-system-charge-merchant|Billing System - Charge Merchant]] — op `append`, tab `Transaction Log` — node "Append row in sheet" (id `294c29c7-8ef3-486f-89e7-ad4d850c092f`)
- [[../../workflows/billing-system-generate-invoices-for-billing-period|Billing System - Generate Invoices for Billing Period]] — op `append`, tab `={{ $('Set spreadsheet name').first().json.sheet_name }}` — node "Append row in sheet" (id `3917d6cb-eff3-4f7d-b2ae-428b987b20c6`)
- [[../../workflows/billing-system-generate-invoices-for-billing-period|Billing System - Generate Invoices for Billing Period]] — op `appendOrUpdate`, tab `={{ $('Set spreadsheet name').first().json.sheet_name }}` — node "Google Sheets" (id `e5568aa0-0256-4692-86f5-02c30b963afd`)
- [[../../workflows/billing-system-generate-invoices-for-billing-period|Billing System - Generate Invoices for Billing Period]] — op `appendOrUpdate`, tab `={{ $('Set spreadsheet name').first().json.sheet_name }}` — node "Google Sheets4" (id `f2485891-d7ba-427f-9f1f-1e2bc4d76894`)
- [[../../workflows/billing-system-generate-invoices-for-billing-period|Billing System - Generate Invoices for Billing Period]] — op `?`, tab `={{ $json.sheet_name }}` — node "Get row(s) in sheet" (id `08536798-f453-489e-95ab-b86e202ecc03`)
- [[../../workflows/billing-system-generate-invoices-for-billing-period|Billing System - Generate Invoices for Billing Period]] — op `create`, tab `null` — node "Create sheet" (id `dd48b366-2e6d-4dde-8c9b-9c17fe2acb4c`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
