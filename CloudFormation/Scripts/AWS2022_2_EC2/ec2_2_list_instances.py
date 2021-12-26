import boto3
from CloudFormation.region import region
ec2 = boto3.resource('ec2', region_name=region)
ec2_client = boto3.client('ec2', region_name=region)


def ec2_list_all():
    """
    列出所有实例
    :return 实例清单:
    """
    # instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    instances = ec2.instances.filter()
    instances_list = []
    for instance in instances:
        instances_list.append(instance.id)
    return instances_list
    # response = ec2client.describe_instances()
    # return response['Reservations'][0]['Instances']


def ec2_list_no_terminate():
    """
    列出所有未被终结的实例
    :return 实例清单:
    """
    # instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    instances = ec2.instances.filter()
    instances_list = []
    for instance in instances:
        if instance.state.get('Name') != 'terminated':
            instances_list.append(instance.id)
    return instances_list


def ec2_list_by_state(ec2_state):
    """
    返回特定状态的实例
    :param ec2_state (实例状态):
    :return 实例清单:
    """
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': [ec2_state]}])
    # instances = ec2.instances.filter()
    instances_list = []
    for instance in instances:
        if instance.state.get('Name') != 'terminated':
            instances_list.append(instance.id)
    return instances_list


def ec2_get_by_tagname(instance_name):
    """
    找到标签Name, 值为输入参数的实例
    :param instance_name:
    :return 实例清单:
    """
    instances = ec2.instances.filter()
    instances_list = []
    for instance in instances:
        if {'Key': 'Name', 'Value': instance_name} in instance.tags and instance.state.get('Name') != 'terminated':
            instances_list.append(instance.id)
    return instances_list


def ec2_instance_detail(instance_id):
    """
    查询特定实例的详细信息
    :param instance_id (实例ID):
    :return 特性实例的详细信息:
    """
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
