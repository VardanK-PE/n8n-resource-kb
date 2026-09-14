#!/usr/bin/env python3
"""Compose the Curbwaste MCC4900 Notification workflow (v1 ajjvV2MZyEtuMj49).

Writes the PUT payload to curbwaste-workflow.json. The data table id is a
placeholder until the table exists in the n8n UI (no public API for data tables).
"""
import json, os

TABLE_ID = os.environ.get("TABLE_ID", "PLACEHOLDER_DATA_TABLE_ID")
TABLE_NAME = "Curbwaste - MCC4900 Notifications"
CURBWASTE_ACCOUNT_ID = "3fc7c27f-c5a6-41db-84cb-f09c4b7164d7"

WF_SEND_EMAIL = ("H9qPciXCz00KxAyF", "Send Email: HTML")
WF_SLACK_BASE = ("VQPaemuwy6FdMa9L", "Slack - Create a base message")
WF_SLACK_NOTIFY = ("U3EyWwhZtcf2tMh5", "Slack - Send notification")

PG_CRED = {"postgres": {"id": "BDw1qoDl0V7mYwj6", "name": "Postgres Production"}}


def nid(n):
    return f"22220000-0000-4000-8000-{n:012x}"


def col(name, typ="string"):
    return {
        "id": name, "displayName": name, "required": False, "defaultMatch": False,
        "display": True, "type": typ, "readOnly": False, "removed": False,
    }


def table_rl():
    return {"__rl": True, "value": TABLE_ID, "mode": "list", "cachedResultName": TABLE_NAME}


def wf_rl(pair):
    return {"__rl": True, "value": pair[0], "mode": "list", "cachedResultName": pair[1]}


def dt_write(operation, values, types):
    """dataTable upsert/update node parameters. Declares ONLY the columns written."""
    return {
        "operation": operation,
        "dataTableId": table_rl(),
        "filters": {"conditions": [{"keyName": "merchant_id", "keyValue": "={{ $json.merchant_id }}"}]},
        "columns": {
            "mappingMode": "defineBelow",
            "value": values,
            "matchingColumns": ["merchant_id"] if operation == "upsert" else [],
            "schema": [col(k, types.get(k, "string")) for k in values],
            "attemptToConvertTypes": False,
            "convertFieldsToString": False,
        },
        "options": {},
    }


def exec_wf(pair, values, types=None):
    types = types or {}
    return {
        "workflowId": wf_rl(pair),
        "workflowInputs": {
            "mappingMode": "defineBelow",
            "value": values,
            "matchingColumns": [],
            "schema": [col(k, types.get(k, "string")) for k in values],
            "attemptToConvertTypes": False,
            "convertFieldsToString": False,
        },
        "options": {},
    }


# --------------------------------------------------------------------------- SQL
FIND_ELIGIBLE_SQL = f"""-- Every ACTIVE Curbwaste merchant, with the three things the notification needs:
-- the business email to write to, the Elavon MID to quote to Visa, and the MCC.
--
-- Readiness is NOT filtered here. The MCC 4900 gate, the MID gate and the email
-- gate are all applied in the following Code node so the Slack report can say how
-- many active merchants were excluded and why. Filtering in SQL would make a wrong
-- gate invisible.
SELECT
  m.id                                                AS merchant_id,
  m.name                                              AS merchant_name,
  (m.data)::jsonb->'business_details'->>'email'       AS business_email,
  (m.data)::jsonb->'business_details'->'dba'->>'name' AS dba,
  (m.data)::jsonb->'business_type'->>'mcc_sic'        AS mcc_raw,
  m.status                                            AS merchant_status,
  -- Earliest transition into 'active', not the latest status row: a
  -- suspend/reactivate cycle must not reset the activation date.
  (SELECT min(s.created_at)
     FROM merchant_status s
    WHERE s.merchant_id = m.id
      AND s.status = 'active')                        AS activated_at,
  -- The ONLY reliable UUID -> Elavon MID bridge. merchant.processor_merchant_id is
  -- null for the merchants that matter. Both filters are required: processor_id
  -- because a merchant can be boarded on several processors, and the numeric test
  -- because non-Elavon gateway ids look like 'org_440947'.
  (SELECT mpd.processor_merchant_id
     FROM merchant_processor_detail mpd
    WHERE mpd.merchant_id = m.id
      AND mpd.processor_id = 'elavon'
      AND mpd.processor_merchant_id ~ '^[0-9]+$'
    LIMIT 1)                                          AS mid
FROM merchant m
WHERE m.account_id = '{CURBWASTE_ACCOUNT_ID}'
  AND m.status = 'active'
ORDER BY m.name;"""

