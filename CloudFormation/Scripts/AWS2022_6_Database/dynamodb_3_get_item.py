import boto3
from CloudFormation.region import region
dynamodb = boto3.resource('dynamodb', region_name=region)
from boto3.dynamodb.conditions import Key


def get_all_item(table_name):
    table = dynamodb.Table(table_name)

    response = table.scan()
    data = response['Items']

    # 过滤
    print(table.scan(FilterExpression=Key('QQ').eq(888999), ConsistentRead=False)['Items'])
    return data


if __name__ == '__main__':
    print(get_all_item('staff'))
