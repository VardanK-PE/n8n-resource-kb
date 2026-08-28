---
n8n_id: "gJfB9BKQfkmsXvyt"
instance: v1
name: "Billing System - Get merchant platform fees"
status: inactive
last_modified: 2026-05-27T22:12:13.700Z
tags: []
fingerprint: "0c1665cef5a49081fdd0b57f3d5965c15af2e8ede780f8c473e7ddfeeba27bd9"
auto_generated_at: 2026-06-01T22:51:45Z
---

<!-- auto:start -->

# Billing System - Get merchant platform fees

## Summary

- **Status:** inactive
- **n8n ID:** `gJfB9BKQfkmsXvyt`
- **Nodes:** 49
- **Last modified:** 2026-05-27T22:12:13.700Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `a3fb5232-f3f9-49cf-92a2-0b23c0462a82`)

## Depends on

### Credentials

- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get TokenExchange Count" (id `1c13bad9-34ab-436a-a949-c69952790eb6`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Gateway Count" (id `1ef7e153-fb06-4877-8535-fb2f4b137cbb`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count2" (id `21824331-aa8b-427d-9bc8-a040e9e3d4ed`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count1" (id `24c42a32-9ccc-4b1c-a29f-61d9021555ad`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Gateway Count1" (id `29bd52bf-930d-4eca-9f4d-a6541de06860`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count iOS Softpos" (id `41bce9a8-a8d8-44d1-bf38-b7fbbb5b846a`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count Android Softpos1" (id `47fabc3a-533d-43dc-a7f3-e2a2760ace65`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get NT Count" (id `49072464-79d1-4405-b340-1b4f613cab81`)
- [[../resources/credentials/jc4f45um3ujq28gc|PF Prod Device Management Replica]] (`postgres`, id `JC4f45um3UjQ28Gc`) — node "Get EMV Device Count" (id `549348e4-582c-4793-b9dd-b232d31da8b8`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens2" (id `56fe67eb-e381-474b-b83c-ac069badce27`)
- [[../resources/credentials/jc4f45um3ujq28gc|PF Prod Device Management Replica]] (`postgres`, id `JC4f45um3UjQ28Gc`) — node "Get EMV Device Count1" (id `67c0461f-8c13-43de-8cd7-71aa7272c661`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Merchant Applications Count1" (id `79576652-e438-4c2e-899a-fcf6816d804f`)
- [[../resources/credentials/b9eqlthyefjazsbz|Google Sheets account (Main One Used)]] (`googleApi`, id `B9eqlthYefJAzSbz`) — node "Get partner billing terms" (id `859845d0-141e-45a4-9af0-cbe0c59978ce`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens" (id `933a8739-0096-428f-a83f-e94c7eaa979b`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count iOS Softpos1" (id `a9e10d5b-7922-41d4-8b41-737c0efa1404`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens3" (id `b198c6ca-1aad-4496-b4da-d85890c099c2`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get NT Count1" (id `d298f233-34db-40d9-8f1e-7c7c4822160f`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count Android Softpos" (id `d957e442-96cb-424e-b653-4e6867d68db6`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Transaction Count" (id `e0fb6d94-6994-43fa-a67c-f636f6d12632`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens4" (id `e86b07e9-cdf5-4d7f-920b-b28160f37c7d`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Merchant Applications Count" (id `e95379c4-be52-413d-842b-da34f8139d31`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get TokenExchange Count1" (id `eeabd4ce-b445-4792-9f85-9082478225bb`)
- [[../resources/credentials/yyswj2rzpvonc8wa|Production / ST - Read Replica Auto Credential]] (`postgres`, id `yysWJ2rZpvONC8WA`) — node "Get Tokens1" (id `f6a3c393-2725-451c-aa8c-3471ee89eb90`)

### Databases

- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get TokenExchange Count" (id `1c13bad9-34ab-436a-a949-c69952790eb6`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Gateway Count" (id `1ef7e153-fb06-4877-8535-fb2f4b137cbb`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count2" (id `21824331-aa8b-427d-9bc8-a040e9e3d4ed`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count1" (id `24c42a32-9ccc-4b1c-a29f-61d9021555ad`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Gateway Count1" (id `29bd52bf-930d-4eca-9f4d-a6541de06860`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count iOS Softpos" (id `41bce9a8-a8d8-44d1-bf38-b7fbbb5b846a`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count Android Softpos1" (id `47fabc3a-533d-43dc-a7f3-e2a2760ace65`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get NT Count" (id `49072464-79d1-4405-b340-1b4f613cab81`)
- [[../resources/databases/postgres-jc4f45um3ujq28gc|postgres (via PF Prod Device Management Replica)]] — op `executeQuery` — node "Get EMV Device Count" (id `549348e4-582c-4793-b9dd-b232d31da8b8`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens2" (id `56fe67eb-e381-474b-b83c-ac069badce27`)
- [[../resources/databases/postgres-jc4f45um3ujq28gc|postgres (via PF Prod Device Management Replica)]] — op `executeQuery` — node "Get EMV Device Count1" (id `67c0461f-8c13-43de-8cd7-71aa7272c661`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Merchant Applications Count1" (id `79576652-e438-4c2e-899a-fcf6816d804f`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens" (id `933a8739-0096-428f-a83f-e94c7eaa979b`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count iOS Softpos1" (id `a9e10d5b-7922-41d4-8b41-737c0efa1404`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens3" (id `b198c6ca-1aad-4496-b4da-d85890c099c2`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get NT Count1" (id `d298f233-34db-40d9-8f1e-7c7c4822160f`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count Android Softpos" (id `d957e442-96cb-424e-b653-4e6867d68db6`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Transaction Count" (id `e0fb6d94-6994-43fa-a67c-f636f6d12632`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens4" (id `e86b07e9-cdf5-4d7f-920b-b28160f37c7d`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Merchant Applications Count" (id `e95379c4-be52-413d-842b-da34f8139d31`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get TokenExchange Count1" (id `eeabd4ce-b445-4792-9f85-9082478225bb`)
- [[../resources/databases/postgres-yyswj2rzpvonc8wa|postgres (via Production / ST - Read Replica Auto Credential)]] — op `executeQuery` — node "Get Tokens1" (id `f6a3c393-2725-451c-aa8c-3471ee89eb90`)

### Google Sheets

- [[../resources/google-sheets/1cum3jrfqqgrvh8xtgacsn-imf4bvryzjwgrcz7bi6lo|Partner Residuals Terms]] (id `1CuM3JRFqqgrvH8XTgACSN-ImF4BVryzjwGRcZ7bi6lo`) — op `?`, tab `Terms` — node "Get partner billing terms" (id `859845d0-141e-45a4-9af0-cbe0c59978ce`)

## Used by (workflows)

- [[billing-system-generate-invoices-for-billing-period|Billing System - Generate Invoices for Billing Period]] — node "Call 'Billing System - Get merchant platform fees'" (id `859b7296-ab39-428d-8dc2-21b1110b46f6`)

<!-- auto:end -->

<!-- manual:start -->

<!-- Human-authored content. Add owner, criticality, runbook URL, business purpose, etc. -->

<!-- manual:end -->
