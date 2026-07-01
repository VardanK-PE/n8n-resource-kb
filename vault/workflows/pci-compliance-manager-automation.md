---
n8n_id: "nethTCkaMDFvPGvO"
name: "PCI Compliance Manager Automation"
status: active
last_modified: 2026-04-29T19:35:14.245Z
tags: []
fingerprint: "052d61af001f6c06d23c4eb15a02e67e8ebcff66bd688d73893b75a02f793f7a"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# PCI Compliance Manager Automation

## Summary

- **Status:** active
- **n8n ID:** `nethTCkaMDFvPGvO`
- **Nodes:** 93
- **Last modified:** 2026-04-29T19:35:14.245Z

## Triggers

- **error** — node "Error Trigger" (id `12019503-b807-40d4-9651-e7e45d84f463`)
- **manual** — node "When clicking ‘Execute workflow’" (id `396c8e88-9393-4f0c-85ca-47757aca038b`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `bbaac9a3-2246-42c3-998a-8bf794994c66`)
- **webhook** — node "Webhook1" (id `c36a8d79-8cd9-4fc0-8f45-ea5e685cca76`) — GET `46191463-2a95-4112-821f-492180c9eafe`
- **schedule** — node "Schedule Trigger" (id `d80a3e21-570c-4761-9365-c8f83e69da0d`) — `every 3 minute(s)`

## Depends on

### Credentials

- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Get many messages" (id `01fafec3-d6e0-4c26-bc82-b8df33490f9b`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet" (id `0e51d9c7-601f-4f31-9fae-57a884861181`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `10ff3273-fed8-4918-8966-9441a2260d10`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Processing Status MIDS" (id `14ba132a-5225-4d9b-baf8-998d6fdf6384`)
- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Execute a SQL query" (id `163c4052-bf60-4ba7-91ad-eb814c2fec62`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message2" (id `23ef8ae5-7b2e-422d-8244-2b4993dc5d20`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message3" (id `2d5dfedd-c8b2-4ae5-9adc-32777322665a`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail1" (id `2dc1ef6c-140e-4e62-896b-224b607d8162`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet1" (id `3832ed15-a5bc-4404-8e57-1dd61781743c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet3" (id `3c2e51d3-830a-411b-ab87-ef765f46c01f`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Check for PCI Portal Welcome Email1" (id `50e93687-88bb-47af-97e9-23dd4b202ab6`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file" (id `75bcabf8-575e-4273-87a2-1d51bd3980b0`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "Gmail" (id `76059c43-6dcf-48bc-b5ae-4ddc0ea73889`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet2" (id `80bb8858-d4b6-4482-9c9d-6396ea4c1572`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get Merchants" (id `a9312dac-ca54-4b96-95e4-290e639fdff0`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `a9d4350f-0cb0-4edc-989e-806460bae67c`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message4" (id `c1946ca1-315f-4121-ae83-e24653a3b49a`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `c26d2223-328c-4377-9c0e-e34e0d9c6261`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message6" (id `cfee3619-04fb-4607-a72a-b5fc6ab00470`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Update row in sheet4" (id `e6d51b40-55c2-4b38-a679-86d785d90afc`)
- [[../resources/credentials/oucdlrjl56jcwuca|PE Merchants Gmail Account (merchants@platformfactory.io)]] (`gmailOAuth2`, id `OUcDLrjl56jcWUCa`) — node "PCIPortalEmail" (id `ef9b68bb-4dbb-43ae-9e8c-4bcb0d1ef542`)

### HTTP URLs

- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `POST https://pcicompliancemanager.com/services/webapi/v2/saq/answerQuestion?apId={{ $('Get Account Details').item.json.data.apId }}` — node "POST SAQ Answers" (id `00ad2101-e669-4b1e-a8e7-7da9adae09a8`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `POST https://pcicompliancemanager.com/services/webapi/v2/attestations?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Submit Attestation" (id `03178057-d677-4504-8c69-2b21ccd41721`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `GET https://pcicompliancemanager.com{{ $json.data.downloadLink }}` — node "Download" (id `0d75bf06-3c01-4450-8d25-4d173299eb84`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `GET https://pcicompliancemanager.com/services/webapi/v2/status?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Get Attestation Details" (id `27b19e80-a27f-4007-a9b4-caf5b084a47f`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `POST https://pcicompliancemanager.com/services/clientapi/login` — node "Get Access Token" (id `3387a6ea-1a63-4b73-b5c0-ad9f042aff24`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `POST https://pcicompliancemanager.com/services/webapi/v2/profile-answers?apId={{ $('Get Account Details').item.json.data.apId }}` — node "POST Business Profile" (id `3bc4c362-cbde-42ce-8782-99cfebd04e2e`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `GET https://pcicompliancemanager.com/services/webapi/v2/users/{{ $('Get Account Details').item.json.data.id }}?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Get User Details" (id `48824e0d-e472-4450-8f1e-df16936d0ae7`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `GET https://pcicompliancemanager.com/services/webapi/v2/users/success` — node "Get Account Details" (id `586ef2f5-3b1c-4250-8c80-1884090ba3ea`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `POST https://pcicompliancemanager.com/services/webapi/v2/user/resetPassword/` — node "Reset Password" (id `6dd46b15-653e-4ce2-89e2-2244490b066d`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `GET https://pcicompliancemanager.com/services/webapi/v2/attestations/create?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Create Attestation" (id `6f8db8cd-7b45-4a4a-90e2-45c00058e8f5`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `GET https://pcicompliancemanager.com/services/webapi/v2/status?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Get Account Status" (id `720a081c-d779-48de-98c9-4b33600235bd`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `GET https://pcicompliancemanager.com/services/webapi/v2/attestations/download/{{ $json.data.validatedAocId }}?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Get Attestation Download Link" (id `a1f917f0-576e-4ab9-996a-faa20ce66f60`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `GET https://pcicompliancemanager.com/services/webapi/v2/profile-answers?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Get Profile Answers" (id `a6522a35-7151-4168-a76f-023ab6fcb459`)
- *(dynamic URL)* — `GET {{ $json.resetLink }}` — node "HTTP Request" (id `ba540a33-22c1-46dd-a16b-def4e80bd9d8`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `POST https://pcicompliancemanager.com/services/webapi/v2/user/forgottenPasswords` — node "Password Reset Request" (id `f26c75f9-47c9-46e9-bf56-309c22e0cb1f`)
- [[../resources/http-urls/pcicompliancemanager-com|pcicompliancemanager.com]] — `POST https://pcicompliancemanager.com/services/webapi/v2/users/{{ $('Get Account Details').item.json.data.id }}/update?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Personalize-Register" (id `f95688fd-bae6-4e07-9bdb-85f3ae854cdf`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Execute a SQL query" (id `163c4052-bf60-4ba7-91ad-eb814c2fec62`)

### Google Sheets

- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update row in sheet" (id `0e51d9c7-601f-4f31-9fae-57a884861181`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Processing Status MIDS" (id `14ba132a-5225-4d9b-baf8-998d6fdf6384`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update row in sheet1" (id `3832ed15-a5bc-4404-8e57-1dd61781743c`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update row in sheet3" (id `3c2e51d3-830a-411b-ab87-ef765f46c01f`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update row in sheet2" (id `80bb8858-d4b6-4482-9c9d-6396ea4c1572`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `?`, tab `mid` — node "Get Merchants" (id `a9312dac-ca54-4b96-95e4-290e639fdff0`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `appendOrUpdate`, tab `all_pci_account_emails` — node "Append or update row in sheet" (id `a9d4350f-0cb0-4edc-989e-806460bae67c`)
- [[../resources/google-sheets/1kiz0yv1iibvxncjyekhyu-xvqoatxwju7ykpy70q4gw|Elavon BI Automation]] (id `1kiZ0YV1iIBvXnCjyEkHYu-XVQOATxwJU7ykPY70q4Gw`) — op `update`, tab `mid` — node "Update row in sheet4" (id `e6d51b40-55c2-4b38-a679-86d785d90afc`)

### Google Drive

- [[../resources/google-drive/1xeztxdaboanuxz0ufjbug-lupfmrn4l4|ElavonPCIComplianceManageAOCs]] (`folder`, id `1xeZTXdaboAnUXz0UfJbUG_lUPfmrN4l4`) — op `?` — node "Upload file" (id `75bcabf8-575e-4273-87a2-1d51bd3980b0`)

### Slack channels

- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Send a message" (id `10ff3273-fed8-4918-8966-9441a2260d10`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Send a message2" (id `23ef8ae5-7b2e-422d-8244-2b4993dc5d20`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Send a message3" (id `2d5dfedd-c8b2-4ae5-9adc-32777322665a`)
- *(dynamic channel)* — op `channel` — node "Send a message4" (id `c1946ca1-315f-4121-ae83-e24653a3b49a`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Send a message1" (id `c26d2223-328c-4377-9c0e-e34e0d9c6261`)
- [[../resources/slack-channels/c09ckmcu3e3|pci-releated-alert]] (id `C09CKMCU3E3`) — op `channel` — node "Send a message6" (id `cfee3619-04fb-4607-a72a-b5fc6ab00470`)

### Sub-workflows (Execute Workflow calls)

- [[pci-compliance-manager-automation|PCI Compliance Manager Automation]] (n8n_id `nethTCkaMDFvPGvO`) — node "Call 'PCI Compliance Manager Automation'" (id `9ccd2762-c83e-44f8-b86c-f18100fd075c`)

## Used by (workflows)

- [[pci-compliance-manager-automation|PCI Compliance Manager Automation]] — node "Call 'PCI Compliance Manager Automation'" (id `9ccd2762-c83e-44f8-b86c-f18100fd075c`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
