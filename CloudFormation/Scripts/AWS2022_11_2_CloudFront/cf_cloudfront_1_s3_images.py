from Scripts.ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../../AWS2022_11_2_CloudFront/cloudfront_1_s3_images.yaml'
    stack_name = 'CloudFront1S3Images'
    print(create_update_cf(stack_name, template_path))

    # 使用 "CloudFormation/Scripts/AWS2022_3_S3/s3_5_upload_dir.py" 上传图片
