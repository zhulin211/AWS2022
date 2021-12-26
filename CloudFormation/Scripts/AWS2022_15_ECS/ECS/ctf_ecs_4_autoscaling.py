from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../../AWS2022_15_ECS/ecs_4_application_autoscaling.yaml'
    stack_name = 'ECSAutoScaling'
    create_update_cf(stack_name, template_path)
