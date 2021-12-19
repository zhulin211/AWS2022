import boto3
from CloudFormation.region import region
dynamodb = boto3.resource('dynamodb', region_name=region)
dynamodb_client = boto3.client('dynamodb', region_name=region)


def delete_table(table_name):
    try:
        response = dynamodb_client.describe_table(TableName=table_name)
    # except介绍
    # https://stackoverflow.com/questions/33068055/how-to-handle-errors-with-boto3
    except dynamodb_client.exceptions.ResourceNotFoundException:
        print(f'未找到表:{table_name}')
        return False

    table = dynamodb.Table(table_name)
    table.delete()
    return True


if __name__ == '__main__':
    delete_table('staff')
