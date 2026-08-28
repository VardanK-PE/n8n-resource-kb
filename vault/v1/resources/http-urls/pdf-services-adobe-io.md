---
type: http-url
instance: v1
resource_id: "pdf-services.adobe.io"
current_name: "pdf-services.adobe.io"
aliases: ["pdf-services.adobe.io"]
auto_generated_at: 2026-08-19T19:25:44Z
---

<!-- auto:start -->

# pdf-services.adobe.io

- **Resource id (canonical):** `pdf-services.adobe.io`
- **Current name:** pdf-services.adobe.io
- **Host:** `pdf-services.adobe.io`

## Used by

- [[../../workflows/compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] — `DELETE https://pdf-services.adobe.io/assets/{{ $json.assetID }}` — node "Delete Original Asset" (id `e2af1c16-ae09-44f3-90f2-518949e1526e`)
- [[../../workflows/compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] — `DELETE https://pdf-services.adobe.io/assets/{{ $json.compressedAssetID }}` — node "Delete Compressed Asset" (id `347a96d8-3a35-4edc-b677-0d7b6d23026f`)
- [[../../workflows/compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] — `POST https://pdf-services.adobe.io/assets` — node "Create Asset on Adobe Cloud" (id `adc4537b-8cea-4ddb-a72f-98c5ca45e9e0`)
- [[../../workflows/compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] — `POST https://pdf-services.adobe.io/operation/compresspdf` — node "Start compression job" (id `f9af7549-6015-424a-b2a4-8c4f125c36a1`)
- [[../../workflows/compress-pdf-files-using-adobe-apis|Compress PDF files using Adobe APIs]] — `POST https://pdf-services.adobe.io/token` — node "HTTP Request" (id `a7d30321-c822-4273-8862-67df9f135245`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
