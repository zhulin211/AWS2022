from Scripts.ctf_0_basic_functions import create_update_cf

import boto3
from CloudFormation.region import region
client = boto3.client('cloudformation', region_name=region)

if __name__ == "__main__":
    template_path = '../../AWS2022_6_Database/database_1_rds.yaml'
    stack_name = 'Database1RDS'
    parameters = [
        {'ParameterKey': "DBClusterName", "ParameterValue": 'qytdbcluster'},
        {'ParameterKey': "DBName", "ParameterValue": 'qytdb'},
        {'ParameterKey': "DBUsername", "ParameterValue": 'qytdbuser'},
        {'ParameterKey': "DBPassword", "ParameterValue": 'Cisc0123'},
        {'ParameterKey': "SubnetStackName", "ParameterValue": 'VPC2Subnets'},
        {'ParameterKey': "SecurityGroupStackName", "ParameterValue": 'VPC5SecurityGroup'},
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