# ------------------------------------------------------------------- Code bodies
COLLAPSE_JS = """// Collapse to exactly one item so the Postgres query downstream executes ONCE.
// The data-table read emits one item per existing row, so without this the
// eligibility query would run once per tracked merchant (an N x M fan-out — the
// same trap that produced 44,944 rows during the Elavon commodity-table load).
return [{ json: { ...$('Run mode').first().json } }];"""

PLAN_JS = """// Decide what this run should do.
//
//   backfill — one-time seed. Records every merchant that is eligible TODAY as
//              already handled, so switching the schedule on does not fire a
//              burst of emails at the existing Curbwaste book.
//   notify   — steady state. Picks up merchants that are eligible and not yet
//              recorded, plus previously-failed ones still under the retry cap.
//
// "New" deliberately means "eligible and not in the tracking table" rather than
// "activated recently": a merchant can become eligible long after signup (an MCC
// edit, a reactivation), so an activated_at watermark would silently miss them.
const cfg = $('Run mode').first().json;
const mode = String(cfg.run_mode || 'notify').trim().toLowerCase();
const MAX_ATTEMPTS = Number(cfg.max_attempts || 3);
const TARGET_MCC = String(cfg.target_mcc || '4900').trim();

// Existing tracking rows, keyed by merchant_id.
const existing = new Map();
for (const it of $('Get existing records').all()) {
  const id = it.json && it.json.merchant_id;
  if (id) existing.set(String(id), it.json);
}

// null, not '' — activated_at is a dateTime column and an empty string is not a
// valid value for one. A merchant with no merchant_status 'active' row (possible
// for older records) must write NULL, not "".
const iso = (v) => {
  if (!v) return null;
  const d = new Date(v);
  return isNaN(d.getTime()) ? null : d.toISOString();
};

const out = [];
const excluded = [];       // active but not eligible — reported, never written
const mccExcluded = [];    // excluded by the MCC gate specifically — listed by name
                           // in the Slack report so a human can eyeball them.
let alreadyHandled = 0;
let retrying = 0;

for (const it of $('Find eligible').all()) {
  const r = it.json || {};
  if (!r.merchant_id) continue;
  const id = String(r.merchant_id);

  const mid = String(r.mid == null ? '' : r.mid).trim();
  const email = String(r.business_email == null ? '' : r.business_email).trim();
  const mccRaw = String(r.mcc_raw == null ? '' : r.mcc_raw).trim();

  // MCC normalisation. Three shapes occur in merchant.data.business_type.mcc_sic
  // and only the first is directly usable:
  //   "4900"  fine
  //   "0742"  zero-padded — strip leading zeros before comparing
  //   "5999J" non-numeric — REJECT, never coerce
  let mcc = '';
  let mccReason = null;
  if (!mccRaw) mccReason = 'business_type.mcc_sic is empty';
  else if (!/^[0-9]+$/.test(mccRaw)) mccReason = `business_type.mcc_sic is non-numeric ("${mccRaw}")`;
  else {
    mcc = mccRaw.replace(/^0+/, '') || '0';
    if (mcc !== TARGET_MCC) mccReason = `MCC is ${mcc}, not ${TARGET_MCC}`;
  }

  let blocked = null;
  if (mccReason) blocked = mccReason;
  else if (!mid) blocked = 'no numeric Elavon MID in merchant_processor_detail';
  else if (!email) blocked = 'business_details.email is empty';

  const businessName = String(r.dba || '').trim() || String(r.merchant_name || '').trim();

  if (blocked) {
    const row = { merchant_id: id, name: businessName, mcc: mcc || mccRaw, mid, blocked };
    excluded.push(row);
    // MCC-driven exclusions that are otherwise emailable (have a MID) get listed
    // by name in the Slack report. They are the ones worth a human glance: if the
    // merchant really is a waste hauler, the fix is the merchant record in
    // PayEngine, which is upstream of this workflow.
    //
    // Deliberately NOT cross-checked against Elavon. Both Elavon sources are
    // untrusted: the `Elavon - MIDs` data table's sync workflow
    // (z06gndFj1h0pcspx) is inactive so the mirror is ~10 months stale, and the
    // Elavon BI spreadsheet it mirrors is itself suspected of sync problems.
    if (mccReason && mid) mccExcluded.push(row);
    continue;
  }

  const prior = existing.get(id);
  const priorStatus = prior ? String(prior.status || '') : null;
  const priorAttempts = prior ? Number(prior.attempt_count || 0) : 0;

  const base = {
    merchant_id: id,
    merchant_name: String(r.merchant_name || ''),
    dba: String(r.dba || ''),
    business_name: businessName,
    business_email: email,
    mid,
    mcc,
    activated_at: iso(r.activated_at),
    first_seen_at: (prior && prior.first_seen_at) || new Date().toISOString(),
    attempt_count: priorAttempts + 1,
  };

  if (mode === 'backfill') {
    // Only seed merchants that are actually eligible. Baselining a blocked
    // merchant would permanently hide it: when it later gets a MID, an email or a
    // 4900 MCC it would already be "known" and never picked up.
    if (prior) { alreadyHandled++; continue; }
    out.push({ json: { ...base, action: 'baseline', attempt_count: 0 } });
    continue;
  }

  if (prior) {
    // Retry only transient failures, and only up to the cap. baseline /
    // processing / notified / skipped are all left alone. 'simulated' rows are
    // dry-run or draft records, not completed work, so they stay available for a
    // real send run.
    const reprocessable = priorStatus === 'simulated' ||
                          (priorStatus === 'failed' && priorAttempts < MAX_ATTEMPTS);
    if (reprocessable) { retrying++; out.push({ json: { ...base, action: 'notify' } }); }
    else alreadyHandled++;
    continue;
  }

  out.push({ json: { ...base, action: 'notify' } });
}

const summary = {
  mode,
  delivery_mode: String(cfg.delivery_mode || 'dry-run'),
  active_total: $('Find eligible').all().length,
  to_act: out.length,
  retrying,
  already_handled: alreadyHandled,
  excluded_count: excluded.length,
  mcc_excluded_count: mccExcluded.length,
};
console.log(JSON.stringify(summary));
if (excluded.length) {
  console.log('excluded (never written to the table; picked up if they become eligible):');
  for (const b of excluded.slice(0, 40)) console.log(`  ${b.merchant_id} ${b.name} — ${b.blocked}`);
}

// The report item rides along as item 0 rather than going through workflow static
// data (which would persist between runs) or being recomputed downstream (which
// would duplicate every gate and let the two drift). 'Attach slack thread' filters
// it back out, so it never reaches the merchant path.
return [
  { json: { action: 'report', summary, excluded: excluded.slice(0, 100), mcc_excluded: mccExcluded.slice(0, 100) } },
  ...out,
];"""

