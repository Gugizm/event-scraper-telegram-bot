from manage import AbstractEvent, AbstractDateManager, AbstractEventFactrory


class EventFactory(AbstractEventFactrory):
    def __init__(self, event_class: AbstractEvent, date_manager: AbstractDateManager):
        self._event_class = event_class
        self._date_manager = date_manager

    
    def create_event(self, **kwargs):
        return self._event_class(date_manager=self._date_manager, **kwargs)
