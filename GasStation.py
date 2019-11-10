from MapPoint import MapPoint
import googlemaps
import json
from pprint import pprint
import requests
key = "AIzaSyB3O7rrXNzMCbD1dK3Kmme_yCx3PruCVwk"

class GasStation:

    def __init__(self, address, price):
        self.address = address
        self.price = price
        self.geocode_address(address)
        self.point = MapPoint(self.lat, self.lng)

    def geocode_address(self, address):
        gmap = googlemaps.Client(key='AIzaSyB3O7rrXNzMCbD1dK3Kmme_yCx3PruCVwk')
        gc = googlemaps.geocoding.geocode(gmap, address=address)

        self.lat = gc[0]['geometry']['location']['lat']
        self.lng = gc[0]['geometry']['location']['lng']
