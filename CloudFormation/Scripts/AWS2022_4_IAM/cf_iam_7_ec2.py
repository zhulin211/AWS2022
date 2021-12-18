from Scripts.ctf_0_basic_functions import create_update_cf

import boto3
from CloudFormation.region import region
client = boto3.client('cloudformation', region_name=region)

if __name__ == "__main__":
    template_path = '../../AWS2022_4_IAM/iam_7_ec2.yaml'
    stack_name = 'IAMRoleEC2'
    print(create_update_cf(stack_name, template_path))
