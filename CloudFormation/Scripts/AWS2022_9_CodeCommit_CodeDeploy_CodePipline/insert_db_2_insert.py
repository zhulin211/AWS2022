from CloudFormation.Scripts.AWS2022_9_CodeCommit_CodeDeploy_CodePipline.insert_db_0_db import stu_db
import boto3
from CloudFormation.region import region

dynamodb = boto3.resource('dynamodb', region)

table = dynamodb.Table('staff')

with table.batch_writer() as batch:
    for student in stu_db:
        batch.put_item(Item=student)