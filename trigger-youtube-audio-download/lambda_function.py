import os
import json
import boto3


def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))

    if not body.get("program_url", None):
        return {"statusCode": 400, "body": "Missing 'program_url' parameter"}

    sqs = boto3.client("sqs")
    sqs.send_message(
        QueueUrl=os.environ["QUEUE_URL"],
        MessageBody=json.dumps({"program_url": body.get("program_url")}),
    )

    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": "Download queued",
    }
