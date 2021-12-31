from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_4_IAM/iam_3_policy_for_group.yaml'
    stack_name = 'IAMPolicy'
    print(create_update_cf(stack_name, template_path))
