import googlemaps
import json

gmap = googlemaps.Client(key='AIzaSyB3O7rrXNzMCbD1dK3Kmme_yCx3PruCVwk')

def getRequest(gmap, origin, destination):
    result = gmap.directions(origin, destination)
    return result
def jsonify(request_info):
    with open('json_dump.json', 'w') as ofile:
        json.dump(request_info, ofile)
jsonify(getRequest(gmap, '42 wilsey street, newark, nj', 'test_address'))
#test print(getRequest(gmap, '42 wilsey street, newark, nj', 'test_address'))

