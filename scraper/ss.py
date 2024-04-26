import requests
from datetime import datetime
from bs4 import BeautifulSoup

#class:theDay - day
#class:event - event
#class:flagCur - flag
#class:time - time
#class:act - actual
#class:fore - forcast
#class:prev - previus


#with data if date is current date then scrap what is 
#first need to check that date is today
#if date == today lets take first hours when starts and what starts and befor 30 minuts call again this code
#if there is no date lets call every half hours

class TableParser:
    def __init__(self, html_content):
        self.html_content = html_content


    def parse_event(self):
        try:
            soup = BeautifulSoup(self.html_content, 'lxml')
            print(self.html_content)
            # Select the economic calendar
            table = soup.select('table.genTable')[0]
            # Day of event
            scrape_date = table.select('tr')
            for i in scrape_date:
                print(">>>>>>>>>", i, "<<<<<<<<<\n")
                
            date_str = scrape_date[0].get_text()
            # print(date_str, 'thisss')
            # print(date_str.it)
            event_date = datetime.strptime(date_str, "%A, %B %d, %Y").date()
            
            # if event_date == datetime.now().date():
            if True:
                parent_tr = scrape_date.find_parent('tr')
                parsed_event = parent_tr.find_next('tr')
                print(parsed_event)
                event = {
                    'time': parsed_event.select_one('td.time').get_text(),
                    'country': parsed_event.select_one('td.flagCur').get_text(),
                    'event_name': parsed_event.select_one('td.event').get_text().strip(),
                    'actual': parsed_event.select_one('td.act').get_text().strip(),
                    'forcast': parsed_event.select_one('td.fore'),
                    'previous': parsed_event.select_one('td.prev').get_text().strip()
                }

                return event
        
        except Exception as e:
            print(f"An error occurred while parsing HTML content here: {e}")



