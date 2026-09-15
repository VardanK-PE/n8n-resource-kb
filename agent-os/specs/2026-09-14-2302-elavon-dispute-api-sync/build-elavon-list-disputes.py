#!/usr/bin/env python3
"""Compose the `Elavon API - List Disputes` sub-workflow (v1) — Task 4.

The discovery step of the Elavon dispute sync. It answers one question:
"which disputes need work this run?" and returns that list. Tasks 5-7 then
only run for cases that actually moved.

Why a rolling window instead of a watermark
-------------------------------------------
`POST /disputes/search` filters on `receivedDate` (and `expirationDate`).
Neither is a "last changed" field, so a watermark on received date would only
ever find NEWLY RECEIVED disputes. A case received 60 days ago that moves to
"Declined" today would never appear, and the sync would never write a terminal
status.

Elavon may or may not accept a filter on `updatedDateTime`. We are not relying
on it: an unrecognised filter key is SILENTLY IGNORED by this API (the
PascalCase `DisputePhaseStatus` key does exactly that), and against mocked
sandbox data a test cannot tell "the filter worked" from "the filter was
ignored". A false positive there would ship a sync that silently never notices
a status change.

So the window is a fixed trailing period long enough to cover a whole dispute
lifecycle (respond-by runs about 90 days). Re-reading every live case costs
almost nothing, because re-reading IS the search, and the search is cheap. The
expensive calls are the per-dispute detail fetches in Task 5, and those stay
gated by the change check below.

Change detection needs no extra calls: each search row already carries
`disputePhase`, `disputePhaseStatus` and `disputePhaseTimeStamp`, and that
triple is exactly what decides the PayEngine status. Fingerprint it, compare
against the last-seen value in the sync-state table, emit only what differs.

The data table
--------------
`Dispute - API Sync State` must be created in the n8n UI first - data tables
have no public API. Pass its id in and re-run:

    TABLE_ID=<id> python3 build-elavon-list-disputes.py

Expected columns:
    dispute_id       string   (the key)
    merchant_id      string
    phase            string
    phase_status     string
    phase_timestamp  string
    fingerprint      string
    last_synced_at   dateTime
    quarantined      boolean
    retry_count      number

This workflow only READS that table. Rows are written after a dispute is
actually upserted, which belongs to the orchestrator (Task 8) - marking a
dispute as synced before syncing it would lose the case on the next run.
"""
import json
import os

TABLE_ID = os.environ.get("TABLE_ID", "PLACEHOLDER_SYNC_STATE_TABLE_ID")
TABLE_NAME = "Dispute - API Sync State"

# --- Fixed references, verified against the live v1 instance ----------------
REQUEST_WORKFLOW = ("cfoYK5Jvg1yz1CA6", "Elavon API - Request")  # Task 3
GLOBAL_ERROR_WORKFLOW = "KBN9sWK9juozY766"  # Dispute - Global error handling

# Staging only, per the spec. A production Postgres node gets added at cutover
# (Task 9), mirroring how `Dispute - Update Console` carries both.
PG_STAGING = {"postgres": {"id": "7298gzDHlw0sSdFs", "name": "Postgres Staging Sandbox"}}

WORKFLOW_NAME = "Elavon API - List Disputes"

DEFAULT_WINDOW_DAYS = 180
MID_BATCH_SIZE = 100
MAX_PAGES = 25  # same cap the existing sandbox integration uses


def nid(n):
    return f"44440000-0000-4000-8000-{n:012x}"


def col(name, typ="string"):
    return {
        "id": name, "displayName": name, "required": False, "defaultMatch": False,
        "display": True, "type": typ, "readOnly": False, "removed": False,
    }


TRIGGER = {
    "id": nid(1),
    "name": "When Executed by Another Workflow",
    "type": "n8n-nodes-base.executeWorkflowTrigger",
    "typeVersion": 1.1,
    "position": [-900, 0],
    "parameters": {
        "workflowInputs": {
            "values": [
                {"name": "use_prod", "type": "boolean"},
                {"name": "window_days", "type": "number"},
                # Optional explicit MID list. Supplying it skips the database
                # lookup, which is how this gets tested: the Elavon sandbox
                # holds mocked MIDs that no PayEngine environment knows about.
                {"name": "mids", "type": "array"},
                {"name": "access_token"},
                {"name": "passthrough_item", "type": "object"},
            ]
        }
    },
}

