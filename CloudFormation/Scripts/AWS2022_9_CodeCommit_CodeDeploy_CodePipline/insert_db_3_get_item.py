import boto3
from CloudFormation.region import region
dynamodb = boto3.resource('dynamodb', region)


def get_all_item(table_name):
    table = dynamodb.Table(table_name)

    response = table.scan()
    data = response['Items']
    return data


if __name__ == '__main__':
    print(get_all_item('staff'))
