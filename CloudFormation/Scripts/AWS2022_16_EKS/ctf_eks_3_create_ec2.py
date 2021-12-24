from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_16_EKS/eks_3_ec2_full_bastion.yaml'
    ec2_stack_name = 'EC2Bastion'
    ec2_parameters = [
        {'ParameterKey': "NetworkStackName", "ParameterValue": 'EKSVPCNETS'},
    ]
    create_update_cf(ec2_stack_name, template_path, parameters=ec2_parameters)