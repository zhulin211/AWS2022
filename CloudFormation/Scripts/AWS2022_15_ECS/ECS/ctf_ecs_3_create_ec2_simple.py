from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../../AWS2022_15_ECS/ecs_3_ec2_full_bastion_simple.yaml'
    stack_name = 'ECSEC2Bastion'
    parameters = [
        {'ParameterKey': "NetworkStackName", "ParameterValue": 'ECSVPCNETS'},
    ]
    create_update_cf(stack_name, template_path, parameters=parameters)