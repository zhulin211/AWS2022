import boto3
import botocore
from region import region
client = boto3.client('cloudformation', region_name=region)


def get_stack_status(stack_name):
    response = client.list_stacks()

    for s in response.get('StackSummaries'):
        if s.get('StackName') == stack_name and s.get('StackStatus') == 'CREATE_COMPLETE':
            return True
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'UPDATE_COMPLETE':
            return True
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'UPDATE_ROLLBACK_COMPLETE':
            return True
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'ROLLBACK_COMPLETE':
            delete_stack(stack_name)
            return False
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS':
            return True
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'DELETE_IN_PROGRESS':
            return True
    return False


def create_update_cf(stack_name, template_path, parameters=None):
    if get_stack_status(stack_name):
        try:
            response = client.update_stack(
                StackName=stack_name,
                Parameters=parameters if parameters else [],
                Capabilities=[
                    'CAPABILITY_IAM',
                    'CAPABILITY_AUTO_EXPAND'
                ],
                TemplateBody=open(template_path, encoding='UTF-8').read()
            )
            return response
        except botocore.exceptions.ClientError as e:
            if 'No updates are to be performed' in str(e):
                print('无需更新!')
            print(e)
    else:
        try:
            response = client.create_stack(
                StackName=stack_name,
                Parameters=parameters if parameters else [],
                Capabilities=[
                    'CAPABILITY_IAM',
                    'CAPABILITY_AUTO_EXPAND'
                ],
                TemplateBody=open(template_path, encoding='UTF-8').read(),
                Tags=[
                    {
                        'Key': 'Name',
                        'Value': stack_name
                    },
                ],
            )
            return response
        except Exception as e:
            print(f'出现错误:{str(e)}')


def delete_stack(stack_name):
    response = client.delete_stack(
        StackName=stack_name,
    )
    return response