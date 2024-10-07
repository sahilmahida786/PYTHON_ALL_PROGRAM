import shutil

folder_path = 'hello' #delete all folder with data!
try:
    shutil.rmtree(folder_path)
    print(f"Folder '{folder_path}' and its contents removed successfully.")
except OSError as e:
    print(f"Error removing folder '{folder_path}': {e}")