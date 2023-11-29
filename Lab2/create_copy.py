import logging
import os
import csv
import shutil
import void


def get_file_path(data_dir_name: str, new_dir_name: str, new_csv_name: str) -> void:
    """getting file paths and the number of stars"""
    file_info_list: list = []
    for stars in os.listdir(data_dir_name):
        for file_name_txt in os.listdir(os.path.join(data_dir_name, stars)):
            path_copied_file: str = os.path.join(data_dir_name, stars, file_name_txt)
            path_new_file: str = os.path.join(new_dir_name, stars + "_" + file_name_txt)
            absolute_path_file: str = os.path.abspath(path_new_file)
            file_info_list.append([absolute_path_file, path_new_file, stars[0]])
            copy_files(path_copied_file, path_new_file)
            make_new_csv(new_csv_name, file_info_list)


def create_copy_dir(new_dir_name: str) -> void:
    try:
        os.mkdir(os.path.join(new_dir_name))
    except NameError:
        logging.warning("Error! A file with this name already exists!", NameError)


def copy_files(path_copied_file: str, path_new_file: str):
    shutil.copy(path_copied_file, path_new_file)


def make_new_csv(new_csv_name: str, file_info_list: list) -> void:
    with open(os.path.join(new_csv_name), "w", newline="", encoding='utf-8') as file:
        write = csv.writer(file)
        write.writerow(["Absolute path", "Relative path", "Number of stars"])
        write.writerows(file_info_list)
