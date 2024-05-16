import logging
import asyncio
import telegram
from scraper import AbstractEvent


class TelegramBot:
    def __init__(self, token, chat_id):
        self._bot = telegram.Bot(token=token)
        self._chat_id = chat_id
        
    
    async def send_message(self, message):
        tryies = 3
        while tryies != 0:
            try:
                await self._bot.send_message(chat_id=self._chat_id, text=message, parse_mode="Markdown")
                return True
            except Exception as e:
                logging.error(f'While trying to send message to telegram bot occurred error {e}!')
                tryies -= 1
        await self.error_message()
    
    async def error_message(self):
        error = '**Warning!**\nDetected ERROR!!!\nContact with support\n'
        await self._bot.send_message(chat_id=self._chat_id, text=error, parse_mode="Markdown")
