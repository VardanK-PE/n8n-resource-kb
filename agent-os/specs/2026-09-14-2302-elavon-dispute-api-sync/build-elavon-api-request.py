#!/usr/bin/env python3
"""Compose the `Elavon API - Request` sub-workflow (v1) — Task 3.

This is the shared auth + call layer for the Elavon dispute sync. Every Elavon
call in Tasks 4-6 goes through it, so the sandbox quirks are handled once.

Writes the create/update payload to elavon-api-request.json. Push it with:

    scripts/n8n-api.sh v1 /api/v1/workflows \\
      -X POST -H 'Content-Type: application/json' \\
      --data-binary @agent-os/specs/.../elavon-api-request.json

To update an existing workflow, use PUT /api/v1/workflows/<id> instead.
"""
import json

# --- Fixed references, all verified against the live v1 instance -------------
# The disputes API credential is NOT `Elavon Basic Auth` (E72ZxLRqrWEyxF18).
# That one belongs to the bare endpoint spike. The credential that actually
# works against /service/dispute-management/v2 is the one below.
ELAVON_BASIC_AUTH = {"id": "w4wa61x6UmWXzrlF", "name": "Elavon Disputes API (Sandbox)"}
GLOBAL_ERROR_WORKFLOW = "KBN9sWK9juozY766"  # Dispute - Global error handling
SANDBOX_HOST = "https://sandbox.elavonapi.com"
API_BASE = "/service/dispute-management/v2"

WORKFLOW_NAME = "Elavon API - Request"


def nid(n):
    return f"33330000-0000-4000-8000-{n:012x}"


# --- Node 1: sub-workflow entry point ---------------------------------------
# Typed inputs, matching the house style of `Dispute - Update Console`:
# a `use_prod` boolean and a `passthrough_item` object on every sub-workflow.
TRIGGER = {
    "id": nid(1),
    "name": "When Executed by Another Workflow",
    "type": "n8n-nodes-base.executeWorkflowTrigger",
    "typeVersion": 1.1,
    "position": [-460, 0],
    "parameters": {
        "workflowInputs": {
            "values": [
                {"name": "use_prod", "type": "boolean"},
                {"name": "method"},
                {"name": "path"},
                {"name": "body", "type": "object"},
                {"name": "query", "type": "object"},
                {"name": "expect_field"},
                {"name": "allow_no_match", "type": "boolean"},
                {"name": "access_token"},
                {"name": "passthrough_item", "type": "object"},
            ]
        }
    },
}

# --- Node 2: environment + input normalisation ------------------------------
RESOLVE_ENV_JS = r"""
/*
 * Resolve the host and normalise the caller's inputs.
 *
 * There is no Elavon production host or credential yet - only the sandbox. We
 * fail loudly on use_prod rather than quietly calling sandbox, because a sync
 * that believes it is in production but reads sandbox data would create real
 * disputes from test rows.
 */
const inp = $input.first().json || {};

if (inp.use_prod === true) {
  throw new Error(
    'Elavon production host and credentials are not configured yet. ' +
    'Only the sandbox is available. Call with use_prod = false.'
  );
}

const method = String(inp.method || 'GET').toUpperCase();
if (!['GET', 'POST', 'PUT', 'PATCH'].includes(method)) {
  throw new Error('Elavon request: unsupported method "' + method + '".');
}

// Accept a path with or without the API base prefix, and with or without a
// leading slash. Callers should pass '/disputes/search'.
let path = String(inp.path || '').trim();
if (!path) throw new Error('Elavon request: `path` is required.');
if (!path.startsWith('/')) path = '/' + path;
if (!path.startsWith(BASE)) path = BASE + path;

return [{
  json: {
    elavonHost: HOST,
    method: method,
    path: path,
    body: inp.body || null,
    query: inp.query || null,
    // Response-shape check. Elavon can return one endpoint's body for another
    // (see the request node), so the caller names a field only its own
    // endpoint returns. Empty string disables the check.
    expectField: String(inp.expect_field || ''),
    // A search that matches nothing is an ordinary state for most callers.
    allowNoMatch: inp.allow_no_match === true,
    accessToken: String(inp.access_token || ''),
    needToken: String(inp.access_token || '') === '',
    passthrough_item: inp.passthrough_item || {},
  }
}];
""".replace("HOST", json.dumps(SANDBOX_HOST)).replace("BASE", json.dumps(API_BASE))

