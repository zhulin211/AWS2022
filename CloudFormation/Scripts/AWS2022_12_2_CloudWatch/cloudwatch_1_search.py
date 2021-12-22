# https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html
#
# { $.awsRegion = "ap-northeast-2" && $.eventSource="codecommit.amazonaws.com"}
#
# { $.eventSource="codecommit.amazonaws.com" && $.eventName="GitPull" }
#
# { ($.eventSource="codecommit.amazonaws.com" && $.userIdentity.userName="qytangadmin" ) && $.eventName="GitPull"}
#
#
# { ($.eventSource="s3.amazonaws.com" && $.userIdentity.userName="qytangadmin" ) && $.eventName="PutObject"}
#
# { ($.eventSource="s3.amazonaws.com" && $.userIdentity.userName="qytangadmin" ) && $.eventName="DeleteObjects"}
import boto3
from datetime import datetime, timedelta
import time
import json
from CloudFormation.region import region as  region_name
client = boto3.client('logs', region_name=region_name)


def cloudwatch_log_filter(log_group, query, last_n_hours):
    start_query_response = client.start_query(
        logGroupName=log_group,
        startTime=int((datetime.today() - timedelta(hours=last_n_hours)).timestamp()),
        endTime=int(datetime.now().timestamp()),
        queryString=query,
    )

    query_id = start_query_response['queryId']

    response = None

    while not response or response['status'] == 'Running':
        # print('Waiting for query to complete ...')
        time.sleep(1)
        response = client.get_query_results(
            queryId=query_id
        )
    log_list = []
    for x in response.get('results'):
        for y in x:
            try:
                if "eventVersion" in y.get('value'):

                    log_list.append(json.loads(y.get('value')))
            except AttributeError:
                pass
    return log_list


if __name__ == '__main__':
    import json
    log_group = 'aws2022_trail_log_group'
    query = 'fields @timestamp, @message ' \
            '| sort @timestamp desc ' \
            '| limit 25 ' \
            '| filter awsRegion="us-east-1" ' \
            'and userIdentity.userName="qytangadmin" ' \
            'and eventSource="dynamodb.amazonaws.com" ' \
            'and eventName="CreateTable"'

    # query = 'fields @timestamp, @message ' \
    #         '| sort @timestamp desc ' \
    #         '| limit 25 ' \
    #         '| filter awsRegion="ap-northeast-2" ' \
    #         'and userIdentity.userName="qytangadmin" ' \
    #         'and eventSource="s3.amazonaws.com" ' \
    #         'and eventName="PutObject"'
    # query = 'fields @timestamp, @message ' \
    #         '| sort @timestamp desc ' \
    #         '| limit 25 ' \
    #         '| filter awsRegion="ap-northeast-2" ' \
    #         'and userIdentity.userName="qytangadmin" ' \
    #         'and eventSource="s3.amazonaws.com" ' \
    #         'and eventName="DeleteObjects"'
    # query = 'fields @timestamp, @message ' \
    #         '| sort @timestamp desc ' \
    #         '| limit 25 ' \
    #         '| filter awsRegion="ap-northeast-2" ' \
    #         'and eventSource="codecommit.amazonaws.com" ' \
    #         'and userIdentity.userName="qytangadmin" ' \
    #         'and eventName="GitPull"'
    print(json.dumps(cloudwatch_log_filter(log_group, query, 5), indent=4))
