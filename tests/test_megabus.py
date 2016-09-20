from bs4 import BeautifulSoup
from datetime import date, datetime, time, timedelta
from annoyingbus.megabus import MegabusWebsite 
from annoyingbus.information import Information
import tests
import os
import unittest


class TestMegabus(unittest.TestCase):

    def test_cookies(self):
        web = MegabusWebsite()
        web.container = Information()
        web.update_date(date.today())
        self.assertEqual(web.load().history, [])
    
    def test_prices(self):
        dirpath = os.path.dirname(tests.__file__)
        path = os.path.join(dirpath, "data", "Megabus.html")
        with open(path, 'r') as f:
            content = f.read()

        soup = BeautifulSoup(content, "html.parser") 
        web = MegabusWebsite()
        web.container = Information()
        prices = []
        for row in web.get_rows(soup):
            web.set_price(row)
            prices.append(web.container.row_info["Price"])
        l = ["59.00", "38.00", "38.00", "38.00", "38.00", "38.00",
             "38.00", "33.00", "38.00", "38.00", "43.00", "38.00",
             "33.00", "33.00"]
        prices = [str(x) for x in prices]
        self.assertEqual(prices, l)

    def test_departure(self):
        dirpath = os.path.dirname(tests.__file__)
        path = os.path.join(dirpath, "data", "Megabus.html")
        with open(path, 'r') as f:
            content = f.read()

        soup = BeautifulSoup(content, "html.parser") 
        web = MegabusWebsite()
        departures = []
        web.container = Information()
        for row in web.get_rows(soup):
            web.set_departure(row)
            departures.append(web.container.row_info["Departure"])
        l = ["00:30", "06:30", "07:30", "08:30", "09:30", "10:30",
            "12:00", "13:30", "14:30", "16:00", "17:00", 
            "18:00", "19:00", "21:00"]
        departures = [str(x) for x in departures]
        self.assertEqual(departures, l)


    def test_duration(self):
        dirpath = os.path.dirname(tests.__file__)
        path = os.path.join(dirpath, "data", "Megabus.html")
        with open(path, 'r') as f:
            content = f.read()
        soup = BeautifulSoup(content, "html.parser") 
        web = MegabusWebsite()
        web.container = Information()
        durations = []
        for row in web.get_rows(soup):
            web.set_duration(row)
            durations.append(web.container.row_info["Duration"])
        l = [
            "06:10", "05:45", "06:20", "06:30", "05:45", "06:20",
            "05:45", "05:45", "06:30", "05:45",
            "05:45", "05:45", "05:45", "06:10"]
        durations = [str(x) for x in durations]
        self.assertEqual(durations, l) 

