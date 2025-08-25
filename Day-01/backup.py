# backup.py
# This script creates a backup of a specified directory and saves it as a zip file.

import shutil
import datetime
import os

def backup_file(source, destination):
    today = datetime.datetime.today()
    backup_file_name = (f"backup_{today.strftime('%Y%m%d')}")
    print(f"Creating backup from {source} to {backup_file_name}")
    if not os.path.exists(destination):
        os.makedirs(destination)
    shutil.make_archive(backup_file_name,'zip', source)
    print(f"Backup created at: {backup_file_name}")

source = r"C:\Users\p.kumar.l\Documents\DevOps\Python-WorkShop"
destination = r"C:\Users\p.kumar.l\Documents\DevOps\Python-WorkShop\Backups"
backup_file(source, destination)