REPORT_JS = """// Build the single Slack base message for this run.
//
// Plan always emits a 'report' item, so this runs even when nothing was selected —
// a quiet run still reports, which is how you tell "nothing new" from "the monitor
// is dead".
const cfg = $('Run mode').first().json;
const all = $('Plan').all().map((i) => i.json || {});
const report = all.find((j) => j.action === 'report') || {};
const plan = all.filter((j) => j.action === 'baseline' || j.action === 'notify');

const s = report.summary || {};
const excluded = report.excluded || [];
const mccExcluded = report.mcc_excluded || [];

const mode = String(cfg.run_mode || 'notify');
const delivery = String(cfg.delivery_mode || 'dry-run');
const emoji = delivery === 'send' ? ':envelope_with_arrow:' : ':pencil:';

// Group the exclusion reasons so the report stays one screen tall no matter how
// many merchants Curbwaste has.
const reasons = {};
for (const e of excluded) {
  const key = String(e.blocked || 'unknown').replace(/\\("[^"]*"\\)/, '(...)')
                                            .replace(/^MCC is \\d+, not/, 'MCC is not');
  reasons[key] = (reasons[key] || 0) + 1;
}

const lines = [];
lines.push(`${emoji} *Curbwaste MCC 4900 notification run* — \\`${mode}\\` / \\`${delivery}\\``);
lines.push(`Active Curbwaste merchants: *${s.active_total ?? 0}*  |  ` +
           `eligible & selected: *${plan.length}*  |  already handled: *${s.already_handled ?? 0}*`);
if (s.retrying) lines.push(`Retrying previously failed: *${s.retrying}*`);

if (Object.keys(reasons).length) {
  lines.push(`Excluded: *${excluded.length}*`);
  for (const [reason, n] of Object.entries(reasons).sort((a, b) => b[1] - a[1])) {
    lines.push(`  • ${n} — ${reason}`);
  }
}
if (mccExcluded.length) {
  // Named, not just counted: these have a MID and an email and would be emailable
  // if their MCC were right, so they are the list somebody should actually read.
  lines.push(`:warning: Excluded on MCC but otherwise emailable — check the merchant record:`);
  for (const m of mccExcluded.slice(0, 25)) {
    lines.push(`  • ${m.name} (MID ${m.mid}) — MCC ${m.mcc || '(empty)'}`);
  }
  if (mccExcluded.length > 25) lines.push(`  • …and ${mccExcluded.length - 25} more`);
}
if (delivery !== 'send') {
  lines.push(delivery === 'dry-run'
    ? '_Dry run — Gmail is not invoked at all. No email can leave._'
    : '_Draft mode — drafts are created in merchants@platformfactory.io. Nothing is sent._');
}
if (plan.length) {
  lines.push('Selected:');
  for (const p of plan.slice(0, 20)) {
    lines.push(`  • ${p.business_name} (MID ${p.mid}) → ${p.business_email}`);
  }
  if (plan.length > 20) lines.push(`  • …and ${plan.length - 20} more`);
}

return [{ json: { base_message: lines.join('\\n'), selected: plan.length } }];"""

