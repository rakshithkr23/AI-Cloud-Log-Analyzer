import boto3
import json


bedrock = boto3.client(
    "bedrock-runtime",
    region_name="eu-north-1"
)


def summarize_logs(log_text):

    prompt = f"""
You are a Linux system administrator.

Analyze these logs:

{log_text}

Give:
1. Error explanation
2. Root cause
3. Solution
"""


    response = bedrock.invoke_model(
        modelId="anthropic.claude-opus-5",
        body=json.dumps(
            {
                "prompt": prompt,
                "max_tokens_to_sample":500
            }
        )
    )


    result = json.loads(
        response["body"].read()
    )


    return result

