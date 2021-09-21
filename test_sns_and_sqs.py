import json
import os

import boto3
from moto import mock_sns, mock_sqs
import aws_service

# Test SQS queue subscribing to sns topic

@mock_sns
@mock_sqs
def test_read_from_sqs_queue():
    sns_resource = boto3.resource("sns", region_name="us-east-1")
    topic = sns_resource.create_topic(Name="test-topic")
    os.environ["sns_topic_arn"] = topic.arn

    sqs_resource = boto3.resource("sqs",region_name="us-east-1")
    queue = sqs_resource.create_queue(QueueName="test-queue")
    os.environ["sqs_queue_url"] = queue.url
    
    topic.subscribe(Protocol="sqs", Endpoint=queue.attributes["QueueArn"]) # make this queue subscribe to the test sns topic

    test_message = "this is a mock"
    message_id = aws_service.publish_message_to_sns(test_message)
    messages = aws_service.read_from_sqs_queue() # the queue will get messages from the topic subscribed to
    message_body = json.loads(messages["Messages"][0]["Body"])

    assert message_body["MessageId"] == message_id["MessageId"]
    assert message_body["Message"] == test_message