ATTACH_JS = """// Re-emit the merchants Plan selected, annotated with the Slack thread to reply
// under. Slack is deliberately kept OFF the merchant path: the base-message
// sub-workflow returns its own item shape, so reading Plan's output directly
// leaves Claim -> Build email -> Send untouched.
const wantName = String($('Run mode').first().json.slack_channel || '').replace(/^#/, '').trim();

let ts = '';
try {
  const b = $('Post Slack base message').first().json || {};
  ts = b.message_ts == null ? '' : String(b.message_ts);
} catch (e) { /* Slack is best-effort; the notification still proceeds */ }
if (!ts) console.log('no Slack thread ts — per-merchant email notices will post unthreaded');

// Drops the empty item that alwaysOutputData produces on a quiet run, so the
// If node below never sees an action-less item.
return $('Plan').all()
  .filter((it) => ['baseline', 'notify'].includes((it.json || {}).action))
  .map((it) => ({ json: { ...it.json, slack_channel: wantName, slack_message_ts: ts } }));"""

BUILD_EMAIL_JS = """// Render the merchant-facing email. Kept in code rather than a Set node so the
// body is readable and the numbering cannot drift.
//
// $input here is 'Claim merchant', and a data-table write returns the WRITTEN ROW
// rather than the item that went in — so business_name and the Slack thread are
// gone. Iterate the claimed rows (authoritative on what was actually claimed) and
// re-attach the rest from 'Attach slack thread' by merchant_id.
const cfg = $('Run mode').first().json;
const delivery = String(cfg.delivery_mode || 'dry-run').trim().toLowerCase();

const planned = new Map();
for (const it of $('Attach slack thread').all()) {
  const j = it.json || {};
  if (j.merchant_id) planned.set(String(j.merchant_id), j);
}

return $input.all().map((it) => {
  const row = it.json || {};
  const p = planned.get(String(row.merchant_id)) || {};
  const j = { ...p, ...row };
  const name = String(j.business_name || j.dba || j.merchant_name || '').trim();
  const mid = j.mid;
  if (!name) throw new Error(`no business name resolved for merchant ${row.merchant_id}`);
  if (!mid) throw new Error(`no MID resolved for merchant ${row.merchant_id}`);

  const subject = `Notification to register with Visa for Utilities Program (MCC 4900) ` +
                  `for Curbwaste Merchant Account ${name} ${mid}`;

  // HTML body. Switched from the plain-text sender 2026-09-14: in plain text the
  // link is only clickable if the RECEIVING client autolinks it, and Gmail's
  // plain-text composer never does — so it could not be verified from a draft.
  // An explicit <a href> removes the guesswork.
  //
  // Merchant names are escaped: several contain "&" (S&P Dumpsters, Superior
  // Waste & Recycling), which would otherwise emit invalid markup.
  const esc = (v) => String(v == null ? '' : v)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

  const body = [
    `<p>Hi ${esc(name)},</p>`,
    '<p>To enrol for Visa Utility Program (MCC 4900), you will have to submit direct request to Visa. Here is the enrolment process to be followed</p>',
    '<ol>',
    '<li>Visit <a href="https://www.visaaccess.com">VisaAccess.com</a> and select "Enroll".</li>',
    '<li>Complete the Contact Information and Physical Location sections.</li>',
    '<li>Click "Confirm and Proceed".</li>',
    '<li>After reaching the confirmation screen, a member of Visa\\'s support team will complete the enrollment process and contact you within 2-3 business days.</li>',
    '</ol>',
    '<p>For any questions regarding the enrollment process, merchants can contact Visa at <a href="mailto:VisaUtilitySolutions@visa.com">VisaUtilitySolutions@visa.com</a></p>',
    `<p>Here is the Payment Processor's (Elavon's) Merchant ID required for Visa Enrollment Process: ${esc(mid)}</p>`,
    '<p>Regards,<br>PayEngine Merchant Services (on behalf of Curbwaste Payments Team)</p>',
  ].join('\\n');

  return {
    json: {
      to: j.business_email,
      subject,
      message_body: body,
      slack_channel: j.slack_channel || '',
      slack_message_ts: j.slack_message_ts || '',
      // The two safety levers, derived from ONE config field so they cannot
      // disagree. dry-run: Gmail is never invoked. draft: Gmail creates a draft.
      // send: live. The sub-workflow additionally defaults BOTH to true when null,
      // so a missing field fails safe.
      skip_email: delivery === 'dry-run',
      create_draft: delivery !== 'send',
      // Only the tracking fields ride through the sub-workflow as passthrough_item;
      // the rendered body does not need to make the round trip.
      passthrough: {
        merchant_id: String(row.merchant_id || ''),
        business_name: name,
        business_email: String(j.business_email || ''),
        mid: String(mid),
        mcc: String(j.mcc || ''),
        attempt_count: Number(row.attempt_count || j.attempt_count || 0),
        delivery_mode: delivery,
      },
    },
  };
});"""

