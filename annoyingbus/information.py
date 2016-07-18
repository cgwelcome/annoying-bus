from tabulate import tabulate
from datetime import datetime, timedelta

class Information(object):

    def __init__(self):
        self.prices = []
        self.departure = []
        self.arrival = []
        self.duration = []
        self.origin = None
        self.destination = None

    def show_all(self):
        self.create_arrival()
        depart_fmt = self.date_fmt(self.departure)
        arrive_fmt = self.date_fmt(self.arrival)
        duration_fmt = self.duration_fmt(self.duration)
        print("{} >>> {}".format(self.origin, self.destination))
        print(tabulate(
            zip(depart_fmt, arrive_fmt, duration_fmt, self.prices),
            headers=['Departure', 'Arrival', 'Duration', 'Price'],
            floatfmt=".2f"))
    
    def create_arrival(self):
        for depart, duration in zip(self.departure, self.duration):
            self.arrival.append(depart + duration)
    
    def date_fmt(self, list_dates):
        return [a_date.strftime("%c") for a_date in list_dates] 
    
    def duration_fmt(self, duration):
        list_fmt = []
        for d in duration:
            hour = d.seconds//3600
            minute = d.seconds//60%60
            list_fmt.append("{0}:{1:0>2}".format(hour, minute))
        return list_fmt
