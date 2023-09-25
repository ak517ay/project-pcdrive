import os
from datetime import datetime
import shutil
from tkinter import messagebox
global d
def get_file_creation_time(file_path):
    creation_time = os.path.getctime(file_path)
    return creation_time

def make_directory(directory_path):
    if not os.path.exists(directory_path):
        os.mkdir(directory_path)

def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

source_folder = r"C:\Users\aksha\OneDrive\Desktop\aky drive"
files = os.listdir(source_folder)


for file_name in files:
    if(file_name=="main.py"):
        continue
    file_path = os.path.join(source_folder, file_name)
    creation_time = get_file_creation_time(file_path)
    formatted_creation_time = timestamp_to_date(creation_time)
    
    destination_folder = os.path.join(source_folder, formatted_creation_time)
    make_directory(destination_folder)

    destination_path = os.path.join(destination_folder, file_name)

    shutil.move(file_path, destination_path)
    print(f"Moved '{file_name}' to '{destination_path}'")
messagebox.showinfo(title="aky drive success",message="Your files are put in folders according to their creation time")