CLASSIFY_JS = """// Turn the sub-workflow's reply into a tracking-table status.
//
// Critically, 'notified' is decided by OUR delivery_mode, not by the
// sub-workflow's status: a Gmail DRAFT also comes back as status 'notified'
// (Edit Fields1 sets it on the draft path too). Trusting that would mark a
// merchant permanently done off the back of an unsent draft.
const cfg = $('Run mode').first().json;
const delivery = String(cfg.delivery_mode || 'dry-run').trim().toLowerCase();

return $input.all().map((it) => {
  const j = it.json || {};
  const err = j.error;
  const childStatus = String(j.status || '');
  const messageId = j.message_id == null ? '' : String(j.message_id);

  let status;
  let errorMessage = '';

  if (err) {
    status = 'failed';
    errorMessage = String((err && (err.message || err.description)) || err).slice(0, 500);
  } else if (childStatus === 'notification_failed') {
    status = 'failed';
    errorMessage = 'Send Email: Simple Text reported notification_failed';
  } else if (delivery === 'send' && childStatus === 'notified') {
    status = 'notified';
  } else if (delivery === 'send') {
    // Reached the sender in live mode but came back with neither a success nor a
    // recognised failure. Treat as failed so the retry cap governs it rather than
    // silently marking the merchant done.
    status = 'failed';
    errorMessage = `unexpected child status "${childStatus || '(none)'}" in send mode`;
  } else {
    // dry-run or draft. 'simulated' counts as UNFINISHED, so a later send run
    // picks the merchant up again.
    status = 'simulated';
  }

  return {
    json: {
      ...j,
      status,
      error_message: errorMessage,
      gmail_message_id: status === 'notified' ? messageId : '',
      // null, not '' — notified_at is a dateTime column.
      notified_at: status === 'notified' ? new Date().toISOString() : null,
      child_status: childStatus,
    },
  };
});"""

TALLY_JS = """// Closing tally posted into the run's Slack thread. The Send Email sub-workflow
// already posts a per-merchant notice, so this exists to answer "did they all
// land" in one line.
const cfg = $('Run mode').first().json;
const rows = $('Classify outcome').all().map((i) => i.json || {});

const counts = {};
for (const r of rows) counts[r.status] = (counts[r.status] || 0) + 1;

const failures = rows.filter((r) => r.status === 'failed');
const tally = Object.entries(counts).map(([k, v]) => `*${v}* ${k}`).join(', ');
const lines = [];
lines.push(`Run complete — ${tally || 'nothing processed'}`);
for (const f of failures.slice(0, 10)) {
  lines.push(`  :x: ${f.business_name} (MID ${f.mid}) — ${f.error_message || 'unknown error'}`);
}
if (String(cfg.delivery_mode) !== 'send') {
  lines.push('_No email was sent: delivery_mode is `' + cfg.delivery_mode + '`._');
}

return [{ json: { message: lines.join('\\n') } }];"""

