from Scripts.ctf_0_basic_functions import create_update_cf

import boto3
from Scripts.region import region
client = boto3.client('cloudformation', region_name=region)

if __name__ == "__main__":
    template_path = '/ecs_2_ecs.yaml'
    ecs_stack_name = 'AWS2021_15_ECS'
    ecs_parameters = [
        {'ParameterKey': "VPCStack", "ParameterValue": 'ECSVPCNETS'},
    ]
    create_update_cf(ecs_stack_name, template_path, parameters=ecs_parameters)