---
n8n_id: "IHhwbvnk001UVC3A"
instance: v1
name: "Slack Lists Manager"
status: inactive
last_modified: 2025-09-30T02:54:13.298Z
tags: []
fingerprint: "b4cf6870f2dd9bef14395a3927fd6eb04f6d35883ceab6687de60547f815d52f"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Slack Lists Manager

## Summary

- **Status:** inactive
- **n8n ID:** `IHhwbvnk001UVC3A`
- **Nodes:** 3
- **Last modified:** 2025-09-30T02:54:13.298Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `251cf4d4-1359-470f-ba22-e2b5f8bcc751`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "HTTP Request" (id `2d583080-5f8a-44d1-a125-5f22073150ec`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get a document" (id `3efaa57e-b68b-496c-b561-dcea8664d588`)

### HTTP URLs

- [[../resources/http-urls/slack-com|slack.com]] — `POST https://slack.com/api/slackLists.items.list ` — node "HTTP Request" (id `2d583080-5f8a-44d1-a125-5f22073150ec`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
