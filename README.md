# EventScraperTelegramBot

## Overview
EventScraperTelegramBot is a Python project designed to scrape event data from a specified webpage and send notifications about these events via Telegram. It provides a seamless way to track upcoming events and receive timely reminders.

## Features
- **Event Scraping**: Automatically fetch event data from a specified webpage.
- **Event Management**: Manage events, including creation, updating, and scheduling reminders.
- **Telegram Integration**: Send event notifications and reminders via Telegram.

## Installation
To install EventScraperTelegramBot, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Gugizm/event-scraper-telegram-bot.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure the Telegram bot token and chat ID in `config.py`.

## Usage
To run EventScraperTelegramBot, execute the `main.py` script:

```bash
python main.py