# GitHub repo references. The owner + repository combo identifies the repo;
# both come back as resource locators on n8n's github node.

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
  | select(.type == "n8n-nodes-base.github" or .type == "n8n-nodes-base.githubTool")
  | (.parameters.owner | rl_value) as $owner
  | (.parameters.repository | rl_value) as $repo
  | select($owner != null and $repo != null)
  | {
      node_id: .id,
      node_name: .name,
      node_type: .type,
      owner: $owner,
      repository: $repo,
      repo_full: "\($owner)/\($repo)",
      repo_url: (.parameters.repository | rl_url),
      operation: (.parameters.operation // null),
      resource: (.parameters.resource // null)
    }
] | sort_by(.node_id)
