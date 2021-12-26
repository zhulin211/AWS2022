import boto3
from CloudFormation.Scripts.AWS2022_2_EC2.ec2_2_list_instances import ec2_get_by_tagname
from CloudFormation.region import region
ec2 = boto3.resource('ec2', region_name=region)


def stop_instance(instance_name):
    """
    停止特定实例
    :param instance_name (实例的名字, Name的值):
    :return 不返回:
    """
    ec2.instances.filter(InstanceIds=ec2_get_by_tagname(instance_name)).stop()


def start_instance(instance_name):
    """
    开始特定实例
    :param instance_name (实例的名字, Name的值):
    :return 不返回:
    """
    ec2.instances.filter(InstanceIds=ec2_get_by_tagname(instance_name)).start()


if __name__ == '__main__':
    ec2_instance_name = 'EC2Full'
    # stop_instance(ec2_instance_name)
    start_instance(ec2_instance_name)
