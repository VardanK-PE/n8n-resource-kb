---
n8n_id: "EakX0ekwO8MImof6"
name: "IC Qual Assessments"
status: inactive
last_modified: 2025-10-24T17:56:22.644Z
tags: []
fingerprint: "07a36394f046d82e1266a99d4b76fb685c2ecfc5e445d40f74c33498f9ff85fe"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# IC Qual Assessments

## Summary

- **Status:** inactive
- **n8n ID:** `EakX0ekwO8MImof6`
- **Nodes:** 5
- **Last modified:** 2025-10-24T17:56:22.644Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `0f38aa4a-3e54-4453-8200-e301d611fb5f`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `2501d4b9-16be-4478-8f42-78247beee20d`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Execute a SQL query" (id `9570f244-e18b-4661-8e98-5aa4f03aa92d`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `f7db99c0-400e-4df4-a200-044c9b98377c`)

### Databases

- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Execute a SQL query" (id `9570f244-e18b-4661-8e98-5aa4f03aa92d`)

### Google Sheets

- [[../resources/google-sheets/1noa2t3kgoqbhi87ep-jvezhpn9l7dlwft-5qi1itrp8|202508-ELAVON_US_1Master]] (id `1noA2t3KGOQBHi87Ep_jveZHpn9l7dlWft_5Qi1iTrp8`) — op `?`, tab `202508_MS0PFORM_ICQualReport.dat` — node "Get row(s) in sheet" (id `2501d4b9-16be-4478-8f42-78247beee20d`)
- [[../resources/google-sheets/1lin7ekligpwkqkoszz-uz4a19geyi4ok1r8dlbnniby|Hearth_ICQual Assessments]] (id `1LiN7EKLIgPWKqkoSzZ_Uz4A19GeYi4Ok1r8dlbNNibY`) — op `appendOrUpdate`, tab `Sheet1` — node "Append or update row in sheet" (id `f7db99c0-400e-4df4-a200-044c9b98377c`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
