import math
from decimal import Decimal

class Cargo(object):

    def __init__(self, row):
        self.product = row[0]
        self.origin_city = row[1]
        self.origin_state = row[2]
        self.origin_lat = Decimal(row[3])
        self.origin_lng = Decimal(row[4])
        self.destination_city = row[5]
        self.destination_state = row[6]
        self.destination_lat = Decimal(row[7])
        self.destination_lng = Decimal(row[8])

    def origin_dist(self, lat, lng):
        return self.__dist(lat, self.origin_lat, lng, self.origin_lng)

    def origin_destination_dist(self):
        return self.__dist(self.origin_lat, self.destination_lat, self.origin_lng, self.destination_lng)

    def __dist(self, x1, x2, y1, y2):
        return math.hypot(x2 - x1, y2 - y1)


class Truck(object):

    def __init__(self, row):
        self.truck = row[0]
        self.city = row[1]
        self.state = row[2]
        self.lat = Decimal(row[3])
        self.lng = Decimal(row[4])

