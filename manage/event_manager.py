import asyncio
import logging
from datetime import datetime
from tzlocal import get_localzone 
from manage import AbstractEvent, AbstractEventManager


logger = logging.getLogger(__name__)


class EventManager(AbstractEventManager):
        def __init__(self, fetcher, bot):
            self._fetcher = fetcher
            self._bot = bot
            self._events = []
            self._counter = 0


        async def allocate_events(self):
            for event in self._fetcher.scrape_events():

                tryies = 3
                while tryies > 0:
                    try:
                        if event not in self._events:
                            self._events.append(event)
                            await self.send_markdown(event, 'Scheduled Event')
                            self._counter += 1
                            asyncio.create_task(self.schedule_event(event))
                            break
                        break

                    except Exception as e:
                        logger.error(f'Ocuared Error - {e}')
                        tryies -= 1
                        if tryies == 0:
                            logger.error(f'Max rtetries reached')
                            await self._bot.error_message()
                            break
                    
                    
        async def schedule_event(self, event: AbstractEvent):
            reminder = False

            while True:
                now = datetime.now(get_localzone())
                if now >= event.dates.reminder and not reminder:
                    await self.send_markdown(event, 'Reminder')
                    reminder = True

                if now >= event.dates.event_date:
                    self._fetcher.update_event(event)
                    await self.send_markdown(event, 'Event Occurs as Scheduled')
                    self._events.remove(event)
                    break
                await asyncio.sleep(30)


        async def send_markdown(self, event, title):
            markdown = f'**{title}**\n' + event.markdown()
            await self._bot.send_message(markdown)
