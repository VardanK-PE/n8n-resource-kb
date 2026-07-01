---
type: http-url
resource_id: "sheets.googleapis.com"
current_name: "sheets.googleapis.com"
aliases: ["sheets.googleapis.com"]
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# sheets.googleapis.com

- **Resource id (canonical):** `sheets.googleapis.com`
- **Current name:** sheets.googleapis.com
- **Host:** `sheets.googleapis.com`

## Used by

- [[../../workflows/financial-tracker|Financial Tracker]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $json.file_id }}?includeGridData=false ` — node "Get Sheets" (id `686164f1-bf75-432e-b2b3-372cbd63a274`)
- [[../../workflows/maroo-onboarding-job-update-google-sheet-v2|Maroo Onboarding Job - Update Google Sheet v2]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $json.id }}` — node "HTTP Request2" (id `64daad7d-5805-4d2f-bfdb-9eb469e44fea`)
- [[../../workflows/maroo-onboarding-job-update-google-sheet-v2|Maroo Onboarding Job - Update Google Sheet v2]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $json.spreadsheetID }}:batchUpdate` — node "Add Locks (All)" (id `cc2474fe-f0c3-459a-b343-0458876ff135`)
- [[../../workflows/maroo-onboarding-job-update-google-sheet-v2|Maroo Onboarding Job - Update Google Sheet v2]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $json.spreadsheetID }}:batchUpdate` — node "Add Single Lock" (id `f69c9b65-e368-47e1-8737-4399d346d9f2`)
- [[../../workflows/maroo-onboarding-job-update-google-sheet-v2|Maroo Onboarding Job - Update Google Sheet v2]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $json.spreadsheetID }}:batchUpdate` — node "Remove Locks" (id `617aa8ff-aeb1-4980-87f7-556010652414`)
- [[../../workflows/residuals-generator-v4-2024-05-05|Residuals Generator V4 (2024-05-05)]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs:batchUpdate` — node "HTTP Request" (id `8da39847-be96-4e85-b8af-6d944a98cebb`)
- [[../../workflows/residuals-generator-v4-2024-05-05|Residuals Generator V4 (2024-05-05)]] — `GET https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs?includeGridData=false` — node "HTTP Request2" (id `2bb47846-d83d-4d28-8baf-62f255c04874`)
- [[../../workflows/residuals-generator-v4-2024-05-05|Residuals Generator V4 (2024-05-05)]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1UNyfPl1I1IFSfVMVMSw5wEXMVqDxKj6CJzBZYlPVvAQ:batchUpdate` — node "HTTP Request5" (id `4070c02f-760c-449c-9d2f-1b03f571924c`)
- [[../../workflows/residuals-generator-v4-2024-05-05|Residuals Generator V4 (2024-05-05)]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get MerchantDetailReport.dat').all()[0].json.spreadsheetId }}?includeGridData=false ` — node "HTTP Request3" (id `6a227ebe-e416-4b33-8e06-3d21dae1bfe6`)
- [[../../workflows/residuals-generator-v4-2024-05-05|Residuals Generator V4 (2024-05-05)]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').all()[0].json.spreadsheetId }}:batchUpdate ` — node "HTTP Request4" (id `90326b4a-1459-4d0f-bda1-9cfd215a5431`)
- [[../../workflows/residuals-generator-v4-2024-05-05|Residuals Generator V4 (2024-05-05)]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').first().json.spreadsheetId }}:batchUpdate ` — node "HTTP Request6" (id `8b72ebba-959a-4c1a-91a0-e6a8e73b5136`)
- [[../../workflows/residuals-generator-v5-active-latest-2024-10-17-inactivenow|Residuals Generator V5 (ACTIVE) (latest 2024-10-17) INACTIVENOW]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs:batchUpdate` — node "HTTP Request" (id `5241a048-4423-4c61-a26a-745d1508ab3a`)
- [[../../workflows/residuals-generator-v5-active-latest-2024-10-17-inactivenow|Residuals Generator V5 (ACTIVE) (latest 2024-10-17) INACTIVENOW]] — `GET https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs?includeGridData=false` — node "HTTP Request2" (id `977ba77b-8797-4571-9581-78671499f75c`)
- [[../../workflows/residuals-generator-v5-active-latest-2024-10-17-inactivenow|Residuals Generator V5 (ACTIVE) (latest 2024-10-17) INACTIVENOW]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1UNyfPl1I1IFSfVMVMSw5wEXMVqDxKj6CJzBZYlPVvAQ:batchUpdate` — node "HTTP Request5" (id `54363418-9061-4a31-875e-80ef6255a699`)
- [[../../workflows/residuals-generator-v5-active-latest-2024-10-17-inactivenow|Residuals Generator V5 (ACTIVE) (latest 2024-10-17) INACTIVENOW]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get MerchantDetailReport.dat').all()[0].json.spreadsheetId }}?includeGridData=false ` — node "HTTP Request3" (id `c3126941-5a14-4485-b908-857e19345aa7`)
- [[../../workflows/residuals-generator-v5-active-latest-2024-10-17-inactivenow|Residuals Generator V5 (ACTIVE) (latest 2024-10-17) INACTIVENOW]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').all()[0].json.spreadsheetId }}:batchUpdate ` — node "HTTP Request4" (id `88c36aaf-4c38-450a-85a8-6483e6081360`)
- [[../../workflows/residuals-generator-v5-active-latest-2024-10-17-inactivenow|Residuals Generator V5 (ACTIVE) (latest 2024-10-17) INACTIVENOW]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').first().json.spreadsheetId }}:batchUpdate ` — node "HTTP Request6" (id `b9f31a55-2821-475f-99aa-bc0f9cda59f7`)
- [[../../workflows/residuals-generator-v5-yumna-dev-latest-2025-01-31|Residuals Generator V5 (Yumna Dev) (latest 2025-01-31)]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs:batchUpdate` — node "HTTP Request" (id `28983bbf-4358-43b2-8735-4c987209cb25`)
- [[../../workflows/residuals-generator-v5-yumna-dev-latest-2025-01-31|Residuals Generator V5 (Yumna Dev) (latest 2025-01-31)]] — `GET https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs?includeGridData=false` — node "HTTP Request2" (id `476702a7-0004-409d-9eec-c1eda03638fa`)
- [[../../workflows/residuals-generator-v5-yumna-dev-latest-2025-01-31|Residuals Generator V5 (Yumna Dev) (latest 2025-01-31)]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1UNyfPl1I1IFSfVMVMSw5wEXMVqDxKj6CJzBZYlPVvAQ:batchUpdate` — node "HTTP Request5" (id `12311d3b-3349-49d9-b869-d9196ca544fc`)
- [[../../workflows/residuals-generator-v5-yumna-dev-latest-2025-01-31|Residuals Generator V5 (Yumna Dev) (latest 2025-01-31)]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get MerchantDetailReport.dat').all()[0].json.spreadsheetId }}?includeGridData=false ` — node "HTTP Request3" (id `941c3230-7d7c-425a-b243-4df827fb672b`)
- [[../../workflows/residuals-generator-v5-yumna-dev-latest-2025-01-31|Residuals Generator V5 (Yumna Dev) (latest 2025-01-31)]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').all()[0].json.spreadsheetId }}:batchUpdate ` — node "HTTP Request4" (id `ef94b997-a6cb-451a-81c1-883a8d2c453d`)
- [[../../workflows/residuals-generator-v5-yumna-dev-latest-2025-01-31|Residuals Generator V5 (Yumna Dev) (latest 2025-01-31)]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').first().json.spreadsheetId }}:batchUpdate ` — node "HTTP Request6" (id `88716889-5fc8-47e0-986c-f5a28133ca25`)
- [[../../workflows/residuals-generator-v6-active-latest-2026-06-01|Residuals Generator V6 (ACTIVE) (latest 2026-06-01)]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs:batchUpdate` — node "HTTP Request" (id `b12d2fc4-32ac-4f49-afe0-232448cd5897`)
- [[../../workflows/residuals-generator-v6-active-latest-2026-06-01|Residuals Generator V6 (ACTIVE) (latest 2026-06-01)]] — `GET https://sheets.googleapis.com/v4/spreadsheets/1MElfsHjOe4rrk3VG6BPyo390z9_BC8bcdIuPugQKqHs?includeGridData=false` — node "HTTP Request2" (id `c60128d9-d45e-4b25-b198-ad42164af506`)
- [[../../workflows/residuals-generator-v6-active-latest-2026-06-01|Residuals Generator V6 (ACTIVE) (latest 2026-06-01)]] — `POST https://sheets.googleapis.com/v4/spreadsheets/1UNyfPl1I1IFSfVMVMSw5wEXMVqDxKj6CJzBZYlPVvAQ:batchUpdate` — node "HTTP Request5" (id `104c1ab3-e2cf-4ba6-a635-edea7b94e706`)
- [[../../workflows/residuals-generator-v6-active-latest-2026-06-01|Residuals Generator V6 (ACTIVE) (latest 2026-06-01)]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get Master Spreadsheet ID').first().json.id }}?includeGridData=false ` — node "HTTP Request3" (id `936f2bfa-1ae6-4c86-87f3-072ad508c173`)
- [[../../workflows/residuals-generator-v6-active-latest-2026-06-01|Residuals Generator V6 (ACTIVE) (latest 2026-06-01)]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $('Get Master Spreadsheet ID').item.json.id }}?fields=sheets(properties(title,sheetId)) ` — node "Get MerchantDetails Sheet Details" (id `e00b2888-4fb5-4a39-b412-f07c697ed289`)
- [[../../workflows/residuals-generator-v6-active-latest-2026-06-01|Residuals Generator V6 (ACTIVE) (latest 2026-06-01)]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').all()[0].json.spreadsheetId }}:batchUpdate ` — node "HTTP Request4" (id `74953663-ee56-4ca1-b56f-491e6d4bb364`)
- [[../../workflows/residuals-generator-v6-active-latest-2026-06-01|Residuals Generator V6 (ACTIVE) (latest 2026-06-01)]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $('Google Sheets5').first().json.spreadsheetId }}:batchUpdate ` — node "HTTP Request6" (id `c89e8e3f-a7a7-4ee4-8013-f3d904ea9460`)
- [[../../workflows/sandbox-live-maroo-testing|Sandbox Live - Maroo Testing]] — `GET https://sheets.googleapis.com/v4/spreadsheets/{{ $json.id }}` — node "HTTP Request2" (id `dea6e1b1-f4f8-4ec0-b924-be44b1929b6c`)
- [[../../workflows/sandbox-live-maroo-testing|Sandbox Live - Maroo Testing]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $json.spreadsheetID }}:batchUpdate` — node "Add Locks (All)" (id `19b13de5-89f8-4417-917b-b596336467cf`)
- [[../../workflows/sandbox-live-maroo-testing|Sandbox Live - Maroo Testing]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $json.spreadsheetID }}:batchUpdate` — node "Add Single Lock" (id `82ff354a-6fa1-43f4-b549-2cc9d4e9a43d`)
- [[../../workflows/sandbox-live-maroo-testing|Sandbox Live - Maroo Testing]] — `POST https://sheets.googleapis.com/v4/spreadsheets/{{ $json.spreadsheetID }}:batchUpdate` — node "Remove Locks" (id `c51eb38a-6513-4e22-9fbb-6546eacb24f1`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
