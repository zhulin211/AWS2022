from Scripts.ctf_0_basic_functions import create_update_cf

import boto3
from CloudFormation.region import region
client = boto3.client('cloudformation', region_name=region)

if __name__ == "__main__":
    template_path = '../../AWS2022_7_EFS/efs_1_efs.yaml'
    stack_name = 'EFS'
    parameters = [
        {'ParameterKey': "SubnetStackName", "ParameterValue": 'VPC2Subnets'},
        {'ParameterKey': "SecurityGroupStackName", "ParameterValue": 'VPC5SecurityGroup'}
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
