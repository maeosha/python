import argparse
from create_csv_file import create_csv
from create_copy import create_copy
from create_copy import create_copy_dir
from create_random import create_random
from create_random import create_random_dir
from file_iterator import FileIterator


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

    create_csv(*(vars(my_variables).values()))

    create_copy_dir(*(vars(my_variables).values()))
    create_copy(*(vars(my_variables).values()))

    create_random_dir(*(vars(my_variables).values()))
    create_random(*(vars(my_variables).values()))

    file_iter = FileIterator("data.csv", 2)
    for review in file_iter:
        print(review)
