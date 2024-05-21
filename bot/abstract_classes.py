from abc import ABC, abstractmethod

class AbstractBot(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def send_message(self):
        pass

    @abstractmethod
    def error_message(self):
        pass