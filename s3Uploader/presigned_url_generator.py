import boto3
from botocore.config import Config


class PresignedUrlGenerator:
    def __init__(self, bucket_name: str, file_name: str, expiration_time: int):
        self.bucketName: str = bucket_name
        self.file_name: str = file_name
        self.expiration_time: int = expiration_time

    def generate_post_url(self):
        client = boto3.client("s3", region_name='eu-central-1', config=Config(signature_version='s3v4'))
        response = client.generate_presigned_post(self.bucketName, self.file_name, ExpiresIn=self.expiration_time)

        return response
