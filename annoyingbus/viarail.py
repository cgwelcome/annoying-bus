from bs4 import BeautifulSoup
from datetime import date
from .website import Website
import requests

class ViaRailWebsite(Website):
    
    def __init__(self):
        self.url = "https://reservia.viarail.ca/search/setSearch.aspx"
        self.origin = "Toronto"
        self.destination = "Montreal"
        self.regioncode = {
            "Toronto": "TRTO",
            "Montreal": "MTRL"
        }
        self.form_data = {
            "cmbStationsFrom_value": self.regioncode[self.origin],
            "cmbStationsTo_value": self.regioncode[self.destination],
            "cmbNbAdults": 1
        }
        self.session = requests.Session()
   
    def update_date(self, date):
        formatted_date = date.strftime("%m/%d/%Y")
        self.form_data["txtDateFrom"] = formatted_date
        self.container.row_info["Date"] = date.strftime("%Y-%m-%d")
    
    def load(self):
        return self.session.post(self.url, data=self.form_data)
    
    def get_company(self):
        company = "ViaRail"
        self.container.row_info["Company"] = company
        return company

    @staticmethod
    def get_rows(soup):
        return soup.find_all("div", class_="train-route-container")

    def set_price(self, row):
        filters= [
            "column column-special-fare",
            "column column-economy-fare column-economy-discounted-fare",
            "column column-economy-fare column-economy-regular-fare",
            "column column-business-fare column-business-discounted-fare",
            "column column-business-fare column-business-regular-fare"
            ]
        for filter_ in filters:
            tag = row.find(class_=filter_).get_text(strip=True)
            if tag != unicode("Sold out", "utf-8"):
                price = tag.split("$")[1]
                self.container.row_info["Price"] = price 
                return 
        self.container.row_info["Price"] = "Sold Out" 

    def set_departure(self, row):
        departure = row.find(class_="schedule-info").get_text()
        self.container.row_info["Departure"] = departure 

    def set_arrival(self, row):
        arrival = row.find_all(class_="schedule-info", limit=2)[1].get_text() 
        self.container.row_info["Arrival"] = arrival

    def set_duration(self, row):
        tag = row.find(class_="schedule-info-duration left column")
        components = tag.get_text(strip=True).strip("m").split("hrs")
        duration = ':'.join([x.zfill(2) for x in components])
        self.container.row_info["Duration"] = duration
    
    def set_locations(self):
        self.container.row_info["Origin"] = self.origin
        self.container.row_info["Destination"] = self.destination
