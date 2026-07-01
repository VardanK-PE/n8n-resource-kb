# Slack channel destinations from slack + slackTool nodes.
# parameters.channelId is a resource-locator; .value is the Slack channel ID (e.g. C06C4LCJADV).
# Some workflows use expression-mode values (={{ ... }}) — those are runtime-dynamic.

def rl_value:
  if type == "object" then (.value // null)
  elif type == "string" then .
  else null end;

def rl_name:
  if type == "object" then (.cachedResultName // .value // null)
  elif type == "string" then .
  else null end;

[
  .nodes[]?
  | select(.type == "n8n-nodes-base.slack" or .type == "n8n-nodes-base.slackTool")
  | (.parameters.channelId | rl_value) as $cv
  | select($cv != null)
  | {
      node_id: .id,
      node_name: .name,
      node_type: .type,
      operation: (.parameters.operation // .parameters.select // null),
      channel_id: $cv,
      channel_name: (.parameters.channelId | rl_name)
    }
] | sort_by(.node_id)
