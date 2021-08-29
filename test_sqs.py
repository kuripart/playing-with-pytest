import pytest

@pytest.fixture
def queue_name():
    return "my-test-queue"

@pytest.fixture
def sqs_test(sqs_client, queue_name):
    sqs_client.create_queue(QueueName=queue_name)
    yield

def test_queue_url(sqs_client, sqs_test, queue_name):
    queue_url = sqs_client.create_queue(QueueName=queue_name)["QueueUrl"]
    assert queue_name in queue_url

def test_receive_message(sqs_client, sqs_test, queue_name):
    queue_url = sqs_client.create_queue(QueueName=queue_name)["QueueUrl"]
    sqs_client.send_message(QueueUrl=queue_url, MessageBody="blah")
    assert sqs_client.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)["Messages"][0]["Body"] == "blah"