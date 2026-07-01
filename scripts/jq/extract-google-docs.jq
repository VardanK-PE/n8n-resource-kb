# Google Docs documents referenced by googleDocs / googleDocsTool nodes.
# The document handle is either parameters.documentURL (a doc ID or URL) or
# parameters.documentId (rare; resource-locator).

def rl_value:
  if type == "object" then (.value // null)
  elif type == "string" then .
  else null end;

def rl_name:
  if type == "object" then (.cachedResultName // .value // null)
  elif type == "string" then .
  else null end;

# documentURL is usually a bare doc ID. If it looks like a full URL, strip to the ID.
def doc_id_from_url:
  . as $s
  | if ($s | tostring | startswith("http")) then
      ($s | capture("/document/d/(?<id>[A-Za-z0-9_-]+)").id // $s)
    else $s
    end;

[
  .nodes[]?
  | select(.type == "n8n-nodes-base.googleDocs" or .type == "n8n-nodes-base.googleDocsTool")
  | (
      (.parameters.documentURL | if . != null and . != "" then doc_id_from_url else null end)
      // (.parameters.documentId | rl_value)
    ) as $doc_id
  | select($doc_id != null)
  | {
      node_id: .id,
      node_name: .name,
      node_type: .type,
      document_id: $doc_id,
      document_name: (.parameters.documentId | rl_name),
      operation: (.parameters.operation // null)
    }
] | sort_by(.node_id)
