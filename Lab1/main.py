import argparse

from website_parse import start_parse


parser = argparse.ArgumentParser()

parser.add_argument("--page",
                    type=int,
                    default=2,
                    help="number of page, (default: 2)")

parser.add_argument('--url',
                    type=str,
                    default="https://www.livelib.ru/reviews/~2",
                    help='address of the LiveLib page')

my_variables = parser.parse_args()

if __name__ == "__main__":
    count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    page = my_variables.page
    url = my_variables.url

    start_parse(page, count, url)






