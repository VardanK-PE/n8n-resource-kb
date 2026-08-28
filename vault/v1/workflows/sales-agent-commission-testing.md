---
n8n_id: "AmSSTQ2gkE8aJAGr"
name: "Sales Agent Commission - Testing"
status: inactive
last_modified: 2025-02-06T23:04:33.048Z
tags: []
fingerprint: "2d029967f55851b89152950c0189652058ecf608b94c8107465bc395b8a24cfa"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Sales Agent Commission - Testing

## Summary

- **Status:** inactive
- **n8n ID:** `AmSSTQ2gkE8aJAGr`
- **Nodes:** 7
- **Last modified:** 2025-02-06T23:04:33.048Z

## Triggers

- **execute-workflow** — node "Execute Workflow Trigger" (id `69a3d018-3141-433f-ad5d-2198dc80d4d1`)

## Depends on

### Credentials

- [[../resources/credentials/mla6ntr86w0mqqdf|PE AWS Account (Prod)]] (`aws`, id `mLa6NtR86w0mqQDF`) — node "AWS S3" (id `b7a55df2-5309-4b4c-94bc-b95027026315`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Read Final Sheet" (id `ecbed6aa-7362-4804-84ac-2963c44ec046`)
- [[../resources/credentials/67fejotk4a3tgz6y|Kafka account]] (`kafka`, id `67fEjoTk4A3tGZ6Y`) — node "Kafka" (id `ed80bf38-d95b-4ee9-9097-694a76743f68`)

### Google Sheets

- [[../resources/google-sheets/1ijgpwsj4vtbtpujitdgwnqz30k50dwnqwn14hagjnfu|202501_Test Partner]] (id `1IJGpwSJ4vtBtPUJItdGWNqz30k50dWNQWn14HAGJNFU`) — op `?`, tab `Residual Details` — node "Read Final Sheet" (id `ecbed6aa-7362-4804-84ac-2963c44ec046`)

### AWS S3 buckets

- [[../resources/s3-buckets/partner-residuals-prod|partner-residuals-prod]] — op `upload` — node "AWS S3" (id `b7a55df2-5309-4b4c-94bc-b95027026315`)

### Kafka topics

- [[../resources/kafka-topics/partner-residuals|partner-residuals]] (`producer`) — node "Kafka" (id `ed80bf38-d95b-4ee9-9097-694a76743f68`)

## Used by (workflows)

*(populated in the resource-aggregation pass after all workflows are rendered)*

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
