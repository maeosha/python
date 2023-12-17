import pandas as pd
import csv
import logging

logging.basicConfig(level=logging.INFO)


def make_data_frame(path_csv: str) -> pd.DataFrame:
    """The function creates a date frame"""
    texts: list = []
    stars: list = []
    count_words: list = []
    with open(path_csv, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        reader.__next__()
        for row in reader:
            stars.append(int(row[2]))
            with open(row[0], 'r', encoding='utf-8') as txtfile:
                lines = txtfile.readlines()
                text = ''
                for index in range(3, len(lines)):
                    text += lines[index]

                texts.append(text[6:])
                count_words.append(len(text))
    data_frame = pd.DataFrame({'review': texts, 'number of words': count_words, 'stars': stars}).dropna()

    logging.info("DataFrame was created!")

    return data_frame


def get_stats_information(data_frame: pd.DataFrame):
    return data_frame.describe()


def filter_by_number_of_words(data_frame: pd.DataFrame, limit_value: int):
    return data_frame[data_frame["number of words"] <= limit_value]


def filter_by_stars(data_frame: pd.DataFrame, stars: int):
    if stars < 0 or stars > 5:
        logging.warning("Invalid number of stars!")
    else:
        return data_frame[data_frame["stars"] == stars]


def get_stats_information(data_frame: pd.DataFrame, stars: int):
    return data_frame.groupby('stars').agg({'number of words': ['max', 'min', 'mean']})




