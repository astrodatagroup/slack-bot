import boto3
from datetime import datetime
import json

lambda_client = boto3.client("lambda")


def lambda_handler(event, context):
    msg = {"key": "new_invocation", "at": str(datetime.now())}
    lambda_client.invoke(
        FunctionName="actually-create-new-deck",
        InvocationType="Event",
        Payload=json.dumps(msg),
    )
    return {
        "statusCode": "200",
        "body": """
{
  "response_type": "ephemeral",
  "text": "I'm working on making you a new deck!"
}
        """,
        "headers": {"Content-Type": "application/json"},
    }
