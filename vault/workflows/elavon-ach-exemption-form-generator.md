---
n8n_id: "c4rexPHrWGfGDBUP"
name: "Elavon ACH Exemption Form Generator"
status: inactive
last_modified: 2025-09-05T06:09:31.143Z
tags: []
fingerprint: "5161af9a63ecd956e429bc8e2c437ba3e0d9f5b0b293c5310d9bae48f435e5ee"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Elavon ACH Exemption Form Generator

## Summary

- **Status:** inactive
- **n8n ID:** `c4rexPHrWGfGDBUP`
- **Nodes:** 12
- **Last modified:** 2025-09-05T06:09:31.143Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `1334fd16-3ec4-4009-b1b2-2ae58c9cd884`)
- **manual** — node "When clicking ‘Execute workflow’" (id `5dd53776-6028-4b46-9f4a-c915bde796c3`)

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Share file" (id `17289735-7670-4377-b149-2a7916ee0672`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file" (id `1fc27ab0-05ec-4b1f-a945-340491894e63`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive" (id `e9491a42-e1e0-4b84-96bd-53ad4048a3f9`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-pdf-form|n8n-nodes-pdf-form]] — type `n8n-nodes-pdf-form.pdfForm` — node "PDF Form" (id `b171dbb1-f746-4573-bd3e-4fdcca405d31`)

### Google Drive

- *(dynamic)* — op `share` — node "Share file" (id `17289735-7670-4377-b149-2a7916ee0672`)
- [[../resources/google-drive/1mvns6-ys6hp4im42gzbfivexembd-bvn|Elavon Max ACH Exemption Forms]] (`folder`, id `1MvNs6-YS6hp4iM42gZbfIvEXembD-Bvn`) — op `?` — node "Upload file" (id `1fc27ab0-05ec-4b1f-a945-340491894e63`)
- [[../resources/google-drive/11ynpnqojkcnde89ms1hw5idbe0z-ggdy|Elavon - ACH Max Check Exemption Form.pdf]] (`file`, id `11YnpNQOJKCnDE89MS1Hw5IDbE0Z-ggDY`) — op `download` — node "Google Drive" (id `e9491a42-e1e0-4b84-96bd-53ad4048a3f9`)

## Used by (workflows)

- [[elavon-ach-enrollment-project|Elavon ACH Enrollment Project]] — node "Execute Workflow1" (id `40919da8-cbc9-4653-9743-9aa1e218bb45`)
- [[payengineai-bot-v1|PayEngineAI Bot (v1)]] — node "Elavon ECS/ACH Max Check Size Generator" (id `d2654b32-5b57-42e0-9c5b-ad31902dbe5e`)
- [[payengineai-bot-v1-1-feb-26-2026|PayEngineAI Bot (v1.1) - Feb 26 2026]] — node "Elavon ECS/ACH Max Check Size Generator" (id `ce996276-c9a4-4a86-a434-3cde348aa3bc`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
