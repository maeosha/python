import logging

import void
import matplotlib.pyplot as plt
import argparse

from nltk import SnowballStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

from data_frame import create_data_frame
from data_frame import filter_by_stars


logging.basicConfig(level=logging.INFO)


def create_histogram(path_csv: str, stars: int) -> list:
    """The function creates a histogram"""
    data_frame = create_data_frame(path_csv)

    stemmer = SnowballStemmer("russian")
    lemmatizer = WordNetLemmatizer()
    lemmas = []

    reviews = filter_by_stars(data_frame, stars)["review"]
    for review in reviews:
        for word in word_tokenize(review):
            if ord(word[0]) > 191:
                lemmas.append(lemmatizer.lemmatize(word))
    logging.info("Histogram have created!")
    return lemmas


def draw_histogram(path_csv: str) -> void:
    """The function draws a histogram"""
    plt.bar(range(0, 6), [len(create_histogram(path_csv, stars)) for stars in range(0, 6)])
    plt.xlabel("Number of stars")
    plt.ylabel("Number of words in review")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Input csv path, label of class")
    parser.add_argument("--csv", help="Input csv path", default="data_csv", type=str)
    args = parser.parse_args()
    draw_histogram(args.csv)








