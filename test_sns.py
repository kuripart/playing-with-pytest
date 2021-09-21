import os
import boto3
from moto import mock_sns
import aws_service

@mock_sns
def test_publish_message_to_sns():
    sns_resource = boto3.resource("sns", region_name="us-east-1")
    topic = sns_resource.create_topic(Name="test-topic")
    os.environ["sns_topic_arn"] = topic.arn
    message_id = aws_service.publish_message_to_sns("mock test")
    assert message_id["ResponseMetadata"]["HTTPStatusCode"] == 200