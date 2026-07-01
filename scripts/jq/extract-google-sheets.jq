# Google Sheets nodes → spreadsheet ID + tab + operation.
# n8n-nodes-base.googleSheets uses resource-locator objects for documentId and sheetName:
#   { __rl, value, mode, cachedResultName, cachedResultUrl }
# The spreadsheet ID is the canonical resource handle; the name can drift.

def rl_value:
  if type == "object" then (.value // null)
  elif type == "string" then .
  else null
  end;

def rl_name:
  if type == "object" then (.cachedResultName // .value // null)
  elif type == "string" then .
  else null
  end;

def rl_url:
  if type == "object" then (.cachedResultUrl // null)
  else null
  end;

[
  .nodes[]?
  | select(.type == "n8n-nodes-base.googleSheets" or .type == "n8n-nodes-base.googleSheetsTool")
  | {
      node_id: .id,
      node_name: .name,
      operation: (.parameters.operation // null),
      spreadsheet_id: (.parameters.documentId | rl_value),
      spreadsheet_name: (.parameters.documentId | rl_name),
      spreadsheet_url: (.parameters.documentId | rl_url),
      sheet_tab_value: (.parameters.sheetName | rl_value | tostring),
      sheet_tab_name: (.parameters.sheetName | rl_name | tostring)
    }
  | select(.spreadsheet_id != null)
] | sort_by(.node_id)
