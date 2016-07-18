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
        web.create_request()
        web.create_date_request(0, date.today())
        self.assertEqual(web.load().history, [])
    
    def test_prices(self):
        dirpath = os.path.dirname(tests.__file__)
        path = os.path.join(dirpath, "data", "JourneyResults.aspx.html")
        with open(path, 'r') as f:
            content = f.read()

        soup = BeautifulSoup(content, "html.parser") 
        web = MegabusWebsite()
        web.container = Information()
        web.get_prices(soup)
        l = ["59.00", "38.00", "38.00", "38.00", "38.00", "38.00",
             "38.00", "33.00", "38.00", "38.00", "43.00", "38.00",
             "33.00", "33.00"]
        self.assertEqual(web.container.prices, l)

    def test_departure(self):
        dirpath = os.path.dirname(tests.__file__)
        path = os.path.join(dirpath, "data", "JourneyResults.aspx.html")
        with open(path, 'r') as f:
            content = f.read()

        soup = BeautifulSoup(content, "html.parser") 
        web = MegabusWebsite()
        web.container = Information()
        web.travel_date = date(2016, 7, 22)
        web.get_departure(soup)
        times = [
            time(0, 30), time(6, 30), time(7, 30),
            time(8, 30), time(9, 30), time(10, 30),
            time(12, 0), time(13, 30), time(14, 30),
            time(16, 0), time(17, 0), time(18, 0),
            time(19, 0), time(21, 0)]
        dates = [datetime.combine(web.travel_date, t) for t in times]
        self.assertEqual(web.container.departure, dates)


    def test_duration(self):
        dirpath = os.path.dirname(tests.__file__)
        path = os.path.join(dirpath, "data", "JourneyResults.aspx.html")
        with open(path, 'r') as f:
            content = f.read()
        soup = BeautifulSoup(content, "html.parser") 
        web = MegabusWebsite()
        web.container = Information()
        web.get_duration(soup)
        durations = [
            timedelta(hours=6, minutes=10), timedelta(hours=5, minutes=45),
            timedelta(hours=6, minutes=20), timedelta(hours=6, minutes=30),
            timedelta(hours=5, minutes=45), timedelta(hours=6, minutes=20),
            timedelta(hours=5, minutes=45), timedelta(hours=5, minutes=45),
            timedelta(hours=6, minutes=30), timedelta(hours=5, minutes=45),
            timedelta(hours=5, minutes=45), timedelta(hours=5, minutes=45),
            timedelta(hours=5, minutes=45), timedelta(hours=6, minutes=10)]
        self.assertEqual(web.container.duration, durations) 

