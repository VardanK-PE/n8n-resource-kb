---
type: google-sheets
resource_id: "1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM"
current_name: "FORTE TRANSACTION REPORTS"
aliases: ["FORTE TRANSACTION REPORTS","PE ACH TRANSACTION REPORTS"]
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# FORTE TRANSACTION REPORTS

- **Resource id (canonical):** `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`
- **Current name:** FORTE TRANSACTION REPORTS
- **Historical aliases:**
  - FORTE TRANSACTION REPORTS
  - PE ACH TRANSACTION REPORTS
- **URL:** https://docs.google.com/spreadsheets/d/1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM/edit?usp=drivesdk
- **Spreadsheet ID:** `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`

## Used by

- [[../../workflows/billing-system-generate-invoices-for-billing-period|Billing System - Generate Invoices for Billing Period]] — op `?`, tab `={{ $('Set spreadsheet name').first().json.snapshot_period }}-ALL-AGGREGATE` — node "Get ACH Transactions" (id `6ab626c7-4447-43a5-a821-a0ca83ff1238`)
- [[../../workflows/billing-system-get-merchant-ach-transactions|Billing System - Get merchant ACH transactions]] — op `?`, tab `={{ $('Entry').first().json.period }}-ALL` — node "Get Merchant Transactions" (id `78fa450a-ff70-4df9-a0c8-754d30aec28e`)
- [[../../workflows/billing-system-get-merchant-ach-transactions|Billing System - Get merchant ACH transactions]] — op `?`, tab `={{ $('Entry').item.json.period }}-ALL-AGGREGATE` — node "Get Merchant Aggregated Data" (id `17d0fefc-1b69-4ddd-984f-faa9073a911a`)
- [[../../workflows/check-pci-ach-transaction-status|Check PCI/ACH Transaction Status]] — op `update`, tab `={{ $('Spreadsheet Name1').first().json.spreadsheet_name }}-ALL-AGGREGATE` — node "Update row in sheet1" (id `b377b72b-f614-4337-ac4d-950f6cc5b0ee`)
- [[../../workflows/check-pci-ach-transaction-status|Check PCI/ACH Transaction Status]] — op `?`, tab `={{ $json.spreadsheet_name }}-ALL-AGGREGATE` — node "Get ACH Fees" (id `b400bd0a-797b-4977-8693-e6530bd8b29b`)
- [[../../workflows/locate-failed-transactions-for-canadian-merchant|Locate failed transactions for Canadian merchant]] — op `?`, tab `={{ $json.month }}-ALL-AGGREGATE` — node "Get row(s) in sheet2" (id `fa104d18-ab47-47b2-a7f3-4798f0fadab1`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `?`, tab `2025-07-ALL-AGGREGATE` — node "Get row(s) in sheet5" (id `2e780a86-6215-414a-994b-25201479e733`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `?`, tab `2025-08-ALL-AGGREGATE` — node "Get row(s) in sheet4" (id `8c1b04e6-837c-43ee-81db-5ac402d6d3aa`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `?`, tab `2025-09-ALL-AGGREGATE` — node "Get row(s) in sheet3" (id `16a474bd-02be-4a2e-bb8f-93630d79bbeb`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `update`, tab `={{ $('Entry 4').first().json.month }}-ALL-AGGREGATE` — node "Google Sheets4" (id `19d9f385-72d5-4b4a-9877-9ee5b4f5ba47`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `update`, tab `={{ $('Entry').first().json.month }}-ALL-AGGREGATE` — node "Google Sheets10" (id `9f369faf-bc24-4838-967b-acf2751e1283`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `?`, tab `={{ $('Entry').item.json.month }}-ALL` — node "Get Merchant Transactions" (id `7193b05c-c478-4753-8524-b64cad6b77a9`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `?`, tab `={{ $('Entry').item.json.month }}-ALL-AGGREGATE` — node "Google Sheets8" (id `7ee92533-d06a-4e30-bb7e-3b539734a9b3`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `append`, tab `={{ $('InputFields').first().json["start-date"] }}-ALL-AGGREGATE` — node "Append to Aggregate Data" (id `829996ca-d9c4-4019-bff4-b291519bb21f`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `append`, tab `={{ $('InputFields').item.json["start-date"] }}-ALL` — node "Append to All Transactions" (id `597e6d97-33cc-4a36-bebe-bacd31d0ce16`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `append`, tab `={{ $('InputFields').item.json["start-date"] }}-FORTE` — node "Google Sheets1" (id `669fce6a-2c8a-4f33-91e7-8c8881e3d870`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `update`, tab `={{ $('When clicking ‘Execute workflow’').item.json['start-date'] }}-ALL-AGGREGATE` — node "Update Bank Account Fields" (id `9a1c2530-e51e-4f5c-ae2a-b2fd8a155acc`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `update`, tab `={{ $('When clicking ‘Execute workflow’').item.json['start-date'] }}-ALL-AGGREGATE` — node "Update Transaction Details" (id `d5e0c0cc-398f-45b8-995f-b984dffeed03`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `update`, tab `={{ $('When clicking ‘Execute workflow’').item.json['start-date'] }}-ALL-AGGREGATE` — node "Update Transaction Details1" (id `10f93267-286c-4070-9d2d-934de30650b4`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `update`, tab `={{ $('Workflow Settings').item.json.month }}-ALL-AGGREGATE` — node "Get row(s) in sheet2" (id `d60cd683-4732-464f-9a8c-c169e04b20aa`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `?`, tab `={{ $json.month }}-ALL-AGGREGATE` — node "Google Sheets3" (id `fed6c61c-cbf7-4b0b-bb99-6f15e243535d`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `?`, tab `={{ $json['month'] }}-ALL-AGGREGATE` — node "Get row(s) in sheet1" (id `083a8209-bcdc-412a-8edc-118fcbcdc951`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `?`, tab `={{ $json['start-date'] }}-ALL-AGGREGATE` — node "Get row(s) in sheet" (id `71e74552-063f-43aa-922d-f24b8e1dccd6`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `append`, tab `BANK_ACCOUNT_TOKENS_LOG` — node "Tokens Logs" (id `be22ab14-2791-417a-be30-b34cc559f065`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `appendOrUpdate`, tab `FEE_SCHEDULES` — node "Append or update fee schedule table" (id `5bf59762-943d-4909-9332-9ccada8efab5`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `appendOrUpdate`, tab `FEE_SCHEDULES` — node "Append or update fee schedule table1" (id `eb3fd5f8-6738-416d-8cd1-1f417ca21959`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `?`, tab `FEE_SCHEDULES` — node "Get Fee Schedules" (id `d16181b9-ce7a-46c2-976d-afc35d2c0bdc`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `?`, tab `FEE_SCHEDULES` — node "Parsed Fee Schedules" (id `3e244988-f7a2-4bdf-bb08-6a0777ec56d7`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `append`, tab `PE_FORTE_TRANSACTIONS_LOG` — node "Append row in sheet" (id `eede0d28-edd5-4b10-ac55-e707b0d21456`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `append`, tab `QB LOGS - CUSTOMERS CREATED` — node "Log Created Customer" (id `6d7797bc-2793-41f5-9b1f-4a495a47b95c`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `append`, tab `QB LOGS - CUSTOMERS CREATED` — node "Log Created Customer1" (id `913bfac5-1d60-4069-8200-c69f5f2f877c`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `?`, tab `QB LOGS - INVOICES` — node "Google Sheets6" (id `2f2d6035-1434-4a51-bf28-384f38783e4f`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `append`, tab `QB LOGS - INVOICES` — node "Log Created Invoice" (id `744375ca-85ff-4a6d-9dfb-79cbdc4997e6`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `create`, tab `null` — node "Create Start-Date ALL Sheet" (id `5ea9bb3c-15c8-4a1e-93a6-01d77c5d217f`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `create`, tab `null` — node "Create Start-Date ALL-AGGREGATE Sheet" (id `92b832ae-1380-48da-aa3a-d357e78b4ef4`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — op `create`, tab `null` — node "Google Sheets" (id `1efbcb93-222c-4a2e-aa0e-72fc66363f6d`)
- [[../../workflows/residuals-generator-v6-active-latest-2026-06-01|Residuals Generator V6 (ACTIVE) (latest 2026-06-01)]] — op `?`, tab `={{ $('Get Master Spreadsheet ID').item.json.name.substring(0, 4) }}-{{ $('Get Master Spreadsheet ID').item.json.name.substring(4, 6) }}-ALL-AGGREGATE` — node "All ACH Transactions Report" (id `eed9c8da-3b50-4d06-a3ee-5e4b915eac3e`)
- [[../../workflows/residuals-generator-v6-active-latest-2026-06-01|Residuals Generator V6 (ACTIVE) (latest 2026-06-01)]] — op `?`, tab `={{ $json.name.substring(0, 4) }}-{{ $json.name.substring(4, 6) }}-ALL-AGGREGATE` — node "Get row(s) in sheet2" (id `e2b447b9-8ace-4232-b0d5-f90172823bf2`)
- [[../../workflows/upload-monthly-ach-statements-to-pe|Upload monthly ACH statements to PE]] — op `update`, tab `={{ $('Set environment variables').item.json.table_name }}` — node "Update row in sheet" (id `5fa8d63e-5728-4b0f-b527-a0d4b6f0e399`)
- [[../../workflows/upload-monthly-ach-statements-to-pe|Upload monthly ACH statements to PE]] — op `?`, tab `={{ $json.table_name }}` — node "Get row(s) in sheet" (id `86c5aff7-0989-45ee-b8fd-7f94d44a64bc`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
