---
n8n_id: "y7XoLOhnEzGYovtj"
name: "Gitbook Auth"
status: active
last_modified: 2025-10-14T22:17:48.018Z
tags: []
fingerprint: "d95b3af7260680fa8c834916b3f9e9ddd8b923af29b6a8b385942e361de92d32"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Gitbook Auth

## Summary

- **Status:** active
- **n8n ID:** `y7XoLOhnEzGYovtj`
- **Nodes:** 37
- **Last modified:** 2025-10-14T22:17:48.018Z

## Triggers

- **form** — node "API Docs Form Trigger" (id `0e0df042-3911-4355-81c2-d2984cea7592`) — GET `db4c5cf2-75e4-4727-990c-6661016d3eaf-old`
- **form** — node "On form submission" (id `2beaa3e3-2ad3-459b-8266-b049114cc300`)
- **form** — node "n8n Form Trigger1" (id `43abfe73-7744-41d5-8dc1-ef02a5beb41b`) — GET `db4c5cf2-75e4-4727-990c-6661016d3rta`
- **webhook** — node "Webhook" (id `4d070c7b-5010-4399-9d92-d4c1fe99c31b`) — GET `357de330-e0d1-43f1-beba-9a3a31fb94e0`
- **form** — node "n8n Form Trigger" (id `95b02452-637a-4994-ad6d-3457a57be988`) — GET `db4c5cf2-75e4-4727-990c-6661016d3eaf-x`
- **webhook** — node "Webhook1" (id `be52bda9-5d8e-4b96-85cd-d0e33962ae5f`) — GET `f59a332c-ad50-455f-8877-5357137a0668`

## Depends on

### Credentials

- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AuthenticatedUser2" (id `1b33689b-45bf-41ac-8ae0-21bf8974f8c2`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "LogUser" (id `4b9d409c-4b09-4ce3-9e39-d647061678a7`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `9ee50b49-523b-4d75-92bc-c095d0d3afd1`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "NotifyPE" (id `baef9ee1-47b3-46f9-a149-33a45d3595c8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AuthenticatedUser" (id `d438cd84-0182-42af-9905-7dbe3e79d598`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "AuthenticatedUser1" (id `d4fed1de-77c0-446d-bd6f-f8d8b708c709`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-dev|console.payengine.dev]] — `POST https://console.payengine.dev/api/user/auth` — node "Check Credentials" (id `3ac9ea38-bce8-43e2-aa3c-e62079e99d80`)
- [[../resources/http-urls/console-payengine-dev|console.payengine.dev]] — `POST https://console.payengine.dev/api/user/auth` — node "HTTP Request" (id `3e3e4669-1edb-4672-9f89-73c591ba1b43`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-aes|n8n-nodes-aes]] — type `n8n-nodes-aes.AES` — node "AES" (id `a61072aa-4f67-49c0-ba06-9cb07bd6bd1e`)

### Google Sheets

- [[../resources/google-sheets/1uaapksyymujoqqrljxypj2ttyrevusdoauqjxr3u31q|N8N Authentication]] (id `1UAAPKSyymUjoQqRLjXYpJ2tTyREvuSDOaUqJXR3u31Q`) — op `append`, tab `logs` — node "AuthenticatedUser2" (id `1b33689b-45bf-41ac-8ae0-21bf8974f8c2`)
- [[../resources/google-sheets/1uaapksyymujoqqrljxypj2ttyrevusdoauqjxr3u31q|N8N Authentication]] (id `1UAAPKSyymUjoQqRLjXYpJ2tTyREvuSDOaUqJXR3u31Q`) — op `append`, tab `logs` — node "LogUser" (id `4b9d409c-4b09-4ce3-9e39-d647061678a7`)
- [[../resources/google-sheets/1uaapksyymujoqqrljxypj2ttyrevusdoauqjxr3u31q|N8N Authentication]] (id `1UAAPKSyymUjoQqRLjXYpJ2tTyREvuSDOaUqJXR3u31Q`) — op `?`, tab `logs` — node "AuthenticatedUser" (id `d438cd84-0182-42af-9905-7dbe3e79d598`)
- [[../resources/google-sheets/1uaapksyymujoqqrljxypj2ttyrevusdoauqjxr3u31q|N8N Authentication]] (id `1UAAPKSyymUjoQqRLjXYpJ2tTyREvuSDOaUqJXR3u31Q`) — op `append`, tab `logs` — node "AuthenticatedUser1" (id `d4fed1de-77c0-446d-bd6f-f8d8b708c709`)

### Slack channels

- [[../resources/slack-channels/c0725s1rwu9|partner-monitoring-alerts]] (id `C0725S1RWU9`) — op `channel` — node "Slack" (id `9ee50b49-523b-4d75-92bc-c095d0d3afd1`)
- [[../resources/slack-channels/c0725s1rwu9|partner-monitoring-alerts]] (id `C0725S1RWU9`) — op `channel` — node "NotifyPE" (id `baef9ee1-47b3-46f9-a149-33a45d3595c8`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
