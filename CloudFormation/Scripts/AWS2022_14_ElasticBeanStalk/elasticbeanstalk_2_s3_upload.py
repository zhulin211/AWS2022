from Scripts.AWS2022_3_S3.s3_1_upload import s3_upload
from Scripts.AWS2022_3_S3.s3_5_upload_dir import upload_folder_to_s3


if __name__ == "__main__":
    # 样本应用介绍与下载
    # https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/tutorials.html
    s3_upload('./python.zip', 'aws2022-s3-elastic-beanstalk', 'python.zip')
    import boto3
    s3 = boto3.resource('s3', region_name='us-east-1')
    s3bucket = s3.Bucket("aws2022-s3-elastic-beanstalk")
    upload_folder_to_s3(s3bucket, "./static", "static")
