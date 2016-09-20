from bs4 import BeautifulSoup
from datetime import datetime, time, timedelta
from .website import Website
import requests
import re

class MegabusWebsite(Website):

    def __init__(self):
        self.url = "http://ca.megabus.com/JourneyResults.aspx" 
        self.cookies =  {"language": "en"}
        self.origin = "Toronto"
        self.destination = "Montreal"
        self.regioncode = {
            "Toronto": 145,
            "Montreal": 280
        }
        self.params = {
            "originCode": self.regioncode[self.origin],
            "destinationCode": self.regioncode[self.destination],
            "passengerCount": 1 
        }
        self.session = requests.Session()
        self.session.cookies.update(self.cookies)

    def update_date(self, date):
        formatted_date = date.strftime("%d/%m/%y")
        self.params["outbounddeparturedate"] = formatted_date
        self.container.row_info["Date"] = date.strftime("%Y-%m-%d")

    def load(self):
        return self.session.get(self.url, params=self.params)
    
    def get_company(self):
        company = "Megabus"
        self.container.row_info["Company"] = company 
        return company

    @staticmethod
    def get_rows(soup):
        return soup.find_all("ul", id=re.compile("JourneyResylt"))

    def set_price(self, row):
        price = row.contents[11].get_text(strip=True).split("$")[1]
        self.container.row_info["Price"] = price

    def set_departure(self, row):
        cell = row.contents[3].get_text(strip=True)
        departure = re.findall("[0-9]{2}:[0-9]{2}", cell)[0].zfill(5)
        self.container.row_info["Departure"] = departure
    
    def set_arrival(self, row):
        cell = row.contents[3].get_text(strip=True)
        arrival = re.findall("[0-9]{2}:[0-9]{2}", cell)[1].zfill(5)
        self.container.row_info["Arrival"] = arrival

    def set_duration(self, row):
        duration_unfmt = row.contents[5].get_text(strip=True).strip("mins")
        duration_fmt = [x.zfill(2) for x in duration_unfmt.split("hrs ")]
        duration = ':'.join(duration_fmt)
        self.container.row_info["Duration"] = duration
    
    def set_locations(self):
        self.container.row_info["Origin"] = self.origin
        self.container.row_info["Destination"] = self.destination
