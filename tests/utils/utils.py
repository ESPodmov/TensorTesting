import logging
import os
import time


def get_logs_path():
    curr_path = os.getcwd()
    if curr_path.endswith("tests"):
        return f"{curr_path}\\logs\\"
    else:
        return f"{curr_path}\\tests\\logs\\"


def get_downloads_path():
    curr_path = os.getcwd()
    if curr_path.endswith("tests"):
        return f"{curr_path}\\downloads"
    else:
        return f"{curr_path}\\tests\\downloads"


def get_last_created_file_in_dir(dir_path, file_extension):
    files = [file for file in os.listdir(dir_path) if file.endswith(file_extension)]
    last_modified_file = sorted(files, key=lambda x: os.path.getmtime(os.path.join(dir_path, x)), reverse=True)[0]
    return f"{dir_path}\\{last_modified_file}"


def wait_for_files_deleted(dir_path, file_extension=".crdownload"):
    def get_files(dir_name, extension):
        return [file for file in os.listdir(dir_name) if file.endswith(extension)]

    part_files = []
    timer = 0
    while not part_files and timer < 10:
        part_files = get_files(dir_path, file_extension)
        time.sleep(1)
        timer += 1

    if not part_files:
        return

    while len(part_files) > 0:
        time.sleep(1)
        part_files = [file for file in os.listdir(dir_path) if file.endswith(file_extension)]

    return
