from datetime import datetime
from .megabus import MegabusWebsite 
from .scraper import Scraper

class AnnoyingBus(object):
    def __init__(self):
        self.megabus = MegabusWebsite()
        self.websites = [self.megabus]
        self.days = 1
        self.date = datetime.today()

    def search(self):
        scraper = Scraper() 
        for website in self.websites:
            scraper.website = website
            scraper.build(self.days, self.date)
        return scraper.get_info()

    def reverse_trip(self):
        for website in self.websites:
            website.reverse_trip()
