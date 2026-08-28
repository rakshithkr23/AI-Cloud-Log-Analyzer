import boto3
from datetime import datetime
import uuid


dynamodb = boto3.resource(
    "dynamodb",
    region_name="eu-north-1"
)


table = dynamodb.Table("log_history")


def store_log(log_data, ai_summary):

    response = table.put_item(
        Item={
            "log_id": str(uuid.uuid4()),

            "timestamp":
            datetime.now().isoformat(),

            "server":
            "EC2-Web-Server",

            "error_type":
            log_data.get("level"),

            "message":
            log_data.get("message"),

            "ai_summary":
            ai_summary,

            "severity":
            "HIGH"
        }
    )

    return response
