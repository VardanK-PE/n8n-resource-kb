---
n8n_id: "YZtVohvbVAaUetMH"
instance: v1
name: "Hearth - Elavon Whitelist Merchants"
status: inactive
last_modified: 2025-09-09T14:50:34.664Z
tags: []
fingerprint: "b7f8376ea1a5af315759ccc7aefb620ecf3a7963a95379672fa8237d5963505f"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Hearth - Elavon Whitelist Merchants

## Summary

- **Status:** inactive
- **n8n ID:** `YZtVohvbVAaUetMH`
- **Nodes:** 6
- **Last modified:** 2025-09-09T14:50:34.664Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `3cddd61a-5be2-42c3-ab22-a4e2b438e058`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Get merchant data" (id `16d23c69-8fdf-4500-bae0-d891dc44346f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `2c35670e-51b5-455a-91ad-53a884701547`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `a0186fbf-2313-4951-a08e-3564c80084a7`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Get merchant data" (id `16d23c69-8fdf-4500-bae0-d891dc44346f`)

### Google Sheets

- [[../resources/google-sheets/1iqpxv6r46oarrittb7zvuwa6zjntkyimagjq6aerpj0|Hearth - Elavon Whitelist Merchants (Aug 2025)]] (id `1IqpXV6R46OaRRitTb7ZvuWa6ZJntKyIMagJQ6aerpj0`) — op `?`, tab `Copy of Aug 2025` — node "Get row(s) in sheet" (id `2c35670e-51b5-455a-91ad-53a884701547`)
- [[../resources/google-sheets/1iqpxv6r46oarrittb7zvuwa6zjntkyimagjq6aerpj0|Hearth - Elavon Whitelist Merchants (Aug 2025)]] (id `1IqpXV6R46OaRRitTb7ZvuWa6ZJntKyIMagJQ6aerpj0`) — op `update`, tab `Copy of Aug 2025` — node "Update row in sheet" (id `a0186fbf-2313-4951-a08e-3564c80084a7`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
