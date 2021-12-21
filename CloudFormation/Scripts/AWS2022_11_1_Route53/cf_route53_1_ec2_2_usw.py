from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_11_1_Route53/route53_1_ec2_2_usw.yaml'
    stack_name = 'Route53EC2USW'
    parameters = [
        {'ParameterKey': "EnvType", "ParameterValue": 'dev'},
    ]
    print(create_update_cf(stack_name, template_path, region='us-west-1', parameters=parameters))
