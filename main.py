from config import *
from selenium import webdriver
from scraper.scraper import Scraper


if __name__ == "__main__":
    fetcher = Scraper(webdriver.Chrome(), WEB_PAGE_URL)
    fetched_data = fetcher.parse()

    # parser = TableParser(fetched_data)
    # event = parser.parse_event()
    # print(event)