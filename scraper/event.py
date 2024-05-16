from abstract_classes import AbstractEvent, AbstractTimeManager


class Event(AbstractEvent):
    def __init__(self, date_manager, id, date, flag, title,
                 actual, forcast, previous):
        self._id = id
        self._dates = date_manager(date)
        self._flag = flag
        self._title = title
        self._actual = actual
        self._forcast = forcast
        self._previous = previous

    @property
    def id(self):
        return self._id

    @property
    def dates(self):
        return self._dates
    
              
    @property
    def flag(self):
        return self._flag
    
    @property
    def title(self):
        return self._title

    @property
    def actual(self):
        return self._actual
    
    @actual.setter
    def actual(self, new_actual):
        self._actual = new_actual

    @property
    def forcast(self):
        return self._forcast
    
    @forcast.setter
    def forcast(self, new_forcast):
        self._forcast = new_forcast
    
    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, new_previous):
        self._previous = new_previous

    def __eq__(self, other):
        if isinstance(other, Event):
            return self._id == other._id
        return False
    

    def markdown(self):
        title = f'Event: {self._title}'
        date = f'Date: {self._dates.event_date}'
        flag = f'Flag: {self._flag}'
        actual = f'Actual: {self._actual}'
        forcast = f'Forcast: {self._forcast}'
        previous = f'Previous: {self._previous}'
        vars = [title, date, flag, actual, forcast, previous]
        markdown_text = ''
        for var in vars:
            if var and var != previous:
                markdown += f'{var}\n'
            elif var == previous:    
                markdown += f'{var}'
        return markdown_text