RESOLVE_ENV = {
    "id": nid(2),
    "name": "Resolve Environment",
    "type": "n8n-nodes-base.code",
    "typeVersion": 2,
    "position": [-240, 0],
    "parameters": {"jsCode": RESOLVE_ENV_JS.strip()},
}

# --- Node 3: skip the token fetch when the caller already has one -----------
# The orchestrator calls this sub-workflow many times per run (once per dispute
# per endpoint). Fetching a token every time is wasted latency against an API
# that is already flaky, so a caller may fetch once and thread it through.
NEED_TOKEN = {
    "id": nid(3),
    "name": "Need a token?",
    "type": "n8n-nodes-base.if",
    "typeVersion": 2.2,
    "position": [-20, 0],
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
                    "id": "need-token",
                    "leftValue": "={{ $json.needToken }}",
                    "rightValue": "",
                    "operator": {"type": "boolean", "operation": "true", "singleValue": True},
                }
            ],
            "combinator": "and",
        },
        "options": {},
    },
}

# --- Node 4: OAuth2 client-credentials token --------------------------------
TOKEN = {
    "id": nid(4),
    "name": "Elavon Token",
    "type": "n8n-nodes-base.httpRequest",
    "typeVersion": 4.2,
    "position": [200, -120],
    "parameters": {
        "method": "POST",
        "url": "={{ $json.elavonHost }}/oauth2/client-credentials/v2/token",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpBasicAuth",
        "sendHeaders": True,
        "headerParameters": {
            "parameters": [
                {"name": "Correlation-ID", "value": "={{ $execution.id }}-token"}
            ]
        },
        "sendBody": True,
        "contentType": "form-urlencoded",
        "bodyParameters": {
            "parameters": [{"name": "grant_type", "value": "client_credentials"}]
        },
        "options": {},
    },
    "credentials": {"httpBasicAuth": ELAVON_BASIC_AUTH},
}