RESOLVE_WINDOW_JS = r"""
/*
 * Work out the search window and decide whether we need the database.
 *
 * The window is a fixed trailing period, not "since last run" - see the header
 * comment in the build script. Respond-by runs about 90 days, so the default
 * comfortably covers a case from open to close.
 */
const inp = $input.first().json || {};

const windowDays = Number(inp.window_days) > 0 ? Number(inp.window_days) : DEFAULT_WINDOW_DAYS;

function ymd(d) {
  return d.toISOString().slice(0, 10);
}

const today = new Date();
const from = new Date(today.getTime() - windowDays * 86400000);

/*
 * A null MID would be sent as the literal string "null" and Elavon rejects the
 * ENTIRE search with a 400 - one bad MID blanks every result. The SQL excludes
 * them and this filter catches anything that slips through.
 */
function cleanMids(list) {
  const out = [];
  for (const mid of (list || [])) {
    const s = String(mid == null ? '' : mid).trim();
    if (s && s !== 'null' && s !== 'undefined') out.push(s);
  }
  return out;
}

const supplied = cleanMids(inp.mids);

return [{
  json: {
    use_prod: inp.use_prod === true,
    windowDays: windowDays,
    fromDate: ymd(from),
    toDate: ymd(today),
    suppliedMids: supplied,
    midsSupplied: supplied.length > 0,
    access_token: String(inp.access_token || ''),
    passthrough_item: inp.passthrough_item || {},
  }
}];
""".replace("DEFAULT_WINDOW_DAYS", str(DEFAULT_WINDOW_DAYS))

RESOLVE_WINDOW = {
    "id": nid(2),
    "name": "Resolve Window",
    "type": "n8n-nodes-base.code",
    "typeVersion": 2,
    "position": [-680, 0],
    "parameters": {"jsCode": RESOLVE_WINDOW_JS.strip()},
}

MIDS_SUPPLIED = {
    "id": nid(3),
    "name": "MIDs supplied?",
    "type": "n8n-nodes-base.if",
    "typeVersion": 2.2,
    "position": [-460, 0],
    "parameters": {
        "conditions": {
            "options": {
                "caseSensitive": True,
                "leftValue": "",
                "typeValidation": "strict",
                "version": 2,
            },
            "conditions": [
                {
                    "id": "mids-supplied",
                    "leftValue": "={{ $json.midsSupplied }}",
                    "rightValue": "",
                    "operator": {"type": "boolean", "operation": "true", "singleValue": True},
                }
            ],
            "combinator": "and",
        },
        "options": {},
    },
}

# `Elavon - MIDs` (EEFXIH6vFSgKmssi) is deliberately NOT the source here. That
# data table is fed from the Elavon BI spreadsheet, which has known sync gaps in
# both directions. A missing MID there would mean silently missing every dispute
# for that merchant. merchant_processor_detail is authoritative for who we have
# on Elavon.
GET_MIDS = {
    "id": nid(4),
    "name": "Get Elavon MIDs",
    "type": "n8n-nodes-base.postgres",
    "typeVersion": 2.6,
    "position": [-240, 140],
    "parameters": {
        "operation": "executeQuery",
        "query": (
            "SELECT DISTINCT btrim(mpd.processor_merchant_id) AS mid\n"
            "FROM merchant_processor_detail mpd\n"
            "WHERE mpd.processor_id = 'elavon'\n"
            "  AND mpd.processor_merchant_id IS NOT NULL\n"
            "  AND btrim(mpd.processor_merchant_id) <> ''\n"
            "ORDER BY 1;"
        ),
        "options": {},
    },
    "credentials": PG_STAGING,
    # An environment with no Elavon merchants must not silently stop the run.
    "alwaysOutputData": True,
}

