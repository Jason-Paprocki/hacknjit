import json
import requests

key = "AIzaSyB3O7rrXNzMCbD1dK3Kmme_yCx3PruCVwk"

#parsejson(filename of whatever json data google sends us to route from A to B)
#gather list of (lat, lng) coordinate pairs of turns along that route
#At every midpoint of two coordinate pairs, we find best gas prices using gasbuddy webscraper
#store that data in a list
#Compare the best prices along the route, and display the top choices


if __name__ == '__main__':
    route_AtoB_json = get_route(gmap, origin, destination)
    pointA = data_from_route[0][0]
    pointB = data_from_route[0][1]
    turns_list = parse_json_for_turns(route_AtoB_json)[1]

    midpoint_list = []
    for i in range(len(turns_list)):
        if i+1 < len(turns_list):
            midpoint = turns_list[i].eucl_midpoint_between(turns_list[i+1])
            midpoint_list.append(midpoint)

    for midpoint in midpoint_list:
        address = midpoint.to_address()

    


import googlemaps
import json

gmap = googlemaps.Client(key='AIzaSyB3O7rrXNzMCbD1dK3Kmme_yCx3PruCVwk')

def get_route(gmap, origin, destination):
    result = gmap.directions(origin, destination)
    return result

def jsonify(request_info):
    with open('json_dump.json', 'w') as ofile:
        json.dump(request_info, ofile)
jsonify(getRequest(gmap, '42 wilsey street, newark, nj', 'test_address'))
