from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_12_2_CloudWatch/cloudwatch_3_alarm.yaml'
    stack_name = 'CloudWatchAlarm'
    print(create_update_cf(stack_name, template_path))
