from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_4_IAM/iam_1_s3.yaml'
    stack_name = 'IAMS3'
    print(create_update_cf(stack_name, template_path))
