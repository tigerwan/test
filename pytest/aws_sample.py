import boto3

class MyS3():
    def __init__(self):
        self.__s3__ = boto3.client('s3', region_name='ap-southeast-2')

    def put_object(self, bucket, key, body):
        return self.__s3__.put_object(Bucket=bucket, Key=key, Body=body)

    def get_object(self, bucket, key):
        return self.__s3__.get_object(Bucket=bucket, Key=key)

class MyDynamodb():
    def __init__(self):
        self.__dynamodb__ = boto3.client('dynamodb', region_name='ap-southeast-2')

    def create_table(self, table, schema):
        return self.__dynamodb__.create_table(TableName=table, KeySchema=schema)

    def scan(self, table):
        return self.__dynamodb__.scan(TableName=table)

    def put_item(self, table, item):
        return self.__dynamodb__.put_item(TableName=table, Item=item)