import boto3
import os


session = boto3.session.Session(profile_name="NAPIDEVIAMR-GlobalAdminsRole-1NHOLM9XOUCTO")
"""
rds_client = boto3.client("rds")
paginator = rds_client.get_paginator('describe_db_instances')
response_iterator = paginator.paginate(DBInstanceIdentifier="abc")
for page in response_iterator:
        print("describe_db_instances:" + page)
"""
"""
asg_client = boto3.client("autoscaling")
paginator = asg_client.get_paginator('describe_auto_scaling_groups')
response_iterator = paginator.paginate(AutoScalingGroupNames=["123"])
print("len:{}".format(len(response_iterator)))
for page in response_iterator:
        print("describe_db_instances:{}".format(page))
"""


ec2_client = session.client("ec2")
paginator = ec2_client.get_paginator('describe_instances')
response_iterator = paginator.paginate(InstanceIds=["i-0d9cc4100bf36a582"])
for page in response_iterator:
        print("describe_db_instances:{}".format(page))
