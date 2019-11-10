import googlemaps
import math
import json

gmap = googlemaps.Client(key='AIzaSyB3O7rrXNzMCbD1dK3Kmme_yCx3PruCVwk')

'''
/html/body/div[1]/div/div[3]/div/div/div[1]/div[1]/form/div/div[1]/div[1]/input
'''
def findNearByGas(currentLat, currentLong, distance,
                  secondLat=None, secondLong = None):
    near = None
    near = gmap.places('gas station',
                    location=latlongify(currentLat, currentLong),
                    radius=mitom(distance))
    '''
        midpoint = midpoint(currentLat, currentLong, secondLat, secondLong)
        
        near = gmap.places('gas_satation', location=midpoint,
                           radius=distance*1.1)'''
    return near
    

def mitom(mi):
    return 1609.34 * mi

def latlongify(lat, long):
    latlong = {
        'lat' : lat,
        'lng' : long
        }
    return latlong

def jsonify(large_text):
    with open('gas_station_dump.json', 'w') as ofile:
        json.dump(large_text, ofile, indent=4)
'''
Mathematical midpoint of lattitude and logitude courtesy of
https://www.movable-type.co.uk/scripts/latlong.html
'''
def midpoint(start_lat, start_lon, end_lat, end_lon):
    #convert to rad
    mlong = math.radians(end_lon) - math.radians(start_lon)
    start_lat = math.radians(start_lat)
    start_lon = math.radians(start_lon)
    end_lat = math.radians(end_lat)
    end_lon = math.radians(end_lon)
    #logic
    rX = math.cos(end_lat) * math.cos(mlong)
    rY = math.cos(end_lat) * math.cos(mlong)
    newLat = math.atan2(math.sin(start_lat)+math.sin(end_lat),
                        math.sqrt((math.cos(start_lat)+rX)*(math.cos(start_lat)+rX) + rY**2))
    newLon = start_lon + math.atan2(rY, math.cos(start_lat) + rX)
    newLon = math.degrees(newLon)
    newLat = math.degrees(newLat)

    return latlongify(newLat, newLon)

a = findNearByGas(40.6738885, -74.4491348, 5)
jsonify(a)
print(a)
