def lambda_handler(event, context):
    return {
        "statusCode": 204,
        "headers": {
            "Access-Control-Allow-Headers": "Authorization,Content-Type",
            "Access-Control-Allow-Origin": "*",
        },
    }
