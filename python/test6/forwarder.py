#!/usr/bin/env python -W ignore
import json
import os
import sys
# import botocore
import traceback
import datetime
# import boto3

try:
    for lib_path in ['/opt', '/opt/autolib_local_repos']:
        sys.path.append(lib_path)
except:
    traceback.print_exc()
    raise
print('Successfully added the library path into system path {}'.format(sys.path))

from autolib_comm.libbof.log2 import Log2
# from autolib_comm.libbof.commfunc import CommFunc

from autolib_aws.libaws.aws_session import AwsSessionI
from autolib_aws.libawsp.awsp_event import AwspCloudWatchEventI


###############################
# Business Logic Related Code.#
###############################


def dump_error(tool_name, account_id, region, resource_id, resource_type, msg):
    """dump error to CoudWatch log"""
    report_meta = {
        'tool': tool_name,
        'type': 'RESULT',
        'account_id': account_id,
        'region': region,
        'utc_time': str(datetime.datetime.utcnow()),
        'resource_id': resource_id,
        'resource_type': resource_type,
        'notification_category': 'support',
        'msg': msg
    }

    Log2.info('Deliver a report as follows:')
    Log2.info(json.dumps(report_meta))


# def get_local_config(config_file):
#    """load local configuration"""
#    local_config = CommFunc.get_config(config_file=config_file)
#    Log2.debug("Got local config from {}:{}".format(config_file, local_config))
#    return local_config


def get_tool_name():
    """"Return tool name"""
    return os.getenv('TOOL')


def get_master_region():
    """"Return tool name"""
    return os.getenv('MASTER_REGION')


def forwarder(event, context):
    """forward the CloudWatch event from the current region to the master region"""

    try:
        Log2.info('Start ...')
        Log2.info('event:{}'.format(event))

        # get local configuration file
        # local_config = get_local_config('./conf/config.json')
        # tool_name = local_config.get('toolname')
        # master_region = local_config.get('aws', {}).get('master_region')
        tool_name = get_tool_name()
        master_region = get_master_region()

        # prepare the event to forward
        entries = [
            {
                'Detail': json.dumps(event.get('detail')),
                'DetailType': event.get('detail-type'),
                'Resources': event.get('resources'),
                'Source': 'awsgo.{}'.format(event.get('source'))
            }
        ]

        # forward event to ther master region
        session = AwsSessionI.c_session(region_name=master_region)
        event_client = AwspCloudWatchEventI(session_rw=session)
        response = event_client.put_events(Entries=entries)

        # error handling
        if response and response.get('FailedEntryCount') > 0:
            raise Exception('Fail to forward event to the master region {}:{}'.format(master_region, response))

        Log2.info('Successfully forward a event to master region {}:{}'.format(master_region, entries))
        Log2.info('Exit ...')

    except Exception as e:

        dump_error(
            tool_name=tool_name,
            account_id=event.get('account'),
            region=event.get('region'),
            resource_id=event.get('resources'),
            resource_type='N/A',
            msg=traceback.format_exc()
        )
        raise

    return
