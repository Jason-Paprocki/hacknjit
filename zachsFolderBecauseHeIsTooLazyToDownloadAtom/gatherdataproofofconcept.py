#from flask import jsonify
import googlemaps
import json
from datetime import datetime

gmap = googlemaps.Client(key='AIzaSyB3O7rrXNzMCbD1dK3Kmme_yCx3PruCVwk')

def getRequest(gmap, origin, destination):
    result = gmap.directions(origin, destination)
    return result
def jsonify(request_info):
    with open('json_dump.json', 'w') as ofile:
        json.dump(request_info, ofile)
jsonify(getRequest(gmap, '42 wilsey street, newark, nj', '25 hamilton ave, berkeley heights, nj'))
#test print(getRequest(gmap, '42 wilsey street, newark, nj', '25 hamilton ave, berkeley heights, nj'))

