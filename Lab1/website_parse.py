from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import os
page = 2

count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}


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

        count[int(float(authors_rating) // 1)] += 1


while sum(count) <= 6000:
    url = f"https://www.livelib.ru/reviews/~{page}#reviews"
    driver = webdriver.Chrome()
    driver.get(url)
    page += 1
