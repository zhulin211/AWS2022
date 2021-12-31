from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_5_VPC/vpc_1_vpc.yaml'
    stack_name = 'VPC1VPC'
    print(create_update_cf(stack_name, template_path))
