---
type: data-table
instance: v1
resource_id: "EEFXIH6vFSgKmssi"
current_name: "EEFXIH6vFSgKmssi"
aliases: ["EEFXIH6vFSgKmssi","Elavon - MIDs"]
auto_generated_at: 2026-08-28T21:31:11Z
---

<!-- auto:start -->

# EEFXIH6vFSgKmssi

- **Resource id (canonical):** `EEFXIH6vFSgKmssi`
- **Current name:** EEFXIH6vFSgKmssi
- **Historical aliases:**
  - EEFXIH6vFSgKmssi
  - Elavon - MIDs
- **Table ID:** `EEFXIH6vFSgKmssi`

## Used by

- [[../../workflows/elavon-mids-to-data-tables-sync|Elavon MIDs to Data Tables sync]] — node "Upsert row(s)" (id `56e23460-b942-4a32-b554-6644b3e5808c`)
- [[../../workflows/njord-api|Njord API]] — node "Fetch Dash PCI" (id `87bb287a-17ab-4b59-943d-fdec9bdbcf63`)
- [[../../workflows/njord-api|Njord API]] — node "Lookup PCI" (id `db6f3467-0b5e-488d-b552-c43dda220fc2`)

<!-- auto:end -->

<!-- manual:start -->

## Role: the merchants table for Elavon work

Keyed on `MID` (Elavon's 10-digit processor merchant id, stored as **number**). Verified
2026-09-02: **2537 rows, every one populated for both `MCC` and `DBA`** (0 missing), across
**94 distinct MCCs**.

> [!warning] No longer used by the CCO enrollment workflow (changed 2026-09-07)
> `Elavon CCO - Edit merchant application (CCO Enrollment)`
> ([[../../workflows/elavon-cco-edit-merchant-application-cco-enrollment]]) used to
> resolve both `MCC` and `DBA` from this table. It now takes **both from Postgres**, and its
> `Get Elavon MCC` node was deleted. This table is still used by
> `Elavon MIDs to Data Tables sync` and `Njord API` — see the auto block.
>
> Two reasons for the move, in order of weight:
> 1. **Staleness.** `Last_Sync` spans `2025-11-11 .. 2026-03-14` — roughly 6 months old at
>    the time. Two of the CCO-eligible merchants were absent entirely, including the only
>    one with a retrievable signed document, so the workflow could never complete a run.
> 2. **No PayEngine UUID.** The workflow is driven by `merchant_id`, so every read needed a
>    UUID→MID hop, and MID is not unique (`8046096999` maps to two merchants).
>
> The trade-off is real and worth re-checking if the eligible set grows: Postgres holds the
> MCC the merchant *applied* with, this table holds what Elavon *boarded*, and they
> genuinely differ for ~11% of merchants. Detail in
> [[../databases/postgres-bdw1qodl0v7mywj6]] → "MCC lives in `merchant.data`".

Historically this was the source of record for the two attributes the CCO enrollment form
needs:

- `MCC` (number) — looked up against [[kepdpgqsjwflp5lz|Elavon - MCC Commodity Codes]] to
  get the Item Commodity Code / Item Description that go on the DATA FIELD ENHANCEMENTS
  SCHEDULE page.
- `DBA` (string) — replaces the `(“Company”)` placeholder in the signature block.
  Note the CCO workflow now prefers PayEngine's `business_details.dba.name`: this column is
  uppercased, depunctuated and truncated at 32 chars (e.g.
  `"SERVICEMASTER RESTORATION BY BUI"`), which is wrong for a signature block.

### Joining to the commodity-code table

`Elavon - MIDs.MCC` is a **number**; `Elavon - MCC Commodity Codes.mcc_code` is a
**string stored verbatim from Elavon's guide** (unpadded, so `742` not `0742`). They join
via `String(MCC)`. Do **not** zero-pad the commodity table to 4 digits — three guide rows
(`742`, `763`, `780`) would then stop matching `String(742)`.

### Coverage gap

92 of the 94 distinct MCCs in this table exist in the commodity guide. The two that do not:

| MCC | Category | Merchants |
|---|---|---|
| 5812 | Eating places / restaurants | 2 |
| 7011 | Lodging / hotels | 2 |

4 of 2537 merchants (0.1%). Almost certainly deliberate on Elavon's side — Commercial Card
Optimization / Level 3 data does not apply to restaurant and lodging MCCs. CCO enrollment
must therefore fail closed for these rather than substitute a default commodity code.

### No PayEngine merchant UUID column

There is no PE merchant UUID here, so a workflow starting from one cannot reach this table
directly. Two known bridges:

- `Merchants activity status` ([[l62ngzosdxe1ef3j]]) holds `merchant_id` (PE UUID) + `mid`.
- Postgres (`Postgres Production`, `BDw1qoDl0V7mYwj6`): `merchant_processor_detail
  .processor_merchant_id` is the MID, joined via `merchant.id`. See
  `Residuals Generator V7 (ACTIVE)` for a working query.

<!-- manual:end -->
