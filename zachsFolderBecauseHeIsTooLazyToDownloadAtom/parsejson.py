from decimal import Decimal
from pprint import pprint
import json
from MapPoint import MapPoint

#Returns a list, where
#   list[0] = A tuple storing (PointA, PointB)
#   list[1] = A list of MapPoint objects corresponding to a turn on the route
def parse_json_for_turns(json_data):
    #load and prepare json_data
    parsed_json = json.load(json_data)
    steps_list = parsed_json[0]['legs'][0]['steps']
    turning_points = []

    #iterate over steps_list and add each step as a MapPoint
    #object to the turning_points list
    for i in steps_list:
        s_lat = i["start_location"]["lat"]
        s_lng = i["start_location"]["lng"]
        dist_string = i["distance"]["text"]
        true_dist_in_miles = parseDistanceToMiles(dist_string)
        s_point = MapPoint(s_lat, s_lng, true_dist_in_miles)
        turning_points.append(s_point)

        #grab pointA and pointB
        pointA_lat = parsed_json[0]['legs'][0]['start_location']['lat']
        pointA_lng = parsed_json[0]['legs'][0]['start_location']['lng']
        pointB_lat = parsed_json[0]['legs'][0]['end_location']['lat']
        pointB_lng = parsed_json[0]['legs'][0]['end_location']['lng']
        pointA = MapPoint(pointA_lat, pointA_lng)
        pointB = MapPoint(pointB_lat, pointB_lng)

        return [(pointA, pointB), turning_points]


def parseDistanceToMiles(dist_string):
    #separate dist_string
    dist_elements = dist_string.split(' ')

    #grab magnitude and units
    mag = float(dist_elements[0])
    unit = dist_elements[-1]

    #convert to miles
    if (unit == 'ft'):
        return format(mag / 5280.0, '.2f')
    elif (unit == 'mi'):
        return format(mag, '.2f')
    else:
        raise NameError('Expected unit in ft/mi')
    return None

#Tester code:
'''
data_from_route = parse_json_for_turns('metadata_dump.json')
#Print: (Point A, Point B)
print("(" + str(data_from_route[0][0]) + ", ", end='')
print(str(data_from_route[0][1]) + ")")

#Print: List of turns
print()
for turn in data_from_route[1]:
    print(turn)

'''
