import os
import shutil
from dotenv import load_dotenv

load_dotenv()

algo_path = os.getenv('MY_ALGO_PATH')
print(algo_path)

# Path to the directory containing the files
dir_path = f'{algo_path}/programmers/lvl_1'

# Iterate over each file in the directory
for file_name in os.listdir(dir_path):
    # Construct the full path to the file
    file_path = os.path.join(dir_path, file_name)
    
    # Check if the file is a regular file
    if os.path.isfile(file_path):
        # Create a directory with the same name as the file
        folder_name = os.path.splitext(file_name)[0]
        folder_path = os.path.join(dir_path, folder_name)
        os.mkdir(folder_path)
        
        # Move the file into the new directory
        shutil.move(file_path, folder_path)

        readme_path = os.path.join(folder_path, 'README.md')
        with open(readme_path, 'w') as f:
            f.write(f'# {folder_name}\n\nThis folder was created from the file {file_name}.')