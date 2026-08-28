---
type: http-url
instance: v1
resource_id: "sandbox.elavonapi.com"
current_name: "sandbox.elavonapi.com"
aliases: ["sandbox.elavonapi.com"]
auto_generated_at: 2026-08-19T19:25:44Z
---

<!-- auto:start -->

# sandbox.elavonapi.com

- **Resource id (canonical):** `sandbox.elavonapi.com`
- **Current name:** sandbox.elavonapi.com
- **Host:** `sandbox.elavonapi.com`

## Used by

- [[../../workflows/my-workflow-6|My workflow 6]] — `GET https://sandbox.elavonapi.com/service/dispute-management/v2/disputes/{{ $('Set search params').first().json.disputeId }}/documents` — node "Get Dispute Documents" (id `d05be302-7c83-4996-a9dc-0a2dde578766`)
- [[../../workflows/my-workflow-6|My workflow 6]] — `GET https://sandbox.elavonapi.com/service/dispute-management/v2/disputes/{{ $('Set search params').first().json.disputeId }}/history` — node "Get Dispute History" (id `410ac07e-c68e-47e8-8929-dd1f73c5287f`)
- [[../../workflows/my-workflow-6|My workflow 6]] — `GET https://sandbox.elavonapi.com/service/dispute-management/v2/disputes/{{ $('Set search params').first().json.disputeId }}/phases/{{ $('Set search params').first().json.disputePhase }}/documents/{{ $('Set search params').first().json.disputeDocumentId }}` — node "Get Dispute Document" (id `49dfb261-a8a5-46fe-8bd3-f0a6db7f3342`)
- [[../../workflows/my-workflow-6|My workflow 6]] — `GET https://sandbox.elavonapi.com/service/dispute-management/v2/disputes/{{ $('Set search params').first().json.disputeId }}/phases/{{ $('Set search params').first().json.disputePhase }}/documents` — node "Get Dispute Phase Documents" (id `cb066964-c0ee-4ee7-a89a-8eacb8361587`)
- [[../../workflows/my-workflow-6|My workflow 6]] — `GET https://sandbox.elavonapi.com/service/dispute-management/v2/disputes/{{ $('Set search params').first().json.disputeId }}/phases/{{ $('Set search params').first().json.disputePhase }}` — node "Get Dispute Phase" (id `4d84a0e7-02f3-4b1b-ad16-c5c6389854ce`)
- [[../../workflows/my-workflow-6|My workflow 6]] — `GET https://sandbox.elavonapi.com/service/dispute-management/v2/disputes/{{ $('Set search params').first().json.disputeId }}/transaction` — node "Get Dispute Transaction" (id `23ebaf40-9d29-4545-9b28-9f1f975f7334`)
- [[../../workflows/my-workflow-6|My workflow 6]] — `GET https://sandbox.elavonapi.com/service/dispute-management/v2/disputes/{{ $('Set search params').first().json.disputeId }}` — node "Get Dispute Details" (id `865930a3-96b4-4d4c-a7d5-cd08ad0d37ed`)
- [[../../workflows/my-workflow-6|My workflow 6]] — `GET https://sandbox.elavonapi.com/service/dispute-management/v2/disputes` — node "Get Disputes" (id `fa764c03-25e8-4c47-b817-6fbf5ac2da5a`)
- [[../../workflows/my-workflow-6|My workflow 6]] — `POST https://sandbox.elavonapi.com/oauth2/client-credentials/v2/token` — node "Get OAuth Token" (id `35bb6352-9a1a-4f30-9ccb-8961ae1edae5`)
- [[../../workflows/my-workflow-6|My workflow 6]] — `POST https://sandbox.elavonapi.com/service/dispute-management/v2/disputes/accept` — node "Post dispute accept" (id `eefd2080-128a-454c-aa08-ecfd170fa4dc`)
- [[../../workflows/my-workflow-6|My workflow 6]] — `POST https://sandbox.elavonapi.com/service/dispute-management/v2/disputes/search` — node "Search Dispute (Filter)" (id `16e26b54-b46d-41e4-b67b-d56b9688c909`)
- [[../../workflows/my-workflow-6|My workflow 6]] — `POST https://sandbox.elavonapi.com/service/dispute-management/v2/disputes/{{ $('Set search params').first().json.disputeId }}/documents` — node "Post dispute document" (id `be804487-f34e-4769-905e-ee41d5387065`)
- [[../../workflows/my-workflow-6|My workflow 6]] — `POST https://sandbox.elavonapi.com/service/dispute-management/v2/disputes/{{ $('Set search params').first().json.disputeId }}/response` — node "Post dispute response" (id `64d8e4fb-d568-4af7-86e4-4ea517104ad1`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Add owner, criticality, runbook URL, rotation cadence, etc. -->

<!-- manual:end -->
