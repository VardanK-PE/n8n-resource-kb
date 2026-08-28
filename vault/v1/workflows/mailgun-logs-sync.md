---
n8n_id: "BnWxRDUX9Mj3FK3r"
instance: v1
name: "Mailgun Logs Sync"
status: active
last_modified: 2025-10-20T23:15:00.843Z
tags: []
fingerprint: "609d2572670cf80af623a277bbd5f03e3512b8d09ec90c76378e7f909070fb0e"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Mailgun Logs Sync

## Summary

- **Status:** active
- **n8n ID:** `BnWxRDUX9Mj3FK3r`
- **Nodes:** 8
- **Last modified:** 2025-10-20T23:15:00.843Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `5be68b95-d0f2-493f-a90d-c6c6d30b8432`)
- **schedule** — node "Schedule Trigger" (id `efc0174f-752a-4b8c-8206-38e3ef7a3bf4`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `11399932-369a-48c8-9130-51447423a67e`)
- [[../resources/credentials/0rkewzgnz3b64frq|Mailgun N8N Key]] (`httpBasicAuth`, id `0rkEwZgnz3b64fRq`) — node "HTTP Request" (id `82e7ae48-d89d-485d-98cb-27152f25cc0f`)
- [[../resources/credentials/0rkewzgnz3b64frq|Mailgun N8N Key]] (`httpBasicAuth`, id `0rkEwZgnz3b64fRq`) — node "HTTP Request2" (id `9715376e-6637-433e-b1a1-bcdf57fa00ed`)
- [[../resources/credentials/0rkewzgnz3b64frq|Mailgun N8N Key]] (`httpBasicAuth`, id `0rkEwZgnz3b64fRq`) — node "HTTP Request1" (id `c237643c-b0eb-4bdc-9639-f20e7c11e341`)

### HTTP URLs

- [[../resources/http-urls/api-mailgun-net|api.mailgun.net]] — `POST https://api.mailgun.net/v1/analytics/logs` — node "HTTP Request" (id `82e7ae48-d89d-485d-98cb-27152f25cc0f`)
- [[../resources/http-urls/api-mailgun-net|api.mailgun.net]] — `GET https://api.mailgun.net/v3/console.payengine.co/events?subject=Dispute*&begin={{ $now.minus(5,'days').toSeconds() }}&end={{ $now.toSeconds() }}` — node "HTTP Request2" (id `9715376e-6637-433e-b1a1-bcdf57fa00ed`)
- [[../resources/http-urls/api-mailgun-net|api.mailgun.net]] — `POST https://api.mailgun.net/v1/analytics/logs` — node "HTTP Request1" (id `c237643c-b0eb-4bdc-9639-f20e7c11e341`)

### Google Sheets

- [[../resources/google-sheets/1rk2k0rsptehzw8t3nyx93nrtvwvf3-qax76psbwsboo|Mailgun Logs]] (id `1rk2K0rsptEHzW8T3nYX93NRtVwvF3_qaX76pSbwsbOo`) — op `appendOrUpdate`, tab `logs` — node "Append or update row in sheet" (id `11399932-369a-48c8-9130-51447423a67e`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
