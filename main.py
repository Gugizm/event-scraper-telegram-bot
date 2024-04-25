import config
from scraper.scraper import TableParser
from scraper.fetcher import Fetcher


if __name__ == "__main__":
    fetcher = Fetcher(config.WEB_PAGE_URL)
    fetched_data = fetcher.fetch_html()
    
    parser = TableParser(fetched_data)
    event = parser.parse_event()
    print(event)