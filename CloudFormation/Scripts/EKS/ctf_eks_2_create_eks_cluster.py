from Scripts.ECS.ctf_0_basic_functions import create_update_cf

import boto3
from region import region
client = boto3.client('cloudformation', region_name=region)

if __name__ == "__main__":
    template_path = '../../EKS/eks_2_create_eks_cluster.yaml'
    eks_cluster_stack_name = 'EKSCluster'
    eks_parameters = [
        {'ParameterKey': "VPCStack", "ParameterValue": 'EKSVPCNETS'},
    ]
    print(create_update_cf(eks_cluster_stack_name, template_path, parameters=eks_parameters))
