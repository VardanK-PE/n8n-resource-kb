---
n8n_id: "1jDrShgq2CNgU8z9"
instance: v1
name: "OpsInternalBot - Token Inport Job"
status: inactive
last_modified: 2026-05-13T11:55:26.991Z
tags: []
fingerprint: "676f949e3481f56ad6086ee61a14a52d5f1fbc828d15221068daa1e583a0cb0c"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# OpsInternalBot - Token Inport Job

## Summary

- **Status:** inactive
- **n8n ID:** `1jDrShgq2CNgU8z9`
- **Nodes:** 52
- **Last modified:** 2026-05-13T11:55:26.991Z

## Triggers

- **schedule** — node "Schedule Trigger" (id `6957f49a-de94-4a74-a5bd-9a688fd465d9`) — `every 10 minute(s)`
- **manual** — node "When clicking ‘Execute workflow’" (id `86e170de-5b80-4df5-841b-d5e9a7346417`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `d4bfb0b4-af9f-4266-b0f7-836006f0aa40`)

## Depends on

### Credentials

- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message3" (id `0e732aa3-1aae-44a6-9614-6c96aa8028ec`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message4" (id `21bb16d8-dd38-47c5-9d2b-7c1b852a3ea6`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message1" (id `28c17727-45a9-4088-a14e-e91e1d778203`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message" (id `319a664c-aa10-44d0-a24e-da194ee6f6fd`)
- [[../resources/credentials/vjyobgaeh30bqna6|n8nio-pg]] (`n8nApi`, id `vJyOBgaEh30bQnA6`) — node "Deactivate a workflow1" (id `44c97e18-37d9-4586-91ac-38e2ae10510b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create sheet" (id `79d5299d-1d9d-4449-93ac-55927cb6e2cd`)
- [[../resources/credentials/vjyobgaeh30bqna6|n8nio-pg]] (`n8nApi`, id `vJyOBgaEh30bQnA6`) — node "Deactivate a workflow" (id `82ec134a-de49-4623-9f5b-6ff88f88c222`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `9055ea1b-00d0-4d18-838a-145b42d74adc`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message5" (id `a7f1b6ad-7215-4d63-affa-12222007048d`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message2" (id `b95f0cf4-b819-4cb6-af57-4f1745a8ef56`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `dd013a82-74d9-43dd-8bea-88c42d4bc0f1`)
- [[../resources/credentials/fj6zpoz0wgka4qq9|OpsInternalBot]] (`slackApi`, id `Fj6zPoZ0Wgka4qq9`) — node "Send a message6" (id `f3665410-a85e-49b0-b15d-22fc6400981f`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Request Tokens cards" (id `ffdbe18e-cb0f-4f39-9715-31e0070c4b22`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `POST https://console.payengine.co/api/payment/sale` — node "HTTP Request1" (id `c3d2bced-385d-489b-979e-4fda302f4264`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Request Tokens cards" (id `ffdbe18e-cb0f-4f39-9715-31e0070c4b22`)

### LLM models

- [[../resources/llm-models/anthropic-claude-sonnet-4-6|anthropic / claude-sonnet-4-6]] — node "Anthropic Chat Model" (id `dd013a82-74d9-43dd-8bea-88c42d4bc0f1`)

### Google Sheets

- [[../resources/google-sheets/1w89aqxd3w7tm-i48dxiewtizwwhtvqoowyco40469jg|PE Token validation by JobID]] (id `1w89Aqxd3W7tm_I48dxieWTiZWWHTvqOOWyco40469Jg`) — op `create`, tab `null` — node "Create sheet" (id `79d5299d-1d9d-4449-93ac-55927cb6e2cd`)
- [[../resources/google-sheets/1w89aqxd3w7tm-i48dxiewtizwwhtvqoowyco40469jg|PE Token validation by JobID]] (id `1w89Aqxd3W7tm_I48dxieWTiZWWHTvqOOWyco40469Jg`) — op `appendOrUpdate`, tab `231b69aa-eedd-41cf-b10d-64c9da2f8191` — node "Append or update row in sheet" (id `9055ea1b-00d0-4d18-838a-145b42d74adc`)

### Data tables (n8n)

- [[../resources/data-tables/kwmbpbzr2l8wthsj|Token Auth - PE Token validation by JobID]] (id `KwMbpbZr2L8wThSj`) — op `upsert` — node "Upsert row(s)" (id `08251670-c3c1-4f96-bdda-260f5ecbd5c3`)
- [[../resources/data-tables/kwmbpbzr2l8wthsj|Token Auth - PE Token validation by JobID]] (id `KwMbpbZr2L8wThSj`) — op `deleteRows` — node "Delete row(s)" (id `391be9d2-cfe1-4976-a42d-002a2cd3bf8c`)
- [[../resources/data-tables/kwmbpbzr2l8wthsj|Token Auth - PE Token validation by JobID]] (id `KwMbpbZr2L8wThSj`) — op `get` — node "Get row(s)2" (id `693becf1-70ac-4ce1-b01e-6c841d25ac3e`)
- [[../resources/data-tables/kwmbpbzr2l8wthsj|Token Auth - PE Token validation by JobID]] (id `KwMbpbZr2L8wThSj`) — op `get` — node "Get row(s)1" (id `97466f2d-5ff7-4861-bcfb-d47fb65d6b4b`)
- [[../resources/data-tables/kwmbpbzr2l8wthsj|Token Auth - PE Token validation by JobID]] (id `KwMbpbZr2L8wThSj`) — op `update` — node "Update row(s)1" (id `9b0a3abc-4ef1-4d23-811d-6cb177cd64a2`)
- [[../resources/data-tables/kwmbpbzr2l8wthsj|Token Auth - PE Token validation by JobID]] (id `KwMbpbZr2L8wThSj`) — op `update` — node "Update row(s)" (id `afa0f86a-b007-42d5-97eb-3d8246eb856b`)
- [[../resources/data-tables/kwmbpbzr2l8wthsj|Token Auth - PE Token validation by JobID]] (id `KwMbpbZr2L8wThSj`) — op `get` — node "Get row(s)" (id `e710caea-805b-49be-8686-243ea4721ca0`)
- [[../resources/data-tables/kwmbpbzr2l8wthsj|Token Auth - PE Token validation by JobID]] (id `KwMbpbZr2L8wThSj`) — op `upsert` — node "Upsert row(s)1" (id `efe622fd-0f5c-4a25-ad96-923417d9e7b9`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Send a message3" (id `0e732aa3-1aae-44a6-9614-6c96aa8028ec`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `21bb16d8-dd38-47c5-9d2b-7c1b852a3ea6`)
- *(dynamic channel)* — op `channel` — node "Send a message1" (id `28c17727-45a9-4088-a14e-e91e1d778203`)
- *(dynamic channel)* — op `channel` — node "Send a message" (id `319a664c-aa10-44d0-a24e-da194ee6f6fd`)
- *(dynamic channel)* — op `channel` — node "Send a message5" (id `a7f1b6ad-7215-4d63-affa-12222007048d`)
- *(dynamic channel)* — op `channel` — node "Send a message2" (id `b95f0cf4-b819-4cb6-af57-4f1745a8ef56`)
- *(dynamic channel)* — op `channel` — node "Send a message6" (id `f3665410-a85e-49b0-b15d-22fc6400981f`)

## Used by (workflows)

- [[opsinternalbot-main|OpsInternalBot - Main]] — node "Call 'OpsInternalBot - Token Inport Job'" (id `eb762010-b582-42ac-a0ad-7fa6c69b6a57`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
