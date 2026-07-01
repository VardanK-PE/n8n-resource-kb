# Database nodes (Postgres, MySQL, MongoDB, etc.) → engine + credential + tables + query snippet.
#
# Host/database typically live on the credential, not the node parameters.
# We emit the credential ref so downstream can group by (engine, credential)
# to identify distinct database instances.

def db_engine($t):
  # Cover both base nodes and their *Tool variants (for AI agents).
  ($t | sub("Tool$"; "")) as $base
  | if   $base == "n8n-nodes-base.postgres"     then "postgres"
    elif $base == "n8n-nodes-base.mysql"        then "mysql"
    elif $base == "n8n-nodes-base.mongoDb"      then "mongodb"
    elif $base == "n8n-nodes-base.microsoftSql" then "mssql"
    elif $base == "n8n-nodes-base.snowflake"    then "snowflake"
    elif $base == "n8n-nodes-base.redshift"     then "redshift"
    elif $base == "n8n-nodes-base.questDb"      then "questdb"
    elif $base == "n8n-nodes-base.timescaleDb"  then "timescaledb"
    else null end;

def first_credential:
  if (.credentials // {}) | length > 0 then
    (.credentials | to_entries[0] | {type: .key, id: (.value.id // null), name: (.value.name // null)})
  else null
  end;

[
  .nodes[]?
  | . as $n
  | (db_engine($n.type)) as $engine
  | select($engine != null)
  | {
      node_id: $n.id,
      node_name: $n.name,
      engine: $engine,
      credential: ($n | first_credential),
      operation: ($n.parameters.operation // null),
      table: ($n.parameters.table // $n.parameters.collection // null),
      schema: ($n.parameters.schema // null),
      query_snippet: (($n.parameters.query // "") | tostring | .[0:200])
    }
] | sort_by(.node_id)
