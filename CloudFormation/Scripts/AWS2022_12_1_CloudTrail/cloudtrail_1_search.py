import boto3
from datetime import datetime
from CloudFormation.region import region as region_name
import json
client = boto3.client('cloudtrail', region_name=region_name)


def cloud_trail_lookup_events(start_datetime, end_datetime, lookupattributes):
    response = client.lookup_events(
        LookupAttributes=[lookupattributes],
        StartTime=start_datetime,
        EndTime=end_datetime,
        # EventCategory='insight',
        MaxResults=50,
        # NextToken='string'
    )
    event_list = response.get('Events')
    return_event_list = []
    for event in event_list:
        cloud_trail_event = event.pop('CloudTrailEvent')
        event.update({'CloudTrailEvent': json.loads(cloud_trail_event)})
        return_event_list.append(event)
    return return_event_list


if __name__ == '__main__':
    #  Contains a list of lookup attributes. Currently the list can contain only one item.
    #  http://boto.cloudhackers.com/en/latest/ref/cloudtrail.html
    from pprint import pprint
    # 过滤条件一
    lookup_attributes = {
            # 'AttributeKey': 'EventId' | 'EventName' | 'ReadOnly' | 'Username' |
            # 'ResourceType' | 'ResourceName' | 'EventSource' | 'AccessKeyId',
            'AttributeKey': 'Username',
            'AttributeValue': 'qytangadmin'
        }

    # 过滤条件二
    lookup_attributes = {
            'AttributeKey': 'EventName',
            'AttributeValue': 'TerminateInstances'
        }

    # 过滤条件三
    lookup_attributes = {
            'AttributeKey': 'EventName',
            'AttributeValue': 'RunInstances'
        }

    i = 1
    for e in cloud_trail_lookup_events(datetime(2021, 12, 10), datetime.now(), lookup_attributes):
        print('=' * 50 + str(i) + '=' * 50)
        pprint(e)
        i += 1
