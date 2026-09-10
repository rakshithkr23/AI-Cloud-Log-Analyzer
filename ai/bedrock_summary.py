import boto3


def summarize_logs(log_text):
    """
    Sends Linux log data to Amazon Bedrock and returns an AI-generated summary.
    """

    client = boto3.client(
        "bedrock-runtime",
        region_name="eu-north-1"
    )

    prompt = f"""
You are an experienced Linux System Administrator.

Analyze the following Linux log file and provide a structured report.

Return only the following sections:

1. Critical Errors
2. Warnings
3. Possible Cause
4. Suggested Fix
5. Overall Summary

Linux Logs:
{log_text}
"""

    response = client.converse(
            modelId="eu.amazon.nova-micro-v1:0",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
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


if __name__ == "__main__":
    sample_logs = """
Aug 29 10:10:22 server sshd[1234]: Failed password for root from 192.168.1.20
Aug 29 10:10:30 server kernel: Out of memory: Kill process 4567 (python)
Aug 29 10:11:01 server systemd: nginx.service: Failed with result 'exit-code'
"""

    print(summarize_logs(sample_logs))
