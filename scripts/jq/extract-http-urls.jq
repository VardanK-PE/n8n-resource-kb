# HTTP Request nodes → host + method + path.
# Covers n8n-nodes-base.httpRequest. Extend here if new HTTP-ish nodes appear.
#
# URL handling notes:
# - n8n expression-mode strings begin with "=" (e.g. "=https://api.example.com/{{ $json.id }}").
#   Strip the leading "=" before parsing.
# - URLs may be a plain string OR a "resource locator" object {__rl, value, mode}.
# - URLs often contain expressions like {{ $json.x }}; we extract the host from the
#   literal prefix and keep the templated URL intact for the note body.

def unwrap_url:
  if type == "object" then (.value // "")
  elif type == "string" then .
  else ""
  end
  | ltrimstr("=");

def parse_host($u):
  ($u | capture("^[a-zA-Z][a-zA-Z0-9+.-]*://(?<h>[^/?#{}]+)").h) // null;

[
  .nodes[]?
  | select(.type == "n8n-nodes-base.httpRequest" or .type == "n8n-nodes-base.httpRequestTool")
  | (.parameters.url // "" | unwrap_url) as $url
  | {
      node_id: .id,
      node_name: .name,
      url: $url,
      method: (.parameters.method // .parameters.requestMethod // "GET"),
      host: parse_host($url)
    }
] | sort_by(.node_id)
