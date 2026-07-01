# Execute-Workflow node references. These create bidirectional workflow→workflow links.
# Parameter shape: .parameters.workflowId can be a string OR an object {value, mode}.

[
  .nodes[]?
  | select(.type == "n8n-nodes-base.executeWorkflow" or .type == "@n8n/n8n-nodes-langchain.toolWorkflow")
  | {
      node_id: .id,
      node_name: .name,
      node_type: .type,
      target_workflow_id: (
        (.parameters.workflowId | if type == "object" then .value else . end)
        // null
      )
    }
] | sort_by(.node_id)
