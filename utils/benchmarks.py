import time

def benchmark_upload(upload_func, file_path, bucket_name):
    start_time = time.time()
    upload_func(file_path, bucket_name)
    elapsed_time = time.time() - start_time
    print(f"Upload time: {elapsed_time} seconds")

def benchmark_encryption(encrypt_func, file_path):
    start_time = time.time()
    encrypt_func(file_path)
    elapsed_time = time.time() - start_time
    print(f"Encryption time: {elapsed_time} seconds")
