from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../../AWS2022_15_ECS/ecs_2_ecs.yaml'
    stack_name = 'ECS'
    parameters = [
        {'ParameterKey': "VPCStack", "ParameterValue": 'ECSVPCNETS'},
    ]
    # 注意创建容易, 删除往往有问题, 建议手动删除资源, 然后删除CloudFormation
    create_update_cf(stack_name, template_path, parameters=parameters)