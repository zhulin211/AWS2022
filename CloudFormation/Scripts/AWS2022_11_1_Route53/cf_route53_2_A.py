from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_11_1_Route53/route53_2_A.yaml'
    stack_name = 'Route53EC2A'
    print(create_update_cf(stack_name, template_path))
