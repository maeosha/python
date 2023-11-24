import os

from time import sleep

from typing import Dict

from selenium import webdriver

from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException


def creating_files():
    """сreates a dataset using the os library"""
    try:
        os.mkdir(os.path.join("data_set"))
    except:
        print("Error! A file with this name already exists!")
        print("Do you want to continue in this file?")
        print("1 - yes, 2 - no")
        answer = int(input())
        if answer == 2:
            quit()

    for i in range(0, 6):
        if not os.path.isdir(os.path.join("data_set", f"{i} stars")):
            os.mkdir(os.path.join("data_set", f"{i} stars"))


def creating_file_name(authors_rating: float, count: Dict[int, int]) -> str:
    """creating a file name for further work"""
    zeros: Dict[int, str] = {1: "000", 2: "00", 3: "0", 4: ""}
    number_of_reviews: int = count[int(authors_rating)]
    number_of_stars: int = int(authors_rating)
    number_of_zeros: str = zeros[len(str(number_of_reviews))]
    file_name: str = os.path.join("data_set", f"{number_of_stars} stars", f"{number_of_zeros}{number_of_reviews}")
    return file_name


def write_to_fail(book_title: str, overall_rating: str, authors_rating: float, full_review: str, file_name: str):
    """writing data to a file"""
    with open(file_name, "w", encoding='utf-8') as file_review:
        file_review.write(f"Название книги: {book_title}\n")
        file_review.write(f"Общая оценка: {overall_rating} / 5\n")
        file_review.write(f"Оценка автора: {authors_rating} / 5\n")
        file_review.write(f"Отзыв: {full_review}\n")


def getting_full_review(driver: WebDriver, count: Dict[int, int]):
    """getting information from the site and transmitting this data to the functions"""
    sleep(5)
    buttons = driver.find_elements(By.CSS_SELECTOR, "a.read-more__link")

    for elem in range(len(buttons)):
        sleep(1)
        driver.execute_script(f'document.getElementsByClassName("read-more__link")[{elem}].click()')

    books = driver.find_elements(By.CSS_SELECTOR, "article.review-card.lenta__item ")
    for book in books:
        book_title = book.find_element(By.CSS_SELECTOR, "a.lenta-card__book-title").text

        try:
            authors_rating: str = book.find_element(By.CSS_SELECTOR, "span.lenta-card__mymark").text
            authors_rating: float = float(authors_rating)
        except NoSuchElementException:
            continue

        if count[int(float(authors_rating))] >= 1001:
            continue

        if book.find_element(By.CSS_SELECTOR, "div.lenta-card__rating"):
            overall_rating: str = book.find_element(By.CSS_SELECTOR, "div.lenta-card__rating").text
        else:
            continue

        if book.find_elements(By.ID, "lenta-card__text-review-full"):
            full_review: str = book.find_element(By.ID, "lenta-card__text-review-full").text
        else:
            full_review: str = book.find_element(By.ID, "lenta-card__text-review-escaped").text

        file_name: str = creating_file_name(authors_rating, count)
        write_to_fail(book_title, overall_rating, authors_rating, full_review, file_name)
        count[int(float(authors_rating) // 1)] += 1


def start_parse(page: int, count: Dict[int, int], url: str):
    """the beginning of parsing"""
    creating_files()

    while sum(count) <= 6000:
        url = f"{url[:-1]}{page}"
        driver: WebDriver = webdriver.Chrome()
        driver.get(url)
        getting_full_review(driver, count)
        page += 1

