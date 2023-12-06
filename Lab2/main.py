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
                    help='the name of the file where the contents of the old file will be copied')

parser.add_argument('--new_csv_name',
                    type=str,
                    default="new_data.csv",
                    help='csv file of the new copy of the directory')

parser.add_argument('--number_of_stars',
                    type=int,
                    default=0,
                    help="getting file paths with this number of stars(default = 0)"
                    )

parser.add_argument('--processing_method',
                    type=int,
                    default=4,
                    help="creating one of this(default = 1):"
                         " 1 - a date annotation file,"
                         " 2 - a copy of the date with an annotation file,"
                         " 3 - a copy of the date with random names and an annotation file,"
                         " 4 - getting paths to files with certain stars"
                    )


if __name__ == "__main__":
    my_variables = parser.parse_args()
    new_csv_name = my_variables.new_csv_name
    random_list: list = list(range(1, 10000))
    start_work(random_list, *(vars(my_variables).values()))