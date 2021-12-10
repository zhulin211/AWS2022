from Scripts.ECS.ctf_0_basic_functions import create_update_cf

import boto3
from region import region
client = boto3.client('cloudformation', region_name=region)

if __name__ == "__main__":
    template_path = '../ECS/ecs_4_application_autoscaling.yaml'
    autoscaling_stack_name = 'ECSAutoScaling'
    autoscaling_parameters = [
        {'ParameterKey': "ECSStack", "ParameterValue": 'ECS'},
    ]
    create_update_cf(autoscaling_stack_name, template_path, parameters=autoscaling_parameters)