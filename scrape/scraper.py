import logging
from selenium.webdriver.common.by import By
from manage import AbstractEvent
from scrape import AbstractScraper


logger = logging.getLogger(__name__)

class EventScraper(AbstractScraper):
    def __init__(self, driver, url, event_maker: AbstractEvent):
        self._driver = driver
        self._url = url
        self._event = event_maker


    def load_url(self):
        self._driver.get(self._url)


    def scrape_events(self):
        self.load_url()
        rows = self._driver.find_elements(By.TAG_NAME, "tr")
        events = []
        for row in rows:
            try:
                event_date = row.get_attribute("event_timestamp")
                if not event_date:
                    continue
                event = self._event.create_event(
                id = row.get_attribute("id"),
                date = event_date,
                flag = row.find_element(By.CLASS_NAME, "flagCur").text,
                title = row.find_element(By.CLASS_NAME, "event").text,
                actual = row.find_element(By.CLASS_NAME, "act").text,
                forcast = row.find_element(By.CLASS_NAME, "fore").text,
                previous = row.find_element(By.CLASS_NAME, "prev").text
                )
                events.append(event)
            except ValueError:
                continue
            
            except Exception as e:
                logger.error(f'while trying to scrape by tr occurred error - {e}!')
        return events
 

    def update_event(self, event: AbstractEvent):
        self.load_url()
        try:
            scraped_event = self._driver.find_element(By.ID, event.id)
            event.actual = scraped_event.find_element(By.CLASS_NAME, "act").text
            event.forcast = scraped_event.find_element(By.CLASS_NAME, "fore").text
            event.previous = scraped_event.find_element(By.CLASS_NAME, "prev").text
        except Exception as e:
            logger.error(f'while trying to scrape by ID occurred error - {e}!')
        