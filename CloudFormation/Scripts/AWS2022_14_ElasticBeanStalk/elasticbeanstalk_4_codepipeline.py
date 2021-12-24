from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_14_ElasticBeanStalk/elasticbeanstalk_3_codepipeline.yaml'
    stack_name = 'QYTEBPipeline'
    parameters = [
        {'ParameterKey': "EBStackName", "ParameterValue": 'QYTEB'},
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
