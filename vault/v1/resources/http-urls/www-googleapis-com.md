---
type: http-url
instance: v1
resource_id: "www.googleapis.com"
current_name: "www.googleapis.com"
aliases: ["www.googleapis.com"]
auto_generated_at: 2026-08-19T19:25:44Z
---

<!-- auto:start -->

# www.googleapis.com

- **Resource id (canonical):** `www.googleapis.com`
- **Current name:** www.googleapis.com
- **Host:** `www.googleapis.com`

## Used by

- [[../../workflows/pe-mail-scanner|PE Mail Scanner]] — `GET https://www.googleapis.com/drive/v3/files/18D5BFZPJOPdhbqkYL-SdaXg3Sz738n2-?fields=*` — node "HTTP Request1" (id `e8290f23-aaf9-4bd0-bb6e-e917601e0edc`)
- [[../../workflows/pe-mail-scanner|PE Mail Scanner]] — `GET https://www.googleapis.com/drive/v3/files/{{ $('Google Drive Trigger').item.json.id }}?fields=*` — node "HTTP Request2" (id `84f37c26-9464-45e3-929e-ba29ee080190`)
- [[../../workflows/pe-mail-scanner|PE Mail Scanner]] — `PATCH https://www.googleapis.com/drive/v3/files/{{ $('Google Drive Trigger').item.json.id }}` — node "HTTP Request" (id `8758e1e6-d60f-4b24-b1b3-850a633daa3f`)
- [[../../workflows/pe-payments-intelligence-overlay|PE Payments Intelligence Overlay]] — `GET https://www.googleapis.com/drive/v3/files/1EInFusCRzH3z8GC0fRa4r4hpGeFolnnzklJEPoc5_n8/export?mimeType=text/plain` — node "Instructions for JavaScript Execution Tool" (id `909bfeca-5705-4082-8449-92a920a42fa3`)
- [[../../workflows/vnp-bulk-transactions-processor|VNP Bulk Transactions Processor]] — `POST https://www.googleapis.com/upload/drive/v3/files?uploadType=media` — node "HTTP Request" (id `aeb3402c-c195-4eb6-93d9-c75c629b9282`)
- [[../../workflows/vnp-bulk-transactions-processor|VNP Bulk Transactions Processor]] — `POST https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart` — node "HTTP Request1" (id `df2d4200-1053-46c7-b982-216fae3a0dd7`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
