import boto3

all_regions = []
session = boto3.session.Session()

def get_regions(session, account_id):

    regions = []
    dyanmodb_client = session.client('dynamodb')
    table_name = 'test-regions'
    resources = dyanmodb_client.scan(TableName=table_name)

    regions = [ region.get('S') for item in resources.get('Items', []) if item.get('accountId', {}).get('S') == account_id for region in item.get('region', {}).get('L')]

    return regions

print("regions:{}".format(get_regions(session, "516859415289")))