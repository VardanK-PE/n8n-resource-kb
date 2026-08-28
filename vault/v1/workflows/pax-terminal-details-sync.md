---
n8n_id: "4ugBRdDoboJ4Uq3e"
name: "PAX Terminal Details Sync"
status: inactive
last_modified: 2026-07-10T13:43:04.122Z
tags: []
fingerprint: "9ae5d6fd0ee8f99fb997cae11cca9628ff1066a11b31ec4814cc6b5567ef728c"
auto_generated_at: 2026-08-19T19:13:32Z
---

<!-- auto:start -->

# PAX Terminal Details Sync

## Summary

- **Status:** inactive
- **n8n ID:** `4ugBRdDoboJ4Uq3e`
- **Nodes:** 21
- **Last modified:** 2026-07-10T13:43:04.122Z

## Triggers

- **execute-workflow** — node "Start" (id `ee453c51-4553-4716-ae4f-9b2aa9756d0e`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `e2b900d0-9103-48ba-a07a-09f3cdae1c24`)

### Google Sheets

- [[../resources/google-sheets/1j5x7fyshienezarsmyizspel4ofqbw40m-34cllz2to|PAX Management]] (id `1J5x7FyshieNEZArSMyIZsPEl4oFQbw40m-34cLlZ2to`) — op `appendOrUpdate`, tab `Devices` — node "Append or update row in sheet" (id `e2b900d0-9103-48ba-a07a-09f3cdae1c24`)

### Data tables (n8n)

- [[../resources/data-tables/exdhb72q9l5gfpis|PAX - Terminal Details]] (id `ExDhB72Q9l5GfPiS`) — op `upsert` — node "Upsert row(s)" (id `8b89f58e-078c-418e-bb7c-a8e3de6c8020`)

### Sub-workflows (Execute Workflow calls)

- [[pax-portal-api-request|PAX Portal API Request]] (n8n_id `T0yGFQaEQnHpmPdt`) — node "GET /terminals/{terminal}" (id `6e60c8fc-b760-4fd7-b69c-4d56ed4009a4`)
- [[pax-portal-api-request|PAX Portal API Request]] (n8n_id `T0yGFQaEQnHpmPdt`) — node "GET /installed-firmware" (id `a9ae5669-168a-4a29-adc4-4f3e966d05d0`)
- [[pax-portal-api-request|PAX Portal API Request]] (n8n_id `T0yGFQaEQnHpmPdt`) — node "GET /param" (id `e514ac11-3dc9-4e51-ac49-ebcfe024aa3d`)
- [[pax-portal-api-request|PAX Portal API Request]] (n8n_id `T0yGFQaEQnHpmPdt`) — node "GET /installed-apks" (id `e7fcf556-538c-478f-9699-042a95bfce82`)

## Used by (workflows)

- [[pax-device-monitoring|PAX Device Monitoring]] — node "Call 'PAX Terminal Details Sync'" (id `6d00218a-9c16-4000-a105-c333f1564369`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
