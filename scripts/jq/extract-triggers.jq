# Trigger nodes: webhook, schedule, cron, errorTrigger, executeWorkflowTrigger, manualTrigger, *Trigger.

def describe_interval($i):
  if ($i | length) == 0 then
    "unconfigured"
  elif $i.field == "cronExpression" then
    ($i.expression // "cron")
  elif $i.field == "seconds" then
    "every \($i.secondsInterval // 1) second(s)"
  elif $i.field == "minutes" then
    "every \($i.minutesInterval // 1) minute(s)"
  elif $i.field == "hours" then
    "every \($i.hoursInterval // 1) hour(s)" +
      (if $i.triggerAtMinute != null then " at :\($i.triggerAtMinute)" else "" end)
  elif $i.field == "days" then
    "every \($i.daysInterval // 1) day(s)" +
      (if $i.triggerAtHour != null then
         " at \($i.triggerAtHour):\((($i.triggerAtMinute // 0) | tostring) | if length == 1 then "0" + . else . end)"
       else "" end)
  elif $i.field == "weeks" then
    "every \($i.weeksInterval // 1) week(s)" +
      (if $i.triggerAtDayOfWeek != null then " on day \($i.triggerAtDayOfWeek)" else "" end)
  elif $i.field == "months" then
    "every \($i.monthsInterval // 1) month(s)" +
      (if $i.triggerAtDayOfMonth != null then " on day \($i.triggerAtDayOfMonth)" else "" end)
  elif ($i.field == null) and ($i.triggerAtHour != null) then
    "daily at \($i.triggerAtHour):\((($i.triggerAtMinute // 0) | tostring) | if length == 1 then "0" + . else . end)"
  elif ($i.field == null) and ($i.triggerAtMinute != null) then
    "hourly at :\((($i.triggerAtMinute) | tostring) | if length == 1 then "0" + . else . end)"
  else
    "schedule (field=\($i.field // "missing"))"
  end;

def schedule_description($p):
  ($p.cronExpression // null) as $cron
  | ($p.rule.interval // []) as $rules
  | if $cron then $cron
    elif ($rules | length) > 0 then ($rules | map(describe_interval(.)) | join(", "))
    else null
    end;

[
  .nodes[]?
  | . as $n
  | select(
      $n.type == "n8n-nodes-base.webhook"
      or $n.type == "n8n-nodes-base.scheduleTrigger"
      or $n.type == "n8n-nodes-base.cron"
      or $n.type == "n8n-nodes-base.errorTrigger"
      or $n.type == "n8n-nodes-base.executeWorkflowTrigger"
      or $n.type == "n8n-nodes-base.manualTrigger"
      or $n.type == "n8n-nodes-base.formTrigger"
      or ($n.type | test("Trigger$"))
    )
  | {
      node_id: $n.id,
      node_name: $n.name,
      node_type: $n.type,
      trigger_type: (
        if   $n.type == "n8n-nodes-base.webhook"               then "webhook"
        elif $n.type == "n8n-nodes-base.scheduleTrigger"       then "schedule"
        elif $n.type == "n8n-nodes-base.cron"                  then "cron"
        elif $n.type == "n8n-nodes-base.errorTrigger"          then "error"
        elif $n.type == "n8n-nodes-base.executeWorkflowTrigger" then "execute-workflow"
        elif $n.type == "n8n-nodes-base.manualTrigger"         then "manual"
        elif $n.type == "n8n-nodes-base.formTrigger"           then "form"
        else "other"
        end
      ),
      path: ($n.parameters.path // null),
      method: ($n.parameters.httpMethod // null),
      schedule: schedule_description($n.parameters),
      form_title: ($n.parameters.formTitle // null)
    }
] | sort_by(.node_id)
