from .information import Information

class Website(object):
    
    def __init__(self):
        self.container = None
        self.origin = None
        self.destination = None

    def reverse_trip(self):
        self.origin, self.destination = self.destination, self.origin
        
