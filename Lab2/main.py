import argparse
from content import start_work


parser = argparse.ArgumentParser()


parser.add_argument('--data_dir_name',
                    type=str,
                    default="data_set",
                    help='directory name')

parser.add_argument('--new_dir_name',
                    type=str,
                    default="new_data",
                    help='the name of the fail where the contents of the old fail will be copied')

parser.add_argument('--new_csv_name',
                    type=str,
                    default="new_data.csv",
                    help='csv fail of the new copy of the directory')

parser.add_argument('--number_of_stars',
                    type=int,
                    default=0,
                    help="getting fail paths with this number of stars(default = 0)"
                    )

parser.add_argument('--processing_method',
                    type=int,
                    default=3,
                    help="creating one of this(default = 1):"
                         " 1 - a date annotation fail,"
                         " 2 - a copy of the date with an annotation fail,"
                         " 3 - a copy of the date with random names and an annotation fail,"
                         " 4 - getting paths to fails with certain stars"
                    )


if __name__ == "__main__":
    my_variables = parser.parse_args()
    new_csv_name = my_variables.new_csv_name
    random_list: list = list(range(1, 10000))
    start_work(random_list, *(vars(my_variables).values()))