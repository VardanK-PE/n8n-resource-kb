---
n8n_id: "1u22D61vqFen7q0m"
instance: v1
name: "Elavon CCO - Submit Qualtrics form"
status: inactive
last_modified: 2026-09-08T18:49:19.610Z
tags: []
fingerprint: "3350dc7549c0b5a1b7004eba95d58f9669c01f3b1abb0780bf8b3db77d20745b"
auto_generated_at: 2026-09-08T19:06:15Z
---

<!-- auto:start -->

# Elavon CCO - Submit Qualtrics form

## Summary

- **Status:** inactive
- **n8n ID:** `1u22D61vqFen7q0m`
- **Nodes:** 4
- **Last modified:** 2026-09-08T18:49:19.610Z

## Triggers

- **manual** — node "When clicking ‘Execute workflow’" (id `77770000-0000-4000-8000-000000000001`)
- **execute-workflow** — node "When Executed by Another Workflow" (id `77770000-0000-4000-8000-000000000002`)

## Used by (workflows)

- [[elavon-cco-enrollment-monitor|Elavon CCO - Enrollment Monitor]] — node "Submit CCO form" (id `11110000-0000-4000-8000-00000000000c`)

<!-- auto:end -->

<!-- manual:start -->

## Purpose

Fills Elavon's **Payment Optimization CCO Request Form**
(`usbank.az1.qualtrics.com/jfe/form/SV_9SvtaSacONfKrpI`) with Playwright, driving a remote
Chrome over CDP, attaches the merchant's CCO PDF, and returns a full-page screenshot as
evidence. Called by [[elavon-cco-enrollment-monitor]]. Built 2026-09-08 after Elavon refused
email intake.

**`submit` defaults to false** — the default run fills the form and stops. The caller can
override it; the monitor passes `'true'` only when its own `delivery_mode` is `submit`.

## Field map (read from the rendered DOM, which is authoritative)

| QID | Field | Control |
|---|---|---|
| QID3 | Doing Business As Name | `#question-QID3 input[type=text]` |
| QID4 | Partner Short Name | `#question-QID4 input[type=text]` |
| QID5 | Contact First / Last | `#form-text-input-QID5-1` / `-2` |
| QID6 | Partner Phone Number | `#question-QID6 input[type=text]` |
| QID7 | Partner Contact Email | `#question-QID7 input[type=text]` |
| QID10 | Merchant Share Rate | `div#QID10[role=combobox]` — 25% / 50% |
| QID11 | Partner Share Rate is 0% | radio `#mc-choice-input-QID11-1` |
| QID12 | Partner Share Rate is | radio `#mc-choice-input-QID12-1` |
| QID14 | Portfolio Manager | `div#QID14[role=combobox]` — 31 names |
| QID16 | **CCO Form 1** (required) | file `#file-upload-QID16` |
| QID19–22 | CCO Form 2–5 | file |
| QID17 | Additional MIDs Spreadsheet | file |
| QID18 | Additional Notes | textarea — **left blank, see below** |
| — | Submit | `#next-button` |

The form's encoded question definitions disagree with the rendered DOM about QID17 and
QID22 — **trust the DOM**. QID17 is the MIDs spreadsheet and QID22 is CCO Form 5, the
reverse of what the encoded definitions imply. No recaptcha.

## Nothing may reveal that this is automated

**Additional Notes (QID18) is deliberately left blank** and the capability to write it was
removed from the code. An earlier version wrote "Submitted by the CCO Enrollment Monitor…"
into that field, which would have been visible to Elavon. The attached PDF is likewise named
`<DBA> CCO Enrollment.pdf` rather than the PayEngine merchant UUID the builder generates.

## The share-rate fields interlock

Elavon takes 50% fixed. Selecting QID10 = 25% reveals **only** QID12 (partner keeps the
remaining 25%); selecting 50% would reveal QID11 (partner gives their share up). They are
display-logic alternatives, which is why both render on a blank form. The code asserts
exactly one is visible and **throws otherwise** — guessing here would misstate commercial
terms on a submitted enrollment.

## Browser connection

`browser_url` is configuration. Production is the internal Browserless
(`ws://pf-prod-ecs-task-container-browserless:3000?token=…`); development is an ngrok tunnel
to a local Chrome. Two things learned the hard way:

- **Chrome's DevTools endpoint rejects a `Host` header that is not an IP or `localhost`**,
  so an ngrok tunnel 500s. The code sends `headers: { Host: 'localhost' }` automatically
  when the URL looks like ngrok.
- **`page.setViewportSize()` does not re-lay-out a CDP-attached real Chrome.** It reported
  1600×1200 while the page stayed 800px wide, so screenshots were cropped to about half the
  width. `Emulation.setDeviceMetricsOverride` via a CDP session does force it; the code also
  widens to the document if it overflows.

Playwright cannot run a browser *inside* the n8n container — it is Alpine/musl with none of
Chromium's shared libraries and no root. Always connect to a remote browser.

## It fails loudly, by design

Throws — and records nothing as submitted — on: a missing required value (before opening a
browser at all), a selector that does not resolve, a dropdown option that is not on the form
(listing what *is* available), an ambiguous share-rate state, and, when submitting, the form
still being displayed or no confirmation text found. Errors carry a screenshot of the page
as it broke.

<!-- manual:end -->
