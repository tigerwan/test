import boto3

response = boto3.client("rds").describe_pending_maintenance_actions()
print(response)