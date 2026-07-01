---
type: http-url
resource_id: "dynamic-host"
current_name: "dynamic-host"
aliases: ["dynamic-host"]
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# dynamic-host

- **Resource id (canonical):** `dynamic-host`
- **Current name:** dynamic-host
- **Host:** `—`

## Used by

- [[../../workflows/alive-ai|Alive AI]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `b3e0efc3-fee2-4402-8a19-e14a3906279d`)
- [[../../workflows/check-elavon-ach-gateway-status|Check Elavon ACH gateway status]] — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Prod - Get ACH state" (id `e544a98f-d3eb-447b-8d9b-46988137bf32`)
- [[../../workflows/check-elavon-ach-gateway-status|Check Elavon ACH gateway status]] — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Stage - Get ACH state" (id `31a57470-0a71-4a95-a499-65844a0d1f24`)
- [[../../workflows/check-elavon-ach-gateway-status-2|Check Elavon ACH gateway status 2]] — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Prod - Get ACH state" (id `3326a9ed-6946-4e5e-a719-5e048052ad40`)
- [[../../workflows/check-elavon-ach-gateway-status-2|Check Elavon ACH gateway status 2]] — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Stage - Get ACH state" (id `5118a558-e1b3-476d-be70-6c0bf4195f75`)
- [[../../workflows/compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] — `GET {{ $('If compression job finished').item.json.compressionJobLocation }}` — node "Check compression progress" (id `d5896afd-342f-4332-927a-ba714c608ae9`)
- [[../../workflows/compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] — `PUT {{ $json.assetURL }}` — node "Upload Original Asset" (id `8d81116c-a08a-4d68-afe1-820e2148bc61`)
- [[../../workflows/compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] — `GET {{ $json.compressedFileURL }}` — node "Download the compressed file" (id `99e75e53-c293-403f-90d8-4d5a28a62bd1`)
- [[../../workflows/disable-elavon-ach-gateway-for-a-given-merchant|Disable Elavon ACH gateway for a given merchant]] — `PATCH {{ $('Set base URL').item.json.pe_console_base_url }}/api/master/merchants/{{ $('Entry Point').first().json.merchantID }}/gateway/{{ $json.id }}` — node "Prod - Disable ACH" (id `7e9467a1-19e4-4aa4-83ec-72a497950420`)
- [[../../workflows/disable-elavon-ach-gateway-for-a-given-merchant|Disable Elavon ACH gateway for a given merchant]] — `PATCH {{ $('Set base URL').item.json.pe_console_base_url }}/api/master/merchants/{{ $('Entry Point').first().json.merchantID }}/gateway/{{ $json.id }}` — node "Stage - Disable ACH" (id `58d04a8f-ca3f-487f-9f13-3a34815f5d8e`)
- [[../../workflows/disable-elavon-ach-gateway-for-a-given-merchant|Disable Elavon ACH gateway for a given merchant]] — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Prod - Get ACH state" (id `7d4f7571-f267-4b45-aa97-8495dc9c4774`)
- [[../../workflows/disable-elavon-ach-gateway-for-a-given-merchant|Disable Elavon ACH gateway for a given merchant]] — `GET {{ $json.pe_console_base_url }}/api/master/merchants/{{ $json.merchantID }}/gateway` — node "Stage - Get ACH state" (id `eefb440e-0106-471c-8a9b-7a208dee9ef6`)
- [[../../workflows/dispute-update-console|Dispute - Update Console]] — `PATCH {{ $json.pe_console_base_url }}/api/transaction/{{ $json.transaction_id }}/dispute` — node "Prod Update Transaction" (id `f7dae2d9-ccd8-4765-89bb-29bd1a68a31b`)
- [[../../workflows/dispute-update-console|Dispute - Update Console]] — `PATCH {{ $json.pe_console_base_url }}/api/transaction/{{ $json.transaction_id }}/dispute` — node "Sandbox Staging Update Transaction" (id `ba32c713-3bb4-46af-9070-8ce2f316206e`)
- [[../../workflows/disputes-monitor-v2|Disputes Monitor V2]] — `GET ` — node "1Pass Connect Server" (id `179bc73c-6b43-4cd8-92ef-82e6fd655c85`)
- [[../../workflows/docusign-download-files|DocuSign Download Files]] — `POST {{ $json.token_url }}` — node "JWT to Access Token1" (id `c60817bb-ce8c-4335-9854-3bd594e73ffc`)
- [[../../workflows/elavon-ach-enrollment-project|Elavon ACH Enrollment Project]] — `GET {{ $json.audit_log_url }}` — node "Download AuditLog" (id `3f8a4156-44dd-4412-aade-6ea90aa02935`)
- [[../../workflows/elavon-ach-enrollment-project|Elavon ACH Enrollment Project]] — `GET {{ $json.document_url }}` — node "Download Signed File" (id `642d994a-be62-448a-bb2a-06eefcad682f`)
- [[../../workflows/elavon-dispute|Elavon Dispute]] — `PATCH {{ $json.parameters.pe_console_base_url }}/api/transaction/{{ $json.parameters.transaction_id }}/dispute` — node "PROD Update Transaction" (id `459be85d-ddc5-4bc9-ab41-2c654f1c275e`)
- [[../../workflows/elavon-dispute|Elavon Dispute]] — `PATCH {{ $json.parameters.pe_console_base_url }}/api/transaction/{{ $json.parameters.transaction_id }}/dispute` — node "Sandbox Staging Update Transaction" (id `ea336132-ee9b-4135-ba51-66e7fe8484ca`)
- [[../../workflows/maroo-merchants-upload-in-pe|Maroo - Merchants Upload In PE]] — `PUT {{ $input.first().json.url }}` — node "Update Group" (id `a1aec6a8-10f0-4f07-8299-7a1bbf3754fe`)
- [[../../workflows/my-workflow-3|My workflow 3]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `f54801bd-a6bd-46bb-a581-d481e363c33d`)
- [[../../workflows/pax-device-monitoring|PAX Device Monitoring]] — `={{ $json.method }} {{ $json.url }}` — node "POST: /passport/loginService Request" (id `87662973-a5d0-4cc6-be74-5930eadf68b5`)
- [[../../workflows/pax-portal-access-token-manager|PAX Portal Access Token Manager]] — `={{ $json.method }} {{ $json.url }}` — node "POST: /passport/loginService Request" (id `8db8da26-64de-4491-a10d-dd2a01dc171c`)
- [[../../workflows/pci-compliance-manager|PCI Compliance Manager]] — `GET {{ $json.audit_log_url }}` — node "Download AuditLog" (id `ed59f97f-deab-4688-96d6-a6fd40dae100`)
- [[../../workflows/pci-compliance-manager|PCI Compliance Manager]] — `GET {{ $json.document_url }}` — node "Download Documents" (id `a21feb4a-4f26-43fb-9c88-c21eaf781a63`)
- [[../../workflows/pci-compliance-manager|PCI Compliance Manager]] — `GET {{ $json.document_url }}` — node "Download Signed File" (id `d0a9ff79-33ab-4a04-aa8c-444f70273ddc`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `GET {{ $json.resetLink }}` — node "HTTP Request" (id `ba540a33-22c1-46dd-a16b-def4e80bd9d8`)
- [[../../workflows/pci-monitoring-LdXwJbJl|PCI Monitoring]] — `GET {{ $json.document_url }}` — node "Download Signed File" (id `5b641278-1a48-4dcd-8791-3de8db24c4bb`)
- [[../../workflows/pe-ai-agents|PE AI Agents]] — `=GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `c10865b3-22bb-4e7a-b167-d407b4e2638f`)
- [[../../workflows/pe-mail-scanner|PE Mail Scanner]] — `GET {{ $('Google Drive Trigger').item.json.thumbnailLink }}` — node "Get Thumnail" (id `73abcc73-3be0-45a1-94d7-3a7c69862a56`)
- [[../../workflows/pe-mcp-server|PE MCP Server]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', `The base of the url needs to start with: https://quickbooks.api.intuit.com/v3/company/9341452828840730/{entity}`, 'string') }}` — node "HTTP Request" (id `ebbd9b38-69a7-4d66-930e-e62409dbcbdd`)
- [[../../workflows/pe-mcp-server|PE MCP Server]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "QBO API HTTP Request" (id `019cd99d-cd96-4629-98d8-340629b8adfe`)
- [[../../workflows/pe-payments-intelligence-overlay|PE Payments Intelligence Overlay]] — `GET ` — node "HTTP Request1" (id `aca95584-06ca-41e2-9154-834a1f81f699`)
- [[../../workflows/send-supermove-statements|Send Supermove Statements]] — `GET {{ $json.fileUrl }}` — node "Download the statement" (id `ca86647b-bc30-4c6e-a1f4-489b1a28ec1b`)
- [[../../workflows/statement-analyzer|Statement Analyzer]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `533cf046-7d2f-425a-9d29-3ca2c66cc8fd`)
- [[../../workflows/statement-analyzer-for-shiftagent|Statement Analyzer (for ShiftAgent)]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `502a9f39-6089-485d-8f5d-ec471bdccf49`)
- [[../../workflows/token-migration-agent|Token Migration Agent]] — `GET {{ /*n8n-auto-generated-fromAI-override*/ $fromAI('URL', ``, 'string') }}` — node "HTTP Request" (id `12285966-26a7-47f8-b285-f9731df616e1`)
- [[../../workflows/upload-monthly-ach-statements-to-pe|Upload monthly ACH statements to PE]] — `POST {{ $json.pe_console_base_url }}/api/merchant/{{ $json.resolved_merchant_id }}/statements` — node "PROD Upload Statement" (id `8ae1527b-d453-46ea-a93d-01b5389c1e4a`)
- [[../../workflows/upload-monthly-ach-statements-to-pe|Upload monthly ACH statements to PE]] — `POST {{ $json.pe_console_base_url }}/api/merchant/{{ $json.resolved_merchant_id }}/statements` — node "Sandbox Staging Upload Statements" (id `ece36f1e-b33c-4ae1-a30d-10eb948459ac`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
