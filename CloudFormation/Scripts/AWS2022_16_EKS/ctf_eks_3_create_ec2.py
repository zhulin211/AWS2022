from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_16_EKS/eks_3_ec2_full_bastion.yaml'
    stack_name = 'EC2Bastion'
    parameters = [
        {'ParameterKey': "NetworkStackName", "ParameterValue": 'EKSVPCNETS'},
    ]
    create_update_cf(stack_name, template_path, parameters=parameters)