import logging
import os
import csv
import shutil
import void
import random
from file_iterator import FileIterator


logging.basicConfig(level=logging.INFO)


def fail_path_information(data_dir_name: str, new_dir_name: str, processing_method: int, random_list: list) -> list:
    """getting file paths and the number of stars and calling all file functions"""
    file_info_list: list = []
    path_new_file: list = [""]
    for stars in os.listdir(data_dir_name):
        for file_name_txt in os.listdir(os.path.join(data_dir_name, stars)):
            path_copied_file: str = os.path.join(data_dir_name, stars, file_name_txt)

            match processing_method:
                case 1:
                    path_new_file[0] = os.path.join(new_dir_name, stars, file_name_txt)
                case 2:
                    path_new_file[0] = os.path.join(new_dir_name, stars + "_" + file_name_txt)
                case 3:
                    random_element: int = random.choice(random_list)
                    path_new_file[0] = os.path.join(new_dir_name, f"{random_element}")
                    random_list.remove(random_element)

            absolute_path_file: str = os.path.abspath(path_new_file[0])

            file_info_list.append([absolute_path_file, path_new_file[0], stars[0], path_copied_file])
    return file_info_list


def create_dir(new_dir_name: str) -> void:
    try:
        os.mkdir(os.path.join(new_dir_name))
    except NameError:
        logging.warning("Error! A file with this name already exists!", NameError)

    logging.info(f"{new_dir_name} successfully created!")


def copy_files(path_copied_files: list, path_new_files: list) -> void:
    """copying txt files from the old directory to the new one"""
    for i in range(len(path_copied_files)):
        shutil.copy(path_copied_files[i], path_new_files[i])


def make_csv(csv_name: str, file_info_list: list) -> void:
    """creating a csv file for a new directory"""
    csv_list: list = []
    for info in file_info_list:
        csv_list.append([info[i] for i in range(3)])

    with open(os.path.join(csv_name), "w", newline="", encoding='utf-8') as file:
        write = csv.writer(file)
        write.writerow(["Absolute path", "Relative path", "Number of stars"])
        write.writerows(csv_list)

    logging.info(f"{csv_name} successfully created!")


def start_work(random_list: list, data_dir_name: str, new_dir_name: str, csv_name: str, number_of_stars: int,
               processing_method: int) -> void:
    """Incredibly, the function is starting to work"""
    file_info_list: list = fail_path_information(data_dir_name, new_dir_name, processing_method, random_list)

    if processing_method > 4 or processing_method < 1:
        logging.warning("The wrong item has been selected!", NameError)

    match processing_method:

        case 1:
            make_csv(csv_name, file_info_list)

        case 2 | 3:
            create_dir(new_dir_name)
            path_copied_files: list = [info[3] for info in file_info_list]
            path_new_files: list = [info[1] for info in file_info_list]
            copy_files(path_copied_files, path_new_files)
            make_csv(csv_name, file_info_list)
        case 4:
            if os.path.isfile(csv_name) == 0:
                logging.warning("The wrong item has been selected!", NameError)

            file_iter = FileIterator(csv_name, number_of_stars)
            for review in file_iter:
                logging.info(review)
