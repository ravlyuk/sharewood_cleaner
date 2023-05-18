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
                if new_file_name.strip() in ["SW.BAND - 150000 курсов ждут тебя!.url",
                                             "DMC.RIP - Качай редкие курсы!.url", "Прочти перед изучением!.docx"]:
                    os.remove(new_file_path)
        for dir_name in dirs:
            if substring in dir_name:
                new_dir_name = dir_name.replace(substring, '')
                old_dir_path = os.path.join(root, dir_name)
                new_dir_path = os.path.join(root, new_dir_name)
                os.rename(old_dir_path, new_dir_path)
                remove_substring_from_filename(new_dir_path, substring)  # Recursively process subdirectories


# Specify the folder path and the substring to remove
folder_path = os.getcwd()
substring = "[SW.BAND]"

# Remove substring from file names and directory names recursively
remove_substring_from_filename(folder_path, substring)

print('\nDone!')