# ------------------------------------------------------------------------- nodes
nodes = [
    {
        "parameters": {"rule": {"interval": [{"field": "hours", "hoursInterval": 4}]}},
        "type": "n8n-nodes-base.scheduleTrigger", "typeVersion": 1.3,
        "position": [-720, -80], "id": nid(1), "name": "Every 4 hours",
    },
    {
        "parameters": {},
        "type": "n8n-nodes-base.manualTrigger", "typeVersion": 1,
        "position": [-720, 140], "id": nid(2), "name": "When clicking ‘Execute workflow’",
    },
    {
        "parameters": {"assignments": {"assignments": [
            {"id": "c1", "name": "run_mode", "value": "notify", "type": "string"},
            {"id": "c2", "name": "delivery_mode", "value": "send", "type": "string"},
            {"id": "c3", "name": "slack_channel", "value": "ops-automation-alert", "type": "string"},
            {"id": "c4", "name": "target_mcc", "value": "4900", "type": "string"},
            {"id": "c5", "name": "max_attempts", "value": 3, "type": "number"},
        ]}, "options": {}},
        "type": "n8n-nodes-base.set", "typeVersion": 3.4,
        "position": [-500, 20], "id": nid(3), "name": "Run mode",
    },
    {
        "parameters": {"operation": "get", "dataTableId": table_rl(), "returnAll": True},
        "type": "n8n-nodes-base.dataTable", "typeVersion": 1,
        "position": [-280, 20], "id": nid(4), "name": "Get existing records",
        "alwaysOutputData": True,
    },
    {
        "parameters": {"jsCode": COLLAPSE_JS},
        "type": "n8n-nodes-base.code", "typeVersion": 2,
        "position": [-60, 20], "id": nid(5), "name": "Collapse",
    },
    {
        "parameters": {"operation": "executeQuery", "query": FIND_ELIGIBLE_SQL, "options": {}},
        "type": "n8n-nodes-base.postgres", "typeVersion": 2.6,
        "position": [160, 20], "id": nid(6), "name": "Find eligible",
        "credentials": PG_CRED,
    },
    {
        "parameters": {"jsCode": PLAN_JS},
        "type": "n8n-nodes-base.code", "typeVersion": 2,
        "position": [380, 20], "id": nid(7), "name": "Plan",
    },
    {
        "parameters": {"mode": "runOnceForAllItems", "jsCode": REPORT_JS},
        "type": "n8n-nodes-base.code", "typeVersion": 2,
        "position": [600, -140], "id": nid(8), "name": "Build run report",
    },
    {
        "parameters": exec_wf(WF_SLACK_BASE, {
            "partner_account": "PE",
            "channel_name": "={{ $('Run mode').first().json.slack_channel }}",
            "base_message": "={{ $json.base_message }}",
            "passthrough_item": "={{ $json }}",
        }, {"passthrough_item": "object"}),
        "type": "n8n-nodes-base.executeWorkflow", "typeVersion": 1.2,
        "position": [820, -140], "id": nid(9), "name": "Post Slack base message",
        "onError": "continueRegularOutput",
    },
    {
        "parameters": {"mode": "runOnceForAllItems", "jsCode": ATTACH_JS},
        "type": "n8n-nodes-base.code", "typeVersion": 2,
        "position": [1040, -140], "id": nid(10), "name": "Attach slack thread",
    },
    {
        "parameters": {"conditions": {"options": {
            "caseSensitive": True, "leftValue": "", "typeValidation": "strict", "version": 2},
            "conditions": [{"id": "r1", "leftValue": "={{ $json.action }}",
                            "rightValue": "baseline",
                            "operator": {"type": "string", "operation": "equals"}}],
            "combinator": "and"}, "options": {}},
        "type": "n8n-nodes-base.if", "typeVersion": 2.3,
        "position": [1260, -140], "id": nid(11), "name": "Backfill?",
    },
    {
        "parameters": dt_write("upsert", {
            "merchant_id": "={{ $json.merchant_id }}",
            "merchant_name": "={{ $json.merchant_name }}",
            "dba": "={{ $json.dba }}",
            "business_email": "={{ $json.business_email }}",
            "mid": "={{ $json.mid }}",
            "mcc": "={{ $json.mcc }}",
            "status": "baseline",
            "first_seen_at": "={{ $json.first_seen_at }}",
            "activated_at": "={{ $json.activated_at }}",
            "attempt_count": 0,
        }, {"first_seen_at": "dateTime", "activated_at": "dateTime", "attempt_count": "number"}),
        "type": "n8n-nodes-base.dataTable", "typeVersion": 1,
        "position": [1500, -260], "id": nid(12), "name": "Write baseline",
    },
    {
        "parameters": dt_write("upsert", {
            "merchant_id": "={{ $json.merchant_id }}",
            "merchant_name": "={{ $json.merchant_name }}",
            "dba": "={{ $json.dba }}",
            "business_email": "={{ $json.business_email }}",
            "mid": "={{ $json.mid }}",
            "mcc": "={{ $json.mcc }}",
            "status": "processing",
            "first_seen_at": "={{ $json.first_seen_at }}",
            "activated_at": "={{ $json.activated_at }}",
            "attempt_count": "={{ $json.attempt_count }}",
        }, {"first_seen_at": "dateTime", "activated_at": "dateTime", "attempt_count": "number"}),
        "type": "n8n-nodes-base.dataTable", "typeVersion": 1,
        "position": [1500, 40], "id": nid(13), "name": "Claim merchant",
    },
    {
        "parameters": {"jsCode": BUILD_EMAIL_JS},
        "type": "n8n-nodes-base.code", "typeVersion": 2,
        "position": [1720, 40], "id": nid(14), "name": "Build email",
    },
    {
        "parameters": dict(exec_wf(WF_SEND_EMAIL, {
            "to": "={{ $json.to }}",
            "subject": "={{ $json.subject }}",
            "message_body": "={{ $json.message_body }}",
            "cc": "",
            "create_draft": "={{ $json.create_draft }}",
            "partner": "Curbwaste",
            "skip_email": "={{ $json.skip_email }}",
            "slack_channel": "={{ $json.slack_channel }}",
            "slack_message_ts": "={{ $json.slack_message_ts }}",
            "debug_info": "={{ 'curbwaste-mcc4900 ' + $json.passthrough.merchant_id }}",
            "passthrough_item": "={{ $json.passthrough }}",
        }, {"create_draft": "boolean", "skip_email": "boolean", "passthrough_item": "object"}),
             **{"mode": "each"}),
        "type": "n8n-nodes-base.executeWorkflow", "typeVersion": 1.2,
        "position": [1940, 40], "id": nid(15), "name": "Call 'Send Email: HTML'",
        "onError": "continueRegularOutput",
    },
    {
        "parameters": {"jsCode": CLASSIFY_JS},
        "type": "n8n-nodes-base.code", "typeVersion": 2,
        "position": [2160, 40], "id": nid(16), "name": "Classify outcome",
    },
    {
        "parameters": dt_write("update", {
            "status": "={{ $json.status }}",
            "delivery_mode": "={{ $json.delivery_mode }}",
            "notified_at": "={{ $json.notified_at }}",
            "gmail_message_id": "={{ $json.gmail_message_id }}",
            "error_message": "={{ $json.error_message }}",
            "attempt_count": "={{ $json.attempt_count }}",
        }, {"notified_at": "dateTime", "attempt_count": "number"}),
        "type": "n8n-nodes-base.dataTable", "typeVersion": 1,
        "position": [2380, 40], "id": nid(17), "name": "Record outcome",
    },
    {
        "parameters": {"mode": "runOnceForAllItems", "jsCode": TALLY_JS},
        "type": "n8n-nodes-base.code", "typeVersion": 2,
        "position": [2600, 40], "id": nid(18), "name": "Tally outcomes",
    },
    {
        "parameters": exec_wf(WF_SLACK_NOTIFY, {
            "partner_account": "PE",
            "channel_name": "={{ $('Run mode').first().json.slack_channel }}",
            "message_ts": "={{ $('Attach slack thread').first().json.slack_message_ts }}",
            "message": "={{ $json.message }}",
            "passthrough_item": "={{ $json }}",
        }, {"passthrough_item": "object"}),
        "type": "n8n-nodes-base.executeWorkflow", "typeVersion": 1.2,
        "position": [2820, 40], "id": nid(19), "name": "Post run tally",
        "onError": "continueRegularOutput",
    },
]

