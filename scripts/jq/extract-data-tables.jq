# n8n built-in dataTable nodes → table ID + operation.
# Resource locator shape:
#   parameters.dataTableId = {__rl, value, mode, cachedResultName, cachedResultUrl}

def rl_value:
  if type == "object" then (.value // null)
  elif type == "string" then .
  else null end;

def rl_name:
  if type == "object" then (.cachedResultName // .value // null)
  elif type == "string" then .
  else null end;

def rl_url:
  if type == "object" then (.cachedResultUrl // null) else null end;

[
  .nodes[]?
  | select(.type == "n8n-nodes-base.dataTable" or .type == "n8n-nodes-base.dataTableTool")
  | {
      node_id: .id,
      node_name: .name,
      node_type: .type,
      operation: (.parameters.operation // null),
      table_id: (.parameters.dataTableId | rl_value),
      table_name: (.parameters.dataTableId | rl_name),
      table_url: (.parameters.dataTableId | rl_url)
    }
  | select(.table_id != null)
] | sort_by(.node_id)
