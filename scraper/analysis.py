from datetime import datetime, time, timedelta
import pytz
from tzlocal import get_localzone 
from scraper.abstract_classes import AbstractDateManager


class DateManager(AbstractDateManager):
    def __init__(self, date):
        self._date = date
        self._event_date = self.date_compare()
        self._reminder = self.calculate_reminder()
    #can provide sleep method, to not to iterate to much while loo
    #or in event class define date = datemanager and thrn use its things

    @property
    def event_date(self):
        return self._event_date


    @property
    def reminder(self):
        return self._reminder


    def date_compare(self):
        now = datetime.now(get_localzone())
        event_date = self.tz_changer(self._date)
        if now < event_date:
            return event_date
        raise ValueError('Date has passed!')
    

    def calculate_reminder(self):
        return self._event_date - timedelta(minutes=30)
        

    @staticmethod
    def tz_changer(date):
        event_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        event_date = pytz.utc.localize(event_date).astimezone(get_localzone())
        return event_date
    

        

