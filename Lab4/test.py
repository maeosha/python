import logging

import pandas as pd
import csv

import void
from nltk import SnowballStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import argparse


logging.basicConfig(level=logging.INFO)


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
    return data_frame.describe()


def filter_by_number_of_words(data_frame: pd.DataFrame, limit_value: int) -> pd.DataFrame:
    """The function filters by the number of words"""
    return data_frame[data_frame["number of words"] <= limit_value]


def filter_by_stars(data_frame: pd.DataFrame, stars: int) -> pd.DataFrame:
    """The function filters by the number of stars"""
    if stars < 0 or stars > 5:
        logging.warning("Invalid number of stars!")
    else:
        return data_frame[data_frame["stars"] == stars]


def get_stats_information(data_frame: pd.DataFrame, stars: int) -> pd.DataFrame:
    """The star-filtered function receives statistical information"""
    data_frame = filter_by_stars(data_frame, stars)
    return data_frame.agg({'number of words': ['max', 'min', 'mean']})


def create_histogram(data_frame: pd.DataFrame, stars: int) -> list:
    """The function creates a histogram"""
    stemmer = SnowballStemmer("russian")
    lemmatizer = WordNetLemmatizer()
    lemmas = []

    reviews = filter_by_stars(data_frame, stars)["review"]
    for review in reviews:
        for word in word_tokenize(review):
            if ord(word[0]) > 191:
                lemmas.append(lemmatizer.lemmatize(word))
    return lemmas


def draw_histogram(data_frame: pd.DataFrame) -> void:
    """The function draws a histogram"""
    plt.bar(range(0, 6), [len(create_histogram(df, i)) for i in range(0, 6)])
    plt.xlabel("Number of stars")
    plt.ylabel("Number of words in review")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Input csv path, label of class")
    parser.add_argument( "--csv", help="Input csv path", default="data_csv", type=str)
    args = parser.parse_args()
    df = create_data_frame(args.csv)
    draw_histogram(df)