BUILD_PLAN_JS = r"""
/*
 * Turn the MID list into page-1 search requests for `Elavon API - Request`.
 *
 * MIDs go in as an ARRAY - verified: an array works, a comma-separated string
 * is accepted and then silently ignored. They are batched because the array
 * length Elavon tolerates is not documented.
 *
 * No `disputePhaseStatus` filter. Earlier dashboard work filtered to open cases
 * because it only counted a live queue; we need closed cases too, or we could
 * never write MERCHANT_WON, MERCHANT_LOST or MERCHANT_ACCEPTED.
 */
const cfg = $('Resolve Window').first().json;

let mids = cfg.suppliedMids || [];
if (!cfg.midsSupplied) {
  const rows = $input.all().map((i) => i.json || {});
  mids = [];
  for (const r of rows) {
    const s = String(r.mid == null ? '' : r.mid).trim();
    if (s && s !== 'null' && s !== 'undefined') mids.push(s);
  }
}

if (!mids.length) {
  throw new Error(
    'Elavon dispute sync found no Elavon MIDs to search. Either the database '
    + 'has no merchant_processor_detail rows with processor_id = \'elavon\', or '
    + 'the `mids` input was empty. Refusing to run, because a search with no '
    + 'MIDs would look like "no disputes" and advance the sync quietly.'
  );
}

const batches = [];
for (let i = 0; i < mids.length; i += BATCH) {
  batches.push(mids.slice(i, i + BATCH));
}

return batches.map((batch, idx) => ({
  json: {
    batchIndex: idx,
    use_prod: cfg.use_prod,
    method: 'POST',
    path: '/disputes/search',
    body: {
      receivedDate: { fromDate: cfg.fromDate, toDate: cfg.toDate },
      merchantId: batch,
      pageMeta: {
        pageSize: 200,
        pageNumber: 1,
        sortBy: 'expirationDate',
        sortOrder: 'ascending',
      },
    },
    query: {},
    // Only the search returns pageMeta. If a body without it comes back, it is
    // another endpoint's response and the request layer rejects it.
    expect_field: 'pageMeta',
    // A batch of MIDs with no disputes is ordinary, not a failure.
    allow_no_match: true,
    access_token: cfg.access_token,
    passthrough_item: { batchIndex: idx, pageNumber: 1 },
  }
}));
""".replace("BATCH", str(MID_BATCH_SIZE))

BUILD_PLAN = {
    "id": nid(5),
    "name": "Build Search Plan",
    "type": "n8n-nodes-base.code",
    "typeVersion": 2,
    "position": [-20, 0],
    "parameters": {"jsCode": BUILD_PLAN_JS.strip()},
}

# The executeWorkflow node processes its input items one at a time, which is
# also what keeps Elavon calls serialised - concurrent calls can come back
# carrying another endpoint's body.
SEARCH_FIRST = {
    "id": nid(6),
    "name": "Search Page 1",
    "type": "n8n-nodes-base.executeWorkflow",
    "typeVersion": 1.3,
    "position": [200, 0],
    "parameters": {
        "workflowId": {
            "__rl": True,
            "value": REQUEST_WORKFLOW[0],
            "mode": "list",
            "cachedResultName": REQUEST_WORKFLOW[1],
        },
        "workflowInputs": {
            "mappingMode": "defineBelow",
            "value": {
                "use_prod": "={{ $json.use_prod }}",
                "method": "={{ $json.method }}",
                "path": "={{ $json.path }}",
                "body": "={{ $json.body }}",
                "query": "={{ $json.query }}",
                "expect_field": "={{ $json.expect_field }}",
                "allow_no_match": "={{ $json.allow_no_match }}",
                "access_token": "={{ $json.access_token }}",
                "passthrough_item": "={{ $json.passthrough_item }}",
            },
            "matchingColumns": [],
            "schema": [],
            "attemptToConvertTypes": False,
            # `body`, `query` and `passthrough_item` are objects on the other
            # side. Stringifying them here would send Elavon "[object Object]".
            "convertFieldsToString": False,
        },
        "options": {"waitForSubWorkflow": True},
    },
}

PLAN_PAGES_JS = r"""
/*
 * Page 1 of each batch told us how many pages that batch has. Emit requests for
 * the rest.
 *
 * Elavon caps pageSize at 200 - undocumented, 250 answers 400.4634.4108 - so
 * more than one page is normal once a window holds many cases.
 *
 * This node always emits at least one item. A node that receives nothing is
 * skipped in n8n, and so is everything downstream of it, which would quietly
 * drop the whole run when there happens to be only one page.
 */
const cfg = $('Resolve Window').first().json;
const plan = $('Build Search Plan').all().map((i) => i.json);
const firstPages = $input.all().map((i) => i.json || {});

const more = [];
for (const res of firstPages) {
  const pt = res.passthrough_item || {};
  const batchIndex = Number(pt.batchIndex);
  if (!Number.isInteger(batchIndex)) continue;

  // noMatch means this batch of MIDs has no disputes at all.
  if (res.noMatch) continue;

  const meta = (res.data || {}).pageMeta || {};
  let pageCount = Number(meta.pageCount) || 1;
  if (pageCount > MAX_PAGES) pageCount = MAX_PAGES;

  const base = plan[batchIndex];
  if (!base) continue;

  for (let page = 2; page <= pageCount; page += 1) {
    more.push({
      json: {
        hasMore: true,
        batchIndex: batchIndex,
        use_prod: base.use_prod,
        method: base.method,
        path: base.path,
        body: Object.assign({}, base.body, {
          pageMeta: Object.assign({}, base.body.pageMeta, { pageNumber: page }),
        }),
        query: {},
        expect_field: base.expect_field,
        allow_no_match: true,
        access_token: cfg.access_token,
        passthrough_item: { batchIndex: batchIndex, pageNumber: page },
      }
    });
  }
}

if (!more.length) {
  return [{ json: { hasMore: false } }];
}
return more;
""".replace("MAX_PAGES", str(MAX_PAGES))

