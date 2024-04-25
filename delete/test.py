import requests
from bs4 import BeautifulSoup
import schedule
import time

# Function to scrape the website and check for upcoming events
def check_upcoming_events():
    url = 'https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&importance=3&features=datepicker,timezone&countries=5&calType=week&timeZone=8&lang=1'
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        # Check for upcoming events in the next 30 minutes
        # You'll need to customize this based on the structure of the website
        upcoming_events = []  # Placeholder for upcoming events
        # Send a notification if there are upcoming events
        if upcoming_events:
            send_notification("Upcoming events will be available in 30 minutes")

# Function to send a notification to Telegram users
def send_notification(message):
    # Your code to send a notification to Telegram users
    pass

# Schedule the function to run every 30 minutes
schedule.every(30).minutes.do(check_upcoming_events)

# Main loop to run the bot
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage