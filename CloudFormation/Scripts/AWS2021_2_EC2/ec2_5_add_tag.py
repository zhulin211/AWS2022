import boto3
from CloudFormation.region import region


def ec2_create_tag(instances_id_list, tags_list):
    ec2 = boto3.resource('ec2', region_name=region)
    ec2.create_tags(Resources=instances_id_list, Tags=tags_list)


if __name__ == "__main__":
    from CloudFormation.Scripts.AWS2021_2_EC2.ec2_2_list_instances import ec2_list_no_terminate
    print(ec2_list_no_terminate())
    ec2_create_tag(ec2_list_no_terminate(), [{"Key": "DLM-30BACKUP", "Value": "YES"}])
