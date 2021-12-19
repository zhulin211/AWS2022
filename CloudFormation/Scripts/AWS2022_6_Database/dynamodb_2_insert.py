import boto3
from CloudFormation.region import region
from CloudFormation.Scripts.AWS2022_6_Database.dynamodb_0_db import stu_db
dynamodb = boto3.resource('dynamodb', region_name=region)

table = dynamodb.Table('staff')

with table.batch_writer() as batch:
    for student in stu_db:
        batch.put_item(Item=student)

