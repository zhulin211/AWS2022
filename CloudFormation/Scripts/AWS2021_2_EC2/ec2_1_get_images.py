import boto3
import re
from CloudFormation.Scripts.region import region
# client = boto3.client('ec2', region_name=region)
client = boto3.client('ec2', region_name="ap-northeast-2")
# client = boto3.client('ec2', region_name="ap-southeast-2")


def get_last_ami2():
    filters = [{'Name': 'description', 'Values': ['Amazon Linux 2 AMI 2.0.*gp2']}]
    # filters = [{'Name': 'description', 'Values': ['Amazon Linux 2 Kernel 5.10 AMI 2.0.*gp2']}]
    response = client.describe_images(Owners=['amazon'], Filters=filters)
    image_list = []
    for image in response.get('Images'):
        image_list.append([image.get('Description'), image.get('ImageId')])
    # for i in image_list:
    #     print(i)
    image_list = sorted(image_list,
                        key=lambda x: int(re.match(r'Amazon Linux 2 AMI 2\.0\.(\d+)[\.\s]+.*', x[0]).groups()[0]),
                        # key=lambda x: int(re.match(r'Amazon Linux 2 Kernel 5.10 AMI 2\.0\.(\d+)[\.\s]+.*', x[0]).groups()[0]),
                        reverse=True)
    return image_list[0][1]


if __name__ == '__main__':
    print(get_last_ami2())
