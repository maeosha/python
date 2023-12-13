import argparse
from enum import Enum

from content import start_work
from content import next_iter


parser = argparse.ArgumentParser()


parser.add_argument('--data_dir_name',
                    type=str,
                    default=" ",
                    help='directory name')

parser.add_argument('--new_dir_name',
                    type=str,
                    default="",
                    help='the name of the fail where the contents of the old fail will be copied')

parser.add_argument('--new_csv_name',
                    type=str,
                    default="C:/Users/mochk/OneDrive/Рабочий стол/coding/python/Lab3/csv_name",
                    help='csv fail of the new copy of the directory')

parser.add_argument('--number_of_stars',
                    type=int,
                    default=0,
                    help="getting fail paths with this number of stars(default = 0)"
                    )

parser.add_argument('--processing_method',
                    type=int,
                    default=4,
                    help="creating one of this(default = 1):"
                         " 1 - a date annotation fail,"
                         " 2 - a copy of the date with an annotation fail,"
                         " 3 - a copy of the date with random names and an annotation fail,"
                         " 4 - getting paths to fails with certain stars"
                    )


if __name__ == "__main__":
    my_variables = parser.parse_args()
    csv_name = "C:/Users/mochk/OneDrive/Рабочий стол/coding/python/Lab3/csvsv"
    random_list: list = list(range(1, 10000))
    fail_list = next_iter(csv_name, 3, 10)
    print(fail_list[0])
    print(fail_list[1])
