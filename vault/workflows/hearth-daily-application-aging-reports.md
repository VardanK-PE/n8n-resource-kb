---
n8n_id: "hSN8aYP7o7OYfGPY"
name: "Hearth - Daily Application Aging Reports"
status: inactive
last_modified: 2025-11-16T08:49:19.233Z
tags: []
fingerprint: "cc8ee8f39bf9c8dca645151124416e09f1911df983f2f6ceef725c487c19139c"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Hearth - Daily Application Aging Reports

## Summary

- **Status:** inactive
- **n8n ID:** `hSN8aYP7o7OYfGPY`
- **Nodes:** 10
- **Last modified:** 2025-11-16T08:49:19.233Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `12d29131-eeb4-4745-86a5-11cafa826ff0`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `9de22428-2f65-47e0-8314-c70683a67b5b`)

## Depends on

### Credentials

- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Send a message" (id `1386fb2f-692a-4aea-922c-ea571e2a3b98`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `a0494fba-272b-4c3a-ab7f-62b0f303589e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet1" (id `f753a8b8-0ebe-4bc1-810c-53c4da9269b4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `fef1da55-d7dd-43e3-a93b-87d4067dba30`)

### Google Sheets

- [[../resources/google-sheets/1l5xrpxmu5n2svnfwsnxrberuic13ni09pbdryzbsrs8|Hearth PayEngine Reports for Elavon]] (id `1L5XrPxmU5n2sVNfwsNxRBEruiC13ni09pBdRyzbSrs8`) — op `appendOrUpdate`, tab `Applications Aging Report` — node "Append or update row in sheet" (id `a0494fba-272b-4c3a-ab7f-62b0f303589e`)
- [[../resources/google-sheets/1p7okrk096r-2g9ikolehdd8baegp4zz-qvslvbwptw|Hearth PayEngine Reports for Hearth]] (id `1P7oKrK096R-2G9IKoLeHdD8BAegP4zz--QvSLVBWptw`) — op `appendOrUpdate`, tab `Applications Aging Report` — node "Append or update row in sheet1" (id `f753a8b8-0ebe-4bc1-810c-53c4da9269b4`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `partnerApplicationsReport` — node "Google Sheets" (id `fef1da55-d7dd-43e3-a93b-87d4067dba30`)

### Slack channels

- [[../resources/slack-channels/c08etnjk6fr|hearth-payengine]] (id `C08ETNJK6FR`) — op `channel` — node "Send a message" (id `1386fb2f-692a-4aea-922c-ea571e2a3b98`)

## Used by (workflows)

- [[elavon-bi-automation-daily-monitor|Elavon BI Automation (Daily Monitor)]] — node "Execute Workflow" (id `7578b694-f52b-4649-a522-f96dec1c6966`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
