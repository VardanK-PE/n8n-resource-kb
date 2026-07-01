# Env-var references found in any string-valued parameter.
# n8n expression syntax for env: {{ $env.MY_VAR }} or {{$env.MY_VAR}}.
# We walk every leaf string under .parameters and regex-find $env.<NAME>.

def all_strings:
  paths(strings) as $p
  | { node: ., path: $p, value: getpath($p) };

[
  .nodes[]?
  | . as $n
  | ($n.parameters // {})
  | paths(strings) as $p
  | getpath($p) as $v
  | $v
  | [scan("\\$env\\.([A-Za-z_][A-Za-z0-9_]*)")[]]
  | .[]
  | { node_id: $n.id, node_name: $n.name, var_name: . }
]
| unique_by([.node_id, .var_name])
| sort_by(.node_id, .var_name)
