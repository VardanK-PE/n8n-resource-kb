---
n8n_id: "3m6DrdMDwD63ztuT"
name: "Gitbook Docs Converter"
status: inactive
last_modified: 2025-05-10T16:54:14.913Z
tags: []
fingerprint: "cf3c98accb30dd7036de336c7f3417181828ca4e8d99466c4242a1a42d9674bd"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Gitbook Docs Converter

## Summary

- **Status:** inactive
- **n8n ID:** `3m6DrdMDwD63ztuT`
- **Nodes:** 70
- **Last modified:** 2025-05-10T16:54:14.913Z

## Triggers

- **manual** — node "When clicking ‘Test workflow’" (id `88374ab4-9a80-4107-8e9d-81a565084a67`)

## Depends on

### Credentials

- [[../resources/credentials/xvtqswgesovpfovr|GitHub account]] (`githubApi`, id `xVtQSWGesoVPFoVr`) — node "GetFileContents1" (id `1f2cb7d3-5d6d-4001-8a50-9d741bd07fec`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model3" (id `212d2e2f-cce4-49cf-abe0-77f35cce227d`)
- [[../resources/credentials/xvtqswgesovpfovr|GitHub account]] (`githubApi`, id `xVtQSWGesoVPFoVr`) — node "CreateFile1" (id `24ed45e3-a8a6-4279-beba-e5e317361c8b`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model3" (id `27c0c470-6a90-43d5-9680-92ae15dd80df`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `2a8e92f8-b4e4-422e-b59b-1b3f88a3db47`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Items1" (id `2c2b77b0-cb30-4133-b06e-fc23f1cd7e2a`)
- [[../resources/credentials/xvtqswgesovpfovr|GitHub account]] (`githubApi`, id `xVtQSWGesoVPFoVr`) — node "HTTP Request2" (id `342cd5e9-96df-44f6-a21f-95ef70127117`)
- [[../resources/credentials/xvtqswgesovpfovr|GitHub account]] (`githubApi`, id `xVtQSWGesoVPFoVr`) — node "GetFileContents2" (id `40d94d85-dba3-43e2-b32e-2cc80b3da1ba`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model2" (id `41ae07a9-d4f9-4967-95db-ca979ad62832`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets2" (id `44894efe-ac94-4eaf-8682-9d7abccb4ed1`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model1" (id `501878ca-a3fc-4be2-ae20-8554376ee0b7`)
- [[../resources/credentials/xvtqswgesovpfovr|GitHub account]] (`githubApi`, id `xVtQSWGesoVPFoVr`) — node "CreateMappingFile" (id `53b64d88-1c9d-4060-b968-433d9e3aad78`)
- [[../resources/credentials/xvtqswgesovpfovr|GitHub account]] (`githubApi`, id `xVtQSWGesoVPFoVr`) — node "HTTP Request1" (id `59685ce2-bb57-4125-a3a2-3e20c04469e7`)
- [[../resources/credentials/1jtiaqogn0rcfpc1|Anthropic account]] (`anthropicApi`, id `1jtIAQOGn0RcFpc1`) — node "Anthropic Chat Model" (id `7385afcf-9b25-41c6-8e33-78b663e5eebe`)
- [[../resources/credentials/xvtqswgesovpfovr|GitHub account]] (`githubApi`, id `xVtQSWGesoVPFoVr`) — node "CreateFile2" (id `804212b1-8b63-4495-ae03-e2ca1dc264b6`)
- [[../resources/credentials/xvtqswgesovpfovr|GitHub account]] (`githubApi`, id `xVtQSWGesoVPFoVr`) — node "CreateMappingFile1" (id `80bd9e81-9a7e-4a77-972a-fc80eaeb9f62`)
- [[../resources/credentials/xvtqswgesovpfovr|GitHub account]] (`githubApi`, id `xVtQSWGesoVPFoVr`) — node "GetFileContents" (id `8a18f142-b1ac-41e4-9760-14be233edbb7`)
- [[../resources/credentials/xvtqswgesovpfovr|GitHub account]] (`githubApi`, id `xVtQSWGesoVPFoVr`) — node "CreateFile" (id `92fc3809-50f2-4f3a-891e-d8e04262b75d`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model2" (id `9a5c4a17-728a-41fc-8215-0922794b6e79`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Items4" (id `a04129fc-d22c-4a5b-a8ef-920845d4cd5a`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Items2" (id `a2cdf857-8f52-422d-aad1-de59a9b8ded1`)
- [[../resources/credentials/xvtqswgesovpfovr|GitHub account]] (`githubApi`, id `xVtQSWGesoVPFoVr`) — node "HTTP Request" (id `a4e612ed-3b81-45fb-84d7-ac3512b55e2c`)
- [[../resources/credentials/xvtqswgesovpfovr|GitHub account]] (`githubApi`, id `xVtQSWGesoVPFoVr`) — node "UpdateFIleContents1" (id `a5e9e9f0-6cc2-41cf-8da5-ca9b3dc91dd4`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Items" (id `abf7bb7d-7b7b-4070-98c2-fc859296b9da`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model1" (id `ae421509-0296-4f6b-8b0b-8665df661d22`)
- [[../resources/credentials/6mtsxoj0epbt8oqw|OpenAi N8N Account 20241221]] (`openAiApi`, id `6MTsXoj0epBT8Oqw`) — node "OpenAI Chat Model" (id `b48f970b-ce86-4488-a73c-5c5677cb7333`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets5" (id `caed95da-292b-4b5a-a999-3dd2980775a3`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Existing Items3" (id `cbf65aa2-5438-4a81-acb0-df638a9a3974`)
- [[../resources/credentials/xvtqswgesovpfovr|GitHub account]] (`githubApi`, id `xVtQSWGesoVPFoVr`) — node "UpdateFIleContents" (id `d3d3ff79-709e-4a85-a98b-b715c8b488bd`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets4" (id `d5d8ebfb-dd54-40ec-b014-8b545a451280`)
- [[../resources/credentials/dllntaqkbzxwow3g|Browserless Credentials account]] (`browserlessApi`, id `DlLnTAQkBzxwow3G`) — node "Browserless" (id `f88e2fbc-14ed-405a-922f-cdc0f32ab008`)

### HTTP URLs

- [[../resources/http-urls/api-github-com|api.github.com]] — `GET https://api.github.com/repos/payengine/gitbook-sync/git/trees/edited-branch?recursive=1` — node "HTTP Request2" (id `342cd5e9-96df-44f6-a21f-95ef70127117`)
- [[../resources/http-urls/api-github-com|api.github.com]] — `GET https://api.github.com/repos/payengine/gitbook-sync/git/trees/synced-branch?recursive=1` — node "HTTP Request1" (id `59685ce2-bb57-4125-a3a2-3e20c04469e7`)
- [[../resources/http-urls/docs-payengine-co|docs.payengine.co]] — `GET https://docs.payengine.co/payengine-api-v2.5` — node "HTTP Request3" (id `6b82a648-b958-4016-b425-154275854750`)
- [[../resources/http-urls/docs-payengine-co|docs.payengine.co]] — `GET https://docs.payengine.co{{ $json.page_links }}` — node "HTTP Request4" (id `925a258f-acd6-4a42-a414-317a4cb9f8c5`)
- [[../resources/http-urls/api-github-com|api.github.com]] — `GET https://api.github.com/repos/payengine/gitbook-sync/git/trees/main?recursive=1` — node "HTTP Request" (id `a4e612ed-3b81-45fb-84d7-ac3512b55e2c`)

### LLM models

- [[../resources/llm-models/openai-o3-mini|openai / o3-mini]] — node "OpenAI Chat Model3" (id `212d2e2f-cce4-49cf-abe0-77f35cce227d`)
- [[../resources/llm-models/anthropic-claude-3-7-sonnet-20250219|anthropic / claude-3-7-sonnet-20250219]] — node "Anthropic Chat Model3" (id `27c0c470-6a90-43d5-9680-92ae15dd80df`)
- [[../resources/llm-models/anthropic-claude-3-7-sonnet-20250219|anthropic / claude-3-7-sonnet-20250219]] — node "Anthropic Chat Model2" (id `41ae07a9-d4f9-4967-95db-ca979ad62832`)
- [[../resources/llm-models/anthropic-claude-3-7-sonnet-20250219|anthropic / claude-3-7-sonnet-20250219]] — node "Anthropic Chat Model1" (id `501878ca-a3fc-4be2-ae20-8554376ee0b7`)
- [[../resources/llm-models/anthropic-claude-3-7-sonnet-20250219|anthropic / claude-3-7-sonnet-20250219]] — node "Anthropic Chat Model" (id `7385afcf-9b25-41c6-8e33-78b663e5eebe`)
- [[../resources/llm-models/openai-o3-mini|openai / o3-mini]] — node "OpenAI Chat Model2" (id `9a5c4a17-728a-41fc-8215-0922794b6e79`)
- [[../resources/llm-models/openai-o3-mini|openai / o3-mini]] — node "OpenAI Chat Model1" (id `ae421509-0296-4f6b-8b0b-8665df661d22`)
- [[../resources/llm-models/openai-o3-mini|openai / o3-mini]] — node "OpenAI Chat Model" (id `b48f970b-ce86-4488-a73c-5c5677cb7333`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-browserless|n8n-nodes-browserless]] — type `n8n-nodes-browserless.Browserless` — node "Browserless" (id `f88e2fbc-14ed-405a-922f-cdc0f32ab008`)

### Google Sheets

- [[../resources/google-sheets/18wppivsbkedjlw7eceuzark7pengmnyy9at1gxpc9y0|PE Docs Revamp Project]] (id `18wPpIvsBkEdjLw7ECEUZaRK7pENGmnyY9at1GxPc9y0`) — op `append`, tab `Processed Status` — node "Google Sheets" (id `2a8e92f8-b4e4-422e-b59b-1b3f88a3db47`)
- [[../resources/google-sheets/18wppivsbkedjlw7eceuzark7pengmnyy9at1gxpc9y0|PE Docs Revamp Project]] (id `18wPpIvsBkEdjLw7ECEUZaRK7pENGmnyY9at1GxPc9y0`) — op `?`, tab `Developer Docs Processed` — node "Existing Items1" (id `2c2b77b0-cb30-4133-b06e-fc23f1cd7e2a`)
- [[../resources/google-sheets/18wppivsbkedjlw7eceuzark7pengmnyy9at1gxpc9y0|PE Docs Revamp Project]] (id `18wPpIvsBkEdjLw7ECEUZaRK7pENGmnyY9at1GxPc9y0`) — op `append`, tab `Developer Docs Processed` — node "Google Sheets2" (id `44894efe-ac94-4eaf-8682-9d7abccb4ed1`)
- [[../resources/google-sheets/18wppivsbkedjlw7eceuzark7pengmnyy9at1gxpc9y0|PE Docs Revamp Project]] (id `18wPpIvsBkEdjLw7ECEUZaRK7pENGmnyY9at1GxPc9y0`) — op `?`, tab `Docs Crawler` — node "Existing Items4" (id `a04129fc-d22c-4a5b-a8ef-920845d4cd5a`)
- [[../resources/google-sheets/18wppivsbkedjlw7eceuzark7pengmnyy9at1gxpc9y0|PE Docs Revamp Project]] (id `18wPpIvsBkEdjLw7ECEUZaRK7pENGmnyY9at1GxPc9y0`) — op `?`, tab `OpenAPI Processed` — node "Existing Items2" (id `a2cdf857-8f52-422d-aad1-de59a9b8ded1`)
- [[../resources/google-sheets/18wppivsbkedjlw7eceuzark7pengmnyy9at1gxpc9y0|PE Docs Revamp Project]] (id `18wPpIvsBkEdjLw7ECEUZaRK7pENGmnyY9at1GxPc9y0`) — op `?`, tab `Processed Status` — node "Existing Items" (id `abf7bb7d-7b7b-4070-98c2-fc859296b9da`)
- [[../resources/google-sheets/18wppivsbkedjlw7eceuzark7pengmnyy9at1gxpc9y0|PE Docs Revamp Project]] (id `18wPpIvsBkEdjLw7ECEUZaRK7pENGmnyY9at1GxPc9y0`) — op `appendOrUpdate`, tab `Docs Crawler` — node "Google Sheets5" (id `caed95da-292b-4b5a-a999-3dd2980775a3`)
- [[../resources/google-sheets/18wppivsbkedjlw7eceuzark7pengmnyy9at1gxpc9y0|PE Docs Revamp Project]] (id `18wPpIvsBkEdjLw7ECEUZaRK7pENGmnyY9at1GxPc9y0`) — op `appendOrUpdate`, tab `Docs Crawler` — node "Existing Items3" (id `cbf65aa2-5438-4a81-acb0-df638a9a3974`)
- [[../resources/google-sheets/18wppivsbkedjlw7eceuzark7pengmnyy9at1gxpc9y0|PE Docs Revamp Project]] (id `18wPpIvsBkEdjLw7ECEUZaRK7pENGmnyY9at1GxPc9y0`) — op `append`, tab `OpenAPI Processed` — node "Google Sheets4" (id `d5d8ebfb-dd54-40ec-b014-8b545a451280`)

### GitHub repos

- [[../resources/github-repos/payengine-gitbook-sync|payengine/gitbook-sync]] — op `get` on `file` — node "GetFileContents1" (id `1f2cb7d3-5d6d-4001-8a50-9d741bd07fec`)
- [[../resources/github-repos/payengine-pe-openapi|payengine/pe-openapi]] — op `?` on `file` — node "CreateFile1" (id `24ed45e3-a8a6-4279-beba-e5e317361c8b`)
- [[../resources/github-repos/payengine-gitbook-sync|payengine/gitbook-sync]] — op `get` on `file` — node "GetFileContents2" (id `40d94d85-dba3-43e2-b32e-2cc80b3da1ba`)
- [[../resources/github-repos/payengine-gitbook-sync|payengine/gitbook-sync]] — op `?` on `file` — node "CreateMappingFile" (id `53b64d88-1c9d-4060-b968-433d9e3aad78`)
- [[../resources/github-repos/payengine-pe-openapi|payengine/pe-openapi]] — op `?` on `file` — node "CreateFile2" (id `804212b1-8b63-4495-ae03-e2ca1dc264b6`)
- [[../resources/github-repos/payengine-gitbook-sync|payengine/gitbook-sync]] — op `?` on `file` — node "CreateMappingFile1" (id `80bd9e81-9a7e-4a77-972a-fc80eaeb9f62`)
- [[../resources/github-repos/payengine-gitbook-sync|payengine/gitbook-sync]] — op `get` on `file` — node "GetFileContents" (id `8a18f142-b1ac-41e4-9760-14be233edbb7`)
- [[../resources/github-repos/payengine-pe-openapi|payengine/pe-openapi]] — op `?` on `file` — node "CreateFile" (id `92fc3809-50f2-4f3a-891e-d8e04262b75d`)
- [[../resources/github-repos/payengine-gitbook-sync|payengine/gitbook-sync]] — op `edit` on `file` — node "UpdateFIleContents1" (id `a5e9e9f0-6cc2-41cf-8da5-ca9b3dc91dd4`)
- [[../resources/github-repos/payengine-gitbook-sync|payengine/gitbook-sync]] — op `edit` on `file` — node "UpdateFIleContents" (id `d3d3ff79-709e-4a85-a98b-b715c8b488bd`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
