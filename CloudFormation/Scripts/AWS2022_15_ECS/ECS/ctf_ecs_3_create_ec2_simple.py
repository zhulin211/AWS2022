from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../../AWS2022_15_ECS/ecs_3_ec2_full_bastion_simple.yaml'
    ec2_stack_name = 'ECSEC2Bastion'
    ec2_parameters = [
        {'ParameterKey': "NetworkStackName", "ParameterValue": 'ECSVPCNETS'},
    ]
    create_update_cf(ec2_stack_name, template_path, parameters=ec2_parameters)