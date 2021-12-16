import boto3
from CloudFormation.region import region
ec2 = boto3.resource('ec2', region_name=region)
ec2_client = boto3.client('ec2', region_name=region)


def ec2_list_all():
    # instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    instances = ec2.instances.filter()
    instances_list = []
    for instance in instances:
        instances_list.append(instance.id)
    return instances_list
    # response = ec2client.describe_instances()
    # return response['Reservations'][0]['Instances']


def ec2_list_no_terminate():
    # instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    instances = ec2.instances.filter()
    instances_list = []
    for instance in instances:
        if instance.state.get('Name') != 'terminated':
            instances_list.append(instance.id)
    return instances_list


def ec2_list_by_state(ec2_state):
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': [ec2_state]}])
    # instances = ec2.instances.filter()
    instances_list = []
    for instance in instances:
        if instance.state.get('Name') != 'terminated':
            instances_list.append(instance.id)
    return instances_list


def ec2_get_by_tagname(instance_name):
    instances = ec2.instances.filter()
    instances_list = []
    for instance in instances:
        if {'Key': 'Name', 'Value': instance_name} in instance.tags and instance.state.get('Name') != 'terminated':
            instances_list.append(instance.id)
    return instances_list


def ec2_instance_detail(instance_id):
    # 只能在列表中传入一个ID
    specificinstance = ec2_client.describe_instances(InstanceIds=[instance_id])
    return specificinstance.get('Reservations')[0].get('Instances')[0]


if __name__ == '__main__':
    from pprint import pprint
    # print(ec2_list_all())
    # print(ec2_list_no_terminate())
    # pprint(ec2_instance_detail(ec2_list_no_terminate()[0]))
    # print(ec2_instance_detail(ec2_list_no_terminate()[0]).get('SecurityGroups'))
    # print(ec2_instance_detail(ec2_list_no_terminate()[0]).get('PublicIpAddress'))
    # for instance in ec2_list_by_state('running'):
    #     print(ec2_instance_detail(instance).get('PublicIpAddress'))
    print(ec2_get_by_tagname('EC2Full'))
