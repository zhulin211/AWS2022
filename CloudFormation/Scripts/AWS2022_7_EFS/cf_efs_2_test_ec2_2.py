from Scripts.ctf_0_basic_functions import create_update_cf

import boto3
from CloudFormation.region import region
client = boto3.client('cloudformation', region_name=region)

if __name__ == "__main__":
    template_path = '../../AWS2022_7_EFS/efs_2_test_ec2_2.yaml'
    stack_name = 'EFSRedisEC22'
    parameters = [
        {'ParameterKey': "VPCStackName", "ParameterValue": 'VPC1VPC'},
        {'ParameterKey': "SubnetStackName", "ParameterValue": 'VPC2Subnets'},
        {'ParameterKey': "SecurityGroupStackName", "ParameterValue": 'VPC5SecurityGroup'},
        {'ParameterKey': "EFSStackName", "ParameterValue": 'EFS'},
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
