import os
import platform
from datetime import datetime
import shutil
def get_file_creation_time(file_path):
    
       
        creation_time = os.path.getctime(file_path)
        
        return creation_time
def makeing_directory(b):
    v=r"C:\Users\aksha\OneDrive\Desktop\aky drive"
    file_path = os.path.join(v,b)
    if os.path.exists(file_path):
        return
    else:
        os.mkdir(file_path)
# C:\Users\aksha\OneDrive\Desktop\aky drive\2023-09-19
def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d ')
def move_file():
    v=r"C:\Users\aksha\OneDrive\Desktop\aky drive"
    h=os.listdir(v)



v=r"C:\Users\aksha\OneDrive\Desktop\aky drive"
h=os.listdir(v)
for i in h:
 file_pathfile = rf'C:\Users\aksha\OneDrive\Desktop\aky drive\{i}' 
 creation_time = get_file_creation_time(file_pathfile)
 formatted_creation_time = timestamp_to_date(creation_time)
 mainfile_path=r"C:\Users\aksha\OneDrive\Desktop\aky drive"
 combined=os.path.join(mainfile_path,formatted_creation_time)
 if(os.path.exists(combined)):
    combined=combined.replace('\\',"\\\\")
    j=rf"C:\Users\aksha\OneDrive\Desktop\aky drive\{i}"
    shutil.move(j,combined)
    print(combined)
 makeing_directory(formatted_creation_time)



