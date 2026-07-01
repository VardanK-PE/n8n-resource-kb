# Google Drive files + folders from googleDrive + googleDriveTool nodes.
# A node may reference a file (.parameters.fileId) AND/OR a folder (.parameters.folderId).
# Both are resource locators.

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
  | select(.type == "n8n-nodes-base.googleDrive" or .type == "n8n-nodes-base.googleDriveTool")
  | . as $n
  | (
      ($n.parameters.fileId | rl_value) as $fv
      | if $fv != null then {
          kind: "file",
          drive_id: $fv,
          drive_name: ($n.parameters.fileId | rl_name),
          drive_url: ($n.parameters.fileId | rl_url)
        }
        else empty end
    ),
    (
      ($n.parameters.folderId | rl_value) as $folv
      | if $folv != null then {
          kind: "folder",
          drive_id: $folv,
          drive_name: ($n.parameters.folderId | rl_name),
          drive_url: ($n.parameters.folderId | rl_url)
        }
        else empty end
    )
  | . + {
      node_id: $n.id,
      node_name: $n.name,
      node_type: $n.type,
      operation: ($n.parameters.operation // null)
    }
] | sort_by(.node_id, .kind)
