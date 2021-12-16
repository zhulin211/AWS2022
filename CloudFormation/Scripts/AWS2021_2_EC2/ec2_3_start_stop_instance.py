import boto3
from CloudFormation.Scripts.AWS2021_2_EC2.ec2_2_list_instances import ec2_get_by_tagname
from CloudFormation.region import region
ec2 = boto3.resource('ec2', region_name=region)


def stop_instance(instance_name):
    ec2.instances.filter(InstanceIds=ec2_get_by_tagname(instance_name)).stop()


def start_instance(instance_name):
    ec2.instances.filter(InstanceIds=ec2_get_by_tagname(instance_name)).start()


if __name__ == '__main__':
    ec2_instance_name = 'EC2Full'
    # stop_instance(ec2_instance_name)
    start_instance(ec2_instance_name)
