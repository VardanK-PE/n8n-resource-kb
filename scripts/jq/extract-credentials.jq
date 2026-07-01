# All credential references across all nodes.
# n8n shape: node.credentials is an object keyed by credential type:
#   { "httpHeaderAuth": { "id": "1", "name": "my-cred" } }

[
  .nodes[]?
  | . as $n
  | (($n.credentials // {}) | to_entries[]?)
  | {
      node_id: $n.id,
      node_name: $n.name,
      credential_type: .key,
      credential_id: (.value.id // null),
      credential_name: (.value.name // null)
    }
] | sort_by(.node_id, .credential_type)
