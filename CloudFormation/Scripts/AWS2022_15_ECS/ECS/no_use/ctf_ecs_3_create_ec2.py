from Scripts.AWS2022_15_ECS.ECS.no_use.ctf_ecs_1_create_vpc_nets import create_update_cf


if __name__ == "__main__":
    template_path = '../../../../AWS2022_15_ECS/no_use/ecs_3_ec2_full_bastion.yaml'
    stack_name = 'EC2Bastion'
    parameters = [
        {'ParameterKey': "NetworkStackName", "ParameterValue": 'ECSVPCNETS'},
    ]
    create_update_cf(stack_name, template_path, parameters=parameters)