import datetime
import boto3
import time

# table_name = 'workspaces-event'
table_name = 'workspaces-always-on-usage'
# table_name = 'workspaces-auto-stop-usage'
client = boto3.client('dynamodb')

keys = []
paginator = client.get_paginator('scan')
response_iterator = paginator.paginate(TableName=table_name)
for page in response_iterator:
    for item in page.get('Items'):
        # item_time = datetime.datetime.strptime(item.get("start", {}).get("S"), "%Y-%m-%dT%H:%M:%SZ")
        # now = datetime.datetime.utcnow()
        # delta = now - item_time
        #if delta.days > 130:
        if item.get("start", {}).get("S", "").startswith("2021-01"):
            # print("{} - {} > 130 days".format(now, item_time))
            keys.append({
                "ws_id": item.get("ws_id"),
                #  "time": item.get("time")
                "start": item.get("start")
            })

total = len(keys)
for index, key in enumerate(keys):
    if index % 500 == 0:
        time.sleep(1)
    print("({}/{}) delete {}".format(index+1, total, key))

    client.delete_item(
        TableName=table_name,
        Key = key
    )





