---
n8n_id: "HSEk0Ep12O8S2waU"
instance: v1
name: "Edit Curbwaste statements"
status: inactive
last_modified: 2026-07-13T18:50:30.768Z
tags: []
fingerprint: "f8a1d397c6f425fc5d15c26fb757bf4199d4441c344770d4e11b4be0d0bca226"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# Edit Curbwaste statements

## Summary

- **Status:** inactive
- **n8n ID:** `HSEk0Ep12O8S2waU`
- **Nodes:** 22
- **Last modified:** 2026-07-13T18:50:30.768Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `731da13d-8377-4aff-b08e-46a28ac626c1`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet2" (id `0ce2c4a9-a6c5-4f84-8036-21526f8f12e5`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `3ba51486-a473-4d63-b82d-9440ba5bed6c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `43ac7068-6fbf-4c18-835a-b163fc8ac7e3`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `446490ad-fc5c-4869-be1d-947338d3c00d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet1" (id `50d448d9-db8d-44a6-b403-9ac5f58fd74f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `6c5c75f3-6728-46ac-b188-13e8681b1cba`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "PROD Upload Statement" (id `9c7313df-0c22-4afd-a2f6-c9be3804af54`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "HTTP Request" (id `a8f7f9fe-dc1c-4f22-9f11-932e7954a198`)
- [[../resources/credentials/l1fdqv2gyxyjgim6|PE Staging Sandbox]] (`httpBearerAuth`, id `l1fDQv2GYxYjgim6`) — node "Sandbox Staging Upload Statements" (id `dd08824d-48da-4dba-9fb3-61d6739bb85a`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "Resolve Statement File URL" (id `ff7311a9-55af-40db-b513-fb69828b8fcd`)

### HTTP URLs

- *(dynamic URL)* — `GET {{ $json.fileUrl }}` — node "Download the statement" (id `220a4a15-20c5-485a-b443-9d49616ae759`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/merchant/{{ $json.mid }}/statements` — node "PROD Upload Statement" (id `9c7313df-0c22-4afd-a2f6-c9be3804af54`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/merchant/{{ $json.id }}/statements?page=1` — node "HTTP Request" (id `a8f7f9fe-dc1c-4f22-9f11-932e7954a198`)
- [[../resources/http-urls/staging-sandbox-payengine-dev|staging-sandbox.payengine.dev]] — `POST https://staging-sandbox.payengine.dev/api/merchant/{{ $json.mid }}/statements` — node "Sandbox Staging Upload Statements" (id `dd08824d-48da-4dba-9fb3-61d6739bb85a`)
- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/merchant/{{ $('Entry Point').item.json.id }}/statements/{{$json.id}}/view` — node "Resolve Statement File URL" (id `ff7311a9-55af-40db-b513-fb69828b8fcd`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `446490ad-fc5c-4869-be1d-947338d3c00d`)

### Google Sheets

- [[../resources/google-sheets/1z5aibipob0b3p2hkx4gonucocfqrr0ab1u-n9au4qq8|Curbwaste merchants on Tiered plan]] (id `1z5AibIPOB0B3p2HKX4GoNUCOcFQRr0aB1U_n9aU4qQ8`) — op `update`, tab `Sheet1` — node "Update row in sheet2" (id `0ce2c4a9-a6c5-4f84-8036-21526f8f12e5`)
- [[../resources/google-sheets/1z5aibipob0b3p2hkx4gonucocfqrr0ab1u-n9au4qq8|Curbwaste merchants on Tiered plan]] (id `1z5AibIPOB0B3p2HKX4GoNUCOcFQRr0aB1U_n9aU4qQ8`) — op `update`, tab `Sheet1` — node "Update row in sheet" (id `3ba51486-a473-4d63-b82d-9440ba5bed6c`)
- [[../resources/google-sheets/1z5aibipob0b3p2hkx4gonucocfqrr0ab1u-n9au4qq8|Curbwaste merchants on Tiered plan]] (id `1z5AibIPOB0B3p2HKX4GoNUCOcFQRr0aB1U_n9aU4qQ8`) — op `appendOrUpdate`, tab `Sheet1` — node "Append or update row in sheet" (id `43ac7068-6fbf-4c18-835a-b163fc8ac7e3`)
- [[../resources/google-sheets/1z5aibipob0b3p2hkx4gonucocfqrr0ab1u-n9au4qq8|Curbwaste merchants on Tiered plan]] (id `1z5AibIPOB0B3p2HKX4GoNUCOcFQRr0aB1U_n9aU4qQ8`) — op `update`, tab `Sheet1` — node "Update row in sheet1" (id `50d448d9-db8d-44a6-b403-9ac5f58fd74f`)
- [[../resources/google-sheets/1z5aibipob0b3p2hkx4gonucocfqrr0ab1u-n9au4qq8|Curbwaste merchants on Tiered plan]] (id `1z5AibIPOB0B3p2HKX4GoNUCOcFQRr0aB1U_n9aU4qQ8`) — op `?`, tab `Sheet1` — node "Get row(s) in sheet" (id `6c5c75f3-6728-46ac-b188-13e8681b1cba`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
