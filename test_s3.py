import tempfile
import pytest, os

class MyModel(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

@pytest.fixture
def bucket_name():
    return "my-test-bucket"

@pytest.fixture
def test_file_name():
    return "FILE_NAME.txt"
    
@pytest.fixture
def s3_test(s3_client, bucket_name):
    s3_client.create_bucket(Bucket=bucket_name)
    yield

def test_my_model_save(s3_client, s3_test, bucket_name):
    model_instance = MyModel('testkey', 'val')
    s3_client.put_object(Bucket='my-test-bucket', Key=model_instance.name, Body=model_instance.value)

    body = s3_client.get_object(Bucket=bucket_name, Key='testkey').get('Body').read().decode()
    assert body == 'val'

def test_list_buckets(s3_client, s3_test, bucket_name):
    response = s3_client.list_buckets()
    assert [bucket["Name"] for bucket in response["Buckets"]] == [bucket_name]

def test_list_objects(s3_client, s3_test, test_file_name, bucket_name):
    try: # Ideally make use of tempfile
        with open(test_file_name, "w") as new_file:
            new_file.write('this is something')
            s3_client.upload_file(test_file_name, bucket_name, "file_test")
            response = s3_client.list_objects(Bucket=bucket_name, Prefix='file')
            assert [object["Key"] for object in response["Contents"]] == ["file_test"]
    finally:
        os.remove(test_file_name)

