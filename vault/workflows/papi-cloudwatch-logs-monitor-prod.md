---
n8n_id: "f9rOEDsZRv4toFvu"
name: "PAPI Cloudwatch Logs Monitor(Prod)"
status: active
last_modified: 2025-06-06T17:33:00.445Z
tags: []
fingerprint: "185ebf97c2438359df2f94ff3817ed125d4a3a01a0bed299809c3153d54e618e"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PAPI Cloudwatch Logs Monitor(Prod)

## Summary

- **Status:** active
- **n8n ID:** `f9rOEDsZRv4toFvu`
- **Nodes:** 32
- **Last modified:** 2025-06-06T17:33:00.445Z

## Triggers

- **manual** — node "When clicking ‘Test workflow’" (id `1f8d6d0d-7091-4f85-ba00-724c60d63573`)
- **schedule** — node "Schedule Trigger" (id `57cdb2a1-1f22-4f2a-971c-42c7f58ca638`) — `every 15 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/ikbo9ffkgfj1bzcs|AWS SDK Wrapper Credentials PE PROD]] (`awsSdkWrapperCredentialsApi`, id `IKBO9fFKgfj1BzcS`) — node "CloudwatchStartQuery" (id `03a299f0-8db7-4e66-bcad-276d616847a2`)
- [[../resources/credentials/ikbo9ffkgfj1bzcs|AWS SDK Wrapper Credentials PE PROD]] (`awsSdkWrapperCredentialsApi`, id `IKBO9fFKgfj1BzcS`) — node "CloudwatchStartQuery1" (id `052fb33c-8371-4be5-be29-8d6e05d5d23c`)
- [[../resources/credentials/kthxawhfb3lnxntf|AWS account 2]] (`aws`, id `kTHXAWhfb3lnXntf`) — node "HTTP Request2" (id `0e2fb09b-ee78-45aa-8260-acf84790fd53`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack" (id `175104fc-8491-4011-88bb-8b23d30f14be`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Google Sheets" (id `29a478e3-b128-4c10-80e8-71d8faa2e03f`)
- [[../resources/credentials/mla6ntr86w0mqqdf|PE AWS Account (Prod)]] (`aws`, id `mLa6NtR86w0mqQDF`) — node "HTTP Request1" (id `2a7acd1a-06d9-4a2a-ab4f-d679aead7bcc`)
- [[../resources/credentials/ikbo9ffkgfj1bzcs|AWS SDK Wrapper Credentials PE PROD]] (`awsSdkWrapperCredentialsApi`, id `IKBO9fFKgfj1BzcS`) — node "AWS Service Request" (id `618bd146-0bd8-44df-b06c-fa2c510109af`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack2" (id `63adbd5f-9c71-4289-a937-7f4c9324d307`)
- [[../resources/credentials/mla6ntr86w0mqqdf|PE AWS Account (Prod)]] (`aws`, id `mLa6NtR86w0mqQDF`) — node "HTTP Request" (id `9979e6d6-c7ec-4148-a7e4-c112f7220251`)
- [[../resources/credentials/ikbo9ffkgfj1bzcs|AWS SDK Wrapper Credentials PE PROD]] (`awsSdkWrapperCredentialsApi`, id `IKBO9fFKgfj1BzcS`) — node "CloudwatchGetQueryResults" (id `bd7ac26c-b6a7-4a62-93b1-85a4f69b0b3c`)
- [[../resources/credentials/ikbo9ffkgfj1bzcs|AWS SDK Wrapper Credentials PE PROD]] (`awsSdkWrapperCredentialsApi`, id `IKBO9fFKgfj1BzcS`) — node "CloudwatchGetQueryResults1" (id `d863fbe0-80e7-41f2-93d9-679ee3b87fe0`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Slack1" (id `d86c8228-6c1b-45ae-9a1d-e214a6c603e5`)

### HTTP URLs

- [[../resources/http-urls/logs-us-east-1-amazonaws-com|logs.us-east-1.amazonaws.com]] — `POST https://logs.us-east-1.amazonaws.com` — node "HTTP Request2" (id `0e2fb09b-ee78-45aa-8260-acf84790fd53`)
- [[../resources/http-urls/logs-us-east-1-amazonaws-com|logs.us-east-1.amazonaws.com]] — `POST https://logs.us-east-1.amazonaws.com` — node "HTTP Request1" (id `2a7acd1a-06d9-4a2a-ab4f-d679aead7bcc`)
- [[../resources/http-urls/m4fenebmzhtsgqzsptoh6fhut40tvktc-lambda-url-us-east-1-on-aws|m4fenebmzhtsgqzsptoh6fhut40tvktc.lambda-url.us-east-1.on.aws]] — `POST https://m4fenebmzhtsgqzsptoh6fhut40tvktc.lambda-url.us-east-1.on.aws` — node "HTTP Request" (id `9979e6d6-c7ec-4148-a7e4-c112f7220251`)

### Custom / community nodes

- [[../resources/custom-nodes/n8n-nodes-aws-sdk-v3|n8n-nodes-aws-sdk-v3]] — type `n8n-nodes-aws-sdk-v3.AWSSDKWrapper` — node "CloudwatchStartQuery" (id `03a299f0-8db7-4e66-bcad-276d616847a2`)
- [[../resources/custom-nodes/n8n-nodes-aws-sdk-v3|n8n-nodes-aws-sdk-v3]] — type `n8n-nodes-aws-sdk-v3.AWSSDKWrapper` — node "CloudwatchStartQuery1" (id `052fb33c-8371-4be5-be29-8d6e05d5d23c`)
- [[../resources/custom-nodes/n8n-nodes-aws-sdk-v3|n8n-nodes-aws-sdk-v3]] — type `n8n-nodes-aws-sdk-v3.AWSSDKWrapper` — node "AWS Service Request" (id `618bd146-0bd8-44df-b06c-fa2c510109af`)
- [[../resources/custom-nodes/n8n-nodes-aws-sdk-v3|n8n-nodes-aws-sdk-v3]] — type `n8n-nodes-aws-sdk-v3.AWSSDKWrapper` — node "CloudwatchGetQueryResults" (id `bd7ac26c-b6a7-4a62-93b1-85a4f69b0b3c`)
- [[../resources/custom-nodes/n8n-nodes-aws-sdk-v3|n8n-nodes-aws-sdk-v3]] — type `n8n-nodes-aws-sdk-v3.AWSSDKWrapper` — node "CloudwatchGetQueryResults1" (id `d863fbe0-80e7-41f2-93d9-679ee3b87fe0`)

### Google Sheets

- [[../resources/google-sheets/1-l5ft2jcpsyxp3lwubrrnlu1rdc-m7f7qn7vlderwci|PAPI Onboarding Data Logs]] (id `1_l5Ft2jcPsyxP3LwUbrRNlu1RDC-M7F7qN7vLdErwcI`) — op `appendOrUpdate`, tab `Logs` — node "Google Sheets" (id `29a478e3-b128-4c10-80e8-71d8faa2e03f`)

### Slack channels

- [[../resources/slack-channels/c0906sg2w5n|papi-logs]] (id `C0906SG2W5N`) — op `channel` — node "Slack2" (id `63adbd5f-9c71-4289-a937-7f4c9324d307`)
- [[../resources/slack-channels/c08r3tpsm33|st-prod-event-logs]] (id `C08R3TPSM33`) — op `channel` — node "Slack1" (id `d86c8228-6c1b-45ae-9a1d-e214a6c603e5`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
