---
type: http-url
resource_id: "pcicompliancemanager.com"
current_name: "pcicompliancemanager.com"
aliases: ["pcicompliancemanager.com"]
auto_generated_at: 2026-08-19T19:25:44Z
---

<!-- auto:start -->

# pcicompliancemanager.com

- **Resource id (canonical):** `pcicompliancemanager.com`
- **Current name:** pcicompliancemanager.com
- **Host:** `pcicompliancemanager.com`

## Used by

- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `GET https://pcicompliancemanager.com/services/webapi/v2/attestations/create?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Create Attestation" (id `6f8db8cd-7b45-4a4a-90e2-45c00058e8f5`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `GET https://pcicompliancemanager.com/services/webapi/v2/attestations/download/{{ $json.data.validatedAocId }}?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Get Attestation Download Link" (id `a1f917f0-576e-4ab9-996a-faa20ce66f60`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `GET https://pcicompliancemanager.com/services/webapi/v2/profile-answers?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Get Profile Answers" (id `a6522a35-7151-4168-a76f-023ab6fcb459`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `GET https://pcicompliancemanager.com/services/webapi/v2/status?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Get Account Status" (id `720a081c-d779-48de-98c9-4b33600235bd`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `GET https://pcicompliancemanager.com/services/webapi/v2/status?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Get Attestation Details" (id `27b19e80-a27f-4007-a9b4-caf5b084a47f`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `GET https://pcicompliancemanager.com/services/webapi/v2/users/success` — node "Get Account Details" (id `586ef2f5-3b1c-4250-8c80-1884090ba3ea`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `GET https://pcicompliancemanager.com/services/webapi/v2/users/{{ $('Get Account Details').item.json.data.id }}?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Get User Details" (id `48824e0d-e472-4450-8f1e-df16936d0ae7`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `GET https://pcicompliancemanager.com{{ $json.data.downloadLink }}` — node "Download" (id `0d75bf06-3c01-4450-8d25-4d173299eb84`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `POST https://pcicompliancemanager.com/services/clientapi/login` — node "Get Access Token" (id `3387a6ea-1a63-4b73-b5c0-ad9f042aff24`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `POST https://pcicompliancemanager.com/services/webapi/v2/attestations?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Submit Attestation" (id `03178057-d677-4504-8c69-2b21ccd41721`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `POST https://pcicompliancemanager.com/services/webapi/v2/profile-answers?apId={{ $('Get Account Details').item.json.data.apId }}` — node "POST Business Profile" (id `3bc4c362-cbde-42ce-8782-99cfebd04e2e`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `POST https://pcicompliancemanager.com/services/webapi/v2/saq/answerQuestion?apId={{ $('Get Account Details').item.json.data.apId }}` — node "POST SAQ Answers" (id `00ad2101-e669-4b1e-a8e7-7da9adae09a8`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `POST https://pcicompliancemanager.com/services/webapi/v2/user/forgottenPasswords` — node "Password Reset Request" (id `f26c75f9-47c9-46e9-bf56-309c22e0cb1f`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `POST https://pcicompliancemanager.com/services/webapi/v2/user/resetPassword/` — node "Reset Password" (id `6dd46b15-653e-4ce2-89e2-2244490b066d`)
- [[../../workflows/pci-compliance-manager-automation|PCI Compliance Manager Automation]] — `POST https://pcicompliancemanager.com/services/webapi/v2/users/{{ $('Get Account Details').item.json.data.id }}/update?apId={{ $('Get Account Details').item.json.data.apId }}` — node "Personalize-Register" (id `f95688fd-bae6-4e07-9bdb-85f3ae854cdf`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
