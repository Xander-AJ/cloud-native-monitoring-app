from collections.abc import Mapping, MutableMapping  # Add this line to import Mapping and MutableMapping
from botocore.exceptions import MD5UnavailableError
import boto3

ecr_client = boto3.client('ecr')

repository_name = "my-flask-app-sample"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)
