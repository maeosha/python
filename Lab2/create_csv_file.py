import csv
import os
import void


def make_csv(file_info_list: list, csv_name: str) -> void:
    """creating a csv file"""
    with open(os.path.join(csv_name), "w", newline="", encoding='utf-8') as file:
        write = csv.writer(file)
        write.writerow(["Absolute path", "Relative path", "Number of stars"])
        write.writerows(file_info_list)


def get_file_info(data_dir_name: str, csv_name: str) -> void:
    """getting file paths and the number of stars"""
    file_info_list: list = []
    for stars in range(6):
        dir_name: str = os.path.join(data_dir_name, f"{stars} stars")
        for file_name_txt in os.listdir(dir_name):
            absolute_path_file: str = os.path.abspath(os.path.join(dir_name, file_name_txt))
            relative_path_file: str = os.path.join(dir_name, file_name_txt)
            file_info_list.append([absolute_path_file, relative_path_file, stars])
    make_csv(file_info_list, csv_name)

