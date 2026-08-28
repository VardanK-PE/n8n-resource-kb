---
type: http-url
resource_id: "api.mailgun.net"
current_name: "api.mailgun.net"
aliases: ["api.mailgun.net"]
auto_generated_at: 2026-08-19T19:25:44Z
---

<!-- auto:start -->

# api.mailgun.net

- **Resource id (canonical):** `api.mailgun.net`
- **Current name:** api.mailgun.net
- **Host:** `api.mailgun.net`

## Used by

- [[../../workflows/mailgun-logs-sync|Mailgun Logs Sync]] — `GET https://api.mailgun.net/v3/console.payengine.co/events?subject=Dispute*&begin={{ $now.minus(5,'days').toSeconds() }}&end={{ $now.toSeconds() }}` — node "HTTP Request2" (id `9715376e-6637-433e-b1a1-bcdf57fa00ed`)
- [[../../workflows/mailgun-logs-sync|Mailgun Logs Sync]] — `POST https://api.mailgun.net/v1/analytics/logs` — node "HTTP Request" (id `82e7ae48-d89d-485d-98cb-27152f25cc0f`)
- [[../../workflows/mailgun-logs-sync|Mailgun Logs Sync]] — `POST https://api.mailgun.net/v1/analytics/logs` — node "HTTP Request1" (id `c237643c-b0eb-4bdc-9639-f20e7c11e341`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
