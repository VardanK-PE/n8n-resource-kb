---
n8n_id: "5SQDZk06HCtloPsK"
instance: v1
name: "DocuSign Download Files"
status: inactive
last_modified: 2025-10-21T06:44:55.822Z
tags: []
fingerprint: "c12547fc2c20ca329f8401be4276d2e0f5e1f1f45f4eb56e8d7756c3d3bf26cc"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# DocuSign Download Files

## Summary

- **Status:** inactive
- **n8n ID:** `5SQDZk06HCtloPsK`
- **Nodes:** 49
- **Last modified:** 2025-10-21T06:44:55.822Z

## Triggers

- **error** — node "Error Trigger" (id `007bd5c0-2268-465a-ae9d-0ff86af5a88d`)
- **manual** — node "When clicking ‘Execute workflow’" (id `030bfa55-28ef-48dd-9ecc-1253f3f92939`)
- **schedule** — node "Schedule Trigger" (id `26b7044b-25ea-4ebd-888e-8f59d7f2790c`) — `every 30 minute(s)`
- **execute-workflow** — node "When Executed by Another Workflow" (id `83054d3c-3317-4122-bf2e-ffbfba193a84`)

## Depends on

### Credentials

- [[../resources/credentials/pyo8mvijlvsr5kld|Generic Bearer JWT Credential]] (`httpBearerAuth`, id `pYo8MvIJlVsR5Kld`) — node "Get Envelopes" (id `02c61879-1926-4a63-9ce3-796bac210d96`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet" (id `2862099b-a440-411b-b79b-402ac4719a7e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file3" (id `306cec62-5c6a-4d0c-9b2c-217452fe669e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet" (id `47b29894-b5a2-4547-b16e-c1b00bd83b0e`)
- [[../resources/credentials/pyo8mvijlvsr5kld|Generic Bearer JWT Credential]] (`httpBearerAuth`, id `pYo8MvIJlVsR5Kld`) — node "HTTP Request2" (id `4aa6aa03-2613-4e69-b5b5-f430ab376d00`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet1" (id `5fbf2010-0d26-46f8-88bb-f7beebd637e7`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Append or update row in sheet4" (id `60eca980-5015-4645-bb48-78d203a8d23e`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Create folder1" (id `7b714f18-fde0-4e3c-a970-e5aba6a7e92f`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message1" (id `87f7089e-40ef-4fe2-bb41-89458538d8ba`)
- [[../resources/credentials/pyo8mvijlvsr5kld|Generic Bearer JWT Credential]] (`httpBearerAuth`, id `pYo8MvIJlVsR5Kld`) — node "Get Envelopes1" (id `a342869c-5bde-4cb3-b893-736108a19ad5`)
- [[../resources/credentials/1hkdk4lbxxyibzyb|Slack account (PEBot)]] (`slackApi`, id `1HkDK4lbXXyibzYb`) — node "Send a message" (id `b2bbe1b9-3abb-4449-a130-58d445360997`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get row(s) in sheet1" (id `eb017a1b-cab3-4d9e-8bc1-81daa7d8ba9c`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Upload file" (id `f4089812-5d16-46e9-9ef3-51fc4a49dc42`)

### HTTP URLs

- [[../resources/http-urls/na4-docusign-net|na4.docusign.net]] — `GET https://na4.docusign.net/restapi/v2.1/accounts/e4e09f72-d9ff-4839-923a-02c5f4484d22/envelopes` — node "Get Envelopes" (id `02c61879-1926-4a63-9ce3-796bac210d96`)
- [[../resources/http-urls/na4-docusign-net|na4.docusign.net]] — `GET https://na4.docusign.net/restapi/v2.1/accounts/e4e09f72-d9ff-4839-923a-02c5f4484d22/envelopes/{{ $json.payload.envelopeId }}/documents/combined?certificate=true` — node "HTTP Request2" (id `4aa6aa03-2613-4e69-b5b5-f430ab376d00`)
- [[../resources/http-urls/account-docusign-com|account.docusign.com]] — `GET https://account.docusign.com/oauth/userinfo` — node "Get Account Info" (id `814f9e62-6dd9-43ca-86ca-8309149c37c8`)
- [[../resources/http-urls/na4-docusign-net|na4.docusign.net]] — `GET https://na4.docusign.net/restapi/v2.1/accounts/e4e09f72-d9ff-4839-923a-02c5f4484d22/envelopes` — node "Get Envelopes1" (id `a342869c-5bde-4cb3-b893-736108a19ad5`)
- *(dynamic URL)* — `POST {{ $json.token_url }}` — node "JWT to Access Token1" (id `c60817bb-ce8c-4335-9854-3bd594e73ffc`)

### Google Sheets

- [[../resources/google-sheets/1dco4c8-hld9fsgshrdlebfmx3rkjyka0jolkf1-clag|DocuSign - Envelope Registry]] (id `1dco4C8_hld9FSgshrDleBFMx3rKJYka0jOLkf1-clAg`) — op `?`, tab `Envelopes` — node "Get row(s) in sheet" (id `2862099b-a440-411b-b79b-402ac4719a7e`)
- [[../resources/google-sheets/1dco4c8-hld9fsgshrdlebfmx3rkjyka0jolkf1-clag|DocuSign - Envelope Registry]] (id `1dco4C8_hld9FSgshrDleBFMx3rKJYka0jOLkf1-clAg`) — op `appendOrUpdate`, tab `Envelopes` — node "Append or update row in sheet" (id `47b29894-b5a2-4547-b16e-c1b00bd83b0e`)
- [[../resources/google-sheets/1dco4c8-hld9fsgshrdlebfmx3rkjyka0jolkf1-clag|DocuSign - Envelope Registry]] (id `1dco4C8_hld9FSgshrDleBFMx3rKJYka0jOLkf1-clAg`) — op `appendOrUpdate`, tab `Envelopes` — node "Append or update row in sheet1" (id `5fbf2010-0d26-46f8-88bb-f7beebd637e7`)
- [[../resources/google-sheets/1dco4c8-hld9fsgshrdlebfmx3rkjyka0jolkf1-clag|DocuSign - Envelope Registry]] (id `1dco4C8_hld9FSgshrDleBFMx3rKJYka0jOLkf1-clAg`) — op `appendOrUpdate`, tab `Envelopes` — node "Append or update row in sheet4" (id `60eca980-5015-4645-bb48-78d203a8d23e`)
- [[../resources/google-sheets/1dco4c8-hld9fsgshrdlebfmx3rkjyka0jolkf1-clag|DocuSign - Envelope Registry]] (id `1dco4C8_hld9FSgshrDleBFMx3rKJYka0jOLkf1-clAg`) — op `?`, tab `Envelopes` — node "Get row(s) in sheet1" (id `eb017a1b-cab3-4d9e-8bc1-81daa7d8ba9c`)

### Google Drive

- *(dynamic)* — op `?` — node "Upload file3" (id `306cec62-5c6a-4d0c-9b2c-217452fe669e`)
- [[../resources/google-drive/14qrgijz-m12fo3ic-rwd1cytdk-swkw-|DocuSign - Files Archive]] (`folder`, id `14QrgiJz_M12fo3Ic_rwd1CYTDK-SwKw_`) — op `?` — node "Create folder1" (id `7b714f18-fde0-4e3c-a970-e5aba6a7e92f`)
- *(dynamic)* — op `?` — node "Upload file" (id `f4089812-5d16-46e9-9ef3-51fc4a49dc42`)

### Slack channels

- [[../resources/slack-channels/c09jr6ph8tx|n8n-sandbox-of-doom]] (id `C09JR6PH8TX`) — op `channel` — node "Send a message1" (id `87f7089e-40ef-4fe2-bb41-89458538d8ba`)
- [[../resources/slack-channels/c09jr6ph8tx|n8n-sandbox-of-doom]] (id `C09JR6PH8TX`) — op `channel` — node "Send a message" (id `b2bbe1b9-3abb-4449-a130-58d445360997`)

### Sub-workflows (Execute Workflow calls)

- [[docusign-download-files|DocuSign Download Files]] (n8n_id `5SQDZk06HCtloPsK`) — node "Call 'DocuSign Download Files'" (id `345e9e2e-df38-46e1-8e70-15d94de9d593`)
- [[docusign-download-files|DocuSign Download Files]] (n8n_id `5SQDZk06HCtloPsK`) — node "Refresh the access token2" (id `97873f6c-dc2b-4135-9771-16a2492564e9`)
- [[docusign-download-files|DocuSign Download Files]] (n8n_id `5SQDZk06HCtloPsK`) — node "Fetch the document" (id `f6c677be-32bc-4e4d-afb2-c091a74f8d5f`)

## Used by (workflows)

- [[docusign-download-files|DocuSign Download Files]] — node "Call 'DocuSign Download Files'" (id `345e9e2e-df38-46e1-8e70-15d94de9d593`)
- [[docusign-download-files|DocuSign Download Files]] — node "Fetch the document" (id `f6c677be-32bc-4e4d-afb2-c091a74f8d5f`)
- [[docusign-download-files|DocuSign Download Files]] — node "Refresh the access token2" (id `97873f6c-dc2b-4135-9771-16a2492564e9`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
