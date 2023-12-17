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
                texts.append(text)
                count_words.append(len(text))
    df = pd.DataFrame({'review': texts, 'count words': count_words, 'stars': stars})

    logging.info("DataFrame was created!")

    return df


