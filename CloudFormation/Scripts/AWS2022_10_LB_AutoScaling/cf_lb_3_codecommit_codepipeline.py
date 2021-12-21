from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_10_LB_AutoScaling/lb_3_codedeploy_codepipeline.yaml'
    stack_name = 'LBCodeDeployCodePipeline'
    parameters = [
        {'ParameterKey': "CodeCommitStack", "ParameterValue": 'CodeCommitAWS2022Flask'},
        {'ParameterKey': "LBStack", "ParameterValue": 'LB'},
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
