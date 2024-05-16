from abc import ABC, abstractmethod

class AbstractEvent(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def __eq__(self):
        pass



class AbstractDateManager(ABC):
    @abstractmethod
    def __init__(self):
        pass


    @abstractmethod
    def date_compare(self):
        pass


    @abstractmethod
    def calculate_reminder(self):
        pass
    


class DateCompeare(ABC):
    def __init__(self, date):
        self.date = date


    def date_comp(self):
        pass


class EventScheduler(ABC):
    @abstractmethod
    def scheduler(self):
        pass
