# Canonical projection of a workflow for fingerprinting.
# See agent-os/standards/sync/fingerprint.md for the contract.
#
# Strips UI-only fields (position, notesInFlow, anything starting with _).
# Sorts nodes by id so JSON ordering doesn't perturb the hash.
# Pipe the output through `jq -cS .` then `shasum -a 256` to get the fingerprint.

def strip_ui_params:
  with_entries(
    select(.key | startswith("_") | not)
  )
  | del(.position, .notesInFlow);

{
  nodes: (
    [
      .nodes[]? | {
        id,
        name,
        type,
        typeVersion,
        parameters: ((.parameters // {}) | strip_ui_params),
        credentials: (.credentials // null),
        disabled: (.disabled // false)
      }
    ] | sort_by(.id)
  ),
  connections: (.connections // {}),
  settings: (.settings // {}),
  active: (.active // false)
}
