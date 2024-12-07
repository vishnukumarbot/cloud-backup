import boto3
import os
import time

# Creates S3 client
def get_s3_client(region=None):
    return boto3.client(
        "s3",
        region_name=region  
    )

#Uploads a file to S3 bucket.
def upload_to_s3(file_path, bucket_name, object_name=None, region=None):
    object_name = object_name or os.path.basename(file_path)

    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return

    s3 = get_s3_client(region)
    try:
        start_time = time.time()
        s3.upload_file(file_path, bucket_name, object_name)
        latency = time.time() - start_time
        print(f"Uploaded {file_path} to {bucket_name}/{object_name} in {latency:.2f} seconds.")
    except Exception as e:
        print(f"Failed to upload {file_path} to {bucket_name}/{object_name}: {e}")


