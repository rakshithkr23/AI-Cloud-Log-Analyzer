import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource(
    "dynamodb",
    region_name="eu-north-1"
)

table = dynamodb.Table("AICloudLogHistory")


def save_log(filename, summary, status):
    log_id = str(uuid.uuid4())

    item = {
        "log_id": log_id,
        "filename": filename,
        "summary": summary,
        "status": status,
        "upload_time": datetime.utcnow().isoformat()
    }

    table.put_item(Item=item)

    return log_id
