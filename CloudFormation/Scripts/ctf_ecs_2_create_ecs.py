from ctf_ecs_1_create_vpc_nets import create_update_cf

import boto3
from region import region
client = boto3.client('cloudformation', region_name=region)

if __name__ == "__main__":
    template_path = '../ECS/ecs_2_ecs.yaml'
    ecs_stack_name = 'ECS'
    ecs_parameters = [
        {'ParameterKey': "VPCStack", "ParameterValue": 'ECSVPCNETS'},
    ]
    create_update_cf(ecs_stack_name, template_path, parameters=ecs_parameters)