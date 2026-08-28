import boto3


def summarize_logs(log_text):
    """
    Sends log data to Amazon Bedrock and returns an AI-generated summary.
    """

    client = boto3.client(
        "bedrock-runtime",
        region_name="eu-north-1"
    )

    response = client.converse(
            modelId="global.amazon.nova-2-lite-v1:0",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": f"""
You are a Linux System Administrator.

Analyze the following Linux log file.

Return:
1. Critical Errors
2. Warnings
3. Possible Cause
4. Suggested Fix
5. Overall Summary

Logs:
{log_text}
"""
                    }
                ]
            }
        ],
        inferenceConfig={
            "maxTokens": 500,
            "temperature": 0.3
        }
    )

    summary = response["output"]["message"]["content"][0]["text"]

    return summary
