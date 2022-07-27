import boto3
import pprint

client = boto3.client('rds')
response = client.describe_db_clusters(
    DBClusterIdentifier='nct-nie-aurora-cluster'
)

pprint.pprint(f'response:{response}')

response = client.stop_db_cluster(
        DBClusterIdentifier='nct-nie-aurora-cluster'
)

pprint.pprint(f'response:{response}')