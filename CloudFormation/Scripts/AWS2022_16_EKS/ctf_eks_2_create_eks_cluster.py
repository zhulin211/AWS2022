from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_16_EKS/eks_2_create_eks_cluster.yaml'
    stack_name = 'EKSCluster'
    parameters = [
        {'ParameterKey': "VPCStack", "ParameterValue": 'EKSVPCNETS'},
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
