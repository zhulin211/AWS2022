import os
import boto3


def upload_folder_to_s3(s3bucket, inputDir, s3Path):
    print("Uploading results to s3 initiated...")
    print("Local Source:", inputDir)
    os.system("ls -ltR " + inputDir)

    print("Dest  S3path:", s3Path)

    try:
        for path, subdirs, files in os.walk(inputDir):
            for file in files:
                dest_path = path.replace(inputDir, "")
                __s3file = os.path.normpath(s3Path + '/' + dest_path + '/' + file)
                __local_file = os.path.join(path, file)
                print("upload : ", __local_file, " to Target: ", __s3file, end="")
                s3bucket.upload_file(__local_file, __s3file)
                print(" ...Success")
    except Exception as e:
        print(" ... Failed!! Quitting Upload!!")
        print(e)
        raise e


if __name__ == "__main__":
    s3 = boto3.resource('s3', region_name='us-east-1')
    s3bucket = s3.Bucket("aws2022imagess3")
    upload_folder_to_s3(s3bucket, "./static", "static")
