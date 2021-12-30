import boto3
session = boto3.Session(profile_name='awslabuser')
# session = boto3.Session(profile_name='default')
s3_client = session.client('s3')


def s3_upload(local_file, s3_bucket, dst_file):
    s3_client.upload_file(local_file,
                          s3_bucket,
                          dst_file,
                          ExtraArgs={'ContentType': 'text/html'}  # 注意: 设置ContentType
                          )


if __name__ == '__main__':
    # s3_upload('./files/index.html', 'aws2022-s3-basic', 'index.html')
    # s3_upload('./files/error.html', 'aws2022-s3-basic', 'error.html')
    # s3_upload('./files/select.csv', 'aws2022-s3-basic', 'select.csv')

    # s3_upload('./files/index.html', 'aws2022-s3-full', 'index.html')
    # s3_upload('./files/error.html', 'aws2022-s3-full', 'error.html')

    # GUI创建的S3
    s3_upload('./files/index.html', 'qytangaws2022s3', 'index.html')
    s3_upload('./files/error.html', 'qytangaws2022s3', 'error.html')
    s3_upload('./files/select.csv', 'qytangaws2022s3', 'select.csv')
