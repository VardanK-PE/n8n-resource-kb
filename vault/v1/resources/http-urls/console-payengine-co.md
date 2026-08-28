---
type: http-url
instance: v1
resource_id: "console.payengine.co"
current_name: "console.payengine.co"
aliases: ["console.payengine.co"]
auto_generated_at: 2026-08-19T19:25:44Z
---

<!-- auto:start -->

# console.payengine.co

- **Resource id (canonical):** `console.payengine.co`
- **Current name:** console.payengine.co
- **Host:** `console.payengine.co`

## Used by

- [[../../workflows/billing-check-transaction-status|Billing - Check transaction status]] — `GET https://console.payengine.co/api/merchant/b860f8af-11e9-4146-99b8-a9d75624c0fd/transaction/{{ $json.payment_id }}` — node "HTTP Request" (id `f9cfd66c-8e6a-43d3-a58e-00f381c4346f`)
- [[../../workflows/billing-system-charge-all-merchants|Billing System - Charge All Merchants]] — `POST https://console.payengine.co/api/payment/ach` — node "Perform the Charge" (id `62753ebd-0ba5-47eb-8bf6-7d209db7a828`)
- [[../../workflows/billing-system-charge-merchant|Billing System - Charge Merchant]] — `POST https://console.payengine.co/api/payment/ach` — node "Perform the Charge" (id `01e44b24-97f5-4c3b-b9ae-175ac56da26f`)
- [[../../workflows/charge-pci-non-compliant-merchants|Charge PCI non compliant merchants]] — `POST https://console.payengine.co/api/payment/ach` — node "Perform the Charge" (id `4b2fe7c3-e7f5-40af-ac42-95705e10fa5c`)
- [[../../workflows/edit-curbwaste-statements|Edit Curbwaste statements]] — `GET https://console.payengine.co/api/merchant/{{ $json.id }}/statements?page=1` — node "HTTP Request" (id `a8f7f9fe-dc1c-4f22-9f11-932e7954a198`)
- [[../../workflows/edit-curbwaste-statements|Edit Curbwaste statements]] — `POST https://console.payengine.co/api/merchant/{{ $('Entry Point').item.json.id }}/statements/{{$json.id}}/view` — node "Resolve Statement File URL" (id `ff7311a9-55af-40db-b513-fb69828b8fcd`)
- [[../../workflows/edit-curbwaste-statements|Edit Curbwaste statements]] — `POST https://console.payengine.co/api/merchant/{{ $json.mid }}/statements` — node "PROD Upload Statement" (id `9c7313df-0c22-4afd-a2f6-c9be3804af54`)
- [[../../workflows/forte-gateway-auto-submitter-v2|Forte Gateway Auto-submitter V2]] — `GET https://console.payengine.co/api/master/merchant-onboarding-api-logs/{{ $('Filter4').item.json.pe_merchant_id }}` — node "PE Merchant merchant-onboarding-api-logs" (id `31b23758-51e8-4be6-8141-ae437eb922df`)
- [[../../workflows/forte-gateway-auto-submitter-v2|Forte Gateway Auto-submitter V2]] — `GET https://console.payengine.co/api/master/merchant-onboarding-api-logs/{{ $json.pe_merchant_id }}` — node "PE Merchant merchant-onboarding-api-logs1" (id `6b96fb98-2dd3-4455-96d6-b27b0dc1807a`)
- [[../../workflows/forte-gateway-auto-submitter-v2|Forte Gateway Auto-submitter V2]] — `GET https://console.payengine.co/api/master/merchants/{{ $json.id }}/processor` — node "Get Merchant Processor" (id `95fb6210-cb92-4cc2-bc7a-bf5a99482083`)
- [[../../workflows/forte-gateway-auto-submitter-v2|Forte Gateway Auto-submitter V2]] — `GET https://console.payengine.co/api/master/merchants?page=1&status=submitted_to_pe&sub_status=a&q=&size=100` — node "Get Merchant Details1" (id `e7c25618-7861-46d7-8cb8-69d218ddb623`)
- [[../../workflows/forte-gateway-auto-submitter-v2|Forte Gateway Auto-submitter V2]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details2" (id `674c2f65-d25c-4c8b-ba78-4554bba40438`)
- [[../../workflows/forte-gateway-auto-submitter-v2|Forte Gateway Auto-submitter V2]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details3" (id `4f6d6aa7-6a2e-4f68-9990-71c4be85c948`)
- [[../../workflows/forte-gateway-auto-submitter-v2|Forte Gateway Auto-submitter V2]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details4" (id `51cc12ae-31f2-4f25-99e5-31f1dd5f0c65`)
- [[../../workflows/forte-gateway-auto-submitter-v2|Forte Gateway Auto-submitter V2]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.merchant_id }}/status` — node "Update Merchant Status (Submitted For Underwriting)" (id `c0159c52-641f-4e23-82ec-56b7012adc7c`)
- [[../../workflows/forte-gateway-auto-submitter-v2|Forte Gateway Auto-submitter V2]] — `POST https://console.payengine.co/api/master/merchants/{{ $('Filter4').item.json.pe_merchant_id }}/gateway` — node "Update Merchant Status (Submitted For Underwriting)1" (id `20e3c6ed-6105-4193-b4c5-a33f775e0538`)
- [[../../workflows/forte-gateway-auto-submitter-v2|Forte Gateway Auto-submitter V2]] — `POST https://console.payengine.co/api/master/merchants/{{ $json.data.id }}/processor` — node "Add Forte Processor" (id `cf081004-c8b1-4ed6-8cc7-c44bab0be129`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchant-onboarding-api-logs/{{ $('Filter4').item.json.pe_merchant_id }}` — node "PE Merchant merchant-onboarding-api-logs" (id `fd521c4d-2f94-412c-ab4a-38ad1104da5a`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchant-onboarding-api-logs/{{ $json.pe_merchant_id }}` — node "PE Merchant merchant-onboarding-api-logs1" (id `4a490fef-56b5-4f56-b545-e73129e71ed9`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants/{{ $json.data[0].merchant_id }}/processor` — node "Get Merchant Processor3" (id `9892bb42-3cd0-44fc-89e9-be0a8b53b024`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants/{{ $json.id }}/gateway` — node "Get Merchant Processor2" (id `0c06ce4e-7203-457e-8d8d-c279ffa40a37`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants/{{ $json.id }}/processor` — node "Get Merchant Processor" (id `89bcc04d-d115-4c80-8300-6439747f20b6`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants/{{ $json.id }}/processor` — node "Get Merchant Processor1" (id `bb8d18e3-9eb4-4d6b-933f-90fd12484473`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants/{{ $json.pe_merchant_id }}/gateway
` — node "PE Merchant Gateways" (id `d009137d-2c4c-4a47-ac77-ca138bb0e80f`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants?page=1&status=submitted_to_pe&sub_status=a&account=4c971cc5-4664-4286-8a98-e9e327c768d3&q=&size=100` — node "Get Merchant Details" (id `86362c4a-b42c-48c5-a03d-29f78aafc488`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants?page=1&status=submitted_to_pe&sub_status=a&account=4c971cc5-4664-4286-8a98-e9e327c768d3&q=&size=100` — node "Get Merchant Details1" (id `15a0142e-fdef-4c6b-8b30-4ab09e50b759`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Account Merchants2" (id `c858169b-b4f1-41e6-973d-2246b4f5e85f`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Account Merchants3" (id `f0b2cb59-d720-4e2b-aa42-5427bfe23218`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details2" (id `d61a8dc7-b434-4545-87b5-3710e375a33e`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details3" (id `45e63418-a6e7-4c1b-b94c-34aa50bd3d5b`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details4" (id `c857f13a-4ec8-4598-a619-fcb28b17ba8f`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details5" (id `5d45cd20-cb1d-4b21-b71f-3eb86d017691`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Merchant Details6" (id `aa1dafc5-b4a5-461d-bb13-cd4b8ed6111f`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.merchant_id }}/status` — node "Update Merchant Status (Submitted For Underwriting)" (id `c3284fd1-a476-465c-b36d-6af625d36257`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `POST https://console.payengine.co/api/master/merchants/{{ $('Filter4').item.json.pe_merchant_id }}/gateway` — node "Update Merchant Status (Submitted For Underwriting)1" (id `c2573670-e5bc-4091-9214-f2933ae70919`)
- [[../../workflows/hearth-applications-autosubmitter|Forte Gateway Autosubmitter]] — `POST https://console.payengine.co/api/master/merchants/{{ $json.data.id }}/processor` — node "Add Forte Processor" (id `f26558e9-1129-4abf-80fa-7b8f815341a8`)
- [[../../workflows/hearth-merchant-capabilities-status|Hearth Merchant Capabilities Status]] — `GET https://console.payengine.co/api/master/merchant-onboarding-api-logs/{{ $json.pe_merchant_id }}` — node "PE Merchant merchant-onboarding-api-logs1" (id `ee40a867-4868-4742-a639-a453fc1317e5`)
- [[../../workflows/managed-by-spartak-ai-agent-partner-merchant-bulk-import-sync|[Managed by Spartak AI Agent] Partner Merchant Bulk Import Sync]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $('Create Merchant').item.json.data?.id ?? $('Create Merchant').item.json.id }}/status` — node "Activate Merchant" (id `activate-merchant`)
- [[../../workflows/managed-by-spartak-ai-agent-partner-merchant-bulk-import-sync|[Managed by Spartak AI Agent] Partner Merchant Bulk Import Sync]] — `POST https://console.payengine.co/api/merchant/{{ $json.data?.id ?? $json.id }}/gateways` — node "Create Gateway" (id `create-gateway`)
- [[../../workflows/managed-by-spartak-ai-agent-partner-merchant-bulk-import-sync|[Managed by Spartak AI Agent] Partner Merchant Bulk Import Sync]] — `POST https://console.payengine.co/api/merchant` — node "Create Merchant" (id `create-merchant`)
- [[../../workflows/maroo-merchants-upload-in-pe|Maroo - Merchants Upload In PE]] — `POST https://console.payengine.co/api/merchant` — node "Create PE Merchant" (id `fbb588ef-8e59-49de-9e67-30d145bad946`)
- [[../../workflows/merchant-garnishment-adjustment-job|Merchant Garnishment/Adjustment Job]] — `POST https://console.payengine.co/api/payment/ach-credit` — node "HTTP Request" (id `2231892c-46d4-4712-bb8a-aea66a1a6322`)
- [[../../workflows/monthly-ach-reports-bk-2025-0924|Monthly ACH Reports - bk 2025-0924]] — `POST https://console.payengine.co/api/payment/ach` — node "Perform the Charge" (id `0e0604a7-8d59-4b27-aab1-4f1c0c56f77d`)
- [[../../workflows/monthly-ach-reports|Monthly ACH Reports]] — `POST https://console.payengine.co/api/payment/ach` — node "Perform the Charge" (id `15d8a51a-bede-4ee2-a406-7e23295b1476`)
- [[../../workflows/one-off-blind-credit-api-call-for-curbwaste|One-off Blind Credit API Call for Curbwaste]] — `POST https://console.payengine.co/api/payment/credit` — node "HTTP Request" (id `bb6e65b7-f098-4da0-b78a-8bc86c474f82`)
- [[../../workflows/one-off-capture-api-call-for-corksy|One-off Capture API Call for Corksy]] — `POST https://console.payengine.co/api/payment/void` — node "HTTP Request" (id `537497bc-71ed-4a6b-8b76-f4a0134bdb30`)
- [[../../workflows/opsinternalbot-token-inport-job|OpsInternalBot - Token Inport Job]] — `POST https://console.payengine.co/api/payment/sale` — node "HTTP Request1" (id `c3d2bced-385d-489b-979e-4fda302f4264`)
- [[../../workflows/pe-master-jwt-generator|PE Master JWT Generator]] — `GET https://console.payengine.co/api/master/merchants?page=1&status=submitted_to_pe&sub_status=a&account=4c971cc5-4664-4286-8a98-e9e327c768d3&q=&size=100` — node "Test Master API (get merchants endpoint)" (id `25590fdb-6600-4750-bc6d-6bdb55cc6e12`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `GET https://console.payengine.co/api/master/accounts` — node "Get Accounts" (id `f836f6ae-1d27-47f0-a07f-4e6275f47c9b`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `GET https://console.payengine.co/api/master/accounts` — node "HTTP Request2" (id `d94597f5-db03-4970-99b2-d429da277ca4`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Account Merchants" (id `77aaa210-5009-4169-aac0-5985fb300aab`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `GET https://console.payengine.co/api/master/merchants` — node "Get Account Merchants1" (id `19ffb938-3eca-4a12-89af-ed8797e57434`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `GET https://console.payengine.co/api/merchant/617e0d27-d114-488e-b24e-285f88ffe9dc/logs` — node "Get Merchant Logs" (id `e875be05-13a6-4de6-81ef-d1c7f267e595`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `GET https://console.payengine.co/api/merchant/{{ $json.pe_merchant_id }}` — node "Get Merchant Details" (id `0ce43ab1-bc32-4c88-a022-5d2ec57e71d1`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `GET https://console.payengine.co/api/merchant/{{ $json.pe_merchant_id }}` — node "Get Merchant Details1" (id `b6d41baf-fbbb-4ba2-aa60-a1c6c679e1c3`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `GET https://console.payengine.co/magic?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hc3RlckBwbGF0Zm9ybWZhY3RvcnkuaW8iLCJsb2dpbklkIjoiZkJ0WnVqYm5OQiIsImlhdCI6MTc1NTM1NTI1OCwiZXhwIjoxNzU1MzU1NTU4fQ.aL3alR2hOgF3kYFDRwc8wOcWpgMp2V7Z6O6YlfK7uVM` — node "HTTP Request1" (id `e69a5d85-e147-442a-8d50-828685248795`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `PATCH https://console.payengine.co/api/v2/merchant/2e5bd48a-bce3-4398-af6b-e4bb33a733df/status` — node "Update Status" (id `46cc84e1-0b0a-41f2-9e4c-eb39b86fcc66`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_merchant_id }}/status` — node "Update Merchant Status" (id `6be3ca71-e1f1-47ea-a3a4-2e3cc45dc695`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_merchant_id }}/status` — node "Update Merchant Status1" (id `b333b9ba-c8be-4db4-b275-77fa2895a6a2`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_merchant_id }}/status` — node "Update Merchant Status2" (id `ba6ad241-b92d-44bc-8569-0eff7c2df7f7`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_merchant_id }}/status` — node "Update Merchant Status3" (id `86cbe687-a06a-4133-99f1-1d53690f53e9`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_merchant_id }}/status` — node "Update Status2" (id `119dae85-f74c-488c-af9c-0d8b565a1cba`)
- [[../../workflows/pe-mid-status-scanner|PE Mid Status Scanner]] — `POST https://console.payengine.co/api/user/auth` — node "HTTP Request" (id `db697696-569b-483d-9d27-8bf2b807b7e0`)
- [[../../workflows/send-supermove-statements|Send Supermove Statements]] — `GET https://console.payengine.co/api/merchant/{{ $json['Merchant ID'] }}/statements?page=1` — node "HTTP Request" (id `032ffaf0-f583-4376-bafe-daa7054f282d`)
- [[../../workflows/send-supermove-statements|Send Supermove Statements]] — `POST https://console.payengine.co/api/merchant/{{ $('Workflow Entry').item.json['Merchant ID'] }}/statements/{{$json.id}}/view` — node "Resolve Statement File URL" (id `dec57477-1d74-4932-b66e-d9069bf09d1c`)
- [[../../workflows/vnp-bulk-transactions-processor-bk-2025-11-17|VNP Bulk Transactions Processor BK 2025-11-17]] — `POST https://console.payengine.co/api/payment/sale` — node "Prod Transaction" (id `2dec6fcf-960c-45a1-84db-728f1060b19e`)
- [[../../workflows/vnp-bulk-transactions-processor-bk-2025-11-17|VNP Bulk Transactions Processor BK 2025-11-17]] — `POST https://console.payengine.co/api/payment/sale` — node "Test Transaction" (id `dfd29563-9af2-484e-b93e-82167268f722`)
- [[../../workflows/vnp-bulk-transactions-processor-perform-sale-with-tokenization-single-shot|VNP Bulk Transactions Processor: Perform Sale with Tokenization (Single Shot)]] — `POST https://console.payengine.co/api/payment/sale` — node "Prod Transaction" (id `d4f73964-d3bf-4381-8ef7-fc334223811f`)
- [[../../workflows/vnp-bulk-transactions-processor-perform-sale-with-tokenization|VNP Bulk Transactions Processor: Perform Sale with Tokenization]] — `POST https://console.payengine.co/api/payment/sale` — node "Prod Transaction" (id `87ec4c01-b17d-4b67-9f65-fbcb98923d78`)
- [[../../workflows/vnp-bulk-transactions-processor-perform-sale-with-tokenization|VNP Bulk Transactions Processor: Perform Sale with Tokenization]] — `POST https://console.payengine.co/api/payment/sale` — node "Prod Transaction1" (id `b3bd326a-c50a-4d49-9528-b05defb7bfcd`)
- [[../../workflows/vnp-bulk-transactions-processor|VNP Bulk Transactions Processor]] — `POST https://console.payengine.co/api/payment/sale` — node "Test Transaction" (id `584330b0-e801-49f4-a8b8-99b9caf761f8`)
- [[../../workflows/vnp-related|VNP Related]] — `GET https://console.payengine.co/api/merchant` — node "Get Submerchants1" (id `4a9ca114-9522-41cb-969e-75c674d2432d`)
- [[../../workflows/vnp-related|VNP Related]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $('Get Submerchants2').item.json.pe_mid }}/status` — node "Activate Submerchants3" (id `2864d847-da41-467e-b4e2-b990586ec819`)
- [[../../workflows/vnp-related|VNP Related]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $('Get Submerchants2').item.json.pe_mid }}` — node "Update Descriptor" (id `b332d4be-a50f-470e-8a77-4c23b6816155`)
- [[../../workflows/vnp-related|VNP Related]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.data.id }}` — node "Update Descriptor1" (id `33cd12dc-60a9-4dda-aa4f-eb340cad4624`)
- [[../../workflows/vnp-related|VNP Related]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.id ?? $json.data.id}}/status` — node "Activate Submerchants" (id `09c02269-f82d-4cd7-897b-e6d46128f6dc`)
- [[../../workflows/vnp-related|VNP Related]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_mid }}/status` — node "Activate Submerchants4" (id `fcf1d2ca-908e-48b0-b768-5f5ae21bb83f`)
- [[../../workflows/vnp-related|VNP Related]] — `PATCH https://console.payengine.co/api/v2/merchant/{{ $json.pe_mid }}/status` — node "Set to editing" (id `ba871b45-848e-4971-9fcd-f995197b4f48`)
- [[../../workflows/vnp-related|VNP Related]] — `POST https://console.payengine.co/api/merchant` — node "Create Submerchants" (id `cd966d4a-fd6a-447e-a53f-719b9a69839a`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
