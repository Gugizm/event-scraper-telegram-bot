from abc import ABC, abstractmethod

class AbstractEvent(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def __eq__(self):
        pass

    @abstractmethod
    def markdown(self):
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
    

class AbstractEventManager(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def allocate_events(self):
        pass

    @abstractmethod
    def schedule_event(self):
        pass

    @abstractmethod
    def send_markdown(self):
        pass


class AbstractEventFactrory(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_event(Self):
        pass


