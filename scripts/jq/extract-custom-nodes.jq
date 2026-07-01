# Custom / community nodes: anything whose `type` doesn't start with
# `n8n-nodes-base.` or `@n8n/`. The package name is everything before the last `.`.

[
  .nodes[]?
  | . as $n
  | select(
      ($n.type | startswith("n8n-nodes-base.") | not)
      and ($n.type | startswith("@n8n/") | not)
    )
  | {
      node_id: $n.id,
      node_name: $n.name,
      type: $n.type,
      package: ($n.type | capture("^(?<p>.+)\\.[^.]+$") | .p)
    }
] | sort_by(.node_id)
