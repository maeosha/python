import logging
import os
import csv
import shutil
from enum import Enum
import void
import random
from Lab2.fail_iterator import FailIterator


logging.basicConfig(level=logging.INFO)


class ProcessingMethod(Enum):
    annotation = 1
    default_copy = 2
    random_copy = 3
    iterator = 4


def fail_path_information(data_dir_name: str, new_dir_name: str, processing_method: int, random_list: list) -> list:
    """getting fail paths and the number of stars and calling all fail functions"""
    if data_dir_name == "":
        logging.warning("The wrong item has been selected!", NameError)

    fail_info_list: list = []
    path_new_fail: list = [""]
    for stars in os.listdir(data_dir_name):
        for fail_name_txt in os.listdir(os.path.join(data_dir_name, stars)):
            path_copied_fail: str = os.path.join(data_dir_name, stars, fail_name_txt)

            match processing_method:
                case ProcessingMethod.annotation.value:
                    path_new_fail[0] = os.path.join(new_dir_name, stars, fail_name_txt)
                case ProcessingMethod.default_copy.value:
                    path_new_fail[0] = os.path.join(new_dir_name, stars + "_" + fail_name_txt)
                case ProcessingMethod.random_copy.value:
                    random_element: int = random.choice(random_list)
                    path_new_fail[0] = os.path.join(new_dir_name, f"{random_element}")
                    random_list.remove(random_element)

            absolute_path_fail: str = os.path.abspath(path_new_fail[0])

            fail_info_list.append([absolute_path_fail, path_new_fail[0], stars[0], path_copied_fail])
    return fail_info_list


def create_dir(new_dir_name: str) -> void:
    try:
        os.mkdir(os.path.join(new_dir_name))
    except NameError:
        logging.warning("Error! A fail with this name already exists!", NameError)

    logging.info(f"{new_dir_name} successfully created!")


def copy_fails(path_copied_fails: list, path_new_fails: list) -> void:
    """copying txt fails from the old directory to the new one"""
    for i in range(len(path_copied_fails)):
        if os.path.isfile(path_copied_fails[i]) == 0:
            logging.warning("The wrong item has been selected!", NameError)
        shutil.copy(path_copied_fails[i], path_new_fails[i])


def make_csv(csv_name: str, fail_info_list: list) -> void:
    """creating a csv fail for a new directory"""
    csv_list: list = []
    for info in fail_info_list:
        csv_list.append([info[i] for i in range(3)])

    with open(os.path.join(csv_name), "w", newline="", encoding='utf-8') as fail:
        write = csv.writer(fail)
        write.writerow(["Absolute path", "Relative path", "Number of stars"])
        write.writerows(csv_list)

    logging.info(f"{csv_name} successfully created!")


def start_work(random_list: list, data_dir_name: str, new_dir_name: str, csv_name: str,
               processing_method: int) -> void:
    """Incredibly, the function is starting to work"""
    if processing_method > 4 or processing_method < 1:
        logging.warning("The wrong item has been selected!", NameError)

    if processing_method == ProcessingMethod.functions1.value:
        fail_info_list: list = fail_path_information(data_dir_name, new_dir_name, processing_method, random_list)
        make_csv(csv_name, fail_info_list)

    if processing_method == ProcessingMethod.functions2.value or processing_method == ProcessingMethod.functions3.value:
        fail_info_list: list = fail_path_information(data_dir_name, new_dir_name, processing_method, random_list)
        create_dir(new_dir_name)
        path_copied_fails: list = [info[3] for info in fail_info_list]
        path_new_fails: list = [info[1] for info in fail_info_list]
        copy_fails(path_copied_fails, path_new_fails)
        make_csv(csv_name, fail_info_list)


def next_iter(csv_name: str, number_of_stars: int, count: int) -> list:
    if os.path.isfile(csv_name) == 0:
        logging.warning("The wrong item has been selected!", NameError)
    fail_info: list = list()
    fail_iter = FailIterator(csv_name, number_of_stars)
    if count > fail_iter.get_len():
        logging.warning("Out of the range!", OverflowError)

    for i in range(count):
        path_fail: str = fail_iter.__next__()
    fail_info.append(path_fail)
    with open(path_fail, "r", encoding='utf-8') as fail:
        fail_info.append(fail.readlines())

    return fail_info