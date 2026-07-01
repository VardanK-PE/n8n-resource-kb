---
n8n_id: "gKC9jXoIFrlbC7vM"
name: "PE Mail Scanner"
status: active
last_modified: 2024-12-21T22:34:06.246Z
tags: []
fingerprint: "69cda448bb46c0a4b7169e2b2b9b0cbe53cc183b47b904f08ada2a3ed65593f3"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PE Mail Scanner

## Summary

- **Status:** active
- **n8n ID:** `gKC9jXoIFrlbC7vM`
- **Nodes:** 17
- **Last modified:** 2024-12-21T22:34:06.246Z

## Triggers

- **other** — node "Google Drive Trigger" (id `edae2cd2-cfec-485b-9e73-fad4e9740599`)

## Depends on

### Credentials

- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `23837587-c11f-49cb-8131-ad9ec13fa675`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `33c051d1-5073-4574-b2b7-d7a66e11fbe5`)
- [[../resources/credentials/wwm73d114letbuus|n8n-service-account Google Service Account account]] (`googleApi`, id `wwm73D114LETBUUS`) — node "Google Vision" (id `683f8217-d16c-4c36-80ad-c10ca7fae56c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive1" (id `711d7086-b676-4afd-bce6-0c1258967c47`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Thumnail" (id `73abcc73-3be0-45a1-94d7-3a7c69862a56`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive" (id `7aeae9d9-dd69-420f-8456-ec1b12acb518`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request2" (id `84f37c26-9464-45e3-929e-ba29ee080190`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request" (id `8758e1e6-d60f-4b24-b1b3-850a633daa3f`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI" (id `a2874a92-98d7-4bbd-ba44-112455cec2dd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "HTTP Request1" (id `e8290f23-aaf9-4bd0-bb6e-e917601e0edc`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Drive Trigger" (id `edae2cd2-cfec-485b-9e73-fad4e9740599`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `f49656b0-3347-4f10-af58-86869bb4e6de`)

### HTTP URLs

- [[../resources/http-urls/cdn3-iconfinder-com|cdn3.iconfinder.com]] — `GET https://cdn3.iconfinder.com/data/icons/aami-web-internet/64/aami4-51-512.png` — node "HTTP Request3" (id `0aab49de-1a36-44a2-a17d-3c7e6b58581b`)
- [[../resources/http-urls/vision-googleapis-com|vision.googleapis.com]] — `POST https://vision.googleapis.com/v1/files:annotate` — node "Google Vision" (id `683f8217-d16c-4c36-80ad-c10ca7fae56c`)
- *(dynamic URL)* — `GET {{ $('Google Drive Trigger').item.json.thumbnailLink }}` — node "Get Thumnail" (id `73abcc73-3be0-45a1-94d7-3a7c69862a56`)
- [[../resources/http-urls/www-googleapis-com|www.googleapis.com]] — `GET https://www.googleapis.com/drive/v3/files/{{ $('Google Drive Trigger').item.json.id }}?fields=*` — node "HTTP Request2" (id `84f37c26-9464-45e3-929e-ba29ee080190`)
- [[../resources/http-urls/www-googleapis-com|www.googleapis.com]] — `PATCH https://www.googleapis.com/drive/v3/files/{{ $('Google Drive Trigger').item.json.id }}` — node "HTTP Request" (id `8758e1e6-d60f-4b24-b1b3-850a633daa3f`)
- [[../resources/http-urls/www-googleapis-com|www.googleapis.com]] — `GET https://www.googleapis.com/drive/v3/files/18D5BFZPJOPdhbqkYL-SdaXg3Sz738n2-?fields=*` — node "HTTP Request1" (id `e8290f23-aaf9-4bd0-bb6e-e917601e0edc`)

### LLM models

- [[../resources/llm-models/openai-unspecified|openai / ?]] — node "OpenAI" (id `a2874a92-98d7-4bbd-ba44-112455cec2dd`)

### Google Drive

- *(dynamic)* — op `update` — node "Google Drive1" (id `711d7086-b676-4afd-bce6-0c1258967c47`)
- *(dynamic)* — op `download` — node "Google Drive" (id `7aeae9d9-dd69-420f-8456-ec1b12acb518`)

### Slack channels

- [[../resources/slack-channels/c082l0unbt3|mail-scanner]] (id `C082L0UNBT3`) — op `channel` — node "Slack" (id `33c051d1-5073-4574-b2b7-d7a66e11fbe5`)
- [[../resources/slack-channels/c082l0unbt3|mail-scanner]] (id `C082L0UNBT3`) — op `channel` — node "Slack1" (id `f49656b0-3347-4f10-af58-86869bb4e6de`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
