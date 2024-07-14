import asyncio
from collections import Counter

import aiohttp
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from tqdm import tqdm

from parsing.ai_common import count_tech_words
from parsing.db_common import save_to_db_hard_skills_and_count
from parsing.selenium_web_driver import CustomChrome


def execute_pagination_script_dou(driver: Chrome) -> None:
    element = driver.find_element(By.CSS_SELECTOR, "div.more-btn > a")
    while True:
        try:
            element.click()
        except WebDriverException:
            break


def parse_all_vacancy_urls_dou(driver: Chrome) -> list[str]:
    return [
        element.find_element(By.CSS_SELECTOR, "a.vt").get_attribute("href")
        for element in tqdm(driver.find_elements(
            By.CSS_SELECTOR,
            "li.l-vacancy"
        ), desc="Parsing dou for vacancy urls")
    ]


async def parse_vacancy_page_dou(session: aiohttp.ClientSession, url: str) -> list[str] | None:
    async with session.get(url) as response:
        if response.status != 200:
            return
        soup = BeautifulSoup(await response.text(), "html.parser")
        return soup.find("div", class_="b-typo vacancy-section").text


async def parse_vacancy_dou(urls: list[str]):
    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(
            *[
                parse_vacancy_page_dou(session, url)
                for url
                in tqdm(urls, desc="Parsing dou vacancies details")
            ]
        )


def count_all_words(list_of_text: list[str]) -> Counter:
    counter = Counter(
        word
        for text in tqdm(list_of_text, desc="Counting words") if text
        for word in count_tech_words(text)
    )
    return Counter({key: count for key, count in counter.items() if count >= 5})


async def parse_and_save_dou():
    with CustomChrome() as driver:
        driver.get("https://jobs.dou.ua/vacancies/?category=Python")
        execute_pagination_script_dou(driver)
        urls = parse_all_vacancy_urls_dou(driver)
    vacancy_html = await parse_vacancy_dou(urls)
    words = count_all_words(vacancy_html)
    save_to_db_hard_skills_and_count(words)
