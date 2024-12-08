import schedule
import time
#from file_backup import monitor_and_backup
from backup.file_backup import monitor_and_backup


def setup_schedule(directory, bucket_name):
    schedule.every().day.at("14:20").do(monitor_and_backup(directory, bucket_name))
    print("Schedule at 14:05")
    while True:
        schedule.run_pending()
        time.sleep(1)

