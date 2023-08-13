# Trigger YouTube audio download
This is a lambda function which handles the `POST` requests to `/download`. It works by validating the payload for a `program_url` and then submitting a message to the SQS queue for a download to take place.

This function facilitates a timely API response while allowing the actual download to take place asynchronously as it may take over the 30s limit for API responses in API Gateway.

## Values
- `QUEUE_URL`: the url for your SQS queue to send programs for downloading