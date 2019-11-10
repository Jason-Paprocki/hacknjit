import requests
impot googlemaps
import json
from collections import Counter

counter = 0
thekey = 'AIzaSyB3O7rrXNzMCbD1dK3Kmme_yCx3PruCVwk'
gmap = googlemaps.Client(key=thekey)
def findNearByGas(map_point_list):
    base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    addresses = {}
    for i in range(0, len(map_point_list)-1, 1):
        map_point = map_point_list[i]
        midpoint = map_point.eucl_midpoint_between(map_point[i+1])
        modurl = base_url + 'key=' + thekey + '&location=' + midpoint.get_lat_lang_str() + '&radius=' + mitom(midpoint.radius*1.1) + '&keyword=' + 'gas station' 
        response = requests.get(modurl)
        pre_parse_json = json.load(response)
        numResponses = Counter(location['geometry'] for location in response)
        for j in numResponses:
            parsed_json = pre_parse_jason['results'][j]['geometry']['location']
            lat = parsed_json['lat']
            lng = parsed_json['lng']
            address = gmap.reverse_geocode(lat, lang)
            adresses.add(address)
    return addresses

def mitom(mi):
    return format(1609.34 * mi, '.1f')

'''
def jsonify(large_text):
    with open('near_gas' + str(counter) + '.json', 'w') as ofile:
        ofile.seek(0)
        ofile.truncate(0) # clear file contents if previous
        json.dump(large_text, ofile, indent=4)
'''
