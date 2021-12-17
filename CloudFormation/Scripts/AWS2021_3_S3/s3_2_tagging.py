import boto3
s3_client = boto3.client('s3')


def s3_tagging(s3_files, s3_bucket, tags_list):
    for file in s3_files:
        s3_client.put_object_tagging(Bucket=s3_bucket,
                                     Key=file,
                                     # VersionId='string',
                                     # ContentMD5='string',
                                     Tagging={'TagSet': tags_list},
                                     # ExpectedBucketOwner='string'
                                     )


if __name__ == '__main__':
    # s3_tagging(['index.html', 'error.html'], 'aws2021-s3-basic', [{'Key': 'web_file', 'Value': 'http_file'}])
    s3_tagging(['index.html', 'error.html'], 'aws2021-s3-full', [{'Key': 'web_file', 'Value': 'http_file'}])
