import boto3

all_regions = []
session = boto3.session.Session()
def get_regions(session, account_id):

    # get all regions
    global all_regions
    regions = []
    if not all_regions:
        dyanmodb_client = session.client('dynamodb')
        # table_name = config['regiontable']['tablename']
        print("fetch region")
        table_name = "ops-prod-regions"
        resources = dyanmodb_client.scan(TableName=table_name)
        all_regions = resources.get('Items')

    regions = [item.get('region', {}).get('S') for item in all_regions if item.get('accountId', []).get('S') == account_id]

    return regions

print("regions:{}".format(get_regions(session, "001049712839")))
print("regions:{}".format(get_regions(session, "021817787677")))