import logging
from config import *
from selenium import webdriver
from scraper import Scraper
from analysis import TimeManager
from event import Event
from datetime import datetime, timedelta
import time
import concurrent.futures
import threading
from bot.bot import TelegramBot
from tzlocal import get_localzone 
from abstract_classes import AbstractEvent, AbstractDateManager

#abstract clas is needed here
class EventFactory:
    def __init__(self, event_class: Event, date_manager: AbstractDateManager):
        self._event_class = event_class
        self._date_manager = date_manager

    
    def create_event(self, **kwargs):
        return Event(date_manager=self._date_manager, **kwargs)
        


class EventManager:
        def __init__(self, fetcher, bot, time_manager):
            self._fetcher = fetcher
            self._time_manager = time_manager
            self._bot = bot
            self._events = []


        async def allocator(self):
            for event in self._fetcher.parse():
                if event not in self._events:
                    self._bot.send_message(self.send_markdown(event, 'Scheduled Event'))
                    self._events.append(event)

                    await self.scheduler(event)

                    
        async def scheduler(self, event: Event):
            while True:
                now = datetime.now(get_localzone())
                if now <= event.dates.reminder:
                    await self.send_markdown(event, 'Reminder')

                if now <= event.dates.event_date:
                    self._fetcher.scrap_id(event)
                    await self.send_markdown(event, 'Event Occurs as Scheduled')
                    self._events.remove(event)
                    print(f'{event.title} finished!')
                    break
                print(f'{event.title} run run run! every 1 second!!!')
                time.sleep(10)


        def send_markdown(self, event, title):
            markdown = f'**{title}**\n' + event.markdown()
            self._bot.send_message(markdown)

# added new event message when in list adding new event
# # if at time can not scrap send_message error message in telegram
# parsed_message = f"**Reminder**\nEvent: {event.title}\nDate: {event.date}\nflag: {event.flag}\nactual: {event.actual}\nforcast: {event.forcast}\nprevious: {event.previous}"
#             print(f"**Reminder**\nEvent: {event.title}\nDate: {event.date}\nflag: {event.flag}\nactual: {event.actual}\nforcast: {event.forcast}\nprevious: {event.previous}")
            