# ------------------------------------------------------------------ sticky notes
STICKY_CONTROL = """## Flow execution control

Everything that decides whether an email leaves the building is on the **Run mode** node.

| `delivery_mode` | `skip_email` | `create_draft` | Effect |
|---|---|---|---|
| `dry-run` | true | true | Gmail is **never invoked**. Table + Slack only. |
| `draft` | false | true | Gmail `resource: draft` → draft in merchants@platformfactory.io. **Nothing sent.** |
| `send` | false | false | Live send. |

`run_mode`:
- `backfill` — seed every currently-eligible merchant as `baseline`. **Emails nobody.**
- `notify` — steady state.

`slack_channel` — `n8n-sandbox-of-doom` while testing, `ops-automation-alert` once live.

This is safe by construction: `Set Email Parameters` inside *Send Email: Simple Text* does
`skip_email == null ? true : skip_email` and the same for `create_draft`, so a **missing**
field cannot cause a send. The failure mode is a silent no-op, not a leak."""

STICKY_GOLIVE = """## Before setting delivery_mode to `send`

1. Run `backfill` + `dry-run`. Confirm the table holds one `baseline` row per eligible
   merchant and that Slack's exclusion breakdown looks sane.
2. Run `notify` + `draft`. Open the drafts in merchants@platformfactory.io. Check the
   business name, the MID, and that **Sent is empty**.
3. Only then `notify` + `send`, and point `slack_channel` at `ops-automation-alert`.

`simulated` rows are dry-run/draft records, **not** completed work — a later `send` run
picks those merchants up again. That is deliberate."""

