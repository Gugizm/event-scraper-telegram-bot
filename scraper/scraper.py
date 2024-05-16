import logging
from selenium.webdriver.common.by import By
from abstract_classes import AbstractEvent
from event import Event


class Scraper:
    def __init__(self, driver, url, event_maker: AbstractEvent):
        self._driver = driver
        self._url = url
        self._event = event_maker


    def restart(self):
        self._driver.get(self._url)


    def parse(self):
        self.restart()
        rows = self._driver.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            try:
                event_date = row.get_attribute("event_timestamp")
                if not event_date:
                    continue

                yield self._event.create_event(
                id = row.get_attribute("id"),
                date = event_date,
                flag = row.find_element(By.CLASS_NAME, "flagCur").text,
                title = row.find_element(By.CLASS_NAME, "event").text,
                actual = row.find_element(By.CLASS_NAME, "act").text,
                forcast = row.find_element(By.CLASS_NAME, "fore").text,
                previous = row.find_element(By.CLASS_NAME, "prev").text
                )

            except ValueError:
                continue
            except Exception as e:
                logging.error(f'while trying to scrape by tr occurred error - {e}!')
 

    def scrap_id(self, event: Event):
        self.restart()
        try:
            scraped_event = self._driver.find_element(By.ID, event.id)
            event.actual = scraped_event.find_element(By.CLASS_NAME, "act").text
            event.forcast = scraped_event.find_element(By.CLASS_NAME, "fore").text
            event.previous = scraped_event.find_element(By.CLASS_NAME, "prev").text
        except Exception as e:
            logging.error(f'while trying to scrape by ID occurred error - {e}!')
        