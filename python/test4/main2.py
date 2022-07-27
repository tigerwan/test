#def get_regions(session, account_id):

    # get all regions
    # regions = []
    # dyanmodb_client = session.client('dynamodb')
    # table_name = config['regiontable']['tablename']
    # print("fetch region")
    # table_name = "ops-prod-regions"
    # resources = dyanmodb_client.scan(TableName=table_name)

def get_regions(account_id):

    resources = {
	"Items": [{ 
  "accountId": {
    "S": "516859415289"
  },
  "region": {
    "L": [
      {
        "S": "us-west-2"
      },
      {
        "S": "us-east-1"
      }
    ]
 
}
}  
]
    }
    regions = [ region.get('S') for item in resources.get('Items', []) if item.get('accountId', {}).get('S') == account_id for region in item.get('region', {}).get('L')]

    return regions

print("regions:{}".format(get_regions("884003394595")))
