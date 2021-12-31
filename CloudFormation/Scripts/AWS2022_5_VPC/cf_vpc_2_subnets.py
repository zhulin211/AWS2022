from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_5_VPC/vpc_2_subnets.yaml'
    stack_name = 'VPC2Subnets'
    parameters = [
        {'ParameterKey': "VPCStackName", "ParameterValue": 'VPC1VPC'},
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
