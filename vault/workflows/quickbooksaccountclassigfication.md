---
n8n_id: "G6j6pFnZrXgLQkOP"
name: "QuickbooksAccountClassigfication"
status: active
last_modified: 2024-10-25T17:19:01.989Z
tags: []
fingerprint: "589c460992a5b8599757afd7f895abe1b8a972db411e64bdc0791f014fd56753"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# QuickbooksAccountClassigfication

## Summary

- **Status:** active
- **n8n ID:** `G6j6pFnZrXgLQkOP`
- **Nodes:** 7
- **Last modified:** 2024-10-25T17:19:01.989Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `9a8c5746-e3b9-4ec4-a2a9-afea6b004823`) — `daily at 4:51`
- **manual** — node "When clicking "Test workflow"" (id `b4632353-bb23-43f6-89e8-c4ef2bc2fc1f`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets1" (id `079a6378-ab83-4cd5-8455-186e57b0f172`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `5d47a503-3958-4cf4-abab-a5a26e78a443`)
- [[../resources/credentials/fs4w5rzordv3aklr|OpenAi account]] (`openAiApi`, id `fs4w5RZOrDV3aKLr`) — node "OpenAI" (id `ed4fa68d-73e6-4c14-be05-454dda3ef102`)

### LLM models

- [[../resources/llm-models/openai-unspecified|openai / ?]] — node "OpenAI" (id `ed4fa68d-73e6-4c14-be05-454dda3ef102`)

### Google Sheets

- [[../resources/google-sheets/1-dya-w5-bkewms5mn88dew3xz2dwdhuoige04rvzeoq|BrexTransactions]] (id `1-dYa-W5_BkEwMs5mn88deW3xz2DwdHUOige04rvZeOQ`) — op `append`, tab `AIOutput` — node "Google Sheets1" (id `079a6378-ab83-4cd5-8455-186e57b0f172`)
- [[../resources/google-sheets/1-dya-w5-bkewms5mn88dew3xz2dwdhuoige04rvzeoq|BrexTransactions]] (id `1-dYa-W5_BkEwMs5mn88deW3xz2DwdHUOige04rvZeOQ`) — op `?`, tab `QBReady` — node "Google Sheets" (id `5d47a503-3958-4cf4-abab-a5a26e78a443`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
