import boto3


sns = boto3.client(
    "sns",
    region_name="eu-north-1"
)


TOPIC_ARN="arn:aws:sns:eu-north-1:099334489422:AI-Log-Alerts"



def send_alert(message):

    sns.publish(

        TopicArn=TOPIC_ARN,

        Message=message,

        Subject="AI Cloud Log Alert"

    )


    return "Alert sent"
