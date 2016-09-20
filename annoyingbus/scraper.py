from bs4 import BeautifulSoup
from datetime import timedelta 
from .information import Information

class Scraper(object):

    def __init__(self):
        self.website = None
        self.container = Information()
    
    def build(self, offset_days, base_date):
        self.website.container = self.container
        company = self.website.get_company()
        for day in range(offset_days):
            print("{1} - Extracting day {0}".format(day+1, company))
            date = base_date + timedelta(days=day)
            self.website.update_date(date)
            html_content = self.website.load().content
            soup = BeautifulSoup(html_content, "html.parser")
            self.website.set_locations()
            for row in self.website.get_rows(soup):
                self.website.set_price(row)
                self.website.set_departure(row)
                self.website.set_arrival(row)
                self.website.set_duration(row)
                self.container.update_row()

    def get_info(self):
        return self.container
