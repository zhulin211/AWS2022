from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_11_1_Route53/route53_1_ec2_1_use.yaml'
    stack_name = 'Route53EC2USE'
    parameters = [
        {'ParameterKey': "EnvType", "ParameterValue": 'dev'},
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
