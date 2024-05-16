import requests
import asyncio
import telegram

FINNHUB_API_KEY = "cobf5a1r01qomlfdst0gcobf5a1r01qomlfdst10"
TELEGRAM_BOT_TOKEN = "6976493225:AAF4TlVvfyEGMymsNZ8jgW2SxYM_mnRZx94"
TELEGRAM_GROUP_CHAT_ID = "-4158572808"


def get_stock_data(symbols):
    base_url = "https://finnhub.io/api/v1/"
    data = []

    for symbol in symbols:
        url = f"{base_url}quote?symbol={symbol}&token={FINNHUB_API_KEY}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            stock_data = response.json()
            processed_data = {
                "symbol": stock_data["c"],
                "price": stock_data["d"],
                "change": stock_data["dp"]
            }
            data.append(processed_data)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {symbol}: {e}")

    return data

async def send_to_telegram(data, bot):
    try:
        for stock in data:
            message = f"**Stock Update:**\nSymbol: {stock['symbol']}\nPrice: ${stock['price']:.2f}\nChange: {stock['change']:.2f}"
            await bot.send_message(chat_id=TELEGRAM_GROUP_CHAT_ID, text=message, parse_mode="Markdown")
        return True
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")
        return False

async def main():
    symbols = ["AAPL", "GOOGL", "MSFT"]  # Add more symbols as needed
    data = get_stock_data(symbols)
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    await send_to_telegram(data, bot)

if __name__ == "__main__":
    asyncio.run(main())