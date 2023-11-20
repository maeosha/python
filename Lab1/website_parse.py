from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import os


def creating_files():
    if not os.path.isdir("data_set"):
        os.mkdir("data_set")
    for i in range(0, 6):
        if not os.path.isdir(f"data_set/{i} stars"):
            os.mkdir(f"data_set/{i} stars")


def creating_file_name(authors_rating, count):
    zero = {1: "000", 2: "00", 3: "0", 4: ""}
    number_of_reviews = count[int(float(authors_rating) // 1)]
    number_of_stars = int(float(authors_rating) // 1)
    number_of_zeros = zero[len(str(number_of_reviews))]
    file_name = f"data_set/{number_of_stars} stars/{number_of_zeros}{number_of_reviews}"
    return file_name


def write_to_fail(book_title, overall_rating, authors_rating, full_review, file_name):
    with open(file_name, "w+", encoding='utf-8') as file_review:
        file_review.write(f"Название книги: {book_title}\n")
        file_review.write(f"Общая оценка: {overall_rating} / 5\n")
        file_review.write(f"Оценка автора: {authors_rating} / 5\n")
        file_review.write(f"Отзыв: {full_review}\n")


def getting_full_review():
    sleep(5)
    buttons = driver.find_elements(By.CSS_SELECTOR, "a.read-more__link")
    for elem in range(len(buttons)):
        sleep(1)
        driver.execute_script(f'document.getElementsByClassName("read-more__link")[{elem}].click()')

    books = driver.find_elements(By.CSS_SELECTOR, "article.review-card.lenta__item ")
    for book in books:
        book_title = book.find_element(By.CSS_SELECTOR, "a.lenta-card__book-title").text

        try:
            authors_rating = book.find_element(By.CSS_SELECTOR, "span.lenta-card__mymark").text
        except NoSuchElementException:
            continue
        if count[int(float(authors_rating) // 1)] >= 1001:
            continue

        if book.find_element(By.CSS_SELECTOR, "div.lenta-card__rating"):
            overall_rating = book.find_element(By.CSS_SELECTOR, "div.lenta-card__rating").text
        else:
            continue

        if book.find_elements(By.ID, "lenta-card__text-review-full"):
            full_review = book.find_element(By.ID, "lenta-card__text-review-full").text
        else:
            full_review = book.find_element(By.ID, "lenta-card__text-review-escaped").text

        file_name = creating_file_name(authors_rating, count)
        write_to_fail(book_title, overall_rating, authors_rating, full_review, file_name)
        count[int(float(authors_rating) // 1)] += 1


creating_files()


page = 2

count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

while sum(count) <= 6000:
    url = f"https://www.livelib.ru/reviews/~{page}#reviews"
    driver = webdriver.Chrome()
    driver.get(url)
    getting_full_review()
    page += 1
