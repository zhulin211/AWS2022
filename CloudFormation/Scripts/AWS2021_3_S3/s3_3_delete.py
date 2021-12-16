import boto3
s3 = boto3.resource('s3')


def s3_delete(s3_files, s3_bucket):
    for file in s3_files:
        s3.Object(s3_bucket, file).delete()


def s3_empty(s3_bucket):
    s3_bucket = s3.Bucket(s3_bucket)
    s3_bucket.objects.all().delete()


def delete_buket(buket_name):
    s3_bucket = s3.Bucket(buket_name)
    s3_bucket.delete()


if __name__ == '__main__':
    # s3_delete(['index.html', 'error.html'], 'aws2021-s3-basic')
    # s3_delete(['select.csv'], 'aws2021-s3-basic')
    # s3_empty('aws2021-s3-basic')
    delete_buket('aws2021-s3-basic')

