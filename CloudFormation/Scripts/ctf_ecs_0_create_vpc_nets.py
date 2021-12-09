#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 聊点高级的
# http://www.mingjiao.org:8088

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
    return False


def create_update_cf(stack_name, template_path):
    if get_stack_status(stack_name):
        try:
            response = client.update_stack(
                StackName=stack_name,
                TemplateBody=open(template_path, encoding='UTF-8').read()
            )
            return response
        except botocore.exceptions.ClientError as e:
            if 'No updates are to be performed' in str(e):
                print('无需更新!')
    else:
        response = client.create_stack(
            StackName=stack_name,
            TemplateBody=open(template_path, encoding='UTF-8').read(),
            Tags=[
                {
                    'Key': 'Name',
                    'Value': stack_name
                },
            ],
        )
        return response


def delete_stack(stack_name):
    response = client.delete_stack(
        StackName=stack_name,
    )
    return response


if __name__ == '__main__':
    template_path = '../ECS/ecs_0_create_vpc_nets.yaml'
    ecs_vpc_nets_stack_name = 'ECSVPCNETS'
    # print(get_stack_status('ECSVPCNETS'))
    # delete_stack(ecs_vpc_nets_stack_name)
    print(create_update_cf(ecs_vpc_nets_stack_name, template_path))
