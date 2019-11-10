import googlemaps
import math
import json

gmap = googlemaps.Client(key='AIzaSyB3O7rrXNzMCbD1dK3Kmme_yCx3PruCVwk')

'''

'''
def findNearByGas(gmap, currentLat, currentLong, distance,
                  secondLat=None, secondLong = None):
    near = None
    if distance < 2.5):
        near = gmap.places('gas_station', radius=mitom(distance))
    else:
        near =#implement
    return near
    

def mitom(mi):
    return 1609.34 * mi

'''
Pseudocode courtesy of 
'''
def midpoint(start_lat, start_lon, end_lat, end_lon):
    mlong = math.radians(end_lon - start_lon)
    rX = math.cos(end_lat) * math.cos(mlong)
    rY = math.cos(endlat) * math.cos(mlong)
    newLat = math.atan2(math.sin(start_lat)+math.sin(end_lat),
                        ((math.cos(start_lat)+rX)**2 + rY**2)**.5
    newLon = start_lon + math.atan2(rY, math.cos(start_lat) + rx)
    return tuple(newLat, newLon)
