import requests


class Fetcher:
    def __init__(self, url) -> None:
        self.url = url


    def fetch_html(self):
        response = requests.get(self.url, params=dict(
            timezone_offset='+4:00' ### check
        ))

        try:
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"An error occurred while retrieving HTML content from {self.url}: {e}")