---
n8n_id: "bgtif3xylCNUFTdG"
name: "Compress PDF files using Adobe APIs"
status: active
last_modified: 2026-01-02T11:21:23.324Z
tags: []
fingerprint: "99f52d3ce912064de6c2d67cc6220b776f93318c096b9163c5a73e568f1dd378"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Compress PDF files using Adobe APIs

## Summary

- **Status:** active
- **n8n ID:** `bgtif3xylCNUFTdG`
- **Nodes:** 50
- **Last modified:** 2026-01-02T11:21:23.324Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `4d923f34-e609-474b-9bd2-22206cb0be1e`) — `every 1 hour(s)`
- **manual** — node "When clicking ‘Execute workflow’" (id `6294463b-0410-43e2-8a4b-664f84263124`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `6ba13d18-3fb2-453f-9caf-92c2780e0bb7`)

## Depends on

### Credentials

- [[../resources/credentials/wmtlps73qf1sk3am|PE Master JWT Secret]] (`jwtAuth`, id `WMTlps73Qf1Sk3aM`) — node "Extract token data" (id `3ecfd864-1e07-4fdc-a317-4b875fe5b42a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `f20155c6-5f2d-4329-9be3-4dbc42f19355`)

### HTTP URLs

- [[../resources/http-urls/pdf-services-adobe-io|pdf-services.adobe.io]] — `DELETE https://pdf-services.adobe.io/assets/{{ $json.compressedAssetID }}` — node "Delete Compressed Asset" (id `347a96d8-3a35-4edc-b677-0d7b6d23026f`)
- *(dynamic URL)* — `PUT {{ $json.assetURL }}` — node "Upload Original Asset" (id `8d81116c-a08a-4d68-afe1-820e2148bc61`)
- *(dynamic URL)* — `GET {{ $json.compressedFileURL }}` — node "Download the compressed file" (id `99e75e53-c293-403f-90d8-4d5a28a62bd1`)
- [[../resources/http-urls/pdf-services-adobe-io|pdf-services.adobe.io]] — `POST https://pdf-services.adobe.io/token` — node "HTTP Request" (id `a7d30321-c822-4273-8862-67df9f135245`)
- [[../resources/http-urls/pdf-services-adobe-io|pdf-services.adobe.io]] — `POST https://pdf-services.adobe.io/assets` — node "Create Asset on Adobe Cloud" (id `adc4537b-8cea-4ddb-a72f-98c5ca45e9e0`)
- *(dynamic URL)* — `GET {{ $('If compression job finished').item.json.compressionJobLocation }}` — node "Check compression progress" (id `d5896afd-342f-4332-927a-ba714c608ae9`)
- [[../resources/http-urls/pdf-services-adobe-io|pdf-services.adobe.io]] — `DELETE https://pdf-services.adobe.io/assets/{{ $json.assetID }}` — node "Delete Original Asset" (id `e2af1c16-ae09-44f3-90f2-518949e1526e`)
- [[../resources/http-urls/pdf-services-adobe-io|pdf-services.adobe.io]] — `POST https://pdf-services.adobe.io/operation/compresspdf` — node "Start compression job" (id `f9af7549-6015-424a-b2a4-8c4f125c36a1`)

### Google Drive

- *(dynamic)* — op `download` — node "Download file" (id `f20155c6-5f2d-4329-9be3-4dbc42f19355`)

### Data tables (n8n)

- [[../resources/data-tables/msddlofgjd28ebzk|PDF Processor - Pending Jobs]] (id `msDdLoFGJD28EBzK`) — op `deleteRows` — node "Delete row(s)" (id `1fc252d2-d14b-463f-b0fe-bb02037bb2ed`)
- [[../resources/data-tables/msddlofgjd28ebzk|PDF Processor - Pending Jobs]] (id `msDdLoFGJD28EBzK`) — op `?` — node "Create Compression Job ID" (id `4435c37d-f764-432c-be0c-8a801649cac6`)
- [[../resources/data-tables/msddlofgjd28ebzk|PDF Processor - Pending Jobs]] (id `msDdLoFGJD28EBzK`) — op `get` — node "Get row(s)2" (id `55e3c9f9-34c1-489e-a1a4-cccce504b952`)
- [[../resources/data-tables/ge6lmhiugshxlwa3|Dispute - Shared Preferences]] (id `GE6LmHiUGSHxLWA3`) — op `get` — node "Get stored PDF processor token" (id `5f80398f-7b0c-4153-b1d7-4f4c6f2092dd`)
- [[../resources/data-tables/msddlofgjd28ebzk|PDF Processor - Pending Jobs]] (id `msDdLoFGJD28EBzK`) — op `get` — node "Get row(s)1" (id `6b0d7d15-d0bb-4654-a821-5024cd4afb92`)
- [[../resources/data-tables/ge6lmhiugshxlwa3|Dispute - Shared Preferences]] (id `GE6LmHiUGSHxLWA3`) — op `upsert` — node "Update PDF processor token" (id `83ad3045-2d80-47a9-a48a-9cafc808b89a`)
- [[../resources/data-tables/msddlofgjd28ebzk|PDF Processor - Pending Jobs]] (id `msDdLoFGJD28EBzK`) — op `upsert` — node "Upsert compression job queued" (id `bee17c79-ee35-4120-b46c-704968211a46`)
- [[../resources/data-tables/msddlofgjd28ebzk|PDF Processor - Pending Jobs]] (id `msDdLoFGJD28EBzK`) — op `upsert` — node "Upsert compression job finished" (id `c8fd841e-f233-46c0-8980-2b3079e5f818`)
- [[../resources/data-tables/msddlofgjd28ebzk|PDF Processor - Pending Jobs]] (id `msDdLoFGJD28EBzK`) — op `upsert` — node "Upsert compression job timeout" (id `d9f8b407-0d0c-4cf2-8298-0c20a046783a`)
- [[../resources/data-tables/msddlofgjd28ebzk|PDF Processor - Pending Jobs]] (id `msDdLoFGJD28EBzK`) — op `upsert` — node "Upsert original asset created" (id `f7613e14-6bfd-4c52-8b46-f126d0881362`)
- [[../resources/data-tables/msddlofgjd28ebzk|PDF Processor - Pending Jobs]] (id `msDdLoFGJD28EBzK`) — op `upsert` — node "Upsert original file uploaded" (id `f8f22933-765b-4a7a-8085-0c93e00bfc69`)

### Sub-workflows (Execute Workflow calls)

- [[compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] (n8n_id `bgtif3xylCNUFTdG`) — node "Get PDF Processor Token 2" (id `7f21d9e8-73d4-455e-a6f2-9b17056713a3`)
- [[compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] (n8n_id `bgtif3xylCNUFTdG`) — node "Get PDF Processor Token" (id `ad90fb4e-8b64-49bd-b1d1-f74b5b1e697d`)

## Used by (workflows)

- [[compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] — node "Get PDF Processor Token" (id `ad90fb4e-8b64-49bd-b1d1-f74b5b1e697d`)
- [[compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] — node "Get PDF Processor Token 2" (id `7f21d9e8-73d4-455e-a6f2-9b17056713a3`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
