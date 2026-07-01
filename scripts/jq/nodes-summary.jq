# Compact per-node summary. Use this to scan a workflow's node list without
# loading the full JSON into context. Output is sorted by node id.
[
  .nodes[]? | {
    id,
    name,
    type,
    typeVersion,
    disabled: (.disabled // false)
  }
] | sort_by(.id)
