from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_2_EC2/ec2_1_full.yaml'
    stack_name = 'EC2BASIC'
    parameters = [
        {'ParameterKey': "NetworkStackName", "ParameterValue": 'EC2VPC'},
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
