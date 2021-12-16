from Scripts.ctf_0_basic_functions import create_update_cf

import boto3
from CloudFormation.region import region
client = boto3.client('cloudformation', region_name=region)

if __name__ == "__main__":
    template_path = '../../AWS2021_2_EC2/ec2_2_snapshot_policy.yaml'
    stack_name = 'EC2SnapshotPolicy'
    print(create_update_cf(stack_name, template_path))