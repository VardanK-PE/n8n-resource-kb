# AWS S3 bucket references. Bucket name is the canonical handle.

[
  .nodes[]?
  | select(.type == "n8n-nodes-base.awsS3" or .type == "n8n-nodes-base.awsS3Tool")
  | (.parameters.bucketName // null) as $bucket
  | select($bucket != null)
  | {
      node_id: .id,
      node_name: .name,
      node_type: .type,
      bucket: $bucket,
      operation: (.parameters.operation // null),
      file_name: (.parameters.fileName // .parameters.fileKey // null)
    }
] | sort_by(.node_id)
