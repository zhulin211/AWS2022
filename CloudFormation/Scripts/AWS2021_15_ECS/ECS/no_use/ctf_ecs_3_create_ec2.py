from Scripts.AWS2021_15_ECS.ECS.no_use.ctf_ecs_1_create_vpc_nets import create_update_cf

import boto3
from region import region
client = boto3.client('cloudformation', region_name=region)

if __name__ == "__main__":
    template_path = '../../../../AWS2021_15_ECS/no_use/ecs_3_ec2_full_bastion.yaml'
    ec2_stack_name = 'EC2Bastion'
    ec2_parameters = [
        {'ParameterKey': "NetworkStackName", "ParameterValue": 'ECSVPCNETS'},
    ]
    create_update_cf(ec2_stack_name, template_path, parameters=ec2_parameters)