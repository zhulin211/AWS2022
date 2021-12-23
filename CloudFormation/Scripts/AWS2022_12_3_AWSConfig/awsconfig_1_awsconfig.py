from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_12_3_AWSConfig/awsconfig_1_awsconfig.yaml'
    stack_name = 'AWSConfig'
    print(create_update_cf(stack_name, template_path, region='us-west-1'))
