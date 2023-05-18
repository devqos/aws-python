import boto3
from botocore.config import Config


def generate_presigned_url(bucket, filename, expiration):
    client = boto3.client("s3", region_name='eu-central-1', config=Config(signature_version='s3v4'))

    response = client.generate_presigned_post(bucket, filename, ExpiresIn=expiration)

    return response
