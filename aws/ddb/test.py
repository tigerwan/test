import boto3
import pprint

session = boto3.session.Session()
dynamodb = session.resource('dynamodb')

table = dynamodb.Table("daniel-test-ddb")

"""
for i in range(2000):
    table.put_item(
        Item={
            "id": str(i),
            "data": str("0123456789"*100)
        }
    )
"""
response = table.scan()
"""
for item in response.get('Items'):
    if item["tool"] == "resourcecleanup-ec2" and item["config_name"] == "task_config":
        v = item["config_value"]
        print(v["task"]["log_level"])
"""

print("resoure: {}".format(len(response["Items"])))

print("---------------------------")


paginator = session.client("dynamodb").get_paginator('scan')
response_iterator = paginator.paginate(TableName="daniel-test-ddb")
page_index=1
for page in response_iterator:
    print("page:{}, items:{}".format(page_index, len(page["Items"])))
    page_index +=1


print("---------------------------")

client = session.client("dynamodb")
response = client.scan(
    TableName = "daniel-test-ddb"
)
page_index=1
print("clinet:{}, {}".format(page_index, len(response.get("Items"))))


next_token = response.get("LastEvaluatedKey")
while next_token:
    page_index +=1
    response = client.scan(
        TableName = "daniel-test-ddb",
        ExclusiveStartKey = next_token
    )
    print("clinet:{}, {}".format(page_index, len(response.get("Items"))))
    next_token = response.get("LastEvaluatedKey")




