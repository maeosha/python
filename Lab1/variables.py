import argparse
count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

parser = argparse.ArgumentParser()
parser.add_argument("--page", type=int, default=2, help="number of pages, (default: 2)")
parser.add_argument("--url",
                    type=str,
                    defoult=f"https://www.livelib.ru/reviews/~{2}#reviews",
                    help="address of the LiveLib page")
my_variables = parser.parse_args()
