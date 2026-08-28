---
n8n_id: "iKChJ9duWwAOzZHd"
name: "Roverpass Cardmix Analysis"
status: inactive
last_modified: 2025-01-26T00:44:53.700Z
tags: []
fingerprint: "3f27c0b9c22632d121d69942b2d28d4193ff1280767e6e3eb908a9949461f6d8"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Roverpass Cardmix Analysis

## Summary

- **Status:** inactive
- **n8n ID:** `iKChJ9duWwAOzZHd`
- **Nodes:** 8
- **Last modified:** 2025-01-26T00:44:53.700Z

## Triggers

- **manual** — node "When clicking ‘Test workflow’" (id `a58a0d5e-cc61-44c1-8108-c18042306c0e`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "CardsCsv" (id `164d384e-0447-46ae-83c5-95b5a671dce7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `622de011-6a81-4a90-83f9-9a5945621aee`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "BInDataItem" (id `af931085-531d-4e8b-a00c-cc84c22da3de`)

### Google Sheets

- [[../resources/google-sheets/191sd9hdohll6qj8svnzwmhbp4j-lqlntl73tuuiftja|processed_rover_sheet]] (id `191sd9HdoHLL6QJ8SVnzWmhbP4J-LqlnTl73tUuifTJA`) — op `append`, tab `Sheet1` — node "Google Sheets" (id `622de011-6a81-4a90-83f9-9a5945621aee`)
- [[../resources/google-sheets/1zzrcj4nrcxa5dto-3qf97r16uq6iacsre7q8rxdf354|bin-list-data]] (id `1Zzrcj4NrCxa5DtO_3QF97r16uQ6IAcsre7q8Rxdf354`) — op `?`, tab `Sheet1` — node "BInDataItem" (id `af931085-531d-4e8b-a00c-cc84c22da3de`)

### Google Drive

- [[../resources/google-drive/1hzy-pj-ya9engksaec1ben1qpp5swuwd|export_20250124-074540_acct_14xlEpJC8S22x0pR_roverpass_masked_sample.csv]] (`file`, id `1hZy-Pj_Ya9EngkSAEc1ben1Qpp5SwUwD`) — op `download` — node "CardsCsv" (id `164d384e-0447-46ae-83c5-95b5a671dce7`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
