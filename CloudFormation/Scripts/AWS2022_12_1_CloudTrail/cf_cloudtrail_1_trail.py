from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_12_1_CloudTrail/cloudtrail_1_trail.yaml'
    stack_name = 'CloudTrailToS3AndCloudWatch'
    print(create_update_cf(stack_name, template_path))
