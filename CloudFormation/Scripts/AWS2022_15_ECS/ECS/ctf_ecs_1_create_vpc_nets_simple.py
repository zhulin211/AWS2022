from Scripts.ctf_0_basic_functions import create_update_cf

import boto3
from Scripts.region import region
client = boto3.client('cloudformation', region_name=region)

if __name__ == "__main__":
    template_path = '/ecs_1_create_vpc_nets_simple.yaml'
    ecs_vpc_nets_stack_name = 'ECSVPCNETS'
    print(create_update_cf(ecs_vpc_nets_stack_name, template_path))
