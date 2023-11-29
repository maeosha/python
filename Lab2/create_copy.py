import logging
import os
import csv
import shutil
import void


logging.basicConfig(level=logging.INFO)


def create_copy(data_dir_name: str, new_dir_name: str, new_csv_name: str) -> void:
    """getting file paths and the number of stars and calling all file functions"""
    file_info_list: list = []
    for stars in os.listdir(data_dir_name):
        for file_name_txt in os.listdir(os.path.join(data_dir_name, stars)):
            path_copied_file:   str = os.path.join(data_dir_name, stars, file_name_txt)
            path_new_file:      str = os.path.join(new_dir_name, stars + "_" + file_name_txt)
            absolute_path_file: str = os.path.abspath(path_new_file)

            file_info_list.append([absolute_path_file, path_new_file, stars[0]])
            copy_files(path_copied_file, path_new_file)

    make_new_csv(new_csv_name, file_info_list)


def create_copy_dir(new_dir_name: str) -> void:
    """creating a new date directory"""
    try:
        os.mkdir(os.path.join(new_dir_name))
    except NameError:
        logging.warning("Error! A file with this name already exists!", NameError)

    logging.info(f"{new_dir_name} successfully created!")


def copy_files(path_copied_file: str, path_new_file: str) -> void:
    """copying txt files from the old directory to the new one"""
    shutil.copy(path_copied_file, path_new_file)


def make_new_csv(new_csv_name: str, file_info_list: list) -> void:
    """creating a csv file for a new directory"""
    with open(os.path.join(new_csv_name), "w", newline="", encoding='utf-8') as file:
        write = csv.writer(file)
        write.writerow(["Absolute path", "Relative path", "Number of stars"])
        write.writerows(file_info_list)
    logging.info(f"{new_csv_name} successfully created!")
