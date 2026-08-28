---
type: http-url
instance: v1
resource_id: "dynamic-host"
current_name: "dynamic-host"
aliases: ["dynamic-host"]
auto_generated_at: 2026-08-19T19:25:44Z
---

<!-- auto:start -->

# dynamic-host

- **Resource id (canonical):** `dynamic-host`
- **Current name:** dynamic-host
- **Host:** `—`

## Used by

- [[../../workflows/alive-ai|Alive AI]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `b3e0efc3-fee2-4402-8a19-e14a3906279d`)
- [[../../workflows/check-elavon-ach-gateway-status-2|Check Elavon ACH gateway status 2]] — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Prod - Get ACH state" (id `3326a9ed-6946-4e5e-a719-5e048052ad40`)
- [[../../workflows/check-elavon-ach-gateway-status-2|Check Elavon ACH gateway status 2]] — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Stage - Get ACH state" (id `5118a558-e1b3-476d-be70-6c0bf4195f75`)
- [[../../workflows/check-elavon-ach-gateway-status|Check Elavon ACH gateway status]] — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Prod - Get ACH state" (id `ae67c7da-35cc-4edd-81ad-718a63b567db`)
- [[../../workflows/check-elavon-ach-gateway-status|Check Elavon ACH gateway status]] — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Stage - Get ACH state" (id `5aa17965-ec99-4a04-83a0-3063af51bea6`)
- [[../../workflows/compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] — `GET {{ $('If compression job finished').item.json.compressionJobLocation }}` — node "Check compression progress" (id `d5896afd-342f-4332-927a-ba714c608ae9`)
- [[../../workflows/compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] — `GET {{ $json.compressedFileURL }}` — node "Download the compressed file" (id `99e75e53-c293-403f-90d8-4d5a28a62bd1`)
- [[../../workflows/compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] — `PUT {{ $json.assetURL }}` — node "Upload Original Asset" (id `8d81116c-a08a-4d68-afe1-820e2148bc61`)
- [[../../workflows/disable-elavon-ach-gateway-for-a-given-merchant|Disable Elavon ACH gateway for a given merchant]] — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Prod - Get ACH state" (id `7d4f7571-f267-4b45-aa97-8495dc9c4774`)
- [[../../workflows/disable-elavon-ach-gateway-for-a-given-merchant|Disable Elavon ACH gateway for a given merchant]] — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Stage - Get ACH state" (id `eefb440e-0106-471c-8a9b-7a208dee9ef6`)
- [[../../workflows/disable-elavon-ach-gateway-for-a-given-merchant|Disable Elavon ACH gateway for a given merchant]] — `PATCH {{ $('Set base URL').item.json.pe_console_base_url }}/api/master/merchants/{{ $('Entry Point').first().json.merchantID }}/gateway/{{ $json.id }}` — node "Prod - Disable ACH1" (id `9f644ab6-6ca2-47d0-aac6-1116bb446ae2`)
- [[../../workflows/disable-elavon-ach-gateway-for-a-given-merchant|Disable Elavon ACH gateway for a given merchant]] — `PATCH {{ $('Set base URL').item.json.pe_console_base_url }}/api/master/merchants/{{ $('Entry Point').first().json.merchantID }}/gateway/{{ $json.id }}` — node "Stage - Disable ACH1" (id `bd78ed8e-34f4-4d80-a3da-a9a730ae4a67`)
- [[../../workflows/dispute-update-console|Dispute - Update Console]] — `PATCH {{ $json.pe_console_base_url }}/api/transaction/{{ $json.transaction_id }}/dispute` — node "Prod Update Transaction" (id `f7dae2d9-ccd8-4765-89bb-29bd1a68a31b`)
- [[../../workflows/dispute-update-console|Dispute - Update Console]] — `PATCH {{ $json.pe_console_base_url }}/api/transaction/{{ $json.transaction_id }}/dispute` — node "Sandbox Staging Update Transaction" (id `ba32c713-3bb4-46af-9070-8ce2f316206e`)
- [[../../workflows/disputes-monitor-v2|Disputes Monitor V2]] — `GET ` — node "1Pass Connect Server" (id `179bc73c-6b43-4cd8-92ef-82e6fd655c85`)
- [[../../workflows/docusign-download-files|DocuSign Download Files]] — `POST {{ $json.token_url }}` — node "JWT to Access Token1" (id `c60817bb-ce8c-4335-9854-3bd594e73ffc`)
- [[../../workflows/edit-curbwaste-statements|Edit Curbwaste statements]] — `GET {{ $json.fileUrl }}` — node "Download the statement" (id `220a4a15-20c5-485a-b443-9d49616ae759`)
- [[../../workflows/elavon-ach-enrollment-project-backup-mar-6-2026|Elavon ACH Enrollment Project - Backup Mar 6, 2026]] — `GET {{ $json.audit_log_url }}` — node "Download AuditLog" (id `07ef7f5d-478b-4e06-a63e-604a68440631`)
- [[../../workflows/elavon-ach-enrollment-project-backup-mar-6-2026|Elavon ACH Enrollment Project - Backup Mar 6, 2026]] — `GET {{ $json.document_url }}` — node "Download Signed File" (id `2655d80f-0f05-430f-86ff-33b188ef29a6`)
- [[../../workflows/elavon-ach-enrollment-project|Elavon ACH Enrollment Project]] — `GET {{ $json.audit_log_url }}` — node "Download AuditLog" (id `3f8a4156-44dd-4412-aade-6ea90aa02935`)
- [[../../workflows/elavon-ach-enrollment-project|Elavon ACH Enrollment Project]] — `GET {{ $json.document_url }}` — node "Download Signed File" (id `642d994a-be62-448a-bb2a-06eefcad682f`)
- [[../../workflows/elavon-dispute|Elavon Dispute]] — `PATCH {{ $json.parameters.pe_console_base_url }}/api/transaction/{{ $json.parameters.transaction_id }}/dispute` — node "PROD Update Transaction" (id `459be85d-ddc5-4bc9-ab41-2c654f1c275e`)
- [[../../workflows/elavon-dispute|Elavon Dispute]] — `PATCH {{ $json.parameters.pe_console_base_url }}/api/transaction/{{ $json.parameters.transaction_id }}/dispute` — node "Sandbox Staging Update Transaction" (id `ea336132-ee9b-4135-ba51-66e7fe8484ca`)
- [[../../workflows/maroo-merchants-upload-in-pe|Maroo - Merchants Upload In PE]] — `PUT {{ $input.first().json.url }}` — node "Update Group" (id `a1aec6a8-10f0-4f07-8299-7a1bbf3754fe`)
- [[../../workflows/my-workflow-3|My workflow 3]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `f54801bd-a6bd-46bb-a581-d481e363c33d`)
- [[../../workflows/my-workflow|My workflow]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `c64249b2-5d55-4ba3-92bd-b04b988d4d9f`)
- [[../../workflows/njord-api|Njord API]] — `POST {{ $json.elavonHost }}/oauth2/client-credentials/v2/token` — node "Elavon Token (D Action)" (id `42348ef5-3a1c-4bd2-b2a6-1f9291c79f41`)
- [[../../workflows/njord-api|Njord API]] — `POST {{ $json.elavonHost }}/oauth2/client-credentials/v2/token` — node "Elavon Token (D Detail)" (id `09a07a65-68db-4b96-a7f5-617196eef422`)
- [[../../workflows/njord-api|Njord API]] — `POST {{ $json.elavonHost }}/oauth2/client-credentials/v2/token` — node "Elavon Token (D Doc)" (id `bc3c9fa0-79a9-4fa9-874c-c8a73eb0d37a`)
- [[../../workflows/njord-api|Njord API]] — `POST {{ $json.elavonHost }}/oauth2/client-credentials/v2/token` — node "Elavon Token (Disputes)" (id `18f4cedc-4060-438b-84cd-56e0737d88f1`)
- [[../../workflows/njord-api|Njord API]] — `POST {{ $json.elavonHost }}/oauth2/client-credentials/v2/token` — node "Elavon Token (M Disputes)" (id `1223b4cc-253c-4e06-bcb6-2b1bdf3c4651`)
- [[../../workflows/pax-device-monitoring-backup-2025-10-25|PAX Device Monitoring backup 2025-10-25]] — `={{ $json.method }} {{ $json.url }}` — node "POST: /passport/loginService Request" (id `c5a5daec-2e35-4c1f-b6b5-a465e6d368fe`)
- [[../../workflows/pax-device-monitoring-bk-2025-10-23-|PAX Device Monitoring (BK-2025-10-23)]] — `={{ $json.method }} {{ $json.url }}` — node "HTTP Request1" (id `b0742a80-27ec-4deb-b8bd-2b3764834b21`)
- [[../../workflows/pax-device-monitoring-bk-2025-10-23-|PAX Device Monitoring (BK-2025-10-23)]] — `GET {{ $json.urlPath }}` — node "HTTP Request" (id `1af727ea-63ca-4ad4-9223-54d4a75adec6`)
- [[../../workflows/pax-device-monitoring-bk-2025-10-23-|PAX Device Monitoring (BK-2025-10-23)]] — `GET {{ $json.urlPath }}` — node "HTTP Request3" (id `fc2c52ec-c9f0-4498-a150-264e0967901e`)
- [[../../workflows/pax-device-monitoring|PAX Device Monitoring]] — `={{ $json.method }} {{ $json.url }}` — node "POST: /passport/loginService Request" (id `87662973-a5d0-4cc6-be74-5930eadf68b5`)
- [[../../workflows/pax-portal-access-token-manager|PAX Portal Access Token Manager]] — `={{ $json.method }} {{ $json.url }}` — node "POST: /passport/loginService Request" (id `8db8da26-64de-4491-a10d-dd2a01dc171c`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `GET {{ $json.resetLink }}` — node "HTTP Request" (id `ba540a33-22c1-46dd-a16b-def4e80bd9d8`)
- [[../../workflows/pci-compliance-manager|PCI Compliance Manager]] — `GET {{ $json.audit_log_url }}` — node "Download AuditLog" (id `ed59f97f-deab-4688-96d6-a6fd40dae100`)
- [[../../workflows/pci-compliance-manager|PCI Compliance Manager]] — `GET {{ $json.document_url }}` — node "Download Documents" (id `a21feb4a-4f26-43fb-9c88-c21eaf781a63`)
- [[../../workflows/pci-compliance-manager|PCI Compliance Manager]] — `GET {{ $json.document_url }}` — node "Download Signed File" (id `d0a9ff79-33ab-4a04-aa8c-444f70273ddc`)
- [[../../workflows/pci-monitoring-LdXwJbJl|PCI Monitoring]] — `GET {{ $json.document_url }}` — node "Download Signed File" (id `5b641278-1a48-4dcd-8791-3de8db24c4bb`)
- [[../../workflows/pci-monitoring-LdXwJbJl|PCI Monitoring]] — `GET {{ $json.documents[0].url }}` — node "Download Signed File1" (id `36f41e15-5c5a-4172-90ab-3c66e19a1e3e`)
- [[../../workflows/pci-monitoring|PCI Monitoring]] — `GET {{ $json.document_url }}` — node "Download Signed File" (id `5b641278-1a48-4dcd-8791-3de8db24c4bb`)
- [[../../workflows/pe-ai-agents|PE AI Agents]] — `=GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `c10865b3-22bb-4e7a-b167-d407b4e2638f`)
- [[../../workflows/pe-mail-scanner|PE Mail Scanner]] — `GET {{ $('Google Drive Trigger').item.json.thumbnailLink }}` — node "Get Thumnail" (id `73abcc73-3be0-45a1-94d7-3a7c69862a56`)
- [[../../workflows/pe-mcp-server-backup-2026-01-06|PE MCP Server - Backup 2026-01-06]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', `The base of the url needs to start with: https://quickbooks.api.intuit.com/v3/company/9341452828840730/{entity}`, 'string') }}` — node "HTTP Request" (id `ebbd9b38-69a7-4d66-930e-e62409dbcbdd`)
- [[../../workflows/pe-mcp-server-backup-2026-01-06|PE MCP Server - Backup 2026-01-06]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "QBO API HTTP Request" (id `019cd99d-cd96-4629-98d8-340629b8adfe`)
- [[../../workflows/pe-mcp-server|PE MCP Server]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', `The base of the url needs to start with: https://quickbooks.api.intuit.com/v3/company/9341452828840730/{entity}`, 'string') }}` — node "HTTP Request" (id `ebbd9b38-69a7-4d66-930e-e62409dbcbdd`)
- [[../../workflows/pe-mcp-server|PE MCP Server]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "QBO API HTTP Request" (id `019cd99d-cd96-4629-98d8-340629b8adfe`)
- [[../../workflows/pe-payments-intelligence-overlay|PE Payments Intelligence Overlay]] — `GET ` — node "HTTP Request1" (id `aca95584-06ca-41e2-9154-834a1f81f699`)
- [[../../workflows/send-supermove-statements|Send Supermove Statements]] — `GET {{ $json.fileUrl }}` — node "Download the statement" (id `ca86647b-bc30-4c6e-a1f4-489b1a28ec1b`)
- [[../../workflows/statement-analyzer-for-shiftagent|Statement Analyzer (for ShiftAgent)]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `502a9f39-6089-485d-8f5d-ec471bdccf49`)
- [[../../workflows/statement-analyzer|Statement Analyzer]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `533cf046-7d2f-425a-9d29-3ca2c66cc8fd`)
- [[../../workflows/token-migration-agent|Token Migration Agent]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `12285966-26a7-47f8-b285-f9731df616e1`)
- [[../../workflows/upload-monthly-ach-statements-to-pe|Upload monthly ACH statements to PE]] — `POST {{ $json.pe_console_base_url }}/api/merchant/{{ $json.resolved_merchant_id }}/statements` — node "PROD Upload Statement" (id `8ae1527b-d453-46ea-a93d-01b5389c1e4a`)
- [[../../workflows/upload-monthly-ach-statements-to-pe|Upload monthly ACH statements to PE]] — `POST {{ $json.pe_console_base_url }}/api/merchant/{{ $json.resolved_merchant_id }}/statements` — node "Sandbox Staging Upload Statements" (id `ece36f1e-b33c-4ae1-a30d-10eb948459ac`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
