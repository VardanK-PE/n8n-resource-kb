---
type: google-sheets
resource_id: "17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0"
current_name: "PCI non compliant merchants"
aliases: ["PCI non compliant merchants"]
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PCI non compliant merchants

- **Resource id (canonical):** `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`
- **Current name:** PCI non compliant merchants
- **URL:** https://docs.google.com/spreadsheets/d/17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0/edit?usp=drivesdk
- **Spreadsheet ID:** `17BppPBTv5QGJkqGCdDyCTUDPn5H4XoiWzRGYUAgusw0`

## Used by

- [[../../workflows/billing-system-charge-all-merchants|Billing System - Charge All Merchants]] — op `?`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Get row(s) in sheet1" (id `d2aeada4-d050-40a9-a576-04b6f849179a`)
- [[../../workflows/billing-system-charge-all-merchants|Billing System - Charge All Merchants]] — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update Bank Account Fields" (id `cb8aeb79-805f-41b5-a45f-a9dd5892d464`)
- [[../../workflows/billing-system-charge-all-merchants|Billing System - Charge All Merchants]] — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update Transaction Details" (id `d1265286-ae69-40f3-8442-e74a0928f39c`)
- [[../../workflows/billing-system-charge-all-merchants|Billing System - Charge All Merchants]] — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update row in sheet" (id `91f48b32-3af6-476f-b707-23b534ed78d6`)
- [[../../workflows/billing-system-charge-all-merchants|Billing System - Charge All Merchants]] — op `?`, tab `={{ $json.spreadsheet_name }}` — node "Get row(s) in sheet" (id `9a63ba87-dd6a-4899-a517-2845a22ee2f3`)
- [[../../workflows/billing-system-charge-all-merchants|Billing System - Charge All Merchants]] — op `append`, tab `Error Log` — node "Update Transaction Details1" (id `2daf3189-781e-45f9-b547-882baf60c98e`)
- [[../../workflows/billing-system-charge-all-merchants|Billing System - Charge All Merchants]] — op `append`, tab `Token Logs` — node "Update Transaction Details2" (id `735307cf-f2eb-418a-9d26-1398804209bc`)
- [[../../workflows/billing-system-charge-all-merchants|Billing System - Charge All Merchants]] — op `append`, tab `Transaction Log` — node "Append row in sheet" (id `1f31e478-d506-4155-abc6-246e74523818`)
- [[../../workflows/billing-system-generate-invoices-for-billing-period|Billing System - Generate Invoices for Billing Period]] — op `?`, tab `={{ $('Set spreadsheet name').first().json.sheet_name }}` — node "Get PCI non compliant merchant details" (id `6cf6d027-82b4-4853-86fc-42536ce80390`)
- [[../../workflows/charge-pci-non-compliant-merchants|Charge PCI non compliant merchants]] — op `?`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Get row(s) in sheet1" (id `e195d898-4e35-49bf-880c-b60e45a6dd88`)
- [[../../workflows/charge-pci-non-compliant-merchants|Charge PCI non compliant merchants]] — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update Bank Account Fields" (id `74ac1b30-29d2-412b-8305-3b194e9c4e2c`)
- [[../../workflows/charge-pci-non-compliant-merchants|Charge PCI non compliant merchants]] — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update Transaction Details" (id `e9eaf914-b1d6-4fab-b9b6-f49709d8ee0f`)
- [[../../workflows/charge-pci-non-compliant-merchants|Charge PCI non compliant merchants]] — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update row in sheet" (id `48097993-96de-4b74-95e7-8713a4f9ed5e`)
- [[../../workflows/charge-pci-non-compliant-merchants|Charge PCI non compliant merchants]] — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Update row in sheet1" (id `fb18da2f-6bc2-40e3-b5e2-df39df494e0b`)
- [[../../workflows/charge-pci-non-compliant-merchants|Charge PCI non compliant merchants]] — op `?`, tab `={{ $json.spreadsheet_name }}` — node "Get row(s) in sheet" (id `118230c5-1860-4532-916c-1073e650a1b4`)
- [[../../workflows/charge-pci-non-compliant-merchants|Charge PCI non compliant merchants]] — op `?`, tab `={{ $json.spreadsheet_name }}` — node "Get row(s) in sheet2" (id `13c12d7f-ecc2-4c84-9ccb-bc89cf009094`)
- [[../../workflows/charge-pci-non-compliant-merchants|Charge PCI non compliant merchants]] — op `append`, tab `Error Log` — node "Update Transaction Details1" (id `31d5d0a1-152a-4a03-8d72-7a09281bdb0d`)
- [[../../workflows/charge-pci-non-compliant-merchants|Charge PCI non compliant merchants]] — op `append`, tab `Token Logs` — node "Update Transaction Details2" (id `85b5eeb7-717d-4ce0-bec3-120907e08d3a`)
- [[../../workflows/charge-pci-non-compliant-merchants|Charge PCI non compliant merchants]] — op `append`, tab `Transaction Log` — node "Append row in sheet" (id `b430183a-e6e8-4950-a87c-0f2682818ca9`)
- [[../../workflows/check-pci-ach-transaction-status|Check PCI/ACH Transaction Status]] — op `update`, tab `={{ $('Spreadsheet Name').first().json.spreadsheet_name }}` — node "Update row in sheet" (id `109da278-109d-4ed1-9098-49f054d6b0a8`)
- [[../../workflows/check-pci-ach-transaction-status|Check PCI/ACH Transaction Status]] — op `?`, tab `={{ $json.spreadsheet_name }}` — node "Get PCI non-compliance charges" (id `6457de1f-a78c-4702-a42e-0010c0666349`)
- [[../../workflows/generate-a-list-of-pci-non-compliant-merchants|Generate a list of PCI non compliant merchants]] — op `append`, tab `={{ $('Entry Point').first().json.sheet_name }}` — node "Append row in sheet1" (id `5f149088-6210-4386-a462-6fda858c574b`)
- [[../../workflows/generate-a-list-of-pci-non-compliant-merchants|Generate a list of PCI non compliant merchants]] — op `remove`, tab `={{ $('Entry Point').first().json.sheet_name }}` — node "Delete sheet1" (id `e54bea50-65e1-41c4-85e3-8f04775feaf1`)
- [[../../workflows/generate-a-list-of-pci-non-compliant-merchants|Generate a list of PCI non compliant merchants]] — op `update`, tab `={{ $('Entry Point').first().json.sheet_name }}` — node "Update row in sheet" (id `68d01ded-337f-4ce0-be3f-e2a41917654a`)
- [[../../workflows/generate-a-list-of-pci-non-compliant-merchants|Generate a list of PCI non compliant merchants]] — op `create`, tab `null` — node "Create sheet1" (id `5351a342-128c-4065-a285-f942941e39f7`)
- [[../../workflows/locate-failed-transactions-for-canadian-merchant|Locate failed transactions for Canadian merchant]] — op `?`, tab `Error Log` — node "Get row(s) in sheet" (id `676b557e-1194-451f-a6f3-eee8940e693d`)
- [[../../workflows/pci-generate-invoices-for-already-charged-merchants|PCI generate invoices for already charged merchants]] — op `update`, tab `={{ $('Entry Point').first().json.spreadsheet_name }}` — node "Google Sheets4" (id `8be56f2f-f8d3-4442-8225-ca426b9686f0`)
- [[../../workflows/pci-generate-invoices-for-already-charged-merchants|PCI generate invoices for already charged merchants]] — op `?`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Get merchants for QB" (id `29613070-54eb-461e-a367-9f95da0c6ed4`)
- [[../../workflows/pci-generate-invoices-for-already-charged-merchants|PCI generate invoices for already charged merchants]] — op `?`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Get merchants for QB1" (id `6ce45f8e-3d61-437a-89e5-f6172f03380a`)
- [[../../workflows/pci-generate-invoices-for-already-charged-merchants|PCI generate invoices for already charged merchants]] — op `?`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Get row(s) in sheet" (id `7439bc3f-2ba6-4b4a-8e4d-ed3f204a0631`)
- [[../../workflows/pci-generate-invoices-for-already-charged-merchants|PCI generate invoices for already charged merchants]] — op `update`, tab `={{ $('Entry Point').item.json.spreadsheet_name }}` — node "Google Sheets10" (id `614e627a-00c7-479b-aa4f-4689af9e3ff7`)
- [[../../workflows/pci-generate-invoices-for-already-charged-merchants|PCI generate invoices for already charged merchants]] — op `append`, tab `QB LOGS - CUSTOMERS CREATED` — node "Log Created Customer" (id `30685938-27c0-4771-a3c4-89bbee00ba4d`)
- [[../../workflows/pci-generate-invoices-for-already-charged-merchants|PCI generate invoices for already charged merchants]] — op `append`, tab `QB LOGS - INVOICES` — node "Log Created Invoice" (id `404785b5-e227-4d12-84bf-ce5df2ca1caf`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
