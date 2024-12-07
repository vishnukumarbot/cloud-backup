import os
from utils.s3_utils import upload_to_s3

def monitor_and_backup(directory, bucket_name):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            print(f"Backing up file: {file_name}")
            upload_to_s3(file_path, bucket_name)

def __init__(self,file_backup):
    self.file_backup=file_backup