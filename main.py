import asyncio
from selenium import webdriver
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_GROUP_CHAT_ID, WEB_PAGE_URL
from manage import EventManager, Event, EventFactory, DateManager
from scrape import EventScraper
from bot import TelegramBot


async def run(event_manager):
    while True:
        await event_manager.allocate_events()

        await asyncio.sleep(30*60)


async def main():
    event_factory = EventFactory(Event, DateManager)
    scraper = EventScraper(webdriver.Chrome(), WEB_PAGE_URL, event_factory)
    bot = TelegramBot(token=TELEGRAM_BOT_TOKEN, chat_id=TELEGRAM_GROUP_CHAT_ID)
    event_manager = EventManager(scraper, bot)

    await asyncio.gather(run(event_manager))

   
if __name__ == "__main__":
    asyncio.run(main())