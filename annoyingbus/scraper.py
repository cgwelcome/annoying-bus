from bs4 import BeautifulSoup
from datetime import date
from .information import Information

class Scraper(object):

    def __init__(self):
        self.website = None
        self.container = Information()
    
    def build(self, days, date):
        self.website.container = self.container
        self.website.create_request()
        for day in range(days):
            print("Extracting day {}".format(day+1))
            self.website.create_date_request(day, date)
            html_content = self.website.load().content
            soup = BeautifulSoup(html_content, "html.parser")
            self.website.get_location()
            self.website.get_prices(soup)
            self.website.get_departure(soup)
            self.website.get_duration(soup)

    def get_info(self):
        return self.container
