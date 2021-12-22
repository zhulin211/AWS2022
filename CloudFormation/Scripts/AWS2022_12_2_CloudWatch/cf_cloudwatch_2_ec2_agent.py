from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_12_2_CloudWatch/cloudwatch_2_ec2_agent.yaml'
    stack_name = 'CloudWatchEC2'
    print(create_update_cf(stack_name, template_path))
