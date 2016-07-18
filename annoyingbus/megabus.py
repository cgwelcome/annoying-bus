from bs4 import BeautifulSoup
from datetime import date, datetime, time, timedelta
from .website import Website
import requests
import re

class MegabusWebsite(Website):

    def __init__(self):
        self.url= "http://ca.megabus.com/JourneyResults.aspx" 
        self.cookies =  {"language": "en"}
        self.origin = "Toronto"
        self.destination = "Montreal"
        self.regioncode = {
            "Toronto": 145,
            "Montreal": 280
        }

    def create_request(self):
        self.request_values = {
            "originCode": self.regioncode[self.origin],
            "destinationCode": self.regioncode[self.destination],
            "passengerCount": 1 
        }

    def create_date_request(self, no_day, date):
        self.travel_date = date + timedelta(days=no_day)
        formatted_date = self.travel_date.strftime("%d/%m/%y")
        self.request_values["outbounddeparturedate"] = formatted_date

    def load(self):
        d = {"params":self.request_values, "cookies": self.cookies}
        return requests.get(self.url, **d)

    def get_prices(self, soup):
        tags = soup.find_all("ul", id=re.compile("JourneyResylt"))
        for tag in tags:
            price = tag.contents[11].get_text(strip=True).split("$")[1]
            self.container.prices.append(price)
    
    def get_departure(self, soup):
        tags = soup.find_all("ul", id=re.compile("JourneyResylt"))
        for tag in tags:
            cell = tag.contents[3].get_text(strip=True)
            departure_time_str = re.findall("[0-9]{2}:[0-9]{2}", cell)[0]
            departure_time = time(*map(int, departure_time_str.split(":")))
            departure_full = datetime.combine(self.travel_date, departure_time)
            self.container.departure.append(departure_full)
    
    def get_duration(self, soup):
        tags = soup.find_all("ul", id=re.compile("JourneyResylt"))
        for tag in tags:
            cell = tag.contents[5].get_text(strip=True)
            hour, minute = map(int, cell.strip("mins").split("hrs "))
            duration = timedelta(hours=hour, minutes=minute)
            self.container.duration.append(duration)
    
    def get_location(self):
        self.container.origin = self.origin
        self.container.destination = self.destination

    def reverse_trip(self):
        self.origin, self.destination = self.destination, self.origin
