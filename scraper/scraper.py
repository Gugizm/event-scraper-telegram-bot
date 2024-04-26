from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, time


class Scraper:
    def __init__(self, driver, url) -> None:
        self._driver = webdriver.Chrome()
        self._driver.get(url)
        print(self._driver)


    def parse(self):
        rows = self._driver.find_elements(By.TAG_NAME, 'tr')

        events = []
        for row in rows:
            event = {}
            print(row.text)
            try:
                event['time'] = row.find_element(By.CLASS_NAME, "time").text
                if event['time'] == 'Time':
                    continue
                event['id'] = row.get_attribute("id")
                event['flag'] = row.find_element(By.CLASS_NAME, "flagCur").text
                event['event'] = row.find_element(By.CLASS_NAME, "event").text
                event['actual'] = row.find_element(By.CLASS_NAME, "act").text
                event['forcast'] = row.find_element(By.CLASS_NAME, "fore").text
                event['previous'] = row.find_element(By.CLASS_NAME, "prev").text
                
                events.append(event)
            except Exception:
                continue
        print(events)
        return events


    @staticmethod
    def time_parser(time_str):
        parsed_time = datetime.strftime(time_str, "%H:%M").time()
        return parsed_time        
