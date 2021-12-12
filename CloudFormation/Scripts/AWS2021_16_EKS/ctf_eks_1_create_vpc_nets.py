from Scripts.AWS2021_15_2_ECS.ctf_0_basic_functions import create_update_cf

import boto3
from region import region
client = boto3.client('cloudformation', region_name=region)

if __name__ == "__main__":
    template_path = '../../AWS2021_16_EKS/eks_1_create_vpc_nets.yaml'
    eks_vpc_nets_stack_name = 'EKSVPCNETS'
    print(create_update_cf(eks_vpc_nets_stack_name, template_path))
