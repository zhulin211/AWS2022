from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_16_EKS/eks_0_gui_iam_role.yaml'
    stack_name = 'EKSGUIRole'
    print(create_update_cf(stack_name, template_path))
