from CloudFormation.Scripts.AWS2022_3_S3.s3_1_upload import s3_upload
from CloudFormation.Scripts.AWS2022_3_S3.s3_2_tagging import s3_tagging


if __name__ == '__main__':
    s3_upload('../AWS2022_3_S3/files/index.html', 'aws2022-iam-s3', 'index.html')
    s3_upload('../AWS2022_3_S3/files/error.html', 'aws2022-iam-s3', 'error.html')
    s3_tagging(['index.html', 'error.html'], 'aws2022-iam-s3', [{'Key': 'web_file', 'Value': 'http_file'}])