PLAN_PAGES = {
    "id": nid(7),
    "name": "Plan Remaining Pages",
    "type": "n8n-nodes-base.code",
    "typeVersion": 2,
    "position": [420, 0],
    "parameters": {"jsCode": PLAN_PAGES_JS.strip()},
}

HAS_MORE = {
    "id": nid(8),
    "name": "More pages?",
    "type": "n8n-nodes-base.if",
    "typeVersion": 2.2,
    "position": [640, 0],
    "parameters": {
        "conditions": {
            "options": {
                "caseSensitive": True,
                "leftValue": "",
                "typeValidation": "strict",
                "version": 2,
            },
            "conditions": [
                {
                    "id": "has-more",
                    "leftValue": "={{ $json.hasMore }}",
                    "rightValue": "",
                    "operator": {"type": "boolean", "operation": "true", "singleValue": True},
                }
            ],
            "combinator": "and",
        },
        "options": {},
    },
}

SEARCH_REST = {
    "id": nid(9),
    "name": "Search Remaining Pages",
    "type": "n8n-nodes-base.executeWorkflow",
    "typeVersion": 1.3,
    "position": [860, -140],
    "parameters": SEARCH_FIRST["parameters"],
}

COLLECT_JS = r"""
/*
 * Gather every row from every page of every batch.
 *
 * `Search Remaining Pages` only runs when some batch had more than one page, so
 * reading it has to tolerate the node not having executed.
 */
function rowsFrom(items) {
  const out = [];
  for (const it of items) {
    const res = it.json || {};
    if (res.noMatch) continue;
    for (const row of ((res.data || {})._embedded || [])) out.push(row);
  }
  return out;
}

const rows = rowsFrom($('Search Page 1').all());

try {
  for (const row of rowsFrom($('Search Remaining Pages').all())) rows.push(row);
} catch (e) {
  // Single page across all batches - nothing more to add.
}

/*
 * The overlap between pages means a case can appear twice. Keep one row per
 * dispute, preferring the newest phase timestamp.
 */
const byId = new Map();
for (const r of rows) {
  const id = String(r.disputeId || r.externalDisputeId || '');
  if (!id) continue;
  const prev = byId.get(id);
  if (!prev || String(r.disputePhaseTimeStamp || '') > String(prev.disputePhaseTimeStamp || '')) {
    byId.set(id, r);
  }
}

return [{ json: { rows: Array.from(byId.values()), rowCount: byId.size } }];
"""

COLLECT = {
    "id": nid(10),
    "name": "Collect Rows",
    "type": "n8n-nodes-base.code",
    "typeVersion": 2,
    "position": [1080, 0],
    "parameters": {"jsCode": COLLECT_JS.strip()},
}

GET_STATE = {
    "id": nid(11),
    "name": "Get Sync State",
    "type": "n8n-nodes-base.dataTable",
    "typeVersion": 1,
    "position": [1300, 0],
    "parameters": {
        "operation": "get",
        "dataTableId": {
            "__rl": True,
            "value": TABLE_ID,
            "mode": "list",
            "cachedResultName": TABLE_NAME,
        },
        "filters": {"conditions": []},
        "limit": 10000,
    },
    # The table is empty on the first run. Without this the node emits nothing
    # and every node after it is skipped.
    "alwaysOutputData": True,
}

