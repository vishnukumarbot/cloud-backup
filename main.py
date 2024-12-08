from encryption.encryptor import encrypt_file
from backup.file_backup import monitor_and_backup
from backup.db_backup import backup_database
from notifications.sns_notifications import send_notification
from task_scheduler.scheduler import setup_schedule

if __name__ == "__main__":
    DIRECTORY_TO_BACKUP = "D:/aws/files_to_backup"
    BUCKET_NAME = "databackup123"
    DB_CONFIG = {
        "host": "localhost",
        "user": "root",
        "password": "mypass",
        "database": "aws"
    }
    SNS_TOPIC_ARN = " "

    encrypted_file = encrypt_file(f"{DIRECTORY_TO_BACKUP}/back.mp3")

    monitor_and_backup(DIRECTORY_TO_BACKUP, BUCKET_NAME)

    # Database Backup Example
    backup_database(DB_CONFIG["host"], DB_CONFIG["user"], DB_CONFIG["password"], DB_CONFIG["database"], BUCKET_NAME)

    # Notification Example
    send_notification("Backup Completed Successfully!", SNS_TOPIC_ARN)

    # Schedule Backups
    setup_schedule(DIRECTORY_TO_BACKUP, BUCKET_NAME)
