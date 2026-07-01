---
n8n_id: "VzmhPP1YuR4bXS8K"
name: "Supermove: Transaction Alerts"
status: active
last_modified: 2025-11-11T17:46:37.488Z
tags: []
fingerprint: "e5b163b603366c4345e14be250bc8baeebab70d2851c940e006331b8c3ce3bfc"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Supermove: Transaction Alerts

## Summary

- **Status:** active
- **n8n ID:** `VzmhPP1YuR4bXS8K`
- **Nodes:** 14
- **Last modified:** 2025-11-11T17:46:37.488Z

## Triggers

- **error** — node "Error Trigger" (id `33813f8b-e4de-491a-9271-3d137b65aa44`)
- **manual** — node "When clicking ‘Execute workflow’" (id `c99970fd-f84a-4380-bbcf-88ca9e4e8685`)
- **schedule** — node "Schedule Trigger" (id `e34e11b7-3e83-492b-aac4-a18599aed7e8`) — `every 1 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres" (id `232ea2a5-16e7-4f26-9c98-affc5eee0e20`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Postgres1" (id `2aba7eb1-cd96-4441-baef-6b6e3b3e2547`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Slack" (id `99883b92-0a89-475a-8fe9-177b9c381ac9`)
- [[../resources/credentials/nuywkwefalsyaavg|Support slack]] (`slackApi`, id `NuyWkwefAlSyAaVg`) — node "Slack1" (id `f1bce854-491d-48b2-8847-c570ab620854`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message5" (id `f63ed7ce-2440-40ce-a48b-e4c996bf3377`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres" (id `232ea2a5-16e7-4f26-9c98-affc5eee0e20`)
- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Postgres1" (id `2aba7eb1-cd96-4441-baef-6b6e3b3e2547`)

### Slack channels

- [[../resources/slack-channels/c072d0nfhd5|supermove-transaction-alerts]] (id `C072D0NFHD5`) — op `channel` — node "Slack" (id `99883b92-0a89-475a-8fe9-177b9c381ac9`)
- [[../resources/slack-channels/c072d0nfhd5|supermove-transaction-alerts]] (id `C072D0NFHD5`) — op `channel` — node "Slack1" (id `f1bce854-491d-48b2-8847-c570ab620854`)
- [[../resources/slack-channels/c09pc6hkhpy|payengine-ai-alerts]] (id `C09PC6HKHPY`) — op `channel` — node "Send a message5" (id `f63ed7ce-2440-40ce-a48b-e4c996bf3377`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
