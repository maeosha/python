import argparse
import logging
from enum import Enum

import pandas as pd
import csv

logging.basicConfig(level=logging.INFO)


class ProcessingMethod(Enum):
    stats_information = 1
    stats_information_by_stars = 2
    filter_by_stars = 3
    filter_by_number_of_words = 4


def create_data_frame(path_csv: str) -> pd.DataFrame:
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


def get_stats_information(data_frame: pd.DataFrame) -> pd.DataFrame:
    """The function receives statistical information"""
    logging.info("Statistics received!")
    return data_frame.describe()


def get_stats_information_by_stars(data_frame: pd.DataFrame, stars: int) -> pd.DataFrame:
    """The star-filtered function receives statistical information"""
    data_frame = filter_by_stars(data_frame, stars)
    logging.info("Statistics received!")
    return data_frame.agg({'number of words': ['max', 'min', 'mean']})


def filter_by_number_of_words(data_frame: pd.DataFrame, limit_value: int) -> pd.DataFrame:
    """The function filters by the number of words"""
    logging.info("The dataframe is filtered out!")
    return data_frame[data_frame["number of words"] <= limit_value]


def filter_by_stars(data_frame: pd.DataFrame, stars: int) -> pd.DataFrame:
    """The function filters by the number of stars"""
    if stars < 0 or stars > 5:
        logging.warning("Invalid number of stars!")
    else:
        logging.info("The dataframe is filtered out!")
        return data_frame[data_frame["stars"] == stars]


def start(path_csv: str, stars: int, number_of_words: int, processing_method: int) -> pd.DataFrame:
    if processing_method < 1 or processing_method > 4:
        logging.warning("Invalid processing method!")
    if stars < 0 or stars > 5:
        logging.warning("Invalid number of stars!")

    processing_method = ProcessingMethod(processing_method)
    df = create_data_frame(path_csv)
    match processing_method:
        case processing_method.stats_information:
            df = get_stats_information(df)
        case processing_method.stats_information_by_stars:
            df = get_stats_information_by_stars(df, stars)
        case processing_method.filter_by_stars:
            df = filter_by_stars(df, stars)
        case processing_method.filter_by_number_of_words:
            df = filter_by_number_of_words(df, number_of_words)
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Input csv path, label of class")
    parser.add_argument("--path_csv", help="Input csv path", default="data_csv", type=str)
    parser.add_argument("--stars", help="Input number of stars", default=0, type=int)
    parser.add_argument("--number_of_words", help="Input number of words", default=1000, type=int)
    parser.add_argument("--processing_method",
                        help="creating one of this(default = 1):"
                             " 1 - get statistical data,"
                             " 2 - get statistics from a filtered dataframe,"
                             " 3 - filtering by the number of words,"
                             " 4 - filtering by the number of stars",
                        default=1,
                        type=int)

    args = parser.parse_args()
    df = create_data_frame("data_csv")
    df.to_csv("data_frames", index=False)

