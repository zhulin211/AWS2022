import boto3
from CloudFormation.region import region
dynamodb = boto3.resource('dynamodb', region_name=region)


def update_item_email(table_name, username, phone, email):
    table = dynamodb.Table(table_name)

    table.update_item(
        Key={
            'username': username,
            'phone': phone
        },
        UpdateExpression="SET email = :val1",
        ExpressionAttributeValues={
            ":val1": email
        }
    )


if __name__ == '__main__':
    update_item_email('staff', '秦柯', '13911116666', 'collinsctk@gmail.com')
