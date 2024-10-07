# remove empty folders
import os

folder_path ='hello' #delete folder without data
os.rmdir(folder_path) # (error = only empty folders are remove)
print(f"Folder '{folder_path}' removed successfully.")

