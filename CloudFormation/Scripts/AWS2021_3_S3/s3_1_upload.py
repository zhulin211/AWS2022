import boto3
s3_client = boto3.client('s3')


def s3_upload(local_file, s3_bucket, dst_file):
    s3_client.upload_file(local_file, s3_bucket, dst_file, ExtraArgs={'ContentType': 'text/html'})


if __name__ == '__main__':
    # s3_upload('./files/index.html', 'aws2021-s3-basic', 'index.html')
    # s3_upload('./files/error.html', 'aws2021-s3-basic', 'error.html')
    # s3_upload('./files/select.csv', 'aws2021-s3-basic', 'select.csv')

    s3_upload('./files/index.html', 'aws2021-s3-full', 'index.html')
    s3_upload('./files/error.html', 'aws2021-s3-full', 'error.html')
