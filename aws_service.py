import os
import boto3

def publish_message_to_sns(message: str):
    sns_client = boto3.client("sns", region_name="us-east-1")
    message_id = sns_client.publish(TopicArn=os.environ.get("sns_topic_arn", "test"), Message=message,)
    return message_id

def read_from_sqs_queue():
    sqs_client = boto3.client("sqs", region_name="us-east-1")
    messages = sqs_client.receive_message(QueueUrl=os.environ.get("sqs_queue_url", "test"),MaxNumberOfMessages=1)
    return messages