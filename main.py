import asyncio
from selenium import webdriver
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_GROUP_CHAT_ID, WEB_PAGE_URL
from scraper import Scraper, EventManager, Event, EventFactory
from scraper import DateManager
from bot import TelegramBot
from scraper import EventManager


async def scheduler(event_manager):
    while True:
        await event_manager.allocator()

        await asyncio.sleep(10)


async def main():
    event_factory = EventFactory(Event, DateManager)
    fetcher = Scraper(webdriver.Chrome(), WEB_PAGE_URL, event_factory)
    bot = TelegramBot(token=TELEGRAM_BOT_TOKEN, chat_id=TELEGRAM_GROUP_CHAT_ID)
    event_manager = EventManager(fetcher, bot)

    await asyncio.gather(scheduler(event_manager))

   
if __name__ == "__main__":
    asyncio.run(main())