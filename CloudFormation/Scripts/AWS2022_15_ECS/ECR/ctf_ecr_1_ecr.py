from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../../AWS2022_15_ECS/ecr_1_create_repos.yaml'
    stack_name = 'ECR'
    print(create_update_cf(stack_name, template_path))
