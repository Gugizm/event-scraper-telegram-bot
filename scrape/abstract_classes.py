from abc import ABC, abstractmethod

class AbstractScraper(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def scrape_events(self):
        pass

    @abstractmethod
    def update_event(self):
        pass