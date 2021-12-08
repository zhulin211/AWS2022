#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 聊点高级的
# http://www.mingjiao.org:8088

import boto3
from region import region
templates_path = '../ECS/ecs_0_create_vpc_nets.yaml'
client = boto3.client('cloudformation', region_name=region)

# response = client.create_stack(
#     StackName='ECSVPCNETS',
#     TemplateBody=open(templates_path, encoding='UTF-8').read(),
#     Tags=[
#         {
#             'Key': 'Name',
#             'Value': 'ECSVPCNETS'
#         },
#     ],
# )


# response = client.update_stack(
#     StackName='ECSVPCNETS',
#     TemplateBody=open(templates_path).read()
# )

response = client.delete_stack(
    StackName='ECSVPCNETS',
)