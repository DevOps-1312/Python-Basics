# utils.py
# Utility functions for various operations

import os
import datetime

def run_command(command):
    return os.system(command)

command = "dir"  # Example command to list directory contents
run_command(command)

def get_current_datetime():
    return datetime.datetime.now()

today = get_current_datetime()
print("Current date and time:", today)