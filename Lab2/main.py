import argparse
from create_csv_file import create_csv
from create_copy import create_copy
from create_copy import create_copy_dir
from create_random import create_random
from create_random import create_random_dir


parser = argparse.ArgumentParser()

parser.add_argument('--csv_name',
                    type=str,
                    default="data.csv",
                    help='csv file name')

parser.add_argument('--new_csv_name',
                    type=str,
                    default="new_data.csv",
                    help='csv file of the new copy of the directory')

parser.add_argument('--random_csv_name',
                    type=str,
                    default="random_data.csv",
                    help='he name of the csv file with random placement of txt files')


parser.add_argument('--data_dir_name',
                    type=str,
                    default="data_set",
                    help='directory name')

parser.add_argument('--new_dir_name',
                    type=str,
                    default="new_data",
                    help='the name of the file where the contents of the old file will be copied')

parser.add_argument('--random_dir_name',
                    type=str,
                    default="random_data",
                    help='the name of the file with random placement of txt files')

if __name__ == "__main__":
    my_variables = parser.parse_args()

    csv_name:        str = my_variables.csv_name
    new_csv_name:    str = my_variables.new_csv_name
    random_csv_name: str = my_variables.random_csv_name

    data_dir_name:   str = my_variables.data_dir_name
    new_dir_name:    str = my_variables.new_dir_name
    random_dir_name: str = my_variables.random_dir_name

    create_csv(data_dir_name, csv_name)

    create_copy_dir(new_dir_name)
    create_copy(data_dir_name, new_dir_name, new_csv_name)

    create_random_dir(random_dir_name)
    create_random(data_dir_name, random_dir_name, random_csv_name)
