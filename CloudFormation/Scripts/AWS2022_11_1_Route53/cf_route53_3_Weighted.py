from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path_use = '../../AWS2022_11_1_Route53/route53_3_Weighted_2_usw.yaml'
    template_path_usw = '../../AWS2022_11_1_Route53/route53_3_Weighted_1_use.yaml'
    stack_name_use = 'Route53WeightedUSE'
    stack_name_usw = 'Route53WeightedUSW'
    parameters_use = [
        {'ParameterKey': "EC2StackName", "ParameterValue": 'Route53EC2USE'},
    ]
    parameters_usw = [
        {'ParameterKey': "EC2StackName", "ParameterValue": 'Route53EC2USW'},
    ]
    print(create_update_cf(stack_name_use, template_path_use, region='us-east-1', parameters=parameters_use))
    print(create_update_cf(stack_name_usw, template_path_usw, region='us-west-1', parameters=parameters_usw))
