from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_5_VPC/vpc_4_routetable.yaml'
    stack_name = 'VPC4RouteTable'
    parameters = [
        {'ParameterKey': "VPCStackName", "ParameterValue": 'VPC1VPC'},
        {'ParameterKey': "SubnetStackName", "ParameterValue": 'VPC2Subnets'},
        {'ParameterKey': "InternetGWStackName", "ParameterValue": 'VPC3InternetGW'}
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