# --- Node 5: the call itself ------------------------------------------------
# Helpers ported from the read integration that was built against the sandbox
# (`Njord API`, CLtY9Ihkm5vAGNVX): correlationId, headers, isNoMatch,
# describeError, the retry loop and guard. Each one encodes a quirk that cost a
# debugging cycle to find, so they are kept rather than rewritten.
REQUEST_JS = r"""
/*
 * The one place the dispute sync talks to Elavon.
 *
 * Quirks handled here, each verified against the sandbox:
 *
 *  - A search matching NOTHING answers HTTP 400 carrying error code
 *    '404.1567.4040 Resource Not Found'. It does NOT return an empty set. The
 *    identical body returns 200 for a MID that does have disputes. So that one
 *    prefix maps onto `noMatch`, while every other failure still throws.
 *  - Elavon can return ONE ENDPOINT'S BODY FOR ANOTHER when several calls are
 *    in flight. Two defences: callers must invoke this sub-workflow serially,
 *    and `expectField` names a field only the intended endpoint returns.
 *  - It is flaky enough that one retry is standard.
 *  - 'Request failed with status code 400' says nothing on its own, so
 *    describeError carries Elavon's own error body into the thrown message.
 *
 * This node makes exactly ONE call. Serialisation is the caller's job.
 */
const cfg = $('Resolve Environment').first().json;

// The token node only runs when the caller did not supply a token, so reading
// it has to tolerate the node not having executed.
let token = cfg.accessToken;
if (!token) {
  try {
    token = ($('Elavon Token').first().json || {}).access_token || '';
  } catch (e) {
    token = '';
  }
}
if (!token) {
  throw new Error('Elavon request: no access token available.');
}

function correlationId() {
  return [8, 4, 4, 4, 12]
    .map((n) => Array.from({ length: n }, () => '0123456789abcdef'[Math.floor(Math.random() * 16)]).join(''))
    .join('-');
}

function headers() {
  return {
    Authorization: 'Bearer ' + token,
    Accept: 'application/json',
    'Content-Type': 'application/json',
    'Correlation-ID': correlationId(),
    'tenant-ID': 'master',
  };
}

function queryString(q) {
  if (!q) return '';
  const parts = [];
  for (const key of Object.keys(q)) {
    const v = q[key];
    if (v === null || v === undefined || v === '') continue;
    parts.push(encodeURIComponent(key) + '=' + encodeURIComponent(v));
  }
  return parts.length ? '?' + parts.join('&') : '';
}

function isNoMatch(e) {
  const res = e && e.response;
  if (!res || Number(res.status) !== 400) return false;
  const body = res.data || res.body || {};
  return ((body && body.errors) || []).some(
    (x) => String((x && x.code) || '').indexOf('404.') === 0);
}

function describeError(e) {
  const res = e && e.response;
  const body = res && (res.data || res.body);
  return ((e && e.message) || String(e))
    + (res && res.status ? ' [http ' + res.status + ']' : '')
    + (body ? ' ' + JSON.stringify(body).slice(0, 400) : '');
}

/*
 * Arrow function on purpose: it captures the node's `this`, which a plain
 * function declaration would lose.
 */
const rawRequest = (opts) => this.helpers.httpRequest(opts);

/*
 * Two attempts, no delay between them - the same shape the sandbox work used.
 * Timers are not dependable inside the Code sandbox, so this deliberately does
 * not back off.
 */
async function callOnce(opts) {
  let last = null;
  for (let attempt = 0; attempt < 2; attempt += 1) {
    try {
      return { noMatch: false, data: await rawRequest(opts) };
    } catch (e) {
      if (isNoMatch(e)) return { noMatch: true, data: null };
      last = e;
    }
  }
  throw new Error('Elavon ' + opts.method + ' ' + cfg.path + ' failed: ' + describeError(last));
}

/*
 * Elavon also reports failure inside a 200 body, so a successful HTTP status is
 * not enough on its own.
 */
function guard(res) {
  if (!res || typeof res !== 'object') return res;
  const meta = res.pageMeta || {};
  if (meta.errors) {
    throw new Error('Elavon ' + cfg.path + ' failed: ' + JSON.stringify(meta.errors));
  }
  if (res.code || res.errors) {
    throw new Error('Elavon ' + cfg.path + ' failed: '
      + JSON.stringify(res.errors || res.message || res.code));
  }
  return res;
}

function validateShape(res) {
  if (!cfg.expectField) return res;
  if (!res || typeof res !== 'object' || !Object.prototype.hasOwnProperty.call(res, cfg.expectField)) {
    throw new Error(
      'Elavon ' + cfg.path + ' returned an unexpected body: field "'
      + cfg.expectField + '" is missing. This is how a crossed response from '
      + 'another endpoint shows up. Keys seen: '
      + Object.keys(res || {}).join(', ')
    );
  }
  return res;
}

const url = cfg.elavonHost + cfg.path + queryString(cfg.query);

const result = await callOnce({
  method: cfg.method,
  url: url,
  headers: headers(),
  body: cfg.body || undefined,
  json: true,
});

if (result.noMatch && !cfg.allowNoMatch) {
  throw new Error(
    'Elavon ' + cfg.method + ' ' + cfg.path + ' matched nothing, and the caller '
    + 'did not set allow_no_match. Treating this as an error so a silent gap in '
    + 'the sync is impossible.'
  );
}

const data = result.noMatch ? null : validateShape(guard(result.data));

return [{
  json: {
    ok: true,
    noMatch: result.noMatch,
    method: cfg.method,
    requestUrl: url,
    data: data,
    // Handed back so the caller can thread it through the rest of the run
    // instead of paying for a token on every call.
    access_token: token,
    passthrough_item: cfg.passthrough_item,
  }
}];
"""

REQUEST = {
    "id": nid(5),
    "name": "Elavon Request",
    "type": "n8n-nodes-base.code",
    "typeVersion": 2,
    "position": [420, 0],
    "parameters": {"jsCode": REQUEST_JS.strip()},
}

# --- Node 6: single terminal node -------------------------------------------
# A sub-workflow returns whatever ran last, so the graph keeps exactly one
# ending node. Anything dangling would silently become the return value.
FINAL = {
    "id": nid(6),
    "name": "Final Output",
    "type": "n8n-nodes-base.noOp",
    "typeVersion": 1,
    "position": [640, 0],
    "parameters": {},
}

