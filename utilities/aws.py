from dotenv import load_dotenv
import os
import boto3
from botocore.config import Config
import base64, datetime

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variable
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
ACCESS_KEY_SECRET = os.getenv("ACCESS_KEY_SECRET")

config = Config(
    region_name='ap-south-1',
    signature_version='s3v4',
    retries={
        'max_attempts': 10,
        'mode': 'standard'
    },
    s3={'addressing_style': 'path'}
)
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_KEY_SECRET,
)

s3_client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_KEY_SECRET,
    config=config
)


def get_url(location='', bucket_name = 'tushar-default-bucket'):
    
    url = s3_client.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': bucket_name,
            'Key': str(location),
        },
        ExpiresIn='604800')
    
    return url


def upload_document(file, location='', bucket_name = 'tushar-default-bucket'):

    [content_type, fileData] = file.split(';base64,')
    content_type = content_type.split(':')[1]
    
    from uuid import uuid4
    document_id = str(uuid4())
    
    obj = s3.Object(
        bucket_name,
        location + document_id
    )
    obj.put(
        Body=base64.b64decode(fileData),
        ContentType=content_type,
        ServerSideEncryption='AES256'
    )

    location = location + document_id

    return location
