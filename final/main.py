import json
import requests
import googlemaps
import FindCloseGasStation
from route_data_parser import parse_json_for_turns
import MapPoint
import app
from webscrape_gas_prices import get_station_at_address

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
    #in place insertion sort
    for gs in gs_list:
        # sort in place
        for i in range(1, len(gs_list)):
            current = gs_list[i]

            while i > 0 and gs_list[i-1].price > current.price:
                gs_list[i] = my_list[i-1]
                i -= 1

            gs_list[i] = current

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

    #insert start and end coordinates
    turns_list.insert(0, pointA)
    turns_list.append(pointB)
    gas_station_addresses = findNearByGas(turns_list)
   
    #create a list of gas station objects
    gasStations = []
    for gas_station_address in gas_station_addresses:
        gasStations.append(get_station_at(gas_station_address))

    #gather final google maps url of pointA->gas_stations[0]->pointB
    gas_station_addresses = sort_by_price(gas_station_addresses)
    route_url = generate_final_routes(pointA, pointB, gas_stations[0])

    # send route url back to requester UNIMPLEMENTED WAITING FOR JASON
    print(route_url)

if __name__ == '__main__':
    # requires implemented app
    main(origin, destination)
