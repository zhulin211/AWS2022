import boto3
session = boto3.Session(profile_name='awslabuser')
# session = boto3.Session(profile_name='default')
s3 = session.resource('s3')


def s3_delete(s3_files, s3_bucket):
    for file in s3_files:
        s3.Object(s3_bucket, file).delete()


def s3_empty(s3_bucket):
    s3_bucket = s3.Bucket(s3_bucket)
    try:
        bucket_versioning = s3.BucketVersioning(s3_bucket)

        if bucket_versioning.status == 'Enabled':
            s3_bucket.object_versions.delete()
        else:
            s3_bucket.objects.all().delete()
    except Exception:
        s3_bucket.objects.all().delete()


def delete_bucket(bucket_name):
    s3_bucket = s3.Bucket(bucket_name)
    s3_bucket.delete()


def empty_and_delete_bucket(bucket_name):
    s3_empty(bucket_name)
    delete_bucket(bucket_name)


if __name__ == '__main__':
    # s3_delete(['index.html', 'error.html'], 'aws2022-s3-basic')
    # s3_delete(['select.csv'], 'aws2022-s3-basic')
    # s3_empty('aws2022-s3-basic')
    # delete_buket('aws2022-s3-basic')

    # 删除GUI创建的文件
    s3_delete(['index.html', 'error.html'], 'qytangaws2022s3')
    # # 删除GUI创建的S3
    # empty_and_delete_bucket('qytangaws2022s3')


