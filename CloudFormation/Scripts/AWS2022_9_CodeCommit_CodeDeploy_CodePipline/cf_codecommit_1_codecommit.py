from Scripts.ctf_0_basic_functions import create_update_cf

import boto3
from CloudFormation.region import region
client = boto3.client('cloudformation', region_name=region)

if __name__ == "__main__":
    template_path = '../../AWS2022_9_CodeCommit_CodeDeploy_CodePipline/codecommit_1_codecommit.yaml'
    stack_name = 'CodeCommitAWS2022Flask'
    print(create_update_cf(stack_name, template_path))
