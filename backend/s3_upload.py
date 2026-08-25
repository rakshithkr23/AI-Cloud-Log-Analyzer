import boto3 

s3 = boto3.client(
        "s3",
        region_name = "eu-north-1"
        )
BUCKET_NAME = "ai-cloud-log-analyzer" 

def upload_log(file_path):
    bucket_name = "ai-cloud-log-analyzer"
    object_name = "parsed_logs.json"

    s3.upload_file(
            file_path,
            BUCKET_NAME,
            "uploaded_logs.json"
            )
    return "upload completed" 

if __name__ == "__main__":
    upload_log(
            "logs/parsed_logs.json"
            )
