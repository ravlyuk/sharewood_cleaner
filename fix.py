"""
RUN FROM COURSE FOLDER:
python3 fix.py
"""

import os


def rename_folders_and_files_recursively(path: str, substr: str) -> None:
    for root, dirs, files in os.walk(path, topdown=False):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            new_file_name = file_name.replace(substr, "")
            new_file_path = os.path.join(root, new_file_name)
            os.rename(file_path, new_file_path)

        for folder_name in dirs:
            folder_path = os.path.join(root, folder_name)
            new_folder_name = folder_name.replace(substr, "")
            new_folder_path = os.path.join(root, new_folder_name)
            os.rename(folder_path, new_folder_path)


def delete_files_by_name(path: str) -> None:
    for root, dirs, files in os.walk(path):
        for file_name in files:
            if '.url' in file_name or 'прочти перед изучением!' in file_name.lower():
                os.remove(os.path.join(root, file_name))


scan_path = os.getcwd()
substring = '[SW.BAND]'

rename_folders_and_files_recursively(scan_path, substring)
delete_files_by_name(scan_path)

print('Complete!')
