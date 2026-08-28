---
type: google-sheets
instance: v1
resource_id: "1kXKJXQxQ8xYYmtb1mAbdeZPHKrUXamIklwLeqpfwRwM"
current_name: "Elavon BI (mids) snapshots"
aliases: ["Elavon BI (mids) snapshots"]
auto_generated_at: 2026-08-28T21:31:11Z
---

<!-- auto:start -->

# Elavon BI (mids) snapshots

- **Resource id (canonical):** `1kXKJXQxQ8xYYmtb1mAbdeZPHKrUXamIklwLeqpfwRwM`
- **Current name:** Elavon BI (mids) snapshots
- **URL:** https://docs.google.com/spreadsheets/d/1kXKJXQxQ8xYYmtb1mAbdeZPHKrUXamIklwLeqpfwRwM/edit?usp=drivesdk
- **Spreadsheet ID:** `1kXKJXQxQ8xYYmtb1mAbdeZPHKrUXamIklwLeqpfwRwM`

## Used by

- [[../../workflows/generate-a-list-of-pci-non-compliant-merchants|Generate a list of PCI non compliant merchants]] — op `append`, tab `={{ $('Entry Point').first().json.sheet_name }}` — node "Append row in sheet" (id `2084221f-fedc-4367-b63b-cd8fe30d3f2d`)
- [[../../workflows/generate-a-list-of-pci-non-compliant-merchants|Generate a list of PCI non compliant merchants]] — op `remove`, tab `={{ $('Entry Point').first().json.sheet_name }}` — node "Delete sheet" (id `52575859-0fc4-49d7-889f-2e8e43323559`)
- [[../../workflows/generate-a-list-of-pci-non-compliant-merchants|Generate a list of PCI non compliant merchants]] — op `?`, tab `={{ $('Entry Point').first().json.sheet_name }}` — node "Request non compliant active merchants" (id `d484c7d6-68d3-467f-9625-b885ba7daf12`)
- [[../../workflows/generate-a-list-of-pci-non-compliant-merchants|Generate a list of PCI non compliant merchants]] — op `create`, tab `null` — node "Create sheet" (id `77e0731b-66c5-4b24-9d17-2fe9acfd1aaf`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
