#Name: Automated File Backup
#Discription: Created a backup folder by updating the original folder daily. 

import os
import shutil
import datetime
import schedule
import time
import threading

source_dir = "C:/Users/ngan1/OneDrive/Documents/Python/Python Projects/New_File"
destination_dir = "C:/Users/ngan1/OneDrive/Documents/Python/Python Projects/Backup_File"

paused = False
running = True

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    os.makedirs(dest, exist_ok=True)

    try:
        shutil.copytree(source, dest_dir)
        print(f"✅ Folder copied to: {dest_dir}")
    except FileExistsError: 
        print(f"⚠️ Folder already exists: {dest_dir}")

def backup_daily():
    if not paused:
        copy_folder_to_directory(source_dir, destination_dir)
    else:
        print("⏸️ Backup is currently paused. Skipping...")

# Schedule the task
schedule.every().day.at("19:41").do(backup_daily)

def scheduler_loop():
    print("🔁 Backup scheduler running. Press 'p' to pause, 'r' to resume, 'q' to quit.")
    while running:
        schedule.run_pending()
        time.sleep(1)

def input_listener():
    global paused, running
    while running:
        cmd = input().strip().lower()
        if cmd == 'p':
            paused = True
            print("⏸️ Paused backup.")
        elif cmd == 'r':
            paused = False
            print("▶️ Resumed backup.")
        elif cmd == 'q':
            running = False
            print("🛑 Exiting backup scheduler...")
            break

# Run in parallel: one for scheduler, one for user input
threading.Thread(target=scheduler_loop, daemon=True).start()
input_listener()
quit
    

    
