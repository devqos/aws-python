import boto3
import botocore.config
import botocore.client
import typing


class PresignedUrlGenerator:
    def __init__(self, bucket_name: str, file_name: str, expiration_time: int):
        self.bucketName: str = bucket_name
        self.file_name: str = file_name
        self.expiration_time: int = expiration_time

    def generate_post_url(self) -> dict[str, typing.Any]:
        client: botocore.client.BaseClient = boto3.client("s3",
                                                          region_name='eu-central-1',
                                                          config=botocore.config.Config(signature_version='s3v4'))

        return client.generate_presigned_post(self.bucketName,
                                              self.file_name,
                                              ExpiresIn=self.expiration_time)
