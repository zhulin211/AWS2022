import boto3
import botocore
import time


def get_stack_status(stack_name, region='us-east-1'):
    client = boto3.client('cloudformation', region_name=region)
    response = client.list_stacks()

    for s in response.get('StackSummaries'):
        # print(s.get('StackStatus'))
        if s.get('StackName') == stack_name and s.get('StackStatus') == 'CREATE_COMPLETE':
            return True
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'UPDATE_COMPLETE':
            return True
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'UPDATE_ROLLBACK_COMPLETE':
            return True
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'ROLLBACK_COMPLETE':
            delete_stack(stack_name, region=region)
            print('等待五秒删除处于\'ROLLBACK_COMPLETE\'状态的Stack')
            time.sleep(5)
            return False
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS':
            return True
        elif s.get('StackName') == stack_name and s.get('StackStatus') == 'DELETE_IN_PROGRESS':
            return True
    return False


def create_update_cf(stack_name, template_path, region='us-east-1', parameters=None):
    client = boto3.client('cloudformation', region_name=region)
    if get_stack_status(stack_name, region=region):
        try:
            response = client.update_stack(
                StackName=stack_name,
                Parameters=parameters if parameters else [],
                Capabilities=[
                    'CAPABILITY_IAM',
                    'CAPABILITY_AUTO_EXPAND',
                    'CAPABILITY_NAMED_IAM'
                ],
                TemplateBody=open(template_path, encoding='UTF-8').read()
            )
            try:
                status_code = response.get('ResponseMetadata').get('HTTPStatusCode')
                if status_code == 200:
                    return "一切正常"
                else:
                    print("出现错误")
                    return status_code
            except Exception as e:
                return f"出现错误: {str(e)}"

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
                    'CAPABILITY_AUTO_EXPAND',
                    'CAPABILITY_NAMED_IAM'
                ],
                TemplateBody=open(template_path, encoding='UTF-8').read(),
                Tags=[
                    {
                        'Key': 'Name',
                        'Value': stack_name
                    },
                ],
            )
            try:
                status_code = response.get('ResponseMetadata').get('HTTPStatusCode')
                if status_code == 200:
                    return "一切正常"
                else:
                    print("出现错误")
                    return status_code
            except Exception as e:
                return f"出现错误: {str(e)}"

        except Exception as e:
            print(f'出现错误:{str(e)}')


def delete_stack(stack_name, region='us-east-1'):
    client = boto3.client('cloudformation', region_name=region)
    response = client.delete_stack(
        StackName=stack_name,
    )
    return response