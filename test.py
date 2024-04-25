import requests
from datetime import datetime
from bs4 import BeautifulSoup


response = requests.get('https://sslecal2.investing.com/?columns=exc_currency,exc_actual,exc_forecast,exc_previous&importance=3&countries=5&calType=day&timeZone=73&lang=1')

try:
    response.raise_for_status()
    html = response.text

except Exception as e:
    print(f"An error occurred while retrieving HTML content from {e}")



soup = BeautifulSoup(html, 'lxml')

table = soup.select('table#economicCalendarData')[0]
# print(table)
date_string = table.select_one('tr td.theDay')
event_day = date_string.get_text()
# here should be if date == now
parsed_date = datetime.strptime(event_day, "%A, %B %d, %Y").date()

# if datetime.now().date() == parsed_date:
parent_tr = date_string.find_parent('tr')
parsed_event = parent_tr.find_next_sibling('tr')
event = {
    'time': parsed_event.select_one('td.time').get_text(),
    'country': parsed_event.select_one('td.flagCur span')['title'],
    'imp': parsed_event.select_one('td.sentiment')['title'],
    'event_href': 'https://www.investing.com' + parsed_event.select_one('td.event a').get('href'), 
    'event_name': parsed_event.select_one('td.event a').get_text().strip(), 
    'actual': parsed_event.select_one('td.act').get_text().strip(),
    'forcast': parsed_event.select_one('td.fore').get_text().strip(),
    'previous': parsed_event.select_one('td.prev').get_text().strip()
}

print(event)   

# print(next_tr)

# text = date_string.get_text()
# print(text)
#     print('lollaaa')
# else:
#     print(datetime.now().date())