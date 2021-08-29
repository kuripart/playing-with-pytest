
import pytest

@pytest.fixture
def ami_image(ec2_client):
    image_response = ec2_client.describe_images()
    return image_response['Images'][0]['ImageId']
     
@pytest.fixture
def ec2_test(ec2_client, ami_image):
    ec2_client.run_instances(ImageId=ami_image, MinCount=1, MaxCount=1)
    yield

def test_create_instances_with_decorator(ec2_client, ec2_test, ami_image):
  instances = ec2_client.describe_instances()['Reservations'][0]['Instances']
  assert len(instances) == 1
  assert instances[0]['ImageId'] == ami_image
