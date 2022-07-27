import boto3

if __name__ == '__main__':

    client = boto3.client('ec2')
    paginator = client.get_paginator('describe_security_groups')
    pages = paginator.paginate(    
#        PaginationConfig={
#            'PageSize': 50
#        }
    )

    for page_id, page in enumerate(pages):
        print('SG: {}/{}'.format(page_id, len(page.get('SecurityGroups', []))))
            

