from Scripts.ctf_0_basic_functions import create_update_cf
from Scripts.AWS2022_3_S3.s3_3_delete import delete_buket, s3_empty
import time


if __name__ == "__main__":
    try:
        s3_empty('aws2022-s3-pipeline-asg')
        time.sleep(3)
    except Exception as e:
        print(e)

    try:
        delete_buket('aws2022-s3-pipeline-asg')
        time.sleep(3)
    except Exception as e:
        print(e)

    template_path = '../../AWS2022_10_LB_AutoScaling/lb_6_codedeploy_codepipeline.yaml'
    stack_name = 'ASGCodeDeployCodePipeline'
    parameters = [
        {'ParameterKey': "CodeCommitStack", "ParameterValue": 'CodeCommitAWS2022Flask'},
        {'ParameterKey': "LBStack", "ParameterValue": 'LB'},
        {'ParameterKey': "ASGStack", "ParameterValue": 'AutoScalingGroup'},
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
