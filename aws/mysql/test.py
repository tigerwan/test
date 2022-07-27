import boto3
import sys
sys.path.append("./packages")

import mysql.connector as mysql_connector
import tornado.escape as tornado

if __name__  == '__main__':

    response = boto3.client('health', region_name='us-east-1').describe_event_details_for_organization(
        organizationEventDetailFilters=[
            {
                'awsAccountId': '596134558493',
                'eventArn': 'arn:aws:health:ap-northeast-1::event/EC2/AWS_EC2_OPERATIONAL_NOTIFICATION/AWS_EC2_OPERATIONAL_NOTIFICATION_a2aab6b0-9c08-4021-9ba5-f8e0b7d14159'
            }
        ],
        locale='en'
    )
    description = response.get('successfulSet', [{}])[0].get('eventDescription', {}).get('latestDescription')

    cnx = mysql_connector.connect(
        user='admin',
        password='adminpass',
        host='localhost',
        port=3306,
        database='test'
    )

    cursor  = cnx.cursor()
    params = (
        """
        REPLACE INTO test_tb
        (id, text)
        VALUES (%s,%s);
        """,
        (
            "1",
            description
        )
    )
    cursor.execute(*params)
    cnx.commit()

    with open('x.text', 'w') as f:
        f.write(description)

    with open('x.html', 'w') as f:
        # f.write(tornado.xhtml_unescape(tornado.linkify(description)))
        f.write(tornado.linkify(description.replace("\n", "\n<br>")))