DETECT_JS = r"""
/*
 * The change gate. Only disputes that actually moved go on to Tasks 5-7, where
 * each case costs four serialised Elavon calls.
 *
 * The fingerprint is the phase triple, because that triple is what decides the
 * PayEngine status. Anything else changing on a dispute does not change what we
 * would write.
 *
 * Quarantined cases are re-emitted even when unchanged. An unknown status sits
 * in AWAITING_CHARGEBACK_DETAILS and has to keep alerting until a human
 * resolves it - going quiet would let the respond-by date pass.
 */
const rows = ($('Collect Rows').first().json || {}).rows || [];

const seen = new Map();
for (const it of $input.all()) {
  const r = it.json || {};
  // An empty table emits one item with no columns on it.
  if (!r || !r.dispute_id) continue;
  seen.set(String(r.dispute_id), r);
}

function fingerprint(row) {
  return [
    String(row.disputePhase || ''),
    String(row.disputePhaseStatus || ''),
    String(row.disputePhaseTimeStamp || ''),
  ].join('|');
}

const work = [];
let unchanged = 0;
let quarantineRetries = 0;

for (const row of rows) {
  const id = String(row.disputeId || row.externalDisputeId || '');
  if (!id) continue;

  const fp = fingerprint(row);
  const prev = seen.get(id);
  const changed = !prev || String(prev.fingerprint || '') !== fp;
  const quarantined = !!(prev && (prev.quarantined === true || prev.quarantined === 'true'));

  if (!changed && !quarantined) {
    unchanged += 1;
    continue;
  }
  if (!changed && quarantined) quarantineRetries += 1;

  work.push({
    // Everything Task 5 needs to address the case. A dispute has no
    // addressable URL - all of these come off the search row.
    disputeId: id,
    externalDisputeId: row.externalDisputeId || null,
    customerLocationEnterpriseId: row.customerLocationEnterpriseId || null,
    merchantId: row.merchantId != null ? String(row.merchantId) : null,
    disputePhase: row.disputePhase || null,
    disputePhaseStatus: row.disputePhaseStatus || null,
    disputePhaseTimeStamp: row.disputePhaseTimeStamp || null,

    isNew: !prev,
    wasQuarantined: quarantined,
    retryCount: prev ? Number(prev.retry_count || 0) : 0,
    fingerprint: fp,
    previousFingerprint: prev ? String(prev.fingerprint || '') : null,

    // Carried so Task 7 does not have to re-read the search row.
    searchRow: row,
  });
}

const cfg = $('Resolve Window').first().json;

return [{
  json: {
    work: work,
    summary: {
      window: { fromDate: cfg.fromDate, toDate: cfg.toDate, days: cfg.windowDays },
      found: rows.length,
      changed: work.length,
      unchanged: unchanged,
      quarantineRetries: quarantineRetries,
      newCases: work.filter((w) => w.isNew).length,
    },
    access_token: cfg.access_token,
    passthrough_item: cfg.passthrough_item,
  }
}];
"""

DETECT = {
    "id": nid(12),
    "name": "Detect Changes",
    "type": "n8n-nodes-base.code",
    "typeVersion": 2,
    "position": [1520, 0],
    "parameters": {"jsCode": DETECT_JS.strip()},
}

FINAL = {
    "id": nid(13),
    "name": "Final Output",
    "type": "n8n-nodes-base.noOp",
    "typeVersion": 1,
    "position": [1740, 0],
    "parameters": {},
}

MANUAL_TRIGGER = {
    "id": nid(14),
    "name": "When clicking 'Execute workflow'",
    "type": "n8n-nodes-base.manualTrigger",
    "typeVersion": 1,
    "position": [-1120, 220],
    "parameters": {},
}

TEST_INPUTS = {
    "id": nid(15),
    "name": "Test Inputs",
    "type": "n8n-nodes-base.set",
    "typeVersion": 3.4,
    "position": [-900, 220],
    "parameters": {
        "mode": "raw",
        "jsonOutput": json.dumps(
            {
                "use_prod": False,
                "window_days": DEFAULT_WINDOW_DAYS,
                "mids": ["REPLACE_WITH_A_REAL_ELAVON_MID"],
                "access_token": "",
                "passthrough_item": {},
            },
            indent=2,
        ),
        "options": {},
    },
}

