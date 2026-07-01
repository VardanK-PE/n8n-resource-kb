# Kafka topic references — covers both kafka (producer) and kafkaTrigger (consumer).
# Each unique topic is a resource.

[
  .nodes[]?
  | select(.type == "n8n-nodes-base.kafka" or .type == "n8n-nodes-base.kafkaTrigger")
  | (.parameters.topic // null) as $topic
  | select($topic != null)
  | {
      node_id: .id,
      node_name: .name,
      node_type: .type,
      topic: $topic,
      role: (if .type == "n8n-nodes-base.kafkaTrigger" then "consumer" else "producer" end),
      group_id: (.parameters.groupId // null)
    }
] | sort_by(.node_id)
