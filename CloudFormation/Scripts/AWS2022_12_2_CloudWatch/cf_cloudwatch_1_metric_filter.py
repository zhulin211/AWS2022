from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_12_2_CloudWatch/cloudwatch_1_metric_filter.yaml'
    stack_name = 'CloudWatchMetricFilter'
    parameters_usw = [
        {'ParameterKey': "TrailStackName", "ParameterValue": 'CloudTrailToS3AndCloudWatch'},
    ]
    print(create_update_cf(stack_name, template_path))
