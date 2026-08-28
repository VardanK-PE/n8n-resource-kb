---
n8n_id: "jYTz952jPsD9jjWV"
name: "Billing System - Get Or Create QB merchant info"
status: inactive
last_modified: 2026-03-18T19:55:10.927Z
tags: []
fingerprint: "7c379ed1be34c106d98c1ec289dcd2bbc926a829bee4a188b5a1480c66301821"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Billing System - Get Or Create QB merchant info

## Summary

- **Status:** inactive
- **n8n ID:** `jYTz952jPsD9jjWV`
- **Nodes:** 16
- **Last modified:** 2026-03-18T19:55:10.927Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `1e6544c9-ad52-40b4-96cd-40cdbfa2f967`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `62da0080-e047-46cb-a6ba-2c01ec2df304`)

## Depends on

### Credentials

- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "Create Customer1" (id `1dae3dfa-1930-4b47-b611-ee712a5d05c8`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Log Created Customer" (id `9e4fb002-bc97-4dc3-a366-81974fc39251`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Execute a SQL query" (id `bc76670a-6fbb-4ea9-b405-93a6e6935f6b`)
- [[../resources/credentials/8lz6ah2z95cu5rwo|QuickBooks Online account]] (`quickBooksOAuth2Api`, id `8Lz6ah2z95CU5rwO`) — node "FindCustomer" (id `cd217a85-5a08-41ff-832c-aa044129fe5a`)

### HTTP URLs

- [[../resources/http-urls/quickbooks-api-intuit-com|quickbooks.api.intuit.com]] — `POST https://quickbooks.api.intuit.com/v3/company/9341452828840730/customer?minorversion=75` — node "Create Customer1" (id `1dae3dfa-1930-4b47-b611-ee712a5d05c8`)

### Databases

- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Execute a SQL query" (id `bc76670a-6fbb-4ea9-b405-93a6e6935f6b`)

### Google Sheets

- [[../resources/google-sheets/1hxh00hkhzskiwupgayf-bljqvrvjty0m88gx4h9zbri|N8N Quick Book Logs]] (id `1hXh00hKHzsKiwUPGAyf-BljqVRVJtY0m88gx4h9zbrI`) — op `append`, tab `Account Creation Log` — node "Log Created Customer" (id `9e4fb002-bc97-4dc3-a366-81974fc39251`)

## Used by (workflows)

- [[billing-system-generate-invoices-for-billing-period|Billing System - Generate Invoices for Billing Period]] — node "Get Or Create Merchant QB ID" (id `db4ade9d-7fe1-4121-aec0-348134259121`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