STICKY_DESIGN = """## Load-bearing design decisions

**"New" = eligible and absent from the tracking table** — never an `activated_at` watermark.
A merchant can become eligible long after signup (MCC edit, reactivation), so a timestamp
watermark silently misses them. The full active set is diffed every run.

**`Collapse` stops an N×M fan-out.** The data-table read emits one item per existing row, so
without collapsing first the eligibility query would run once per tracked merchant.

**`alwaysOutputData` on `Get existing records`** — the table is empty on the first run and
without it nothing downstream executes at all.

**`Plan` always emits a `report` item as item 0**, so a quiet run still reaches Slack — that
is how you tell "nothing new" from "the monitor is dead". `Attach slack thread` filters it
back out so it never reaches the merchant path. It rides along rather than going through
workflow static data (which would persist between runs) or being recomputed in
`Build run report` (which would duplicate every gate and let the two drift).

**A data-table write returns the WRITTEN ROW, not the item that went in.** `business_name`
and the Slack thread do not survive `Claim merchant`, which is why `Build email` re-attaches
them from `Attach slack thread` by `merchant_id`.

**`Claim merchant` writes `processing` BEFORE the email.** Claim-then-act makes this
at-most-once: a crash leaves a visible stuck row rather than re-emailing on the next tick.

**`Classify outcome` trusts OUR `delivery_mode`, not the child's status.** A Gmail *draft*
also returns `status: notified`. Believing it would mark a merchant permanently done off the
back of an unsent draft.

**The MCC gate uses Postgres `business_type.mcc_sic`, and nothing else.** Elavon's assigned
MCC is deliberately NOT consulted: the `Elavon - MIDs` data table is a mirror of the Elavon
BI spreadsheet whose sync workflow (`z06gndFj1h0pcspx`) is **inactive**, leaving the mirror
~10 months stale, and the spreadsheet itself is suspected of sync problems. Do not wire
either source into the eligibility decision. Merchants excluded on MCC but otherwise
emailable are listed by name in the Slack report so the merchant record can be fixed
upstream in PayEngine, which is where the fix belongs.

**Data-table write nodes declare only the columns they write.** Declaring the full schema
makes the n8n panel render every other column as an empty editable field — omitted at
runtime, but one keystroke from wiping real data.

**Both Slack calls are best-effort** (`continueRegularOutput`). Losing the report is better
than losing the notification. `passthrough_item` is mandatory on both — they do
`jsonOutput = {{ trigger.passthrough_item }}` on the no-thread path and throw without it."""

for i, (name, content, pos, size) in enumerate([
    ("Flow execution control", STICKY_CONTROL, [-500, -420], [620, 320]),
    ("Go-live checklist", STICKY_GOLIVE, [160, -420], [420, 320]),
    ("Design decisions", STICKY_DESIGN, [620, 200], [640, 620]),
], start=20):
    nodes.append({
        "parameters": {"content": content, "height": size[1], "width": size[0]},
        "type": "n8n-nodes-base.stickyNote", "typeVersion": 1,
        "position": pos, "id": nid(i), "name": name,
    })


def main_conn(*targets):
    return {"main": [[{"node": t, "type": "main", "index": 0} for t in targets]]}


connections = {
    "Every 4 hours": main_conn("Run mode"),
    "When clicking ‘Execute workflow’": main_conn("Run mode"),
    "Run mode": main_conn("Get existing records"),
    "Get existing records": main_conn("Collapse"),
    "Collapse": main_conn("Find eligible"),
    "Find eligible": main_conn("Plan"),
    "Plan": main_conn("Build run report"),
    "Build run report": main_conn("Post Slack base message"),
    "Post Slack base message": main_conn("Attach slack thread"),
    "Attach slack thread": main_conn("Backfill?"),
    "Backfill?": {"main": [
        [{"node": "Write baseline", "type": "main", "index": 0}],
        [{"node": "Claim merchant", "type": "main", "index": 0}],
    ]},
    "Claim merchant": main_conn("Build email"),
    "Build email": main_conn("Call 'Send Email: HTML'"),
    "Call 'Send Email: HTML'": main_conn("Classify outcome"),
    "Classify outcome": main_conn("Record outcome"),
    "Record outcome": main_conn("Tally outcomes"),
    "Tally outcomes": main_conn("Post run tally"),
}

payload = {
    "name": "Curbwaste Merchant MCC4900 Notification",
    "nodes": nodes,
    "connections": connections,
    "settings": {"executionOrder": "v1", "callerPolicy": "workflowsFromSameOwner"},
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "curbwaste-workflow.json")
with open(out, "w") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)
print(f"wrote {out}: {len(nodes)} nodes, {len(connections)} connection sources")
