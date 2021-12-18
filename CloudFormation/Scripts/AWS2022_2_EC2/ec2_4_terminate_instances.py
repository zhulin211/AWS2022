import boto3
from CloudFormation.region import region


def terminate_ec2_instances(instances_id_list):
    ec2 = boto3.resource('ec2', region_name=region)
    ec2.instances.filter(InstanceIds=instances_id_list).terminate()


if __name__ == '__main__':
    from CloudFormation.Scripts.AWS2022_2_EC2.ec2_2_list_instances import ec2_list_no_terminate
    terminate_ec2_instances(ec2_list_no_terminate())
