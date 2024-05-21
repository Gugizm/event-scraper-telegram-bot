import logging
import asyncio
import telegram

logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self, token, chat_id):
        self._bot = telegram.Bot(token=token)
        self._chat_id = chat_id
        
    
    async def send_message(self, message):
        try:
            await self._bot.send_message(chat_id=self._chat_id, text=message, parse_mode="Markdown")
        except TimeoutError:
            await asyncio.sleep(5)
        except Exception as e:
            logger.error(f'While trying to send message, occurred error {e}!')
            raise Exception(f'While trying to send message, occurred error {e}!')
    

    async def error_message(self):
        error = '**Warning!**\nDetected ERROR!!!\nContact with support\n'
        await self.send_message(error)
        