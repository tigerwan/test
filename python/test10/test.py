import boto3
import os

os.environ["AWS_MAX_ATTEMPTS"] = "20"
os.environ["AWS_RETRY_MODE"] = "standard"

def count_ws_v1():
    ws_count=0
    client = boto3.client('workspaces')
    response = client.describe_workspaces()
    ws_count += len(response.get('Workspaces'))
    next_token = response.get('NextToken')

    loop_count = 0
    while next_token:
        loop_count = loop_count + 1
        print("loop:{}".format(loop_count))
        print("token:{}".format(next_token))
        print("ws count:{}".format(ws_count))
        response = client.describe_workspaces(NextToken=next_token)
        ws_count += len(response.get('Workspaces'))
        next_token = response.get('NextToken')
        if not next_token:
            break

    print("all ws count:{}".format(ws_count))

def count_ws_v2():
    paginator = boto3.client("workspaces").get_paginator('describe_workspaces')
    response_iterator = paginator.paginate()
    ws_count=0
    ws_ids = []
    for index, page in enumerate(response_iterator):
        print("loop:{}".format(index))
        ws_count += len(page["Workspaces"])
        print("ws count:{}".format(ws_count))
        ws_ids += [ws['WorkspaceId'] for ws in page["Workspaces"]]
        next_token = page.get("NextToken")
        print("next token:{}".format(next_token))

    print("all ws count:{}".format(len(set(ws_ids))))
    print("all ws ids:{}".format(set(ws_ids)))

if __name__ == "__main__":
    count_ws_v2()

