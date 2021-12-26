import boto3
from CloudFormation.region import region


# 给实例清单的所有实例打标签
def ec2_create_tag(instances_id_list, tags_list):
    ec2 = boto3.resource('ec2', region_name=region)
    ec2.create_tags(Resources=instances_id_list, Tags=tags_list)


if __name__ == "__main__":
    from CloudFormation.Scripts.AWS2022_2_EC2.ec2_2_list_instances import ec2_list_no_terminate
    print(ec2_list_no_terminate())
    # 为所有处于未终结状态的实例打标签
    ec2_create_tag(ec2_list_no_terminate(), [{"Key": "DLM-30BACKUP", "Value": "YES"}])
