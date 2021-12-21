from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_10_LB_AutoScaling/lb_5_autoscalinggroup.yaml'
    stack_name = 'AutoScalingGroup'
    parameters = [
        {'ParameterKey': "LaunchTemplateStackName", "ParameterValue": 'LaunchTemplate'},
        {'ParameterKey': "SubnetStackName", "ParameterValue": 'VPC2Subnets'},
        {'ParameterKey': "LBStack", "ParameterValue": 'LB'},
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
