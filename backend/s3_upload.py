import boto3 

s3 = boto3.client(
        "s3",
        region_name = "eu-north-1"
        )
BUCKET_NAME = "ai-cloud-log-analyzer" 

def upload_to_s3(file_content,filename):
    """ Upload file bytes to Amazon s3 """
    s3.put_object(
            Bucket = BUCKET_NAME,
            Key=filename,
            Body=file_content
            )

    return {
            "status" : "success",
            "message" : f"{filename} uploaded successfully."
            }

