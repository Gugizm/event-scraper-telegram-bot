from datetime import datetime, time, timedelta
import pytz
from tzlocal import get_localzone 
from scraper.abstract_classes import Computing


class TimeManager(Computing):
    @staticmethod
    def tz_changer(date):
        event_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        event_date = pytz.utc.localize(event_date).astimezone(get_localzone())
        return event_date
    

    @staticmethod
    def date_compare(date):
        now = datetime.now(get_localzone())
        event_date = TimeManager.tz_changer(date)
        if now < event_date:
            return event_date
        print('Time is more then')
        return False
    
    @staticmethod
    def reminder(date):
        return date - timedelta(minutes=30)
        

