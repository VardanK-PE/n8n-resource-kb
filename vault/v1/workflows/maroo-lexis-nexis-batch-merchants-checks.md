---
n8n_id: "x5WA6xH0z0STmRh9"
instance: v1
name: "Maroo - Lexis Nexis Batch Merchants Checks"
status: inactive
last_modified: 2025-01-21T13:28:19.980Z
tags: []
fingerprint: "b0c70f2f0c6a8b36205b0724d4ed0ba83ab4ba0a20c19c1f78aab2755f6ae302"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Maroo - Lexis Nexis Batch Merchants Checks

## Summary

- **Status:** inactive
- **n8n ID:** `x5WA6xH0z0STmRh9`
- **Nodes:** 12
- **Last modified:** 2025-01-21T13:28:19.980Z

## Triggers

- **manual** — node "When clicking ‘Test workflow’" (id `6fa90c2a-701f-46fb-9ef9-0022b00ca430`)

## Depends on

### Credentials

- [[../resources/credentials/67fejotk4a3tgz6y|Kafka account]] (`kafka`, id `67fEjoTk4A3tGZ6Y`) — node "Kafka - Api Logs" (id `00cfceab-e7a4-4dc7-8eaa-e3dd3cc57e69`)
- [[../resources/credentials/8tbje6sseoduty6r|Lexis Nexis [PROD]]] (`httpBasicAuth`, id `8tbje6SSeODUtY6r`) — node "HTTP Request" (id `1cb63308-5876-44d6-bd40-41e450e0e892`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `509a001a-1abf-48d9-b3ac-a8fe169ea03c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Output" (id `bbe5c995-a23a-4ff1-af0e-b8a1a4117c97`)

### HTTP URLs

- [[../resources/http-urls/wsonline-seisint-com|wsonline.seisint.com]] — `POST https://wsonline.seisint.com/WsIdentity/BusinessInstantID2?ver_=3.12` — node "HTTP Request" (id `1cb63308-5876-44d6-bd40-41e450e0e892`)
- [[../resources/http-urls/api-ipify-org|api.ipify.org]] — `GET https://api.ipify.org?format=json` — node "WhatIsMyIP" (id `6dc5ebac-a5e6-47c1-bfdc-264522379d26`)

### Google Sheets

- [[../resources/google-sheets/1kyciagn3jbwpyz6-n8gar4-ysjkielebwxmpqxnsos4|PayEngine_data_maroo_filled_v2]] (id `1KycIaGn3jBWPYz6-N8gAr4-ysJKIelEbWxMpqXNSos4`) — op `?`, tab `Add Loc Master Demographics` — node "Google Sheets" (id `509a001a-1abf-48d9-b3ac-a8fe169ea03c`)
- [[../resources/google-sheets/1kyciagn3jbwpyz6-n8gar4-ysjkielebwxmpqxnsos4|PayEngine_data_maroo_filled_v2]] (id `1KycIaGn3jBWPYz6-N8gAr4-ysJKIelEbWxMpqXNSos4`) — op `append`, tab `Output` — node "Output" (id `bbe5c995-a23a-4ff1-af0e-b8a1a4117c97`)

### Kafka topics

- [[../resources/kafka-topics/lexis-nexis-api-logs|lexis_nexis_api_logs]] (`producer`) — node "Kafka - Api Logs" (id `00cfceab-e7a4-4dc7-8eaa-e3dd3cc57e69`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
