import os
import boto3
import datetime


def lambda_handler(event, context):
    s3_object = event['Records'][0]['s3']['object']['key']
    s3_object_size = event['Records'][0]['s3']['object']['size']

    object_name = os.path.splitext(s3_object)[0]
    object_extension = os.path.splitext(s3_object)[1]

    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get('DYNAMODB_TABLE_NAME')

    table = dynamodb.Table(table_name)
    table.put_item(
        Item={
            'ObjectName': object_name,
            'ObjectExtension': object_extension,
            'ObjectSize': s3_object_size,
            'CreatedDate': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }
    )
