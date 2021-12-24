from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_16_EKS/eks_1_create_vpc_nets.yaml'
    eks_vpc_nets_stack_name = 'EKSVPCNETS'
    print(create_update_cf(eks_vpc_nets_stack_name, template_path))
