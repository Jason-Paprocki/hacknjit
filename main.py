import json
import requests
import googlemaps
from route_data_parser import parse_json_for_turns
import MapPoint
from webscrape_gas_prices import get_station_at_address
from pprint import pprint

key = "AIzaSyB3O7rrXNzMCbD1dK3Kmme_yCx3PruCVwk"
gmap = googlemaps.Client(key='AIzaSyB3O7rrXNzMCbD1dK3Kmme_yCx3PruCVwk')
origin = "20 John St, Little Ferry, NJ"
destination = "250 Central Ave, Newark, NJ"
#Gets Google Map route from Origin to Destination
def get_route(gmap, origin, destination):
    result = gmap.directions(origin, destination)
    return result

def jsonify(request_info):
    return json.dump(request_info)

#Sorts Gas Station objects by their price
def sort_by_price(gs_list):
    # Traverse through all array elements
    for i in range(gs_list):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if gs_list[j].price > gs_list[j+1].price :
                gs_list[j], gs_list[j+1] = gs_list[j+1], gs_list[j]


#generates a GoogleMaps url to nearest gas Station
#in close proximity of original route from A to B
def generate_final_route(pointA, pointB, gs):
    url = "https://www.google.com/maps/dir/?"
    payload = {"api" : 1,
               "origin" : pointA,
               "destination" : pointB ,
               "waypoints" : gs}

    final_url = url + "api=1"
    final_url += "origin=" + pointA.get_lat_lng_str()
    final_url += "destination=" + pointB.get_lat_lng_str()
    final_url += "waypoints=" + gs.point.get_lat_lng_str()

    return final_url

def main(origin, destination):
    #generate a json file to grab turn data from route of origin->destination
    route_AtoB_json = get_route(gmap, origin, destination)[0]
    parsed_json = parse_json_for_turns(route_AtoB_json)
    pointA = parsed_json[0][0]
    pointB = parsed_json[0][1]
    turns_list = parsed_json[1]

    #calculate the midpoint of all consecutive turns and list them
    midpoint_list = []
    for i in range(len(turns_list)):
        if i+1 < len(turns_list):
            midpoint = turns_list[i].eucl_midpoint_between(turns_list[i+1])
            midpoint_list.append(midpoint)

    #determine best gas stations in proximity to to each midpoint
    gas_stations = []
    for midpoint in midpoint_list:
        address = midpoint.reverse_geocode()
        gas_stations.append(get_station_at_address(address))

    #gather final google maps url of pointA->gas_stations[0]->pointB
    gas_stations = sort_by_price(gas_stations)
    route_url = generate_final_routes(pointA, pointB, gas_stations[0])

    print(route_url)

if __name__ == '__main__':
    main(origin, destination)
