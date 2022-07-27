#!/usr/bin/env python
import boto3
from moto import mock_s3, mock_dynamodb2
from aws_sample import MyS3, MyDynamodb
from termcolor import colored

@mock_dynamodb2
@mock_s3
def test():

    # prepare dynamodb talbe
    dynamodb_client = boto3.client('dynamodb')

    dynamodb_client.create_table(
        TableName='test_table',
        KeySchema=[{
            'AttributeName': 'name',
            'KeyType': 'HASH'
        }],
        AttributeDefinitions=[{
            'AttributeName': 'name',
            'AttributeType': 'S'
        }]
    )

    dynamodb_client.put_item(
        TableName='test_table',
        Item={
            'name': {
                'S': 'item1'
            }
        }
    )
    dynamodb_client.put_item(
        TableName='test_table',
        Item={
            'name': {
                'S': 'item2'
            }
        }
    )
    print(colored('Created Dynamodb table and items', 'green'))

    # test dynamodb code
    print('About to verify Dynamodb table and items')
    mys3=MyDynamodb()
    result = mys3.scan('test_table')
    print('result:', result)
    item1 = result.get('Items')[0]['name']['S']
    item2 = result.get('Items')[1]['name']['S']    
    assert item1 == 'item1'
    assert item2 == 'item2'
    print(colored('Dynamodb table and items matches !!!', 'green'))

    # prepare s3 bucket
    s3_client = boto3.client('s3')
    s3_client.create_bucket(Bucket='test_bucket')
    # s3_client.put_object(Bucket='test_bucket', Key='test_file', Body='this is a test file')
    print(colored('Created s3 bucket and file', 'green'))

    # test s3 code
    print('About to verify s3 bucket and file')
    mys3=MyS3()
    mys3.put_object('test_bucket', 'test_file', 'this is a test file')
    s3_file = mys3.get_object('test_bucket', 'test_file')
    file_body = s3_file['Body'].read().decode("utf-8")
    assert file_body == 'this is a test file'
    print(colored('S3 bucket and file matches !!!', 'green'))


if __name__ == '__main__':
    test()