# --- Manual test path -------------------------------------------------------
MANUAL_TRIGGER = {
    "id": nid(7),
    "name": "When clicking 'Execute workflow'",
    "type": "n8n-nodes-base.manualTrigger",
    "typeVersion": 1,
    "position": [-680, 220],
    "parameters": {},
}

# A search for one MID over the last 90 days. `merchantId` is an ARRAY on
# purpose: a comma-separated string is accepted and then silently ignored.
TEST_INPUTS = {
    "id": nid(8),
    "name": "Test Inputs",
    "type": "n8n-nodes-base.set",
    "typeVersion": 3.4,
    "position": [-460, 220],
    "parameters": {
        "mode": "raw",
        "jsonOutput": json.dumps(
            {
                "use_prod": False,
                "method": "POST",
                "path": "/disputes/search",
                "body": {
                    "receivedDate": {"fromDate": "2025-01-01", "toDate": "2025-12-31"},
                    "merchantId": ["REPLACE_WITH_A_REAL_ELAVON_MID"],
                    "pageMeta": {
                        "pageSize": 200,
                        "pageNumber": 1,
                        "sortBy": "expirationDate",
                        "sortOrder": "ascending",
                    },
                },
                "query": {},
                "expect_field": "pageMeta",
                "allow_no_match": True,
                "access_token": "",
                "passthrough_item": {},
            },
            indent=2,
        ),
        "options": {},
    },
}

STICKY = {
    "id": nid(9),
    "name": "Sticky Note",
    "type": "n8n-nodes-base.stickyNote",
    "typeVersion": 1,
    "position": [-720, -300],
    "parameters": {
        "width": 900,
        "height": 240,
        "content": (
            "## Elavon API - Request\n"
            "Shared auth and call layer for the Elavon dispute sync. Every Elavon call goes through here.\n\n"
            "**Callers must invoke this serially.** Elavon can return one endpoint's body for another when "
            "several calls are in flight. `expect_field` names a field only the intended endpoint returns, "
            "and the call fails if it is missing.\n\n"
            "**`allow_no_match`** — a search that matches nothing comes back as HTTP 400 with error code "
            "`404.1567.4040`, not as an empty set. Set this to `true` and read the `noMatch` flag on the output.\n\n"
            "**`access_token`** — optional. Leave empty and this workflow fetches one. The token is always "
            "returned on the output, so a caller can fetch once and thread it through the rest of the run.\n\n"
            "**Production is not wired up.** Only the sandbox host and credential exist. `use_prod: true` "
            "throws on purpose."
        ),
    },
}

WORKFLOW = {
    "name": WORKFLOW_NAME,
    "nodes": [
        TRIGGER,
        RESOLVE_ENV,
        NEED_TOKEN,
        TOKEN,
        REQUEST,
        FINAL,
        MANUAL_TRIGGER,
        TEST_INPUTS,
        STICKY,
    ],
    "connections": {
        "When Executed by Another Workflow": {
            "main": [[{"node": "Resolve Environment", "type": "main", "index": 0}]]
        },
        "When clicking 'Execute workflow'": {
            "main": [[{"node": "Test Inputs", "type": "main", "index": 0}]]
        },
        "Test Inputs": {
            "main": [[{"node": "Resolve Environment", "type": "main", "index": 0}]]
        },
        "Resolve Environment": {
            "main": [[{"node": "Need a token?", "type": "main", "index": 0}]]
        },
        # true  -> fetch a token first
        # false -> the caller supplied one, go straight to the call
        "Need a token?": {
            "main": [
                [{"node": "Elavon Token", "type": "main", "index": 0}],
                [{"node": "Elavon Request", "type": "main", "index": 0}],
            ]
        },
        "Elavon Token": {
            "main": [[{"node": "Elavon Request", "type": "main", "index": 0}]]
        },
        "Elavon Request": {
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
    import os

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "elavon-api-request.json")
    with open(out, "w") as fh:
        json.dump(WORKFLOW, fh, indent=2)
        fh.write("\n")
    print(f"wrote {out}")
