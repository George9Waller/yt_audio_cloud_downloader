import os
import boto3

from base64 import b64decode


ENCRYPTED_PASSKEY = os.environ["PASSKEY"]
PASSKEY = (
    boto3.client("kms")
    .decrypt(
        CiphertextBlob=b64decode(ENCRYPTED_PASSKEY),
        EncryptionContext={
            "LambdaFunctionName": os.environ["AWS_LAMBDA_FUNCTION_NAME"]
        },
    )["Plaintext"]
    .decode("utf-8")
)


def lambda_handler(event, context):
    token = event.get("identitySource", [""])[0]
    is_authorized = token == PASSKEY
    print(f"Authorization result: {is_authorized}")
    return {"isAuthorized": is_authorized}
