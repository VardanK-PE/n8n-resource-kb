# External MCP servers consumed by workflows via @n8n/n8n-nodes-langchain.mcpClientTool.
# Each unique endpoint URL is a resource — "if this MCP server goes down, what breaks?".

def parse_host($u):
  ($u | tostring | capture("^[a-zA-Z][a-zA-Z0-9+.-]*://(?<h>[^/?#{}]+)").h) // null;

[
  .nodes[]?
  | select(.type == "@n8n/n8n-nodes-langchain.mcpClientTool")
  | (.parameters.endpointUrl // "" | tostring | ltrimstr("=")) as $url
  | select($url != "")
  | {
      node_id: .id,
      node_name: .name,
      endpoint_url: $url,
      host: parse_host($url)
    }
] | sort_by(.node_id)
