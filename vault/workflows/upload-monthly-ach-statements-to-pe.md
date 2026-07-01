---
n8n_id: "QfCAULmE6RbrUzgY"
name: "Upload monthly ACH statements to PE"
status: inactive
last_modified: 2026-06-01T15:30:30.146Z
tags: []
fingerprint: "703fdc17694a8558f83cd851b2052c676d169d5ee03dd67718dffa4faa8f811c"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Upload monthly ACH statements to PE

## Summary

- **Status:** inactive
- **n8n ID:** `QfCAULmE6RbrUzgY`
- **Nodes:** 31
- **Last modified:** 2026-06-01T15:30:30.146Z

## Triggers

- **error** — node "Error Trigger" (id `39a6e94f-47d9-478c-ab5a-0a3e9f3b3b7e`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `7e496db5-f897-44e2-8afd-06546dca94a4`)
- **manual** — node "When clicking ‘Execute workflow’" (id `d9567ef4-83fb-40c4-9ed4-478052e07dcd`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `19240b29-352e-49ec-9ece-869632e394a9`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Download file" (id `371099ba-367f-497b-b385-888bd64901ef`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `5fa8d63e-5728-4b0f-b527-a0d4b6f0e399`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `86c5aff7-0989-45ee-b8fd-7f94d44a64bc`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "PROD Upload Statement" (id `8ae1527b-d453-46ea-a93d-01b5389c1e4a`)
- [[../resources/credentials/l1fdqv2gyxyjgim6|PE Staging Sandbox]] (`httpBearerAuth`, id `l1fDQv2GYxYjgim6`) — node "Sandbox Staging Upload Statements" (id `ece36f1e-b33c-4ae1-a30d-10eb948459ac`)

### HTTP URLs

- *(dynamic URL)* — `POST {{ $json.pe_console_base_url }}/api/merchant/{{ $json.resolved_merchant_id }}/statements` — node "PROD Upload Statement" (id `8ae1527b-d453-46ea-a93d-01b5389c1e4a`)
- *(dynamic URL)* — `POST {{ $json.pe_console_base_url }}/api/merchant/{{ $json.resolved_merchant_id }}/statements` — node "Sandbox Staging Upload Statements" (id `ece36f1e-b33c-4ae1-a30d-10eb948459ac`)

### Google Sheets

- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `update`, tab `={{ $('Set environment variables').item.json.table_name }}` — node "Update row in sheet" (id `5fa8d63e-5728-4b0f-b527-a0d4b6f0e399`)
- [[../resources/google-sheets/1bnohsexajctaewqvznlu5h3xyq6wedubho9spswgycm|PE ACH TRANSACTION REPORTS]] (id `1bnOhseXAJcTAEWqvznLU5H3xYq6weDubHo9spSWgycM`) — op `?`, tab `={{ $json.table_name }}` — node "Get row(s) in sheet" (id `86c5aff7-0989-45ee-b8fd-7f94d44a64bc`)

### Google Drive

- *(dynamic)* — op `download` — node "Download file" (id `371099ba-367f-497b-b385-888bd64901ef`)

### Slack channels

- [[../resources/slack-channels/c09pc6hkhpy|payengine-ai-alerts]] (id `C09PC6HKHPY`) — op `channel` — node "Send a message5" (id `19240b29-352e-49ec-9ece-869632e394a9`)

### Sub-workflows (Execute Workflow calls)

- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Send success notification" (id `0e76f9c0-99f7-4a0f-abe0-d573e7d1e22a`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Send API failure notification" (id `a16dd925-aecc-409d-956d-1a3bafeda1e5`)
- [[slack-create-a-base-message|Slack - Create a base message]] (n8n_id `VQPaemuwy6FdMa9L`) — node "Create the base message" (id `bf21e4ac-5e06-4287-8be0-a8ea176eee32`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Call 'Slack - Send notification'2" (id `d4f9e62c-c681-4eff-9c63-01b067048dc3`)
- [[slack-send-notification|Slack - Send notification]] (n8n_id `U3EyWwhZtcf2tMh5`) — node "Report on missing ACH table" (id `d9c70f69-76b8-4dc8-9894-b5aec7eff553`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
