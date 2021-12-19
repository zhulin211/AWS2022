import boto3
from CloudFormation.region import region
dynamodb = boto3.resource('dynamodb', region_name=region)


def get_item_username(table_name, username, phone):
    table = dynamodb.Table(table_name)

    response = table.get_item(Key={'username': username,
                                   'phone': phone},
                              ConsistentRead=True
                              )
    return response['Item']


if __name__ == '__main__':
    print(get_item_username('staff', '秦柯', '13911116666'))
