import boto3
from project import BaseConfig

def s3connection():
    s3 = boto3.client('s3',
                          aws_access_key_id=BaseConfig.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=BaseConfig.AWS_SECRET_ACCESS_KEY,
                          )
    return s3