from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../../AWS2022_15_ECS/ecs_1_create_vpc_nets_simple.yaml'
    stack_name = 'ECSVPCNETS'
    print(create_update_cf(stack_name, template_path))
