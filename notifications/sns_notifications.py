import boto3
import json
import time

# Load AWS configuration
with open("config/aws_config.json", "r") as file:
    aws_config = json.load(file)

sns = boto3.client(
    "sns",
    aws_access_key_id=aws_config["aws_access_key"],
    aws_secret_access_key=aws_config["aws_secret_key"],
    region_name=aws_config["region"]
)

#Sends a notification via AWS SNS to the specified topic
def send_notification(message, topic_arn):

    if not message or not topic_arn:
        print("Invalid message or topic ARN. Notification not sent.")
        return

    try:
        start_time = time.time()
        response = sns.publish(TopicArn=topic_arn, Message=message)
        latency = time.time() - start_time
        print(f"Notification sent in {latency:.2f} seconds: {response}")
    except Exception as e:
        print(f"Failed to send notification. Error: {e}")
