---
n8n_id: "fMgQKiyw6jrmjIWq"
instance: v2
name: "Slack - Send notification"
status: active
last_modified: 2026-08-31T18:22:54.989Z
tags: []
fingerprint: "e9a33daa9289d003a155d1d6fcf8e4e4b678e03698644dabf38e3cf97226cb94"
auto_generated_at: 2026-09-08T19:19:58Z
---

<!-- auto:start -->

# Slack - Send notification

## Summary

- **Status:** active
- **n8n ID:** `fMgQKiyw6jrmjIWq`
- **Nodes:** 11
- **Last modified:** 2026-08-31T18:22:54.989Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `a2479bfa-3195-4b2b-9b04-3c51b3393c91`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Hearth: Send a message" (id `088f3232-1cc3-4f20-b709-071e8959cb97`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Supermove: Send a message" (id `791ac0d5-0eac-471f-8809-87463a18f315`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "PE: Send a message" (id `918d01b7-b21f-45e2-af01-2eca59db18e0`)

### Slack channels

- *(dynamic channel)* — op `channel` — node "Hearth: Send a message" (id `088f3232-1cc3-4f20-b709-071e8959cb97`)
- *(dynamic channel)* — op `channel` — node "Supermove: Send a message" (id `791ac0d5-0eac-471f-8809-87463a18f315`)
- *(dynamic channel)* — op `channel` — node "PE: Send a message" (id `918d01b7-b21f-45e2-af01-2eca59db18e0`)

## Used by (workflows)

- [[gmail-send-html-email|Gmail - Send HTML Email]] — node "Email not provided notification" (id `af693ff9-3fc9-4be2-8d91-ac164fff5083`)
- [[gmail-send-html-email|Gmail - Send HTML Email]] — node "Email send failed notification" (id `b6cf7891-af9c-4860-8a1e-dc11e9cae71c`)
- [[gmail-send-html-email|Gmail - Send HTML Email]] — node "Email sent notification" (id `f461e202-f24e-479e-a3b9-83ad1b3cd554`)
- [[gmail-send-html-email|Gmail - Send HTML Email]] — node "Email skipped notification" (id `7dc7368c-1db5-456d-9339-66a9270cf14f`)
- [[gmail-send-simple-text-email|Gmail - Send Simple Text Email]] — node "Email not provided notification" (id `b1a6ef78-bfd6-4990-bf75-9d90fd372291`)
- [[gmail-send-simple-text-email|Gmail - Send Simple Text Email]] — node "Email send failed notification" (id `226881ce-92c8-4aae-81d9-8e9b31142bd8`)
- [[gmail-send-simple-text-email|Gmail - Send Simple Text Email]] — node "Email sent notification" (id `0e08c302-6b80-4024-887c-d53a8ca71b89`)
- [[gmail-send-simple-text-email|Gmail - Send Simple Text Email]] — node "Email skipped notification" (id `5b9bbf02-921f-4955-bf5c-54ec0524145c`)
- [[slack-create-a-base-message|Slack - Create a base message]] — node "Call 'Slack - Send notification'" (id `9fc26989-0e06-4e0b-b053-123403509ece`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
