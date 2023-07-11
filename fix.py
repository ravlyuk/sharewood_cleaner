"""

RUN FROM COURSE FOLDER:

python3 fix.py

"""

import os


def remove_substring_from_filename(folder_path, substring):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if substring in file_name:
                new_file_name = file_name.replace(substring, '')
                old_file_path = os.path.join(root, file_name)
                new_file_path = os.path.join(root, new_file_name)
                os.rename(old_file_path, new_file_path)

        for dir_name in dirs:
            if substring in dir_name:
                new_dir_name = dir_name.replace(substring, '')
                old_dir_path = os.path.join(root, dir_name)
                new_dir_path = os.path.join(root, new_dir_name)
                os.rename(old_dir_path, new_dir_path)


def delete_files_by_name(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if '.url' in file_name or 'прочти перед изучением!' in file_name.lower():
                file_path = os.path.join(root, file_name)
                os.remove(file_path)


# Specify the folder path and substring to be removed
folder_path = os.getcwd()
substring = '[SW.BAND]'

# Remove the substring from filenames
remove_substring_from_filename(folder_path, substring)


# Delete the specified files
delete_files_by_name(folder_path)
