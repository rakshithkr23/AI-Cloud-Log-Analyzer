
import os
import boto3
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

s3 = boto3.client(
    "s3",
    region_name=os.getenv("AWS_REGION")
)

BUCKET_NAME = os.getenv("S3_BUCKET")


def upload_to_s3(file_content, filename):
    """Upload file bytes to Amazon S3"""

    try:
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=file_content
        )

        return {
            "status": "success",
            "message": f"{filename} uploaded successfully."
        }

    except ClientError as e:
        return {
            "status": "error",
            "message": str(e)
        }
