import argparse
from website_parse import start_parse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--page",
                        type=int,
                        default=2,
                        help="number of page, (default: 2)")

    parser.add_argument('--url',
                        type=str,
                        default="https://www.livelib.ru/reviews/~2",
                        help='address of the LiveLib page')

    parser.add_argument('--dir_name',
                        type=str,
                        default="data_set",
                        help='directory name')

    parser.add_argument('--max_txt_files',
                        type=int,
                        default=1001,
                        help='maximum number of files per evaluation')

    my_variables = parser.parse_args()
    count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    start_parse(count, my_variables)
