import os
import shutil

# Specify the paths of the current_week and archive folders
current_week_folder = 'C:\Users\Steve\Desktop\Arduino\LHS_Engineering_Curriculum\visitor_station\Current_week'
archive_folder = 'C:\Users\Steve\Desktop\Arduino\LHS_Engineering_Curriculum\visitor_station\Archive'

# Get the list of files in the current_week folder
files = os.listdir(current_week_folder)

# Move each file to the archive folder
for file in files:
    # Construct the source and destination paths
    src = os.path.join(current_week_folder, file)
    dst = os.path.join(archive_folder, file)
    
    # Move the file
    shutil.move(src, dst)