STICKY = {
    "id": nid(16),
    "name": "Sticky Note",
    "type": "n8n-nodes-base.stickyNote",
    "typeVersion": 1,
    "position": [-1160, -420],
    "parameters": {
        "width": 1000,
        "height": 330,
        "content": (
            "## Elavon API - List Disputes\n"
            "Discovery step. Answers \"which disputes need work this run?\" and nothing else.\n\n"
            "**The window is a fixed trailing period, not a watermark.** Elavon's search filters on "
            "`receivedDate`, which is not a \"last changed\" field. A watermark on it would only find newly "
            "received disputes, so a case that moves to Declined months after it opened would never be seen "
            "and we could never write a terminal status.\n\n"
            "**Change detection costs no extra calls.** The search row already carries the phase triple "
            "(`disputePhase`, `disputePhaseStatus`, `disputePhaseTimeStamp`), and that triple is what decides "
            "the PayEngine status. It is fingerprinted and compared against `" + TABLE_NAME + "`. "
            "Only changed cases go downstream, where each one costs four serialised Elavon calls.\n\n"
            "**Quarantined cases are re-emitted even when unchanged**, so an unknown status keeps alerting "
            "until a human resolves it.\n\n"
            "**This workflow only reads the state table.** Rows are written after a dispute is really "
            "upserted (Task 8). Writing here would lose the case if the upsert then failed.\n\n"
            "**MIDs come from `merchant_processor_detail`**, not from the `Elavon - MIDs` data table - that "
            "one is fed from the BI spreadsheet and has known gaps. Pass `mids` explicitly to skip the "
            "database, which is how this is tested against sandbox MIDs."
        ),
    },
}

WORKFLOW = {
    "name": WORKFLOW_NAME,
    "nodes": [
        TRIGGER, RESOLVE_WINDOW, MIDS_SUPPLIED, GET_MIDS, BUILD_PLAN,
        SEARCH_FIRST, PLAN_PAGES, HAS_MORE, SEARCH_REST, COLLECT,
        GET_STATE, DETECT, FINAL, MANUAL_TRIGGER, TEST_INPUTS, STICKY,
    ],
    "connections": {
        "When Executed by Another Workflow": {
            "main": [[{"node": "Resolve Window", "type": "main", "index": 0}]]
        },
        "When clicking 'Execute workflow'": {
            "main": [[{"node": "Test Inputs", "type": "main", "index": 0}]]
        },
        "Test Inputs": {
            "main": [[{"node": "Resolve Window", "type": "main", "index": 0}]]
        },
        "Resolve Window": {
            "main": [[{"node": "MIDs supplied?", "type": "main", "index": 0}]]
        },
        # true  -> caller gave us MIDs, skip the database
        # false -> look them up
        "MIDs supplied?": {
            "main": [
                [{"node": "Build Search Plan", "type": "main", "index": 0}],
                [{"node": "Get Elavon MIDs", "type": "main", "index": 0}],
            ]
        },
        "Get Elavon MIDs": {
            "main": [[{"node": "Build Search Plan", "type": "main", "index": 0}]]
        },
        "Build Search Plan": {
            "main": [[{"node": "Search Page 1", "type": "main", "index": 0}]]
        },
        "Search Page 1": {
            "main": [[{"node": "Plan Remaining Pages", "type": "main", "index": 0}]]
        },
        "Plan Remaining Pages": {
            "main": [[{"node": "More pages?", "type": "main", "index": 0}]]
        },
        # true  -> fetch pages 2..N
        # false -> one page was enough
        "More pages?": {
            "main": [
                [{"node": "Search Remaining Pages", "type": "main", "index": 0}],
                [{"node": "Collect Rows", "type": "main", "index": 0}],
            ]
        },
        "Search Remaining Pages": {
            "main": [[{"node": "Collect Rows", "type": "main", "index": 0}]]
        },
        "Collect Rows": {
            "main": [[{"node": "Get Sync State", "type": "main", "index": 0}]]
        },
        "Get Sync State": {
            "main": [[{"node": "Detect Changes", "type": "main", "index": 0}]]
        },
        "Detect Changes": {
            "main": [[{"node": "Final Output", "type": "main", "index": 0}]]
        },
    },
    "settings": {
        "executionOrder": "v1",
        "callerPolicy": "workflowsFromSameOwner",
        "availableInMCP": False,
        "errorWorkflow": GLOBAL_ERROR_WORKFLOW,
    },
}


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "elavon-list-disputes.json")
    with open(out, "w") as fh:
        json.dump(WORKFLOW, fh, indent=2)
        fh.write("\n")
    print(f"wrote {out}")
    if TABLE_ID.startswith("PLACEHOLDER"):
        print(f"NOTE: data table id is a placeholder. Create '{TABLE_NAME}' in the n8n UI,")
        print("      then re-run with TABLE_ID=<id> and PUT the result.")
