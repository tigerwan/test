import json
import boto3
from boto3.dynamodb.types import TypeDeserializer
from boto3.dynamodb.transform import TransformationInjector


client = boto3.client('dynamodb')
paginator = client.get_paginator('scan')
service_model = client._service_model.operation_model('Scan')
operation_parameters = {
  "TableName": "afterhoursstop"
}
trans = TransformationInjector(deserializer = TypeDeserializer())

page_iterator = paginator.paginate(**operation_parameters)
for page in page_iterator:
	trans.inject_attribute_value_output(page, service_model)
	print(page.get("Items"))

