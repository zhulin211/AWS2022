from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_11_2_CloudFront/cloudfront_2_cloudfront.yaml'
    stack_name = 'CloudFront'
    parameters = [
        {'ParameterKey': "S3Stack", "ParameterValue": 'CloudFront1S3Images'},
        {'ParameterKey': "LBStack", "ParameterValue": 'LB'},
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
