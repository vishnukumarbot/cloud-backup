def backup_database(host, user, password, database, bucket_name):
    import os
    from utils.s3_utils import upload_to_s3

    backup_file = f"{database}_backup.sql"
    dump_command = f"mysqldump -h {host} -u {user} -p{password} {database} > {backup_file}"
    os.system(dump_command)

    try:
        upload_to_s3(backup_file, bucket_name, backup_file)
        print(f"Database backup {backup_file} uploaded successfully to {bucket_name}")
    except Exception as e:
        print(f"Failed to upload database backup {backup_file}: {e}")
    finally:
        if os.path.exists(backup_file):
            os.remove(backup_file)
