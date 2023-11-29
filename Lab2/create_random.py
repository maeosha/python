import random
import logging
import os
import csv
import shutil
import void


logging.basicConfig(level=logging.INFO)

general_list: list = list(range(0, 10000))


def create_random(data_dir_name: str, random_dir_name: str, random_csv_name: str) -> void:
    """getting file paths and the number of stars and calling all file functions"""
    file_info_list: list = []
    for stars in os.listdir(data_dir_name):
        for file_name_txt in os.listdir(os.path.join(data_dir_name, stars)):
            random_element:     int = random.choice(general_list)
            path_copied_file:   str = os.path.join(data_dir_name, stars, file_name_txt)
            path_random_file:   str = os.path.join(random_dir_name, f"{random_element}")
            absolute_path_file: str = os.path.abspath(path_random_file)

            general_list.remove(random_element)
            file_info_list.append([absolute_path_file, path_random_file, stars[0]])
            copy_files(path_copied_file, path_random_file)
    make_random_csv(random_csv_name, file_info_list)


def create_random_dir(random_dir_name: str) -> void:
    """creating a new date directory"""
    try:
        os.mkdir(os.path.join(random_dir_name))
    except NameError:
        logging.warning("Error! A file with this name already exists!", NameError)

    logging.info(f"{random_dir_name} successfully created!")


def copy_files(path_copied_file: str, path_random_file: str) -> void:
    """copying txt files from the old directory to the new one"""
    shutil.copy(path_copied_file, path_random_file)


def make_random_csv(random_csv_name: str, file_info_list: list) -> void:
    """creating a csv file for a new directory"""
    with open(os.path.join(random_csv_name), "w", newline="", encoding='utf-8') as file:
        write = csv.writer(file)
        write.writerow(["Absolute path", "Relative path", "Number of stars"])
        write.writerows(file_info_list)

    logging.info(f"{random_csv_name} successfully created!")
