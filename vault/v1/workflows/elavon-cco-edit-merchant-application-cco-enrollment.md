---
n8n_id: "Q16AhMTvfmtLzuI6"
instance: v1
name: "Elavon CCO - Edit merchant application (CCO Enrollment)"
status: inactive
last_modified: 2026-09-08T17:39:22.075Z
tags: []
fingerprint: "a24487a2a60d2eae9c418133fec2a980193f35d472f2b8d2b7bf1f972d16ccb5"
auto_generated_at: 2026-09-08T19:06:15Z
---

<!-- auto:start -->

# Elavon CCO - Edit merchant application (CCO Enrollment)

## Summary

- **Status:** inactive
- **n8n ID:** `Q16AhMTvfmtLzuI6`
- **Nodes:** 10
- **Last modified:** 2026-09-08T17:39:22.075Z

## Triggers

- **execute-workflow** — node "When Executed by Another Workflow" (id `4ae282fe-2261-4c54-8cd3-6638f30aabbc`)
- **manual** — node "When clicking ‘Execute workflow’" (id `d9721d26-c2a1-4b8b-bb2b-5e7ab9da6366`)

## Depends on

### Credentials

- [[../resources/credentials/bdw1qodl0v7mywj6|Postgres Production]] (`postgres`, id `BDw1qoDl0V7mYwj6`) — node "Eligibility + merchant data" (id `5a942ad4-bff0-4009-bba8-e31f87423879`)
- [[../resources/credentials/z7egngearoj2smhw|PE Master Bearer Token]] (`httpBearerAuth`, id `Z7eGNGEAroj2SMhw`) — node "HTTP Request" (id `e673fe53-920d-4baa-a0c5-c01f32d4ce3d`)

### HTTP URLs

- [[../resources/http-urls/console-payengine-co|console.payengine.co]] — `GET https://console.payengine.co/api/merchant/{{ $json.merchant_id }}/download-signed-document` — node "HTTP Request" (id `e673fe53-920d-4baa-a0c5-c01f32d4ce3d`)

### Databases

- [[../resources/databases/postgres-bdw1qodl0v7mywj6|postgres (via Postgres Production)]] — op `executeQuery` — node "Eligibility + merchant data" (id `5a942ad4-bff0-4009-bba8-e31f87423879`)

### Data tables (n8n)

- [[../resources/data-tables/kepdpgqsjwflp5lz|Elavon - MCC Commodity Codes]] (id `kEpDpGqSjWFlP5LZ`) — op `get` — node "Get commodity code" (id `a8c0446d-145b-4403-a7cc-ba035790ac48`)

## Used by (workflows)

- [[elavon-cco-enrollment-monitor|Elavon CCO - Enrollment Monitor]] — node "Build CCO PDF" (id `11110000-0000-4000-8000-00000000000b`)

<!-- auto:end -->

<!-- manual:start -->

## Purpose

Given a PayEngine `merchant_id`, checks CCO eligibility, resolves the four values the form
needs, downloads the merchant's signed agreement, fills the Commercial Card Optimization
pages and returns **just those 3 pages** as a PDF binary (555 kB in → 156 kB out).

Called by [[elavon-cco-enrollment-monitor]]. **Reverse-migrated from v2 to v1 on
2026-08-31** (v2 id `7kB7kmRDMjt8K1hc`) because v2 blocks `require('child_process')`, which
the PDF extraction needs — see the PDF constraints below. Migrating back meant clamping
typeVersions down to the 1.123.18 ceilings: `set` 3.4, `httpRequest` 4.3, `code` 2.

## Two entry points

| Trigger | Use |
|---|---|
| `When clicking 'Execute workflow'` → `Edit Fields` | Ad-hoc single merchant; set `merchant_id` in `Edit Fields`. |
| `When Executed by Another Workflow` | Sub-workflow call; `merchant_id` arrives via `workflowInputs`. |

**Both paths must stay entry-point agnostic.** `Eligibility + merchant data` and
`HTTP Request` originally referenced `$('Edit Fields')`, which broke the sub-workflow path
immediately (`Node 'Edit Fields' hasn't been executed`). They now read `$json.merchant_id`,
which works from either trigger because both emit that field. **Do not reintroduce a
`$('Edit Fields')` reference anywhere.**

## Guards, in this order

1. **Partner** — `account_settings.enable_cco_form = 'yes'`. First because only 2 of ~30
   partners are enabled, so it eliminates the most work.
2. **Pricing** — `pricingMethod = 'INTERCHANGE_PLUS'`. Both gates are INNER JOINs so a
   merchant with no fee schedule fails closed (89 of 557 partner-enabled merchants have no
   fee schedule).
3. Then requires an Elavon MID and a usable MCC.

Grounded in the CCO document itself, whose page 22 states that switching to "flat, fixed or
tiered pricing will automatically terminate this Commercial Card Optimization Enrollment".

## MCC source changed 2026-09-07

Was [[../resources/data-tables/eefxih6vfsgkmssi|Elavon - MIDs]] via a `Get Elavon MCC`
node; now `merchant.data->'business_type'->>'mcc_sic'` in the same eligibility query, and
that node is deleted. The table was ~6 months stale and missing eligible merchants.
Full reasoning and the ~11% MCC divergence measurement live in
[[../resources/databases/postgres-bdw1qodl0v7mywj6]].

`Check guards` normalises `mcc_sic` because it is free text: strips leading zeros (`0742` →
`742`, since the guide stores codes unpadded) and rejects non-numeric values (`5999J`)
rather than coercing them.

## PDF handling — hard-won constraints

The signed document is **flattened** (23 pages, `getForm()` succeeds but `field_count: 0`),
so pdf-lib's AcroForm path is unavailable and coordinate-based text extraction is genuinely
required.

- **pdfjs cannot be `require`d in the Code-node sandbox** at any version — its UMD bundle
  manipulates `Error` prototypes across VM realms and throws at `util.js`
  `BaseExceptionClosure`. Worked around by running it in a real Node subprocess via
  `execSync`. Do not spend time trying other versions.
- pdfjs writes a `Cannot polyfill DOMMatrix` / `Cannot find module 'canvas'` warning to
  **stdout**, so the extractor returns JSON via an output **file**, not the pipe.
- Pass the raw Buffer from `getBinaryDataBuffer` straight to `PDFDocument.load()` — wrapping
  it in `new Uint8Array(...)` across realms yields a NaN-length array.
- Use `$input.all()`; `this.getInputData()` does not exist. `this.helpers.*` does work.
- The module installer checks the installed **version** from `package.json`, not just
  `require.resolve()` — the host already had pdfjs-dist 5.x (ESM-only), which made the first
  failure look like a bad path.

The CCO pages are located by **anchoring on text**, not page number — the form sits at pages
21-23 of a 23-page agreement, and page 22 holds the `(“Company”)` placeholder that gets
replaced with the merchant's DBA.

## Known limitations

- The original `(“Company”)` text is still in the PDF's text layer; the DBA is drawn over a
  white rectangle. Visually correct, but the old string is recoverable by text extraction.
- Output filename is still `<merchant_id>-agreement.pdf` although the content is now the
  3-page CCO extract, not the full agreement.
- DBA comes from PayEngine's `business_details.dba.name`, which is a **double-encoded JSON
  string** — parsed defensively in a Code node because a `::jsonb` cast in SQL hard-errors
  on malformed values.

<!-- manual:end -->
